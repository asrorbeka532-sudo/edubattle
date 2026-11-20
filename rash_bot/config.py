from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path


@dataclass(frozen=True)
class Settings:
    bot_token: str
    admin_ids: set[int] = field(default_factory=set)
    teacher_only_admins: bool = False
    db_path: Path = Path("data/rash_yordamchi.db")


def load_settings() -> Settings:
    try:
        from dotenv import load_dotenv

        load_dotenv()
    except ImportError:
        pass

    bot_token = os.getenv("BOT_TOKEN", "").strip()
    if not bot_token:
        raise ValueError(
            "BOT_TOKEN topilmadi! .env faylini yarating va BotFather tokenini kiriting."
        )

    raw_admins = os.getenv("ADMIN_IDS", "").strip()
    admin_ids: set[int] = set()
    if raw_admins:
        for chunk in raw_admins.split(","):
            chunk = chunk.strip()
            if chunk.isdigit():
                admin_ids.add(int(chunk))

    teacher_only_admins = (
        os.getenv("TEACHER_ONLY_ADMINS", "false").strip().lower()
        in {"1", "true", "yes", "ha"}
    )

    db_path = Path(os.getenv("DB_PATH", "data/rash_yordamchi.db").strip())

    return Settings(
        bot_token=bot_token,
        admin_ids=admin_ids,
        teacher_only_admins=teacher_only_admins,
        db_path=db_path,
    )
