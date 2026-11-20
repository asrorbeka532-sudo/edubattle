from __future__ import annotations

import asyncio
import html
from collections import Counter

from aiogram import Bot, F, Router
from aiogram.exceptions import TelegramBadRequest, TelegramForbiddenError
from aiogram.fsm.context import FSMContext
from aiogram.types import BufferedInputFile, CallbackQuery, Message

from rash_bot.config import Settings
from rash_bot.database import Database, SubmissionRecord, TestRecord
from rash_bot.exporter import build_excel_report
from rash_bot.handlers.start import can_create_test
from rash_bot.keyboards import (
    BTN_CREATE_TEST,
    BTN_MY_TESTS,
    cancel_keyboard,
    confirm_delete_keyboard,
    confirm_test_keyboard,
    main_menu_keyboard,
    teacher_tests_keyboard,
    test_manage_keyboard,
)
from rash_bot.parser import ParseError, QuestionSpec, parse_answer_key
from rash_bot.rasch import fit_rasch_model
from rash_bot.states import CreateTestState, RegistrationState

router = Router(name="teacher")


def _format_key_preview(questions: list[QuestionSpec], limit: int = 50) -> str:
    parts: list[str] = []
    for q in questions[:limit]:
        if q.q_type == "closed":
            parts.append(f"{q.number}{q.display_key}")
        else:
            parts.append(f"{q.number}: {html.escape(q.display_key)}")
    preview = "  ".join(parts)
    if len(questions) > limit:
        preview += f"  … (+{len(questions) - limit} ta)"
    return preview


def _format_test_card(test: TestRecord, sub_count: int) -> str:
    status_label = "🟢 Faol (javoblar qabul qilinmoqda)" if test.status == "active" else "🏁 Yakunlangan (Rasch hisoblangan)"
    text = (
        f"📌 <b>{html.escape(test.title)}</b>\n\n"
        f"🔑 Test kodi: <code>{test.code}</code>\n"
        f"📊 Holati: {status_label}\n"
        f"📝 Savollar: <b>{test.total_questions} ta</b> "
        f"(yopiq: {test.closed_count}, ochiq: {test.open_count})\n"
        f"👥 Ishtirokchilar: <b>{sub_count} nafar</b>\n"
        f"🕒 Yaratilgan: {test.created_at} (UTC)"
    )
    if test.finished_at:
        text += f"\n🏁 Yakunlangan: {test.finished_at} (UTC)"
    return text


def _format_top_leaderboard(
    test: TestRecord, submissions: list[SubmissionRecord], top_n: int = 20
) -> str:
    if not submissions:
        return "Hali birorta ham ishtirokchi javob yubormagan."

    lines = [
        f"🏆 <b>{html.escape(test.title)}</b> (Kod: <code>{test.code}</code>)\n"
        f"👥 Jami ishtirokchilar: <b>{len(submissions)}</b>\n"
    ]

    if test.status == "finished":
        grade_counts = Counter(s.rasch_grade or "Darajasiz" for s in submissions)
        order = ["A+", "A", "B+", "B", "C+", "C", "Darajasiz"]
        dist = " | ".join(
            f"<b>{g}</b>: {grade_counts[g]}" for g in order if grade_counts.get(g)
        )
        if dist:
            lines.append(f"📈 Darajalar: {dist}\n")

    sorted_subs = sorted(
        submissions,
        key=lambda s: (
            s.rasch_rank if s.rasch_rank is not None else 999999,
            -s.raw_score,
            s.id,
        ),
    )

    medals = {1: "🥇", 2: "🥈", 3: "🥉"}
    for idx, sub in enumerate(sorted_subs[:top_n], start=1):
        rank = sub.rasch_rank if sub.rasch_rank is not None else idx
        prefix = medals.get(rank, f"{rank}.")
        name = html.escape(sub.full_name)
        if sub.rasch_t_score is not None and sub.rasch_grade is not None:
            lines.append(
                f"{prefix} <b>{name}</b> — {sub.raw_score}/{test.total_questions} | "
                f"<b>{sub.rasch_t_score:.2f}</b> ball (<b>{sub.rasch_grade}</b>)"
            )
        else:
            pct = 100.0 * sub.raw_score / max(test.total_questions, 1)
            lines.append(
                f"{prefix} <b>{name}</b> — {sub.raw_score}/{test.total_questions} ({pct:.1f}%)"
            )

    if len(submissions) > top_n:
        lines.append(f"\n<i>… va yana {len(submissions) - top_n} nafar ishtirokchi (to'liq ro'yxat Excel faylda).</i>")

    return "\n".join(lines)


def _format_student_result_card(
    test: TestRecord, sub: SubmissionRecord, total_participants: int
) -> str:
    pct = 100.0 * sub.raw_score / max(test.total_questions, 1)
    wrong_text = (
        ", ".join(str(x) for x in sub.wrong_numbers)
        if sub.wrong_numbers
        else "Xato yo'q! 🎉"
    )
    if len(wrong_text) > 250:
        wrong_text = wrong_text[:247] + "..."

    return (
        f"🎓 <b>Rasch Natijangiz Tayyor!</b>\n\n"
        f"📌 Test: <b>{html.escape(test.title)}</b> (<code>{test.code}</code>)\n"
        f"👤 Ishtirokchi: <b>{html.escape(sub.full_name)}</b>\n"
        f"━━━━━━━━━━━━━━━━━━\n"
        f"✅ To'g'ri javoblar: <b>{sub.raw_score} / {test.total_questions}</b> ({pct:.1f}%)\n"
        f"📐 Rasch Logit (θ): <b>{sub.rasch_theta:.4f}</b>\n"
        f"🎯 Rasch Ball (T-ball): <b>{sub.rasch_t_score:.2f}</b>\n"
        f"🏅 Milliy Sertifikat darajasi: <b>{sub.rasch_grade}</b>\n"
        f"🏆 O'rningiz: <b>{sub.rasch_rank} / {total_participants}</b>\n"
        f"━━━━━━━━━━━━━━━━━━\n"
        f"❌ Xato savollar: {wrong_text}"
    )


# ---------- Create Test Flow ----------


@router.message(F.text == BTN_CREATE_TEST)
async def start_create_test(
    message: Message,
    state: FSMContext,
    db: Database,
    settings: Settings,
) -> None:
    assert message.from_user is not None
    user = await db.get_user(message.from_user.id)
    if user is None:
        await state.set_state(RegistrationState.waiting_full_name)
        await message.answer("Avval Ism va Familiyangizni kiriting:")
        return

    if not can_create_test(user.user_id, settings):
        await message.answer("⛔ Test yaratish faqat ruxsat etilgan o'qituvchilar uchun.")
        return

    await state.set_state(CreateTestState.waiting_title)
    await message.answer(
        "➕ <b>Yangi test yaratish</b>\n\n"
        "1-qadam: Test nomini kiriting.\n"
        "<i>Masalan: Matematika Milliy Sertifikat #1</i>",
        reply_markup=cancel_keyboard(),
        parse_mode="HTML",
    )


@router.message(CreateTestState.waiting_title, F.text)
async def receive_test_title(message: Message, state: FSMContext) -> None:
    title = (message.text or "").strip()
    if len(title) < 2 or len(title) > 100:
        await message.answer("Test nomi 2 dan 100 tagacha belgidan iborat bo'lishi kerak.")
        return

    await state.update_data(title=title)
    await state.set_state(CreateTestState.waiting_answer_key)
    await message.answer(
        "2-qadam: <b>Javoblar kalitini</b> yuboring.\n\n"
        "Qo'llab-quvvatlanadigan formatlar:\n"
        "1) Oddiy yopiq test:\n"
        "<code>abcdabcdab</code>\n\n"
        "2) Raqamli yopiq test:\n"
        "<code>1a2b3c4d5a</code>\n\n"
        "3) Yopiq + Ochiq savollar (Milliy Sertifikat):\n"
        "<pre>abcd... (yopiq kalitlar)\n"
        "36: 12.5\n"
        "37: 42|42.0\n"
        "38: -3</pre>\n"
        "<i>Eslatma: ochiq savollarda bir nechta to'g'ri variantni <code>|</code> bilan ajratishingiz mumkin.</i>",
        parse_mode="HTML",
    )


@router.message(CreateTestState.waiting_answer_key, F.text)
async def receive_answer_key(message: Message, state: FSMContext) -> None:
    raw = (message.text or "").strip()
    try:
        questions = parse_answer_key(raw)
    except ParseError as exc:
        await message.answer(
            f"❌ <b>Kalitda xatolik:</b>\n{html.escape(str(exc))}\n\n"
            "Iltimos, kalitni to'g'rilab qayta yuboring.",
            parse_mode="HTML",
        )
        return

    data = await state.get_data()
    title = data["title"]
    closed_cnt = sum(1 for q in questions if q.q_type == "closed")
    open_cnt = sum(1 for q in questions if q.q_type == "open")

    await state.update_data(questions=[q.to_dict() for q in questions])
    await state.set_state(CreateTestState.waiting_confirm)

    preview = _format_key_preview(questions)
    await message.answer(
        f"📋 <b>Testni tasdiqlang:</b>\n\n"
        f"📌 Nomi: <b>{html.escape(title)}</b>\n"
        f"📝 Jami savollar: <b>{len(questions)} ta</b> "
        f"(yopiq: {closed_cnt}, ochiq: {open_cnt})\n\n"
        f"🔑 Kalit ko'rinishi:\n<code>{preview}</code>",
        reply_markup=confirm_test_keyboard(),
        parse_mode="HTML",
    )


@router.callback_query(CreateTestState.waiting_confirm, F.data == "create_test:retry")
async def retry_answer_key(callback: CallbackQuery, state: FSMContext) -> None:
    await callback.answer()
    await state.set_state(CreateTestState.waiting_answer_key)
    if callback.message:
        await callback.message.answer("Javoblar kalitini qaytadan yuboring:")


@router.callback_query(CreateTestState.waiting_confirm, F.data == "create_test:cancel")
async def cancel_create_test(
    callback: CallbackQuery, state: FSMContext, settings: Settings
) -> None:
    await callback.answer("Bekor qilindi")
    await state.clear()
    if callback.message:
        await callback.message.edit_text("❌ Test yaratish bekor qilindi.")
        await callback.message.answer(
            "Asosiy menyu:",
            reply_markup=main_menu_keyboard(can_create_test(callback.from_user.id, settings)),
        )


@router.callback_query(CreateTestState.waiting_confirm, F.data == "create_test:confirm")
async def confirm_create_test(
    callback: CallbackQuery,
    state: FSMContext,
    db: Database,
    settings: Settings,
) -> None:
    data = await state.get_data()
    if "title" not in data or "questions" not in data:
        await callback.answer("Sessiya tugagan, qaytadan boshlang.", show_alert=True)
        await state.clear()
        return

    questions = [QuestionSpec.from_dict(x) for x in data["questions"]]
    test = await db.create_test(
        teacher_id=callback.from_user.id,
        title=data["title"],
        questions=questions,
    )
    await state.clear()
    await callback.answer("Test yaratildi!")

    if test.open_count > 0:
        sample = (
            f"<code>{test.code}*abcd... ({test.closed_count} ta harf)\n"
            f"{test.closed_count + 1}: javob</code>"
        )
    else:
        sample = f"<code>{test.code}*abcd...</code> ({test.closed_count} ta harf)"

    share_msg = (
        f"✅ <b>Test muvaffaqiyatli yaratildi!</b>\n\n"
        f"📢 <b>O'quvchilarga yuborish uchun xabar:</b>\n"
        f"━━━━━━━━━━━━━━━━━━\n"
        f"📌 Test: <b>{html.escape(test.title)}</b>\n"
        f"🔑 Test kodi: <code>{test.code}</code>\n"
        f"📝 Savollar: {test.total_questions} ta "
        f"(yopiq: {test.closed_count}, ochiq: {test.open_count})\n\n"
        f"Javob yuborish namunasi:\n{sample}\n"
        f"━━━━━━━━━━━━━━━━━━"
    )
    if callback.message:
        await callback.message.edit_text(share_msg, parse_mode="HTML")
        await callback.message.answer(
            "Testni boshqarish uchun <b>📋 Mening testlarim</b> bo'limiga kiring.",
            reply_markup=main_menu_keyboard(can_create_test(callback.from_user.id, settings)),
            parse_mode="HTML",
        )


# ---------- Manage Teacher Tests ----------


@router.message(F.text == BTN_MY_TESTS)
async def list_my_tests(message: Message, db: Database, state: FSMContext) -> None:
    assert message.from_user is not None
    user = await db.get_user(message.from_user.id)
    if user is None:
        await state.set_state(RegistrationState.waiting_full_name)
        await message.answer("Avval Ism va Familiyangizni kiriting:")
        return

    tests = await db.list_teacher_tests(user.user_id)
    if not tests:
        await message.answer(
            "Siz hali birorta test yaratmagansiz.\n"
            "Boshlash uchun <b>➕ Test yaratish</b> tugmasini bosing.",
            parse_mode="HTML",
        )
        return

    await message.answer(
        "📋 <b>Siz yaratgan testlar:</b>\n<i>Boshqarish uchun testni tanlang:</i>",
        reply_markup=teacher_tests_keyboard(tests),
        parse_mode="HTML",
    )


@router.callback_query(F.data == "test:list")
async def cb_list_tests(callback: CallbackQuery, db: Database) -> None:
    await callback.answer()
    tests = await db.list_teacher_tests(callback.from_user.id)
    if not callback.message:
        return
    if not tests:
        await callback.message.edit_text("Sizda testlar mavjud emas.")
        return
    await callback.message.edit_text(
        "📋 <b>Siz yaratgan testlar:</b>\n<i>Boshqarish uchun testni tanlang:</i>",
        reply_markup=teacher_tests_keyboard(tests),
        parse_mode="HTML",
    )


async def _load_owned_test(
    callback: CallbackQuery, db: Database, test_id: int
) -> TestRecord | None:
    test = await db.get_test_by_id(test_id)
    if test is None:
        await callback.answer("Test topilmadi.", show_alert=True)
        return None
    if test.teacher_id != callback.from_user.id:
        await callback.answer("Bu test sizga tegishli emas.", show_alert=True)
        return None
    return test


@router.callback_query(F.data.startswith("test:view:"))
async def cb_view_test(callback: CallbackQuery, db: Database) -> None:
    test_id = int(callback.data.split(":")[2])
    test = await _load_owned_test(callback, db, test_id)
    if test is None:
        return
    subs = await db.list_test_submissions(test.id)
    await callback.answer()
    if callback.message:
        try:
            await callback.message.edit_text(
                _format_test_card(test, len(subs)),
                reply_markup=test_manage_keyboard(test, len(subs)),
                parse_mode="HTML",
            )
        except TelegramBadRequest:
            pass


@router.callback_query(F.data.startswith("test:key:"))
async def cb_show_key(callback: CallbackQuery, db: Database) -> None:
    test_id = int(callback.data.split(":")[2])
    test = await _load_owned_test(callback, db, test_id)
    if test is None:
        return
    await callback.answer()
    lines = []
    for q in test.questions:
        if q.q_type == "closed":
            lines.append(f"{q.number}) {q.display_key}")
        else:
            lines.append(f"{q.number}) {html.escape(q.display_key)} [ochiq]")
    key_body = "\n".join(lines)
    if len(key_body) > 3500:
        key_body = key_body[:3490] + "\n..."
    if callback.message:
        await callback.message.answer(
            f"🔑 <b>{html.escape(test.title)}</b> (<code>{test.code}</code>) kaliti:\n\n"
            f"<pre>{key_body}</pre>",
            parse_mode="HTML",
        )


@router.callback_query(F.data.startswith("test:top:"))
async def cb_show_top(callback: CallbackQuery, db: Database) -> None:
    test_id = int(callback.data.split(":")[2])
    test = await _load_owned_test(callback, db, test_id)
    if test is None:
        return
    subs = await db.list_test_submissions(test.id)
    await callback.answer()
    if callback.message:
        await callback.message.answer(
            _format_top_leaderboard(test, subs, top_n=25),
            parse_mode="HTML",
        )


@router.callback_query(F.data.startswith("test:rasch:"))
async def cb_run_rasch(callback: CallbackQuery, db: Database) -> None:
    test_id = int(callback.data.split(":")[2])
    test = await _load_owned_test(callback, db, test_id)
    if test is None:
        return

    subs = await db.list_test_submissions(test.id)
    if not subs:
        await callback.answer(
            "Rasch hisoblash uchun kamida 1 nafar ishtirokchi javob yuborgan bo'lishi kerak!",
            show_alert=True,
        )
        return

    await callback.answer("⏳ Rasch modeli hisoblanmoqda...")

    matrix = [s.binary for s in subs]
    report = fit_rasch_model(matrix)

    await db.save_rasch_results(
        test_id=test.id,
        submission_ids=[s.id for s in subs],
        person_results=report.persons,
        item_results=report.items,
        mean_theta=report.mean_theta,
        std_theta=report.std_theta,
        warning=report.warning,
    )

    updated_test = await db.get_test_by_id(test.id)
    updated_subs = await db.list_test_submissions(test.id)
    assert updated_test is not None

    if callback.message:
        try:
            await callback.message.edit_text(
                _format_test_card(updated_test, len(updated_subs)),
                reply_markup=test_manage_keyboard(updated_test, len(updated_subs)),
                parse_mode="HTML",
            )
        except TelegramBadRequest:
            pass

        # Show Rasch summary + hardest/easiest items
        hardest = sorted(report.items, key=lambda x: x.beta, reverse=True)[:3]
        easiest = sorted(report.items, key=lambda x: x.beta)[:3]
        hard_str = ", ".join(
            f"№{it.item_number} ({it.p_value * 100:.0f}%, β={it.beta:+.2f})"
            for it in hardest
        )
        easy_str = ", ".join(
            f"№{it.item_number} ({it.p_value * 100:.0f}%, β={it.beta:+.2f})"
            for it in easiest
        )

        summary_msg = _format_top_leaderboard(updated_test, updated_subs, top_n=20)
        summary_msg += (
            f"\n\n📐 <b>Rasch tahlili:</b>\n"
            f"• O'rtacha θ: <code>{report.mean_theta:+.4f}</code> | SD: <code>{report.std_theta:.4f}</code>\n"
            f"• Eng qiyin savollar: {hard_str}\n"
            f"• Eng oson savollar: {easy_str}"
        )
        if report.warning:
            summary_msg += f"\n\n⚠️ <i>{html.escape(report.warning)}</i>"

        await callback.message.answer(summary_msg, parse_mode="HTML")


@router.callback_query(F.data.startswith("test:excel:"))
async def cb_export_excel(callback: CallbackQuery, db: Database) -> None:
    test_id = int(callback.data.split(":")[2])
    test = await _load_owned_test(callback, db, test_id)
    if test is None:
        return
    subs = await db.list_test_submissions(test.id)
    if not subs:
        await callback.answer("Ishtirokchilar yo'q.", show_alert=True)
        return

    await callback.answer("📥 Excel fayl tayyorlanmoqda...")
    xlsx_bytes = build_excel_report(test, subs)
    filename = f"rasch_test_{test.code}.xlsx"
    doc = BufferedInputFile(xlsx_bytes, filename=filename)
    if callback.message:
        await callback.message.answer_document(
            document=doc,
            caption=(
                f"📊 <b>{html.escape(test.title)}</b> (Kod: <code>{test.code}</code>)\n"
                f"Ishtirokchilar: {len(subs)} nafar | 3 ta varaq: Natijalar, Savollar tahlili, 0/1 Matritsa."
            ),
            parse_mode="HTML",
        )


@router.callback_query(F.data.startswith("test:broadcast:"))
async def cb_broadcast_results(
    callback: CallbackQuery, db: Database, bot: Bot
) -> None:
    test_id = int(callback.data.split(":")[2])
    test = await _load_owned_test(callback, db, test_id)
    if test is None:
        return
    if test.status != "finished":
        await callback.answer(
            "Avval testni yakunlab, Rasch ballarini hisoblang!", show_alert=True
        )
        return

    subs = await db.list_test_submissions(test.id)
    if not subs:
        await callback.answer("Yuborish uchun ishtirokchilar yo'q.", show_alert=True)
        return

    await callback.answer("📢 Natijalar yuborilmoqda...")
    sent = 0
    failed = 0
    total = len(subs)
    for sub in subs:
        if sub.rasch_t_score is None or sub.rasch_grade is None:
            continue
        card = _format_student_result_card(test, sub, total)
        try:
            await bot.send_message(chat_id=sub.user_id, text=card, parse_mode="HTML")
            sent += 1
        except (TelegramForbiddenError, TelegramBadRequest):
            failed += 1
        await asyncio.sleep(0.05)

    if callback.message:
        await callback.message.answer(
            f"📢 <b>Natijalar tarqatildi!</b>\n"
            f"✅ Yetkazildi: <b>{sent}</b>\n"
            f"⚠️ Yetkazilmadi (bot bloklangan): <b>{failed}</b>",
            parse_mode="HTML",
        )


@router.callback_query(F.data.startswith("test:reopen:"))
async def cb_reopen_test(callback: CallbackQuery, db: Database) -> None:
    test_id = int(callback.data.split(":")[2])
    test = await _load_owned_test(callback, db, test_id)
    if test is None:
        return
    await db.reopen_test(test.id)
    updated = await db.get_test_by_id(test.id)
    subs = await db.list_test_submissions(test.id)
    assert updated is not None
    await callback.answer("Test qayta ochildi!")
    if callback.message:
        await callback.message.edit_text(
            _format_test_card(updated, len(subs)),
            reply_markup=test_manage_keyboard(updated, len(subs)),
            parse_mode="HTML",
        )


@router.callback_query(F.data.startswith("test:del_ask:"))
async def cb_delete_ask(callback: CallbackQuery, db: Database) -> None:
    test_id = int(callback.data.split(":")[2])
    test = await _load_owned_test(callback, db, test_id)
    if test is None:
        return
    await callback.answer()
    if callback.message:
        await callback.message.edit_text(
            f"⚠️ <b>{html.escape(test.title)}</b> (<code>{test.code}</code>) testini va "
            "uning barcha natijalarini butunlay o'chirmoqchimisiz?",
            reply_markup=confirm_delete_keyboard(test.id),
            parse_mode="HTML",
        )


@router.callback_query(F.data.startswith("test:del_yes:"))
async def cb_delete_confirm(callback: CallbackQuery, db: Database) -> None:
    test_id = int(callback.data.split(":")[2])
    test = await _load_owned_test(callback, db, test_id)
    if test is None:
        return
    await db.delete_test(test.id)
    await callback.answer("Test o'chirildi")
    if callback.message:
        await callback.message.edit_text(
            f"🗑 <b>{html.escape(test.title)}</b> testi o'chirildi.",
            parse_mode="HTML",
        )
