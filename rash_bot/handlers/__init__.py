from aiogram import Router

from rash_bot.handlers.start import router as start_router
from rash_bot.handlers.student import router as student_router
from rash_bot.handlers.teacher import router as teacher_router


def setup_routers() -> Router:
    root = Router()
    root.include_router(start_router)
    root.include_router(teacher_router)
    # student_router is last because it includes the quick `CODE*answers` text handler
    root.include_router(student_router)
    return root
