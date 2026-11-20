from __future__ import annotations

import logging
import os
from pathlib import Path
from typing import Any

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Update

from rash_bot.config import Settings
from rash_bot.database import Database
from rash_bot.handlers import setup_routers

logger = logging.getLogger("rash_bot.webhook")

_bot: Bot | None = None
_dp: Dispatcher | None = None
_db: Database | None = None
_webhook_url: str | None = None
_db_path_str: str | None = None
_last_error: str | None = None


def _resolve_db_path() -> Path:
    explicit = os.getenv("RASH_DB_PATH", "").strip()
    if explicit:
        return Path(explicit)

    data_dir = os.getenv("DATA_DIR", "").strip()
    if not data_dir and Path("/data").is_dir():
        data_dir = "/data"
    if data_dir:
        return Path(data_dir) / "rash_yordamchi.db"

    return Path("data/rash_yordamchi.db")


def _load_webhook_settings() -> Settings | None:
    token = os.getenv("RASH_BOT_TOKEN", "").strip()
    if not token:
        return None

    raw_admins = os.getenv("RASH_ADMIN_IDS", "").strip()
    admin_ids: set[int] = set()
    if raw_admins:
        for chunk in raw_admins.split(","):
            chunk = chunk.strip()
            if chunk.isdigit():
                admin_ids.add(int(chunk))

    teacher_only = (
        os.getenv("RASH_TEACHER_ONLY_ADMINS", "false").strip().lower()
        in {"1", "true", "yes", "ha"}
    )

    return Settings(
        bot_token=token,
        admin_ids=admin_ids,
        teacher_only_admins=teacher_only,
        db_path=_resolve_db_path(),
    )


async def init_rash_bot(render_url: str) -> dict[str, Any]:
    """Initialize Rash Yordamchi bot and register its Telegram webhook."""
    global _bot, _dp, _db, _webhook_url, _db_path_str, _last_error

    settings = _load_webhook_settings()
    if settings is None:
        _last_error = "RASH_BOT_TOKEN environment variable is not set."
        logger.warning("[RashBot] %s", _last_error)
        return {"configured": False, "error": _last_error}

    try:
        if _bot is not None:
            try:
                await _bot.session.close()
            except Exception:
                pass

        db = Database(settings.db_path)
        await db.init()

        bot = Bot(
            token=settings.bot_token,
            default=DefaultBotProperties(parse_mode=ParseMode.HTML),
        )
        dp = Dispatcher(storage=MemoryStorage())
        dp.include_router(setup_routers())
        dp["db"] = db
        dp["settings"] = settings

        target_url = f"{render_url.rstrip('/')}/api/rash-telegram-webhook"
        await bot.set_webhook(url=target_url, drop_pending_updates=False)

        _bot = bot
        _dp = dp
        _db = db
        _webhook_url = target_url
        _db_path_str = str(settings.db_path)
        _last_error = None

        logger.info("[RashBot] Webhook registered: %s (DB: %s)", target_url, _db_path_str)
        return {
            "configured": True,
            "initialized": True,
            "webhook_url": _webhook_url,
            "db_path": _db_path_str,
        }
    except Exception as exc:
        _last_error = str(exc)
        logger.exception("[RashBot] Failed to initialize: %s", exc)
        return {"configured": True, "initialized": False, "error": _last_error}


async def handle_rash_webhook(
    update_dict: dict[str, Any], render_url: str
) -> dict[str, Any]:
    """Process an incoming Telegram webhook update for Rash Yordamchi."""
    if _bot is None or _dp is None:
        res = await init_rash_bot(render_url)
        if not res.get("initialized"):
            return {"ok": False, "error": res.get("error", "Bot not initialized")}

    assert _bot is not None and _dp is not None
    try:
        update = Update.model_validate(update_dict, context={"bot": _bot})
        await _dp.feed_update(_bot, update)
        return {"ok": True}
    except Exception as exc:
        logger.exception("[RashBot] Error handling webhook update: %s", exc)
        return {"ok": False, "error": str(exc)}


def get_rash_status() -> dict[str, Any]:
    return {
        "configured": bool(os.getenv("RASH_BOT_TOKEN", "").strip()),
        "initialized": _bot is not None and _dp is not None,
        "webhook_url": _webhook_url,
        "db_path": _db_path_str,
        "error": _last_error,
    }


async def shutdown_rash_bot() -> None:
    global _bot, _dp, _db
    if _bot is not None:
        try:
            await _bot.session.close()
        except Exception:
            pass
    _bot = None
    _dp = None
    _db = None
