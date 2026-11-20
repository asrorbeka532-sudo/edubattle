from __future__ import annotations

import json
import random
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import aiosqlite

from rash_bot.parser import QuestionSpec
from rash_bot.rasch import ItemRaschResult, PersonRaschResult


def _utc_now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")


@dataclass(frozen=True)
class UserRecord:
    user_id: int
    full_name: str
    username: str | None
    created_at: str


@dataclass(frozen=True)
class TestRecord:
    id: int
    code: str
    teacher_id: int
    title: str
    questions: list[QuestionSpec]
    total_questions: int
    closed_count: int
    open_count: int
    status: str  # "active" | "finished"
    created_at: str
    finished_at: str | None
    rasch_summary: dict[str, Any] | None


@dataclass(frozen=True)
class SubmissionRecord:
    id: int
    test_id: int
    user_id: int
    full_name: str
    username: str | None
    answers: dict[int, str]
    binary: list[int]
    raw_score: int
    wrong_numbers: list[int]
    rasch_theta: float | None
    rasch_t_score: float | None
    rasch_grade: str | None
    rasch_rank: int | None
    submitted_at: str


class Database:
    def __init__(self, db_path: Path | str) -> None:
        self.db_path = Path(db_path)

    async def init(self) -> None:
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute("PRAGMA foreign_keys = ON;")
            await db.executescript(
                """
                CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY,
                    full_name TEXT NOT NULL,
                    username TEXT,
                    created_at TEXT NOT NULL
                );

                CREATE TABLE IF NOT EXISTS tests (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    code TEXT NOT NULL UNIQUE,
                    teacher_id INTEGER NOT NULL,
                    title TEXT NOT NULL,
                    questions_json TEXT NOT NULL,
                    total_questions INTEGER NOT NULL,
                    closed_count INTEGER NOT NULL,
                    open_count INTEGER NOT NULL,
                    status TEXT NOT NULL DEFAULT 'active',
                    created_at TEXT NOT NULL,
                    finished_at TEXT,
                    rasch_summary_json TEXT,
                    FOREIGN KEY (teacher_id) REFERENCES users(user_id)
                );

                CREATE TABLE IF NOT EXISTS submissions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    test_id INTEGER NOT NULL,
                    user_id INTEGER NOT NULL,
                    answers_json TEXT NOT NULL,
                    binary_json TEXT NOT NULL,
                    raw_score INTEGER NOT NULL,
                    wrong_json TEXT NOT NULL,
                    rasch_theta REAL,
                    rasch_t_score REAL,
                    rasch_grade TEXT,
                    rasch_rank INTEGER,
                    submitted_at TEXT NOT NULL,
                    UNIQUE(test_id, user_id),
                    FOREIGN KEY (test_id) REFERENCES tests(id) ON DELETE CASCADE,
                    FOREIGN KEY (user_id) REFERENCES users(user_id)
                );

                CREATE INDEX IF NOT EXISTS idx_tests_teacher ON tests(teacher_id);
                CREATE INDEX IF NOT EXISTS idx_submissions_test ON submissions(test_id);
                CREATE INDEX IF NOT EXISTS idx_submissions_user ON submissions(user_id);
                """
            )
            await db.commit()

    # ---------- Users ----------

    async def upsert_user(
        self,
        user_id: int,
        full_name: str,
        username: str | None = None,
    ) -> UserRecord:
        now = _utc_now_iso()
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute(
                """
                INSERT INTO users (user_id, full_name, username, created_at)
                VALUES (?, ?, ?, ?)
                ON CONFLICT(user_id) DO UPDATE SET
                    full_name = excluded.full_name,
                    username = excluded.username
                """,
                (user_id, full_name.strip(), username, now),
            )
            await db.commit()
        user = await self.get_user(user_id)
        assert user is not None
        return user

    async def get_user(self, user_id: int) -> UserRecord | None:
        async with aiosqlite.connect(self.db_path) as db:
            db.row_factory = aiosqlite.Row
            async with db.execute(
                "SELECT user_id, full_name, username, created_at FROM users WHERE user_id = ?",
                (user_id,),
            ) as cur:
                row = await cur.fetchone()
                if not row:
                    return None
                return UserRecord(
                    user_id=row["user_id"],
                    full_name=row["full_name"],
                    username=row["username"],
                    created_at=row["created_at"],
                )

    # ---------- Tests ----------

    async def _generate_unique_code(self, db: aiosqlite.Connection) -> str:
        for _ in range(50):
            code = str(random.randint(1000, 9999))
            async with db.execute("SELECT 1 FROM tests WHERE code = ?", (code,)) as cur:
                if await cur.fetchone() is None:
                    return code
        # Fallback to 5-digit codes if 4-digit space gets crowded
        while True:
            code = str(random.randint(10000, 99999))
            async with db.execute("SELECT 1 FROM tests WHERE code = ?", (code,)) as cur:
                if await cur.fetchone() is None:
                    return code

    @staticmethod
    def _row_to_test(row: aiosqlite.Row) -> TestRecord:
        raw_questions = json.loads(row["questions_json"])
        questions = [QuestionSpec.from_dict(item) for item in raw_questions]
        rasch_summary = (
            json.loads(row["rasch_summary_json"])
            if row["rasch_summary_json"]
            else None
        )
        return TestRecord(
            id=row["id"],
            code=row["code"],
            teacher_id=row["teacher_id"],
            title=row["title"],
            questions=questions,
            total_questions=row["total_questions"],
            closed_count=row["closed_count"],
            open_count=row["open_count"],
            status=row["status"],
            created_at=row["created_at"],
            finished_at=row["finished_at"],
            rasch_summary=rasch_summary,
        )

    async def create_test(
        self,
        teacher_id: int,
        title: str,
        questions: list[QuestionSpec],
    ) -> TestRecord:
        now = _utc_now_iso()
        closed_count = sum(1 for q in questions if q.q_type == "closed")
        open_count = sum(1 for q in questions if q.q_type == "open")
        questions_json = json.dumps(
            [q.to_dict() for q in questions], ensure_ascii=False
        )

        async with aiosqlite.connect(self.db_path) as db:
            code = await self._generate_unique_code(db)
            cur = await db.execute(
                """
                INSERT INTO tests (
                    code, teacher_id, title, questions_json,
                    total_questions, closed_count, open_count,
                    status, created_at
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, 'active', ?)
                """,
                (
                    code,
                    teacher_id,
                    title.strip(),
                    questions_json,
                    len(questions),
                    closed_count,
                    open_count,
                    now,
                ),
            )
            await db.commit()
            test_id = cur.lastrowid

        test = await self.get_test_by_id(int(test_id))
        assert test is not None
        return test

    async def get_test_by_id(self, test_id: int) -> TestRecord | None:
        async with aiosqlite.connect(self.db_path) as db:
            db.row_factory = aiosqlite.Row
            async with db.execute(
                "SELECT * FROM tests WHERE id = ?", (test_id,)
            ) as cur:
                row = await cur.fetchone()
                return self._row_to_test(row) if row else None

    async def get_test_by_code(self, code: str) -> TestRecord | None:
        async with aiosqlite.connect(self.db_path) as db:
            db.row_factory = aiosqlite.Row
            async with db.execute(
                "SELECT * FROM tests WHERE code = ?", (code.strip(),)
            ) as cur:
                row = await cur.fetchone()
                return self._row_to_test(row) if row else None

    async def list_teacher_tests(
        self, teacher_id: int, limit: int = 30
    ) -> list[tuple[TestRecord, int]]:
        async with aiosqlite.connect(self.db_path) as db:
            db.row_factory = aiosqlite.Row
            async with db.execute(
                """
                SELECT t.*, COUNT(s.id) AS sub_count
                FROM tests t
                LEFT JOIN submissions s ON s.test_id = t.id
                WHERE t.teacher_id = ?
                GROUP BY t.id
                ORDER BY t.id DESC
                LIMIT ?
                """,
                (teacher_id, limit),
            ) as cur:
                rows = await cur.fetchall()
                return [(self._row_to_test(row), int(row["sub_count"])) for row in rows]

    async def reopen_test(self, test_id: int) -> None:
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute(
                "UPDATE tests SET status = 'active', finished_at = NULL WHERE id = ?",
                (test_id,),
            )
            await db.commit()

    async def delete_test(self, test_id: int) -> None:
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute("PRAGMA foreign_keys = ON;")
            await db.execute("DELETE FROM tests WHERE id = ?", (test_id,))
            await db.commit()

    # ---------- Submissions ----------

    async def create_submission(
        self,
        test_id: int,
        user_id: int,
        answers: dict[int, str],
        binary: list[int],
        raw_score: int,
        wrong_numbers: list[int],
    ) -> int:
        now = _utc_now_iso()
        async with aiosqlite.connect(self.db_path) as db:
            cur = await db.execute(
                """
                INSERT INTO submissions (
                    test_id, user_id, answers_json, binary_json,
                    raw_score, wrong_json, submitted_at
                )
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    test_id,
                    user_id,
                    json.dumps({str(k): v for k, v in answers.items()}, ensure_ascii=False),
                    json.dumps(binary),
                    raw_score,
                    json.dumps(wrong_numbers),
                    now,
                ),
            )
            await db.commit()
            return int(cur.lastrowid)

    @staticmethod
    def _row_to_submission(row: aiosqlite.Row) -> SubmissionRecord:
        raw_answers = json.loads(row["answers_json"])
        return SubmissionRecord(
            id=row["id"],
            test_id=row["test_id"],
            user_id=row["user_id"],
            full_name=row["full_name"],
            username=row["username"],
            answers={int(k): v for k, v in raw_answers.items()},
            binary=json.loads(row["binary_json"]),
            raw_score=row["raw_score"],
            wrong_numbers=json.loads(row["wrong_json"]),
            rasch_theta=row["rasch_theta"],
            rasch_t_score=row["rasch_t_score"],
            rasch_grade=row["rasch_grade"],
            rasch_rank=row["rasch_rank"],
            submitted_at=row["submitted_at"],
        )

    async def get_submission(
        self, test_id: int, user_id: int
    ) -> SubmissionRecord | None:
        async with aiosqlite.connect(self.db_path) as db:
            db.row_factory = aiosqlite.Row
            async with db.execute(
                """
                SELECT s.*, u.full_name, u.username
                FROM submissions s
                JOIN users u ON u.user_id = s.user_id
                WHERE s.test_id = ? AND s.user_id = ?
                """,
                (test_id, user_id),
            ) as cur:
                row = await cur.fetchone()
                return self._row_to_submission(row) if row else None

    async def list_test_submissions(self, test_id: int) -> list[SubmissionRecord]:
        async with aiosqlite.connect(self.db_path) as db:
            db.row_factory = aiosqlite.Row
            async with db.execute(
                """
                SELECT s.*, u.full_name, u.username
                FROM submissions s
                JOIN users u ON u.user_id = s.user_id
                WHERE s.test_id = ?
                ORDER BY
                    COALESCE(s.rasch_t_score, -1) DESC,
                    s.raw_score DESC,
                    s.id ASC
                """,
                (test_id,),
            ) as cur:
                rows = await cur.fetchall()
                return [self._row_to_submission(row) for row in rows]

    async def list_user_results(
        self, user_id: int, limit: int = 20
    ) -> list[tuple[TestRecord, SubmissionRecord]]:
        async with aiosqlite.connect(self.db_path) as db:
            db.row_factory = aiosqlite.Row
            async with db.execute(
                """
                SELECT
                    s.id AS s_id, s.test_id, s.user_id, s.answers_json, s.binary_json,
                    s.raw_score, s.wrong_json, s.rasch_theta, s.rasch_t_score,
                    s.rasch_grade, s.rasch_rank, s.submitted_at,
                    u.full_name, u.username,
                    t.id AS t_id, t.code, t.teacher_id, t.title, t.questions_json,
                    t.total_questions, t.closed_count, t.open_count, t.status,
                    t.created_at, t.finished_at, t.rasch_summary_json
                FROM submissions s
                JOIN users u ON u.user_id = s.user_id
                JOIN tests t ON t.id = s.test_id
                WHERE s.user_id = ?
                ORDER BY s.id DESC
                LIMIT ?
                """,
                (user_id, limit),
            ) as cur:
                rows = await cur.fetchall()
                results: list[tuple[TestRecord, SubmissionRecord]] = []
                for row in rows:
                    test_rec = TestRecord(
                        id=row["t_id"],
                        code=row["code"],
                        teacher_id=row["teacher_id"],
                        title=row["title"],
                        questions=[
                            QuestionSpec.from_dict(x)
                            for x in json.loads(row["questions_json"])
                        ],
                        total_questions=row["total_questions"],
                        closed_count=row["closed_count"],
                        open_count=row["open_count"],
                        status=row["status"],
                        created_at=row["created_at"],
                        finished_at=row["finished_at"],
                        rasch_summary=(
                            json.loads(row["rasch_summary_json"])
                            if row["rasch_summary_json"]
                            else None
                        ),
                    )
                    sub_rec = SubmissionRecord(
                        id=row["s_id"],
                        test_id=row["test_id"],
                        user_id=row["user_id"],
                        full_name=row["full_name"],
                        username=row["username"],
                        answers={
                            int(k): v
                            for k, v in json.loads(row["answers_json"]).items()
                        },
                        binary=json.loads(row["binary_json"]),
                        raw_score=row["raw_score"],
                        wrong_numbers=json.loads(row["wrong_json"]),
                        rasch_theta=row["rasch_theta"],
                        rasch_t_score=row["rasch_t_score"],
                        rasch_grade=row["rasch_grade"],
                        rasch_rank=row["rasch_rank"],
                        submitted_at=row["submitted_at"],
                    )
                    results.append((test_rec, sub_rec))
                return results

    async def save_rasch_results(
        self,
        test_id: int,
        submission_ids: list[int],
        person_results: list[PersonRaschResult],
        item_results: list[ItemRaschResult],
        mean_theta: float,
        std_theta: float,
        warning: str | None,
    ) -> None:
        now = _utc_now_iso()
        summary = {
            "mean_theta": mean_theta,
            "std_theta": std_theta,
            "warning": warning,
            "items": [
                {
                    "item_number": it.item_number,
                    "correct_count": it.correct_count,
                    "total_persons": it.total_persons,
                    "p_value": it.p_value,
                    "beta": it.beta,
                    "difficulty_label": it.difficulty_label,
                }
                for it in item_results
            ],
        }
        async with aiosqlite.connect(self.db_path) as db:
            for sub_id, p_res in zip(submission_ids, person_results):
                await db.execute(
                    """
                    UPDATE submissions
                    SET rasch_theta = ?,
                        rasch_t_score = ?,
                        rasch_grade = ?,
                        rasch_rank = ?
                    WHERE id = ?
                    """,
                    (p_res.theta, p_res.t_score, p_res.grade, p_res.rank, sub_id),
                )
            await db.execute(
                """
                UPDATE tests
                SET status = 'finished',
                    finished_at = ?,
                    rasch_summary_json = ?
                WHERE id = ?
                """,
                (now, json.dumps(summary, ensure_ascii=False), test_id),
            )
            await db.commit()
