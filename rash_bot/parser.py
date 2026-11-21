from __future__ import annotations

import re
from dataclasses import asdict, dataclass
from typing import Any, Literal

CYRILLIC_TO_LATIN_CHOICES = str.maketrans(
    {
        "А": "A",
        "а": "a",
        "В": "B",
        "в": "b",
        "С": "C",
        "с": "c",
        "Д": "D",
        "д": "d",
        "Е": "E",
        "е": "e",
        "Ф": "F",
        "ф": "f",
    }
)

ALLOWED_CLOSED_LETTERS = set("ABCDEFGH")

# All apostrophe / modifier / backtick variants used on Uzbek keyboards (iOS, Android, Windows)
UZBEK_APOSTROPHE_RE = re.compile(r"['‘’ʻʼ`´′ʹˈ‛ˊ]")

# Matches a line consisting strictly of numbered closed choices (e.g. "1a2b3c", "1. A 2) B 3-C")
PURE_NUMBERED_CLOSED_RE = re.compile(
    r"^(?:\d{1,3}\s*[.)\-–—]?\s*[A-Ha-hАаВвСсДдЕеФф][\s,;]*)+$"
)


class ParseError(ValueError):
    """Raised when an answer key or student submission cannot be parsed."""


@dataclass(frozen=True)
class QuestionSpec:
    number: int
    q_type: Literal["closed", "open"]
    accepted: list[str]
    display_key: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "QuestionSpec":
        return cls(
            number=int(data["number"]),
            q_type=data["q_type"],
            accepted=list(data["accepted"]),
            display_key=str(data["display_key"]),
        )


def _normalize_closed_letter(ch: str) -> str:
    return ch.translate(CYRILLIC_TO_LATIN_CHOICES).upper()


def normalize_open_answer(raw: str) -> str:
    """
    Normalize open-ended answer for fair comparison:
    - case-insensitive
    - normalizes all Uzbek apostrophe/modifier variants (' ‘ ’ ʻ ʼ ` ´ ′) to ASCII '
    - collapses whitespace
    - normalizes numbers (e.g. "12,50" -> "12.5", "+5" -> "5", "-0" -> "0")
    """
    text = UZBEK_APOSTROPHE_RE.sub("'", raw.strip().lower())
    text = re.sub(r"\s+", " ", text)
    if not text:
        return ""

    # Try numeric normalization (e.g. "12,50" -> "12.5", "+5" -> "5", "-0" -> "0")
    numeric_candidate = text.replace(" ", "").replace(",", ".")
    if re.fullmatch(r"[+-]?(\d+(\.\d+)?|\.\d+)", numeric_candidate):
        val = float(numeric_candidate)
        if val == 0.0:
            return "0"
        if val.is_integer():
            return str(int(val))
        return f"{val:.10f}".rstrip("0").rstrip(".")

    return text


def _add_open_entry(open_map: dict[int, str], num: int, val: str) -> None:
    if num in open_map:
        raise ParseError(f"{num}-savol kaliti ikki marta kiritilgan.")
    open_map[num] = val


def _extract_numbered_open_entries(text: str) -> tuple[dict[int, str], str]:
    """
    Extract explicit open entries supporting Uzbek words, apostrophes, and flexible separators:
      36: O'zbekiston
      37 = 42|42.0
      38) G'afur G'ulom
      39. Qo'qon
      40-Ma'naviyat
      41 Bo'stonliq
      abcd 5: O'zbekiston 6: G'alla
      36: O'zbekiston; 37: Toshkent
    Returns (open_map, remaining_text).
    """
    open_map: dict[int, str] = {}
    remaining_lines: list[str] = []

    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            continue

        # 1. Pure numbered closed line (e.g. "1a2b3c", "1.A 2)B 3-C") -> keep for closed parser
        if PURE_NUMBERED_CLOSED_RE.fullmatch(line):
            remaining_lines.append(line)
            continue

        # 2. Semicolon-separated open entries (e.g. "36: O'zbekiston; 37: G'alla")
        if ";" in line:
            parts = [p.strip() for p in line.split(";") if p.strip()]
            parsed_parts: list[tuple[int, str]] = []
            all_matched = True
            for part in parts:
                m_part = re.fullmatch(r"(\d{1,3})\s*(?:[:=.)\-–—]|\s)\s*(.+)", part)
                if not m_part:
                    all_matched = False
                    break
                parsed_parts.append((int(m_part.group(1)), m_part.group(2).strip()))
            if all_matched and parsed_parts:
                for num, val in parsed_parts:
                    _add_open_entry(open_map, num, val)
                continue

        # 3. One or more `num: value` / `num=value` entries (optionally after a closed prefix)
        colon_matches = list(re.finditer(r"(?:^|\s)(\d{1,3})\s*[:=]\s*", line))
        if colon_matches:
            # Keep only strictly increasing question numbers with non-empty values
            # so answers like "36: 12:30" or "36: 1:2" are never falsely split.
            selected = [colon_matches[0]]
            for cand in colon_matches[1:]:
                prev = selected[-1]
                prev_num = int(prev.group(1))
                cand_num = int(cand.group(1))
                between = line[prev.end() : cand.start()].strip()
                if cand_num > prev_num and between:
                    selected.append(cand)

            prefix = line[: selected[0].start()].strip()
            if prefix:
                remaining_lines.append(prefix)
            for idx, m in enumerate(selected):
                num = int(m.group(1))
                val_start = m.end()
                val_end = (
                    selected[idx + 1].start()
                    if idx + 1 < len(selected)
                    else len(line)
                )
                val = line[val_start:val_end].strip().rstrip(";")
                if not val:
                    raise ParseError(f"{num}-savol javobi bo'sh qoldirilgan.")
                _add_open_entry(open_map, num, val)
            continue

        # 4. Multiple `num) val` / `num. val` / `num-val` entries on one line
        #    (requires same delimiter and strictly increasing numbers so "36) 1-sentabr" stays intact)
        delim_matches = list(re.finditer(r"(?:^|\s)(\d{1,3})\s*([.)\-–—])\s*", line))
        if len(delim_matches) >= 2:
            selected_d = [delim_matches[0]]
            first_delim = delim_matches[0].group(2)
            for cand in delim_matches[1:]:
                prev = selected_d[-1]
                between = line[prev.end() : cand.start()].strip()
                if (
                    cand.group(2) == first_delim
                    and int(cand.group(1)) > int(prev.group(1))
                    and between
                ):
                    selected_d.append(cand)
            if len(selected_d) >= 2:
                prefix = line[: selected_d[0].start()].strip()
                if prefix:
                    remaining_lines.append(prefix)
                for idx, m in enumerate(selected_d):
                    num = int(m.group(1))
                    val_start = m.end()
                    val_end = (
                        selected_d[idx + 1].start()
                        if idx + 1 < len(selected_d)
                        else len(line)
                    )
                    val = line[val_start:val_end].strip().rstrip(",;")
                    if not val:
                        raise ParseError(f"{num}-savol javobi bo'sh qoldirilgan.")
                    _add_open_entry(open_map, num, val)
                continue

        # 5. Single-line numbered open entry: "36) O'zbekiston", "36. O'zbekiston",
        #    "36-O'zbekiston", "36 - O'zbekiston", "36 O'zbekiston"
        m_single = re.fullmatch(r"(\d{1,3})\s*(?:[.)\-–—]|\s)\s*(.+)", line)
        if m_single:
            num = int(m_single.group(1))
            val = m_single.group(2).strip()
            _add_open_entry(open_map, num, val)
            continue

        remaining_lines.append(line)

    return open_map, "\n".join(remaining_lines).strip()


def _parse_closed_block(text: str) -> dict[int, str]:
    """
    Parse closed answers from either:
    - pure letters: "abcd abcd" -> {1: 'A', 2: 'B', ...}
    - numbered pairs: "1a2b3c", "1.A 2)B 3-C" -> {1: 'A', 2: 'B', 3: 'C'}
    """
    cleaned = text.translate(CYRILLIC_TO_LATIN_CHOICES).strip()
    if not cleaned:
        return {}

    # Try numbered closed format if digits are present
    if any(ch.isdigit() for ch in cleaned):
        pairs = re.findall(r"(\d{1,3})\s*[.):\-–—]?\s*([A-Za-z])", cleaned)
        # Ensure we didn't leave behind stray garbage tokens
        reconstructed = re.sub(r"(\d{1,3})\s*[.):\-–—]?\s*([A-Za-z])", "", cleaned)
        reconstructed = re.sub(r"[\s,;]+", "", reconstructed)
        if reconstructed:
            raise ParseError(
                f"Yopiq javoblar formatida tushunarsiz belgi bor: «{reconstructed[:20]}».\n"
                "Namuna: `abcd...` yoki `1a2b3c...` (ochiq savollar uchun `36: O'zbekiston`)."
            )
        result: dict[int, str] = {}
        for num_str, letter in pairs:
            num = int(num_str)
            upper = letter.upper()
            if upper not in ALLOWED_CLOSED_LETTERS:
                raise ParseError(
                    f"{num}-savolda ruxsat etilmagan harf: «{letter}» (faqat A-H)."
                )
            if num in result:
                raise ParseError(f"{num}-savol ikki marta kiritilgan.")
            result[num] = upper
        return result

    # Pure letters mode (spaces, newlines, dashes, commas ignored)
    letters_only = re.sub(r"[\s,\-_]+", "", cleaned).upper()
    if not letters_only:
        return {}
    invalid = [ch for ch in letters_only if ch not in ALLOWED_CLOSED_LETTERS]
    if invalid:
        raise ParseError(
            f"Yopiq javoblarda ruxsat etilmagan belgi topildi: «{invalid[0]}».\n"
            "Faqat A-H harflarini kiriting (ochiq savollar uchun `36: O'zbekiston` ko'rinishida raqam bilan yozing)."
        )
    return {idx + 1: ch for idx, ch in enumerate(letters_only)}


def parse_answer_key(raw_text: str) -> list[QuestionSpec]:
    """Parse teacher's answer key supporting closed-only, open-only, or mixed tests."""
    text = raw_text.strip()
    if not text:
        raise ParseError("Javoblar kaliti bo'sh bo'lishi mumkin emas.")

    open_raw, closed_text = _extract_numbered_open_entries(text)
    closed_map = _parse_closed_block(closed_text)

    if not closed_map and not open_raw:
        raise ParseError("Birorta ham savol kaliti topilmadi.")

    overlap = set(closed_map).intersection(open_raw)
    if overlap:
        dup = min(overlap)
        raise ParseError(f"{dup}-savol ham yopiq, ham ochiq sifatida kiritilgan.")

    all_nums = sorted(set(closed_map) | set(open_raw))
    expected_nums = list(range(1, len(all_nums) + 1))
    if all_nums != expected_nums:
        missing = sorted(set(range(1, max(all_nums) + 1)) - set(all_nums))
        if missing:
            preview = ", ".join(str(x) for x in missing[:8])
            raise ParseError(
                f"Savol raqamlarida uzilish bor. Quyidagi raqamlar kiritilmagan: {preview}"
            )
        raise ParseError("Savol raqamlari 1 dan boshlab ketma-ket bo'lishi kerak.")

    if len(all_nums) > 200:
        raise ParseError("Savollar soni 200 tadan oshmasligi kerak.")

    specs: list[QuestionSpec] = []
    for num in all_nums:
        if num in closed_map:
            letter = closed_map[num]
            specs.append(
                QuestionSpec(
                    number=num,
                    q_type="closed",
                    accepted=[letter],
                    display_key=letter,
                )
            )
        else:
            raw_val = open_raw[num]
            variants = [v.strip() for v in raw_val.split("|") if v.strip()]
            normalized_variants = [normalize_open_answer(v) for v in variants]
            normalized_variants = [v for v in normalized_variants if v]
            if not normalized_variants:
                raise ParseError(f"{num}-ochiq savol javobi bo'sh.")
            specs.append(
                QuestionSpec(
                    number=num,
                    q_type="open",
                    accepted=normalized_variants,
                    display_key=" | ".join(variants),
                )
            )

    return specs


def split_code_and_answers(raw_text: str) -> tuple[str, str] | None:
    """
    Split a quick-submit message like:
      1001*abcdabcd...
      1001*1a2b3c\n36: O'zbekiston
      1001#abcd...
    Returns (code, answers_body) or None if not matching quick format.
    """
    text = raw_text.strip()
    m = re.match(r"^(\d{3,8})\s*[*#]\s*(.+)$", text, flags=re.DOTALL)
    if m:
        return m.group(1), m.group(2).strip()
    return None


def parse_student_answers(
    raw_text: str,
    questions: list[QuestionSpec],
) -> dict[int, str]:
    """
    Parse a student's submission against the test's question schema.
    Returns mapping {question_number: raw_or_normalized_answer}.
    Omitted open answers default to "" (graded wrong).
    """
    text = raw_text.strip()
    if not text:
        raise ParseError("Javoblar bo'sh bo'lishi mumkin emas.")

    closed_specs = [q for q in questions if q.q_type == "closed"]
    open_specs = [q for q in questions if q.q_type == "open"]
    closed_nums = [q.number for q in closed_specs]
    open_num_set = {q.number for q in open_specs}

    open_raw, closed_text = _extract_numbered_open_entries(text)

    # Support unnumbered submission for open-only tests (e.g. sending "O'zbekiston" directly)
    if not closed_nums and not open_raw and closed_text:
        lines = [ln.strip() for ln in closed_text.splitlines() if ln.strip()]
        if len(open_specs) == 1:
            return {open_specs[0].number: closed_text.strip()}
        if len(lines) == len(open_specs):
            return {q.number: ln for q, ln in zip(open_specs, lines)}

    # Validate open numbers exist in test
    unknown_open = [n for n in open_raw if n not in open_num_set]
    if unknown_open:
        # Allow a student to write e.g. "1: A" for a closed question seamlessly
        for n in list(unknown_open):
            val = _normalize_closed_letter(open_raw[n].strip())
            if n in closed_nums and len(val) == 1 and val in ALLOWED_CLOSED_LETTERS:
                continue
            raise ParseError(
                f"{n}-savol bu testda ochiq savol emas (yoki mavjud emas)."
            )

    student_map: dict[int, str] = {}

    # Move any closed answers accidentally entered as `1: A` into student_map
    for n, val in list(open_raw.items()):
        if n in closed_nums:
            student_map[n] = _normalize_closed_letter(val.strip())
            del open_raw[n]

    if closed_text:
        parsed_closed = _parse_closed_block(closed_text)
        # If pure letters were given and closed questions are contiguous 1..K, they already map 1..K.
        # If closed questions are non-contiguous and pure letters were used, align them in order.
        if (
            not any(ch.isdigit() for ch in closed_text)
            and len(parsed_closed) == len(closed_nums)
        ):
            for q_num, (_, letter) in zip(closed_nums, sorted(parsed_closed.items())):
                student_map[q_num] = letter
        else:
            for q_num, letter in parsed_closed.items():
                if q_num not in closed_nums:
                    raise ParseError(
                        f"{q_num}-savol yopiq savol emas. "
                        f"Bu testda jami {len(closed_nums)} ta yopiq savol bor."
                    )
                student_map[q_num] = letter

    # Verify closed answer count
    if closed_nums:
        provided_closed = sum(1 for n in closed_nums if n in student_map)
        if provided_closed != len(closed_nums):
            raise ParseError(
                f"Yopiq savollar soni mos kelmadi: siz {provided_closed} ta yubordingiz, "
                f"testda esa {len(closed_nums)} ta yopiq savol bor."
            )

    # Populate open answers (missing ones become "")
    for q in open_specs:
        student_map[q.number] = open_raw.get(q.number, "").strip()

    return student_map


def grade_submission(
    student_answers: dict[int, str],
    questions: list[QuestionSpec],
) -> tuple[list[int], int, list[int]]:
    """
    Grade a parsed student submission against question specs.
    Returns (binary_vector, raw_correct_count, wrong_question_numbers).
    """
    binary_vector: list[int] = []
    wrong_numbers: list[int] = []

    for q in sorted(questions, key=lambda item: item.number):
        ans = student_answers.get(q.number, "")
        if q.q_type == "closed":
            is_correct = _normalize_closed_letter(ans) in q.accepted
        else:
            norm = normalize_open_answer(ans)
            normalized_accepted = {normalize_open_answer(a) for a in q.accepted}
            is_correct = bool(norm) and norm in normalized_accepted

        if is_correct:
            binary_vector.append(1)
        else:
            binary_vector.append(0)
            wrong_numbers.append(q.number)

    return binary_vector, sum(binary_vector), wrong_numbers
