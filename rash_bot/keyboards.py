from __future__ import annotations

from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
)

from rash_bot.database import TestRecord

BTN_SUBMIT = "📝 Test yuborish"
BTN_MY_RESULTS = "📊 Mening natijalarim"
BTN_CREATE_TEST = "➕ Test yaratish"
BTN_MY_TESTS = "📋 Mening testlarim"
BTN_PROFILE = "👤 Profil"
BTN_HELP = "ℹ️ Yordam"
BTN_CANCEL = "❌ Bekor qilish"


def main_menu_keyboard(can_create_test: bool = True) -> ReplyKeyboardMarkup:
    rows = [
        [KeyboardButton(text=BTN_SUBMIT), KeyboardButton(text=BTN_MY_RESULTS)],
    ]
    if can_create_test:
        rows.append(
            [KeyboardButton(text=BTN_CREATE_TEST), KeyboardButton(text=BTN_MY_TESTS)]
        )
    rows.append([KeyboardButton(text=BTN_PROFILE), KeyboardButton(text=BTN_HELP)])
    return ReplyKeyboardMarkup(keyboard=rows, resize_keyboard=True)


def cancel_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=BTN_CANCEL)]],
        resize_keyboard=True,
    )


def confirm_test_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="✅ Tasdiqlash va yaratish", callback_data="create_test:confirm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="✏️ Kalitni qayta kiritish", callback_data="create_test:retry"
                ),
                InlineKeyboardButton(
                    text="❌ Bekor qilish", callback_data="create_test:cancel"
                ),
            ],
        ]
    )


def teacher_tests_keyboard(
    tests_with_counts: list[tuple[TestRecord, int]]
) -> InlineKeyboardMarkup:
    buttons: list[list[InlineKeyboardButton]] = []
    for test, count in tests_with_counts:
        icon = "🟢" if test.status == "active" else "🏁"
        title_short = test.title if len(test.title) <= 24 else test.title[:23] + "…"
        label = f"{icon} [{test.code}] {title_short} ({count})"
        buttons.append(
            [InlineKeyboardButton(text=label, callback_data=f"test:view:{test.id}")]
        )
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def test_manage_keyboard(test: TestRecord, sub_count: int) -> InlineKeyboardMarkup:
    rows: list[list[InlineKeyboardButton]] = []
    if test.status == "active":
        rows.append(
            [
                InlineKeyboardButton(
                    text="🧮 Yakunlash va Rasch hisoblash",
                    callback_data=f"test:rasch:{test.id}",
                )
            ]
        )
    else:
        rows.append(
            [
                InlineKeyboardButton(
                    text="🧮 Rasch qayta hisoblash",
                    callback_data=f"test:rasch:{test.id}",
                ),
                InlineKeyboardButton(
                    text="🔄 Qayta ochish",
                    callback_data=f"test:reopen:{test.id}",
                ),
            ]
        )
        if sub_count > 0:
            rows.append(
                [
                    InlineKeyboardButton(
                        text="📢 Natijalarni o'quvchilarga yuborish",
                        callback_data=f"test:broadcast:{test.id}",
                    )
                ]
            )

    if sub_count > 0:
        rows.append(
            [
                InlineKeyboardButton(
                    text="🏆 Top natijalar",
                    callback_data=f"test:top:{test.id}",
                ),
                InlineKeyboardButton(
                    text="📥 Excel (.xlsx)",
                    callback_data=f"test:excel:{test.id}",
                ),
            ]
        )

    rows.append(
        [
            InlineKeyboardButton(
                text="🔑 Kalitni ko'rish",
                callback_data=f"test:key:{test.id}",
            ),
            InlineKeyboardButton(
                text="🗑 O'chirish",
                callback_data=f"test:del_ask:{test.id}",
            ),
        ]
    )
    rows.append(
        [InlineKeyboardButton(text="⬅️ Orqaga", callback_data="test:list")]
    )
    return InlineKeyboardMarkup(inline_keyboard=rows)


def confirm_delete_keyboard(test_id: int) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="✅ Ha, o'chirish", callback_data=f"test:del_yes:{test_id}"
                ),
                InlineKeyboardButton(
                    text="❌ Yo'q", callback_data=f"test:view:{test_id}"
                ),
            ]
        ]
    )


def profile_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="✏️ Ism-familiyani o'zgartirish",
                    callback_data="profile:edit_name",
                )
            ]
        ]
    )
