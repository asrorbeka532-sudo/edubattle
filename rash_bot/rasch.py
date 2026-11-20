from __future__ import annotations

from dataclasses import dataclass

import numpy as np


def _sigmoid(x: np.ndarray | float) -> np.ndarray:
    """Numerically stable logistic sigmoid function."""
    arr = np.asarray(x, dtype=np.float64)
    clipped = np.clip(arr, -500.0, 500.0)
    return np.where(
        clipped >= 0.0,
        1.0 / (1.0 + np.exp(-clipped)),
        np.exp(clipped) / (1.0 + np.exp(clipped)),
    )


@dataclass(frozen=True)
class PersonRaschResult:
    index: int
    raw_score: int
    total_items: int
    percentage: float
    theta: float          # Ability logit
    t_score: float        # Milliy Sertifikat T-ball (50 + 10*z)
    grade: str            # A+, A, B+, B, C+, C, Darajasiz
    rank: int


@dataclass(frozen=True)
class ItemRaschResult:
    item_number: int      # 1-based
    correct_count: int
    total_persons: int
    p_value: float        # Proportion correct (0..1)
    beta: float           # Difficulty logit (higher = harder)
    difficulty_label: str # Oson / O'rta / Qiyin


@dataclass(frozen=True)
class RaschReport:
    persons: list[PersonRaschResult]
    items: list[ItemRaschResult]
    mean_theta: float
    std_theta: float
    converged: bool
    iterations: int
    warning: str | None = None


def assign_milliy_sertifikat_grade(t_score: float) -> str:
    """
    UzBMB Milliy Sertifikat daraja shkalasi:
      A+ : >= 70.0
      A  : 65.0 - 69.99
      B+ : 60.0 - 64.99
      B  : 55.0 - 59.99
      C+ : 50.0 - 54.99
      C  : 46.0 - 49.99
      Darajasiz : < 46.0
    """
    if t_score >= 70.0:
        return "A+"
    if t_score >= 65.0:
        return "A"
    if t_score >= 60.0:
        return "B+"
    if t_score >= 55.0:
        return "B"
    if t_score >= 50.0:
        return "C+"
    if t_score >= 46.0:
        return "C"
    return "Darajasiz"


def classify_item_difficulty(beta: float) -> str:
    if beta <= -1.0:
        return "Oson"
    if beta < 1.0:
        return "O'rta"
    return "Qiyin"


def _solve_scalar_logit(
    target_score: float,
    fixed_params: np.ndarray,
    is_person: bool,
    init_val: float = 0.0,
    max_iter: int = 50,
    tol: float = 1e-6,
    bound: float = 6.0,
) -> float:
    """
    Solve sum(sigmoid(theta - beta_j)) = target_score for theta (if is_person)
    or sum(sigmoid(theta_i - beta)) = target_score for beta (if not is_person).
    """
    val = float(np.clip(init_val, -bound, bound))
    for _ in range(max_iter):
        probs = _sigmoid(val - fixed_params) if is_person else _sigmoid(fixed_params - val)
        expected = float(np.sum(probs))
        info = float(np.sum(probs * (1.0 - probs)))
        if info < 1e-9:
            break
        diff = (target_score - expected) if is_person else (expected - target_score)
        step = float(np.clip(diff / info, -1.0, 1.0))
        val = float(np.clip(val + step, -bound, bound))
        if abs(step) < tol:
            break
    return val


def fit_rasch_model(
    response_matrix: list[list[int]] | np.ndarray,
    max_iter: int = 200,
    tol: float = 1e-5,
    extreme_adj: float = 0.3,
    logit_bound: float = 6.0,
) -> RaschReport:
    """
    Fit a 1PL Rasch IRT model using Joint Maximum Likelihood Estimation (JMLE)
    with Newton-Raphson updates and Winsteps-style extreme score adjustment (0.3).

    Args:
        response_matrix: Binary N x M matrix (N persons, M items), values in {0, 1}.
        max_iter: Maximum JMLE outer iterations.
        tol: Convergence tolerance on max parameter change.
        extreme_adj: Adjustment applied to 0% and 100% extreme scores (default 0.3).
        logit_bound: Safe clipping bound for logits [-logit_bound, +logit_bound].

    Returns:
        RaschReport containing person abilities, T-scores, Milliy Sertifikat grades,
        ranks, and per-item difficulty statistics.
    """
    X = np.asarray(response_matrix, dtype=np.float64)
    if X.ndim != 2 or X.shape[0] == 0 or X.shape[1] == 0:
        raise ValueError("Javoblar matritsasi bo'sh bo'lishi mumkin emas.")
    if not np.all((X == 0.0) | (X == 1.0)):
        raise ValueError("Javoblar matritsasi faqat 0 va 1 qiymatlaridan iborat bo'lishi kerak.")

    n_persons, n_items = X.shape
    raw_person_scores = np.sum(X, axis=1)
    raw_item_scores = np.sum(X, axis=0)

    warning: str | None = None
    if n_persons < 5:
        warning = (
            f"Ishtirokchilar soni kam ({n_persons} nafar). "
            "Rasch modeli aniqroq ishlashi uchun kamida 15-20 nafar ishtirokchi tavsiya etiladi."
        )

    # Identify non-extreme persons and items for core JMLE estimation
    non_ext_persons = (raw_person_scores > 0) & (raw_person_scores < n_items)
    non_ext_items = (raw_item_scores > 0) & (raw_item_scores < n_persons)

    # Initial logit estimates via smooth log-odds
    p_init = (raw_person_scores + 0.5) / (n_items + 1.0)
    theta = np.log(p_init / (1.0 - p_init))
    q_init = (raw_item_scores + 0.5) / (n_persons + 1.0)
    beta = -np.log(q_init / (1.0 - q_init))
    beta -= np.mean(beta)

    converged = True
    iterations = 0

    if np.any(non_ext_persons) and np.any(non_ext_items):
        p_idx = np.where(non_ext_persons)[0]
        i_idx = np.where(non_ext_items)[0]

        X_sub = X[np.ix_(p_idx, i_idx)]
        sub_person_scores = np.sum(X_sub, axis=1)
        sub_item_scores = np.sum(X_sub, axis=0)

        # Some persons/items may become extreme inside the submatrix
        active_p = (sub_person_scores > 0) & (sub_person_scores < len(i_idx))
        active_i = (sub_item_scores > 0) & (sub_item_scores < len(p_idx))

        if np.any(active_p) and np.any(active_i):
            p_core = p_idx[active_p]
            i_core = i_idx[active_i]
            X_core = X[np.ix_(p_core, i_core)]

            th_core = theta[p_core].copy()
            bt_core = beta[i_core].copy()
            bt_core -= np.mean(bt_core)

            converged = False
            for it in range(1, max_iter + 1):
                iterations = it

                # 1) Update item difficulties beta_j
                probs = _sigmoid(th_core[:, None] - bt_core[None, :])
                grad_b = np.sum(probs - X_core, axis=0)
                info_b = np.sum(probs * (1.0 - probs), axis=0)
                step_b = np.where(info_b > 1e-9, np.clip(grad_b / np.maximum(info_b, 1e-9), -1.0, 1.0), 0.0)
                bt_new = np.clip(bt_core + step_b, -logit_bound, logit_bound)
                bt_new -= np.mean(bt_new)

                # 2) Update person abilities theta_i
                probs = _sigmoid(th_core[:, None] - bt_new[None, :])
                grad_t = np.sum(X_core - probs, axis=1)
                info_t = np.sum(probs * (1.0 - probs), axis=1)
                step_t = np.where(info_t > 1e-9, np.clip(grad_t / np.maximum(info_t, 1e-9), -1.0, 1.0), 0.0)
                th_new = np.clip(th_core + step_t, -logit_bound, logit_bound)

                max_delta = float(
                    max(
                        np.max(np.abs(bt_new - bt_core)),
                        np.max(np.abs(th_new - th_core)),
                    )
                )
                bt_core = bt_new
                th_core = th_new

                if max_delta < tol:
                    converged = True
                    break

            # Standard JMLE bias correction factor (M-1)/M when M > 1
            if len(i_core) > 1:
                bias_factor = (len(i_core) - 1.0) / len(i_core)
                bt_core = bt_core * bias_factor

            beta[i_core] = bt_core
            theta[p_core] = th_core

            # Estimate remaining (extreme or submatrix-extreme) items against calibrated persons
            calibrated_thetas = theta[p_core]
            for j in range(n_items):
                if j in i_core:
                    continue
                s_j = float(np.sum(X[p_core, j]))
                n_cal = float(len(p_core))
                adj_s = extreme_adj if s_j <= 0 else (n_cal - extreme_adj if s_j >= n_cal else s_j)
                adj_s = float(np.clip(adj_s, 0.01, max(n_cal - 0.01, 0.02)))
                beta[j] = _solve_scalar_logit(
                    target_score=adj_s,
                    fixed_params=calibrated_thetas,
                    is_person=False,
                    init_val=beta[j],
                    bound=logit_bound,
                )

            # Re-center all betas around 0 while shifting thetas equally (preserves theta - beta)
            beta_mean = float(np.mean(beta))
            beta -= beta_mean
            theta -= beta_mean

            # Estimate ALL person abilities against the full calibrated item bank beta
            for i in range(n_persons):
                r_i = float(raw_person_scores[i])
                if r_i <= 0:
                    adj_r = min(extreme_adj, n_items * 0.25)
                elif r_i >= n_items:
                    adj_r = max(n_items - extreme_adj, n_items * 0.75)
                else:
                    adj_r = r_i
                theta[i] = _solve_scalar_logit(
                    target_score=adj_r,
                    fixed_params=beta,
                    is_person=True,
                    init_val=theta[i],
                    bound=logit_bound,
                )

    # Convert logits to Milliy Sertifikat T-scores: T = 50 + 10 * z
    mean_theta = float(np.mean(theta))
    std_theta = float(np.std(theta, ddof=0))

    if std_theta < 1e-8:
        # All students have identical ability (e.g., 1 student or all tied)
        t_scores = np.full(n_persons, 50.0, dtype=np.float64)
        extra_warn = "Barcha ishtirokchilar bir xil ball to'plagani uchun standart 50.00 T-ball berildi."
        warning = f"{warning} {extra_warn}" if warning else extra_warn
    else:
        z_scores = (theta - mean_theta) / std_theta
        t_scores = np.clip(50.0 + 10.0 * z_scores, 0.0, 100.0)

    # Compute dense/competition ranking by (t_score desc, raw_score desc)
    sort_order = sorted(
        range(n_persons),
        key=lambda i: (round(float(t_scores[i]), 4), int(raw_person_scores[i])),
        reverse=True,
    )
    ranks = [0] * n_persons
    prev_key: tuple[float, int] | None = None
    current_rank = 0
    for pos, idx in enumerate(sort_order, start=1):
        key = (round(float(t_scores[idx]), 2), int(raw_person_scores[idx]))
        if key != prev_key:
            current_rank = pos
            prev_key = key
        ranks[idx] = current_rank

    person_results: list[PersonRaschResult] = []
    for i in range(n_persons):
        t_val = round(float(t_scores[i]), 2)
        raw_s = int(raw_person_scores[i])
        person_results.append(
            PersonRaschResult(
                index=i,
                raw_score=raw_s,
                total_items=n_items,
                percentage=round(100.0 * raw_s / n_items, 1),
                theta=round(float(theta[i]), 4),
                t_score=t_val,
                grade=assign_milliy_sertifikat_grade(t_val),
                rank=ranks[i],
            )
        )

    item_results: list[ItemRaschResult] = []
    for j in range(n_items):
        c_cnt = int(raw_item_scores[j])
        b_val = round(float(beta[j]), 4)
        item_results.append(
            ItemRaschResult(
                item_number=j + 1,
                correct_count=c_cnt,
                total_persons=n_persons,
                p_value=round(c_cnt / n_persons, 4),
                beta=b_val,
                difficulty_label=classify_item_difficulty(b_val),
            )
        )

    return RaschReport(
        persons=person_results,
        items=item_results,
        mean_theta=round(mean_theta, 4),
        std_theta=round(std_theta, 4),
        converged=converged,
        iterations=iterations,
        warning=warning,
    )
