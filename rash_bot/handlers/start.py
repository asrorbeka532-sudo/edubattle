from __future__ import annotations

import html

from aiogram import F, Router
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from rash_bot.config import Settings
from rash_bot.database import Database
from rash_bot.keyboards import (
    BTN_CANCEL,
    BTN_HELP,
    BTN_PROFILE,
    cancel_keyboard,
    main_menu_keyboard,
    profile_keyboard,
)
from rash_bot.states import EditProfileState, RegistrationState

router = Router(name="start")


def can_create_test(user_id: int, settings: Settings) -> bool:
    return (not settings.teacher_only_admins) or (user_id in settings.admin_ids)


HELP_TEXT = (
    "<b>🤖 «Rash Yordamchi» — Yo'riqnoma</b>\n\n"
    "<b>1️⃣ O'quvchilar uchun (Javob yuborish):</b>\n"
    "Test kodini va javoblarni bitta xabarda yuborishingiz mumkin:\n"
    "• Oddiy yopiq test:\n"
    "<code>4821*abcdabcdab</code>\n"
    "• Raqamli yopiq test:\n"
    "<code>4821*1a2b3c4d...</code>\n"
    "• Yopiq + Ochiq (Milliy Sertifikat):\n"
    "<pre>4821*abcd... (35 ta harf)\n"
    "36: 12.5\n"
    "37: 42\n"
    "38: -3</pre>\n\n"
    "<b>2️⃣ O'qituvchilar uchun:</b>\n"
    "• <b>➕ Test yaratish</b> tugmasi orqali nom va kalit kiritasiz.\n"
    "• Ochiq savollarda bir nechta to'g'ri variantni <code>|</code> bilan yozish mumkin "
    "(masalan: <code>36: 12.5|12,5</code>).\n"
    "• <b>📋 Mening testlarim</b> bo'limidan testni yakunlab, <b>Rasch modeli (1PL IRT)</b> "
    "bo'yicha ball va darajalarni hisoblashingiz, Excel hisobot olishingiz va barcha "
    "o'quvchilarga natijani avtomatik yuborishingiz mumkin.\n\n"
    "<b>3️⃣ Milliy Sertifikat daraja shkalasi (T-ball):</b>\n"
    "• <b>A+</b> : 70.0 va undan yuqori\n"
    "• <b>A</b>  : 65.0 – 69.99\n"
    "• <b>B+</b> : 60.0 – 64.99\n"
    "• <b>B</b>  : 55.0 – 59.99\n"
    "• <b>C+</b> : 50.0 – 54.99\n"
    "• <b>C</b>  : 46.0 – 49.99\n"
    "• <b>Darajasiz</b> : 46.0 dan past"
)


@router.message(StateFilter("*"), CommandStart())
async def cmd_start(
    message: Message,
    state: FSMContext,
    db: Database,
    settings: Settings,
) -> None:
    await state.clear()
    assert message.from_user is not None
    user = await db.get_user(message.from_user.id)

    if user is None:
        await state.set_state(RegistrationState.waiting_full_name)
        await message.answer(
            "👋 Assalomu alaykum! <b>«Rash Yordamchi»</b> botiga xush kelibsiz!\n\n"
            "Natijalar jadvalida to'g'ri ko'rinishi uchun <b>Ism va Familiyangizni</b> yuboring.\n"
            "<i>Masalan: Aliyev Vali</i>",
            parse_mode="HTML",
        )
        return

    await message.answer(
        f"👋 Xush kelibsiz, <b>{html.escape(user.full_name)}</b>!\n"
        "Kerakli bo'limni tanlang yoki to'g'ridan-to'g'ri <code>KOD*javoblar</code> yuboring.",
        reply_markup=main_menu_keyboard(can_create_test(user.user_id, settings)),
        parse_mode="HTML",
    )


@router.message(RegistrationState.waiting_full_name, F.text)
async def process_registration_name(
    message: Message,
    state: FSMContext,
    db: Database,
    settings: Settings,
) -> None:
    assert message.from_user is not None
    name = (message.text or "").strip()
    if len(name) < 3 or len(name) > 80:
        await message.answer(
            "Iltimos, to'g'ri Ism va Familiya kiriting (kamida 3 ta belgi).\n"
            "<i>Masalan: Karimova Madina</i>",
            parse_mode="HTML",
        )
        return

    user = await db.upsert_user(
        user_id=message.from_user.id,
        full_name=name,
        username=message.from_user.username,
    )
    await state.clear()
    await message.answer(
        f"✅ Ro'yxatdan o'tdingiz: <b>{html.escape(user.full_name)}</b>!\n\n"
        "Endi test yaratishingiz yoki <code>KOD*javoblar</code> formatida javob yuborishingiz mumkin.",
        reply_markup=main_menu_keyboard(can_create_test(user.user_id, settings)),
        parse_mode="HTML",
    )


@router.message(StateFilter("*"), F.text == BTN_CANCEL)
@router.message(StateFilter("*"), Command("cancel"))
async def cmd_cancel(
    message: Message,
    state: FSMContext,
    db: Database,
    settings: Settings,
) -> None:
    assert message.from_user is not None
    await state.clear()
    user = await db.get_user(message.from_user.id)
    if user is None:
        await state.set_state(RegistrationState.waiting_full_name)
        await message.answer("Avval Ism va Familiyangizni kiriting:")
        return
    await message.answer(
        "Amal bekor qilindi. Asosiy menyu:",
        reply_markup=main_menu_keyboard(can_create_test(user.user_id, settings)),
    )


@router.message(F.text == BTN_HELP)
@router.message(Command("help"))
async def cmd_help(message: Message) -> None:
    await message.answer(HELP_TEXT, parse_mode="HTML")


@router.message(F.text == BTN_PROFILE)
async def show_profile(message: Message, db: Database, state: FSMContext) -> None:
    assert message.from_user is not None
    user = await db.get_user(message.from_user.id)
    if user is None:
        await state.set_state(RegistrationState.waiting_full_name)
        await message.answer("Avval Ism va Familiyangizni kiriting:")
        return

    uname = f"@{html.escape(user.username)}" if user.username else "yo'q"
    await message.answer(
        f"👤 <b>Sizning profilingiz</b>\n\n"
        f"• Ism Familiya: <b>{html.escape(user.full_name)}</b>\n"
        f"• Username: {uname}\n"
        f"• Telegram ID: <code>{user.user_id}</code>",
        reply_markup=profile_keyboard(),
        parse_mode="HTML",
    )


@router.callback_query(F.data == "profile:edit_name")
async def start_edit_name(callback: CallbackQuery, state: FSMContext) -> None:
    await callback.answer()
    await state.set_state(EditProfileState.waiting_new_name)
    if callback.message:
        await callback.message.answer(
            "Yangi <b>Ism va Familiyangizni</b> yuboring:",
            reply_markup=cancel_keyboard(),
            parse_mode="HTML",
        )


@router.message(EditProfileState.waiting_new_name, F.text)
async def save_new_name(
    message: Message,
    state: FSMContext,
    db: Database,
    settings: Settings,
) -> None:
    assert message.from_user is not None
    name = (message.text or "").strip()
    if len(name) < 3 or len(name) > 80:
        await message.answer("Iltimos, kamida 3 ta belgidan iborat Ism Familiya kiriting.")
        return

    user = await db.upsert_user(
        user_id=message.from_user.id,
        full_name=name,
        username=message.from_user.username,
    )
    await state.clear()
    await message.answer(
        f"✅ Ism-familiyangiz yangilandi: <b>{html.escape(user.full_name)}</b>",
        reply_markup=main_menu_keyboard(can_create_test(user.user_id, settings)),
        parse_mode="HTML",
    )
