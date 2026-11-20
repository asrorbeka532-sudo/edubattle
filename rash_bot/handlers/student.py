from __future__ import annotations

import html

from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from rash_bot.config import Settings
from rash_bot.database import Database, TestRecord
from rash_bot.handlers.start import can_create_test
from rash_bot.keyboards import (
    BTN_MY_RESULTS,
    BTN_SUBMIT,
    cancel_keyboard,
    main_menu_keyboard,
)
from rash_bot.parser import (
    ParseError,
    grade_submission,
    parse_student_answers,
    split_code_and_answers,
)
from rash_bot.states import RegistrationState, SubmitAnswerState

router = Router(name="student")


def _submission_format_hint(test: TestRecord) -> str:
    if test.open_count > 0 and test.closed_count > 0:
        first_open = next(q.number for q in test.questions if q.q_type == "open")
        return (
            f"Bu testda <b>{test.closed_count} ta yopiq</b> va <b>{test.open_count} ta ochiq</b> savol bor.\n\n"
            "Javoblarni quyidagi ko'rinishda yuboring:\n"
            f"<pre>abcd... ({test.closed_count} ta harf)\n"
            f"{first_open}: 12.5\n"
            f"{first_open + 1}: 42</pre>"
        )
    if test.open_count > 0:
        return (
            f"Bu testda <b>{test.open_count} ta ochiq</b> savol bor.\n"
            "Javoblarni raqam bilan yuboring:\n"
            "<pre>1: 12.5\n2: 42</pre>"
        )
    return (
        f"Bu testda <b>{test.closed_count} ta yopiq</b> savol bor.\n"
        f"Namuna: <code>abcd...</code> ({test.closed_count} ta harf) yoki <code>1a2b3c...</code>"
    )


async def _process_submission(
    message: Message,
    db: Database,
    settings: Settings,
    test: TestRecord,
    answers_body: str,
    state: FSMContext,
) -> bool:
    """Validate, grade, and store a student's submission. Returns True on success."""
    assert message.from_user is not None
    user_id = message.from_user.id

    if test.status != "active":
        await message.answer(
            f"🏁 <b>{html.escape(test.title)}</b> (<code>{test.code}</code>) testi yakunlangan. "
            "Yangi javoblar qabul qilinmaydi.",
            reply_markup=main_menu_keyboard(can_create_test(user_id, settings)),
            parse_mode="HTML",
        )
        await state.clear()
        return False

    existing = await db.get_submission(test.id, user_id)
    if existing is not None:
        pct = 100.0 * existing.raw_score / max(test.total_questions, 1)
        await message.answer(
            f"ℹ️ Siz <b>{html.escape(test.title)}</b> (<code>{test.code}</code>) testiga "
            "allaqachon javob yuborgansiz.\n"
            f"✅ Qayd etilgan natija: <b>{existing.raw_score} / {test.total_questions}</b> ({pct:.1f}%)",
            reply_markup=main_menu_keyboard(can_create_test(user_id, settings)),
            parse_mode="HTML",
        )
        await state.clear()
        return False

    try:
        parsed_answers = parse_student_answers(answers_body, test.questions)
    except ParseError as exc:
        await message.answer(
            f"❌ <b>Javob formatida xatolik:</b>\n{html.escape(str(exc))}\n\n"
            f"{_submission_format_hint(test)}",
            parse_mode="HTML",
        )
        return False

    binary, raw_score, wrong_numbers = grade_submission(parsed_answers, test.questions)
    await db.create_submission(
        test_id=test.id,
        user_id=user_id,
        answers=parsed_answers,
        binary=binary,
        raw_score=raw_score,
        wrong_numbers=wrong_numbers,
    )
    await state.clear()

    pct = 100.0 * raw_score / max(test.total_questions, 1)
    await message.answer(
        f"✅ <b>Javoblaringiz qabul qilindi!</b>\n\n"
        f"📌 Test: <b>{html.escape(test.title)}</b> (<code>{test.code}</code>)\n"
        f"✅ Dastlabki natija: <b>{raw_score} / {test.total_questions}</b> ({pct:.1f}%)\n\n"
        f"⏳ <i>Rasch balli va Milliy Sertifikat darajasi o'qituvchi testni yakunlagach sizga yuboriladi.</i>",
        reply_markup=main_menu_keyboard(can_create_test(user_id, settings)),
        parse_mode="HTML",
    )
    return True


# ---------- Guided Submission Flow ----------


@router.message(F.text == BTN_SUBMIT)
async def start_submit(
    message: Message,
    state: FSMContext,
    db: Database,
) -> None:
    assert message.from_user is not None
    user = await db.get_user(message.from_user.id)
    if user is None:
        await state.set_state(RegistrationState.waiting_full_name)
        await message.answer("Avval Ism va Familiyangizni kiriting:")
        return

    await state.set_state(SubmitAnswerState.waiting_code_or_full)
    await message.answer(
        "📝 <b>Test javoblarini yuborish</b>\n\n"
        "Test kodini yuboring (masalan: <code>4821</code>) "
        "yoki birdaniga <code>KOD*javoblar</code> formatida yuboring.\n"
        "<i>Namuna:</i> <code>4821*abcdabcd...</code>",
        reply_markup=cancel_keyboard(),
        parse_mode="HTML",
    )


@router.message(SubmitAnswerState.waiting_code_or_full, F.text)
async def receive_code_or_full(
    message: Message,
    state: FSMContext,
    db: Database,
    settings: Settings,
) -> None:
    raw = (message.text or "").strip()

    split = split_code_and_answers(raw)
    if split is not None:
        code, answers_body = split
        test = await db.get_test_by_code(code)
        if test is None:
            await message.answer(
                f"❌ <code>{html.escape(code)}</code> kodli test topilmadi. Kodni tekshirib qayta yuboring.",
                parse_mode="HTML",
            )
            return
        await _process_submission(message, db, settings, test, answers_body, state)
        return

    # Otherwise treat message as test code only
    code = raw.strip()
    if not code.isdigit():
        await message.answer(
            "Iltimos, faqat raqamli test kodini (masalan: <code>4821</code>) "
            "yoki <code>4821*abcd...</code> ko'rinishida yuboring.",
            parse_mode="HTML",
        )
        return

    test = await db.get_test_by_code(code)
    if test is None:
        await message.answer(
            f"❌ <code>{html.escape(code)}</code> kodli test topilmadi.",
            parse_mode="HTML",
        )
        return

    if test.status != "active":
        assert message.from_user is not None
        await state.clear()
        await message.answer(
            f"🏁 <b>{html.escape(test.title)}</b> (<code>{test.code}</code>) testi allaqachon yakunlangan.",
            reply_markup=main_menu_keyboard(can_create_test(message.from_user.id, settings)),
            parse_mode="HTML",
        )
        return

    await state.update_data(test_id=test.id)
    await state.set_state(SubmitAnswerState.waiting_answers)
    await message.answer(
        f"📌 Test: <b>{html.escape(test.title)}</b> (<code>{test.code}</code>)\n\n"
        f"{_submission_format_hint(test)}",
        parse_mode="HTML",
    )


@router.message(SubmitAnswerState.waiting_answers, F.text)
async def receive_guided_answers(
    message: Message,
    state: FSMContext,
    db: Database,
    settings: Settings,
) -> None:
    data = await state.get_data()
    test_id = data.get("test_id")
    if not test_id:
        await state.clear()
        await message.answer("Qaytadan urinib ko'ring.")
        return

    test = await db.get_test_by_id(int(test_id))
    if test is None:
        await state.clear()
        await message.answer("Test topilmadi.")
        return

    await _process_submission(
        message, db, settings, test, (message.text or "").strip(), state
    )


# ---------- Student Results ----------


@router.message(F.text == BTN_MY_RESULTS)
async def show_my_results(message: Message, db: Database, state: FSMContext) -> None:
    assert message.from_user is not None
    user = await db.get_user(message.from_user.id)
    if user is None:
        await state.set_state(RegistrationState.waiting_full_name)
        await message.answer("Avval Ism va Familiyangizni kiriting:")
        return

    rows = await db.list_user_results(user.user_id, limit=15)
    if not rows:
        await message.answer(
            "📊 Siz hali birorta testda qatnashmagansiz.\n"
            "Javob yuborish uchun <b>📝 Test yuborish</b> tugmasini bosing yoki "
            "<code>KOD*javoblar</code> yuboring.",
            parse_mode="HTML",
        )
        return

    lines = ["📊 <b>Oxirgi natijalaringiz:</b>\n"]
    for test, sub in rows:
        pct = 100.0 * sub.raw_score / max(test.total_questions, 1)
        if test.status == "finished" and sub.rasch_t_score is not None:
            lines.append(
                f"🏁 <b>{html.escape(test.title)}</b> (<code>{test.code}</code>)\n"
                f"   • To'g'ri: {sub.raw_score}/{test.total_questions} ({pct:.1f}%)\n"
                f"   • Rasch ball: <b>{sub.rasch_t_score:.2f}</b> | "
                f"Daraja: <b>{sub.rasch_grade}</b> | O'rin: <b>#{sub.rasch_rank}</b>"
            )
        else:
            lines.append(
                f"⏳ <b>{html.escape(test.title)}</b> (<code>{test.code}</code>)\n"
                f"   • To'g'ri: {sub.raw_score}/{test.total_questions} ({pct:.1f}%) "
                f"<i>(Rasch kutilmoqda)</i>"
            )

    await message.answer("\n\n".join(lines), parse_mode="HTML")


# ---------- Instant Quick Submission (`CODE*answers` outside any FSM state) ----------


@router.message(F.text)
async def quick_submit_handler(
    message: Message,
    state: FSMContext,
    db: Database,
    settings: Settings,
) -> None:
    raw = (message.text or "").strip()
    split = split_code_and_answers(raw)
    if split is None:
        return

    assert message.from_user is not None
    user = await db.get_user(message.from_user.id)
    if user is None:
        await state.set_state(RegistrationState.waiting_full_name)
        await message.answer(
            "Javob yuborishdan oldin Ism va Familiyangizni kiriting.\n"
            "<i>Masalan: Aliyev Vali</i>",
            parse_mode="HTML",
        )
        return

    code, answers_body = split
    test = await db.get_test_by_code(code)
    if test is None:
        await message.answer(
            f"❌ <code>{html.escape(code)}</code> kodli test topilmadi.",
            parse_mode="HTML",
        )
        return

    await _process_submission(message, db, settings, test, answers_body, state)
