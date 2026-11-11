import time
import json
import logging
import sqlite3
import os
import requests
import threading
import secrets
import re
from datetime import datetime, timedelta

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] (TelegramBot) %(message)s")

BOT_TOKEN = "9257869395:AAEBBDaRErf08ZkYTlsrORIhsPXd6x8M2-g"
API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"
DB_PATH = os.path.join(os.path.dirname(__file__), "edubattle.db")

# Admin and Payment Configurations
NETLIFY_APP_URL = "https://edubattle-uz.netlify.app"

def get_live_tunnel_url():
    railway_url = os.environ.get("RAILWAY_PUBLIC_DOMAIN") or os.environ.get("RAILWAY_STATIC_URL")
    if railway_url:
        if not railway_url.startswith("http"):
            return f"https://{railway_url}"
        return railway_url
    
    render_url = os.environ.get("RENDER_EXTERNAL_URL")
    if render_url:
        return render_url.rstrip("/")

    public_url = os.environ.get("PUBLIC_URL")
    if public_url:
        return public_url.rstrip("/")

    log_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tunnel.log")
    if os.path.exists(log_file):
        try:
            with open(log_file, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
            m = re.findall(r'https://([a-zA-Z0-9-]+)\.trycloudflare\.com', content)
            if m:
                return f"https://{m[-1]}.trycloudflare.com"
        except:
            pass
    return "https://edubattle-backend-x0v2.onrender.com"

def get_student_app_url():
    t_url = get_live_tunnel_url()
    return f"{t_url}/?v=20261111_1148"

def get_teacher_app_url():
    t_url = get_live_tunnel_url()
    return f"{t_url}/?role=teacher&v=20261111_1148"

PAYMENT_CARD = "9860 0301 2345 6789"
PAYMENT_CARD_HOLDER = "EduBattle Platformasi"
PRO_PRICE = 29000

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def get_pro_price() -> int:
    try:
        conn = get_db()
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS app_settings (key TEXT PRIMARY KEY, value TEXT, updated_at TIMESTAMP)")
        c.execute("SELECT value FROM app_settings WHERE key = 'pro_price'")
        row = c.fetchone()
        conn.close()
        if row and row["value"]:
            return int(row["value"])
    except Exception as e:
        logging.error(f"Error getting pro_price in bot: {e}")
    return PRO_PRICE

def get_main_keyboard(lang="uz"):
    if lang == "ru":
        return {
            "keyboard": [
                [{"text": "🚀 EduBattle Ilovasi", "web_app": {"url": get_student_app_url()}}],
                [{"text": "💎 Купить подписку PRO"}],
                [{"text": "🔑 Код подтверждения (OTP)"}, {"text": "🌐 Сменить язык"}]
            ],
            "resize_keyboard": True,
            "persistent": True
        }
    elif lang == "en":
        return {
            "keyboard": [
                [{"text": "🚀 Open EduBattle App", "web_app": {"url": get_student_app_url()}}],
                [{"text": "💎 Purchase PRO Subscription"}],
                [{"text": "🔑 Verification Code (OTP)"}, {"text": "🔐 Reset Password"}],
                [{"text": "🌐 Change Language (Til / Lang)"}]
            ],
            "resize_keyboard": True,
            "persistent": True
        }
    else:
        return {
            "keyboard": [
                [{"text": "🚀 EduBattle Ilovasi", "web_app": {"url": get_student_app_url()}}],
                [{"text": "💎 PRO Obuna sotib olish"}],
                [{"text": "🔑 Tasdiqlash kodi (OTP)"}, {"text": "🌐 Tilni tanlash"}]
            ],
            "resize_keyboard": True,
            "persistent": True
        }

MAIN_KEYBOARD = get_main_keyboard("uz")

def send_language_menu(chat_id):
    text = (
        "🌐 <b>Iltimos, muloqot tilini tanlang:</b>\n"
        "🌐 <b>Пожалуйста, выберите язык общения:</b>\n"
        "🌐 <b>Please choose your interface language:</b>"
    )
    reply_markup = {
        "inline_keyboard": [
            [{"text": "🇺🇿 O'zbekcha", "callback_data": "set_lang_uz"}],
            [{"text": "🇷🇺 Русский", "callback_data": "set_lang_ru"}],
            [{"text": "🇬🇧 English", "callback_data": "set_lang_en"}]
        ]
    }
    send_message(chat_id, text, reply_markup=reply_markup)

CANCEL_KEYBOARD = {
    "keyboard": [
        [{"text": "❌ Bekor qilish"}]
    ],
    "resize_keyboard": True
}

# In-memory session trackers
user_states = {}   # chat_id -> {"state": "WAITING_FOR_PIN"|"WAITING_FOR_PASS", "data": {...}}
active_sessions = {} # chat_id -> {quiz_id, questions, current_idx, correct_count, wrong_count, start_time, ...}
cached_apk_file_id = "BQACAgIAAxkDAANHaul6OwWi6RevNNW19e3K0mqunUIAAnmtAALr9FFLEjx41LBuPpk9BA"

def tg_request(method, payload=None):
    try:
        url = f"{API_URL}/{method}"
        res = requests.post(url, json=payload, timeout=35)
        return res.json()
    except Exception as e:
        logging.error(f"Telegram API error on {method}: {e}")
        return None

def send_chat_action(chat_id, action="upload_document"):
    return tg_request("sendChatAction", {"chat_id": chat_id, "action": action})

def send_message(chat_id, text, reply_markup=None, parse_mode="HTML"):
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": parse_mode
    }
    if reply_markup is not None:
        payload["reply_markup"] = reply_markup
    return tg_request("sendMessage", payload)

def send_photo(chat_id, photo, caption=None, reply_markup=None, parse_mode="HTML"):
    payload = {
        "chat_id": chat_id,
        "photo": photo,
        "parse_mode": parse_mode
    }
    if caption:
        payload["caption"] = caption
    if reply_markup is not None:
        payload["reply_markup"] = reply_markup
    return tg_request("sendPhoto", payload)

def send_document(chat_id, document, caption=None, reply_markup=None, parse_mode="HTML"):
    payload = {
        "chat_id": chat_id,
        "document": document,
        "parse_mode": parse_mode
    }
    if caption:
        payload["caption"] = caption
    if reply_markup is not None:
        payload["reply_markup"] = reply_markup
    return tg_request("sendDocument", payload)

def edit_message_text(chat_id, message_id, text, reply_markup=None, parse_mode="HTML"):
    payload = {
        "chat_id": chat_id,
        "message_id": message_id,
        "text": text,
        "parse_mode": parse_mode
    }
    if reply_markup is not None:
        payload["reply_markup"] = reply_markup
    return tg_request("editMessageText", payload)

def edit_message_caption(chat_id, message_id, caption, reply_markup=None, parse_mode="HTML"):
    payload = {
        "chat_id": chat_id,
        "message_id": message_id,
        "caption": caption,
        "parse_mode": parse_mode
    }
    if reply_markup is not None:
        payload["reply_markup"] = reply_markup
    return tg_request("editMessageCaption", payload)

def answer_callback_query(callback_query_id, text=None, show_alert=False):
    payload = {
        "callback_query_id": callback_query_id
    }
    if text:
        payload["text"] = text
        payload["show_alert"] = show_alert
    return tg_request("answerCallbackQuery", payload)

def setup_bot_commands():
    try:
        cmds = [
            {"command": "start", "description": "🚀 Ilovani ochish / Главное меню / Main Menu"},
            {"command": "app", "description": "🎮 EduBattle Mini App ochish"},
            {"command": "pro", "description": "💎 PRO Obuna sotib olish / Купить PRO"},
            {"command": "code", "description": "🔑 Tasdiqlash kodi (OTP) / Код подтверждения"},
            {"command": "reset", "description": "🔐 Parolni tiklash / Сброс пароля"},
            {"command": "lang", "description": "🌐 Tilni tanlash / Выбор языка / Language"}
        ]
        res = tg_request("setMyCommands", {"commands": cmds})
        logging.info(f"Bot commands registered: {res}")
        tg_request("setChatMenuButton", {
            "menu_button": {
                "type": "web_app",
                "text": "🎮 EduBattle",
                "web_app": {"url": get_student_app_url()}
            }
        })
    except Exception as e:
        logging.warning(f"Could not register commands: {e}")

def generate_and_save_otp(tg_id=None, tg_username=None, user_id=None, purpose="register"):
    code = f"{secrets.randbelow(900000) + 100000}"
    conn = get_db()
    cursor = conn.cursor()
    if tg_id:
        cursor.execute("UPDATE telegram_verifications SET is_used = 1 WHERE telegram_id = ? AND purpose = ?", (tg_id, purpose))
    if user_id:
        cursor.execute("UPDATE telegram_verifications SET is_used = 1 WHERE user_id = ? AND purpose = ?", (user_id, purpose))
    cursor.execute("""
        INSERT INTO telegram_verifications (code, telegram_id, telegram_username, purpose, user_id, expires_at)
        VALUES (?, ?, ?, ?, ?, datetime('now', '+10 minutes'))
    """, (code, tg_id, tg_username, purpose, user_id))
    conn.commit()
    conn.close()
    return code

chat_lang_cache = {}

def send_otp_to_tg_user(chat_id, user=None, lang="uz"):
    tg_user = user.get("telegram_username") if user else None
    user_id = user.get("id") if user else None
    code = generate_and_save_otp(tg_id=chat_id, tg_username=tg_user, user_id=user_id, purpose="register")
    if lang == "ru":
        text = (
            f"🔑 <b>Код подтверждения EduBattle (OTP):</b>\n\n"
            f"Ваш 6-значный защищенный код:\n\n"
            f"👉 <code>{code}</code> 👈\n\n"
            f"⏳ Код действует <b>10 минут</b>.\n"
            f"Введите этот код в форму регистрации на сайте или в приложении."
        )
    elif lang == "en":
        text = (
            f"🔑 <b>EduBattle Verification Code (OTP):</b>\n\n"
            f"Your 6-digit verification code:\n\n"
            f"👉 <code>{code}</code> 👈\n\n"
            f"⏳ Valid for <b>10 minutes</b>.\n"
            f"Enter this code into the registration form on the website or app."
        )
    else:
        text = (
            f"🔑 <b>EduBattle Tasdiqlash Kodi (OTP):</b>\n\n"
            f"Sizning 6-xonali kiber-himoyalangan tasdiqlash kodingiz:\n\n"
            f"👉 <code>{code}</code> 👈\n\n"
            f"⏳ Ushbu kod <b>10 daqiqa</b> davomida amal qiladi.\n"
            f"Ushbu kodni saytdagi yoki ilovadagi ro'yxatdan o'tish oynasiga kiriting."
        )
    send_message(chat_id, text, reply_markup=get_main_keyboard(lang))

def send_password_reset_to_tg_user(chat_id, user, lang="uz"):
    if not user:
        return
    code = generate_and_save_otp(tg_id=chat_id, tg_username=user.get("telegram_username"), user_id=user.get("id"), purpose="reset")
    login_id = user.get("username") or "Topilmadi"
    if lang == "ru":
        text = (
            f"🔐 <b>Служба сброса пароля EduBattle:</b>\n\n"
            f"👤 <b>Ваш Логин (ID):</b> <code>{login_id}</code>\n\n"
            f"🔑 <b>Одноразовый код для сброса пароля:</b>\n👉 <code>{code}</code> 👈\n\n"
            f"⏳ Код действует <b>10 минут</b>.\n\n"
            f"Откройте приложение или сайт, перейдите в <b>'Забыли пароль?'</b> и введите этот код вместе с новым паролем!"
        )
    elif lang == "en":
        text = (
            f"🔐 <b>EduBattle Password Reset Service:</b>\n\n"
            f"👤 <b>Your Login (ID):</b> <code>{login_id}</code>\n\n"
            f"🔑 <b>One-time Reset Code:</b>\n👉 <code>{code}</code> 👈\n\n"
            f"⏳ Valid for <b>10 minutes</b>.\n\n"
            f"Open the app or website, go to <b>'Forgot password?'</b> and enter this code with your new password!"
        )
    else:
        text = (
            f"🔐 <b>EduBattle Parolni Tiklash Xizmati:</b>\n\n"
            f"👤 <b>Sizning Loginingiz (ID):</b> <code>{login_id}</code>\n\n"
            f"🔑 <b>Bir martalik tiklash kodi:</b>\n👉 <code>{code}</code> 👈\n\n"
            f"⏳ Ushbu kod <b>10 daqiqa</b> davomida amal qiladi.\n\n"
            f"Ilova yoki saytga kiring, <b>'Parolni unutdingizmi?'</b> bo'limiga ushbu kod hamda yangi parolingizni kiriting!"
        )
    send_message(chat_id, text, reply_markup=get_main_keyboard(lang))

def get_download_urls():
    download_url = "https://edubattle-uz.netlify.app/apk"
    site_url = "https://edubattle-uz.netlify.app/download"
    try:
        conn = get_db()
        c = conn.cursor()
        c.execute("SELECT key, value FROM app_settings WHERE key IN ('netlify_download_url', 'netlify_site_url')")
        for r in c.fetchall():
            if r["key"] == "netlify_download_url" and r["value"]:
                download_url = r["value"]
            elif r["key"] == "netlify_site_url" and r["value"]:
                site_url = r["value"]
        conn.close()
    except Exception as e:
        pass
    return download_url, site_url

def send_download_hub(chat_id):
    hub_text = (
        "🚀 <b>EduBattle Ilovasi — Telegram ichida 24/7 jonli!</b>\n\n"
        "Qo'shimcha dastur yoki fayl yuklab olishingiz shart emas!\n\n"
        "EduBattle to'g'ridan-to'g'ri Telegram ichida <b>Telegram Mini App</b> sifatida ishlaydi:\n"
        "🍏 <b>iOS (iPhone va iPad)</b> — Hech qanday sozlashlarsiz darhol ochiladi.\n"
        "🤖 <b>Android</b> — Bir zumda to'liq ekranda ishga tushadi.\n"
        "💻 <b>Kompyuter (Telegram Desktop / Web)</b> — Barcha brauzer va kompyuterlarda qulay ishlaydi.\n\n"
        "Boshlash uchun pastdagi <b>'🚀 EduBattle Ilovasini Ochish'</b> tugmasini bosing:"
    )
    reply_markup = {
        "inline_keyboard": [
            [{"text": "🚀 EduBattle Ilovasini Ochish", "web_app": {"url": get_student_app_url()}}],
            [{"text": "📝 Test topshirish", "callback_data": "btn_quiz"}, {"text": "💎 PRO Obuna", "callback_data": "btn_pro"}]
        ]
    }
    send_message(chat_id, hub_text, reply_markup=reply_markup)

def send_apk_to_user(chat_id):
    global cached_apk_file_id
    dl_url, site_url = get_download_urls()

    caption = (
        "🤖 <b>EduBattle — Rasmiy Android Ilovasi (.APK)</b>\n\n"
        "📦 <b>Fayl:</b> <code>EduBattle.apk</code> (1.6 MB)\n"
        "✨ <b>Versiya:</b> 1.0 Rasmiy\n"
        "📱 <b>Talab:</b> Android 5.0 va undan yuqori\n\n"
        "⚡️ <b>Agar Telegramda yuklash sekin bo'lsa yoki ochilmasa:</b>\n"
        "Quyidagi <b>'🚀 Netlify orqali yuklab olish'</b> tugmasini bosing — brauzeringizda 1 soniyada yuklab beradi!\n\n"
        "📲 <b>Telefoningizga o'rnatish:</b>\n"
        "1. Faylni yuklab oling va ustiga bosing.\n"
        "2. <b>'O'rnatish' (Install)</b> tugmasini bosing.\n"
        "3. Agar xavfsizlik oynasi chiqsa, <i>'Ruxsat berish' (Разрешить)</i>ni bosing.\n"
        "4. O'rnatilgach ilovaga kiring! 🚀"
    )

    reply_markup = {
        "inline_keyboard": [
            [{"text": "🚀 Netlify orqali yuklab olish (.APK)", "url": dl_url}],
            [{"text": "🌐 Netlify Yuklab Olish Portali", "url": site_url}],
            [{"text": "🍏 iPhone (iOS) talqini kerakmi?", "callback_data": "dl_ios"}]
        ]
    }

    send_chat_action(chat_id, "upload_document")

    # If we already have Telegram's file_id, send via file_id instantaneously
    if cached_apk_file_id:
        res = tg_request("sendDocument", {
            "chat_id": chat_id,
            "document": cached_apk_file_id,
            "caption": caption,
            "parse_mode": "HTML",
            "reply_markup": reply_markup
        })
        if res and res.get("ok"):
            return res

    # Otherwise upload the local APK file
    apk_path = os.path.join(os.path.dirname(__file__), "EduBattle.apk")
    if not os.path.exists(apk_path):
        apk_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "EduBattle.apk")
    if not os.path.exists(apk_path):
        apk_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "frontend", "downloads", "EduBattle.apk")

    if os.path.exists(apk_path):
        try:
            url = f"{API_URL}/sendDocument"
            data = {
                "chat_id": str(chat_id),
                "caption": caption,
                "parse_mode": "HTML",
                "reply_markup": json.dumps(reply_markup)
            }
            with open(apk_path, "rb") as f:
                files = {"document": ("EduBattle.apk", f, "application/vnd.android.package-archive")}
                res = requests.post(url, data=data, files=files, timeout=60)
                res_json = res.json()
                if res_json.get("ok"):
                    doc = res_json.get("result", {}).get("document", {})
                    if doc and doc.get("file_id"):
                        cached_apk_file_id = doc.get("file_id")
                return res_json
        except Exception as e:
            logging.error(f"Error sending APK document: {e}")

    # Fallback to direct Netlify button message
    send_message(chat_id, caption, reply_markup=reply_markup)
    return None

def send_ios_guide(chat_id):
    ios_text = (
        "🍏 <b>iPhone va iPad (iOS) uchun EduBattle:</b>\n\n"
        "Hech qanday qo'shimcha havola yoki dastur o'rnatish shart emas!\n"
        "EduBattle Apple qurilmalarida (iPhone/iPad) to'g'ridan-to'g'ri Telegram ichida <b>Mini App</b> formatida 100% mukammal va tezkor ishlaydi.\n\n"
        "Pastdagi <b>'🚀 EduBattle Ilovasini Ochish'</b> tugmasini bosing va darhol foydalaning! 🚀"
    )
    reply_markup = {
        "inline_keyboard": [
            [{"text": "🚀 EduBattle Ilovasini Ochish", "web_app": {"url": get_student_app_url()}}]
        ]
    }
    send_message(chat_id, ios_text, reply_markup=reply_markup)

def send_web_guide(chat_id):
    text = (
        "💻 <b>Kompyuter (Windows / Mac / Linux) foydalanuvchilari uchun:</b>\n\n"
        "EduBattle barcha zamonaviy brauzerlarda (Google Chrome, Microsoft Edge, Opera, Safari, Firefox) to'liq ishlaydi.\n\n"
        "🖥 <b>Kompyuterga mustaqil dastur qilib o'rnatish:</b>\n"
        "1. Brauzerda <code>https://edubattle-uz.netlify.app</code> platformasini oching.\n"
        "2. Brauzerning manzil qatori (URL) o'ng tomonida paydo bo'ladigan <b>'Ilovani o'rnatish' (Install App ⬇️)</b> belgisini bosing.\n"
        "3. <b>'O'rnatish' (Install)</b> tugmasini tasdiqlang.\n"
        "4. EduBattle kompyuteringiz ishchi stoliga va Start menyusiga mustaqil tezkor dastur sifatida o'rnatiladi! ⚡️"
    )
    reply_markup = {
        "inline_keyboard": [
            [{"text": "🤖 Android (.APK yuklab olish)", "callback_data": "dl_android"}],
            [{"text": "🍏 iPhone (iOS) talqini", "callback_data": "dl_ios"}]
        ]
    }
    send_message(chat_id, text, reply_markup=reply_markup)

def generate_auto_login_sync():
    conn = get_db()
    cursor = conn.cursor()
    for _ in range(50):
        code = secrets.randbelow(90000) + 10000
        candidate = f"EB-{code}"
        cursor.execute("SELECT id FROM users WHERE LOWER(username) = ?", (candidate.lower(),))
        if not cursor.fetchone():
            conn.close()
            return candidate
    conn.close()
    return f"EB-{int(time.time()) % 100000}"

def get_registered_user(from_user):
    tg_id = from_user.get("id")
    tg_username = from_user.get("username")

    conn = get_db()
    cursor = conn.cursor()
    # 1. Match by telegram_id with completed registration (pin_code IS NOT NULL)
    cursor.execute("SELECT * FROM users WHERE telegram_id = ? AND pin_code IS NOT NULL", (tg_id,))
    u = cursor.fetchone()
    if u:
        user_dict = dict(u)
        if tg_username and user_dict.get("telegram_username") != tg_username:
            cursor.execute("UPDATE users SET telegram_username = ? WHERE id = ?", (tg_username, user_dict["id"]))
            conn.commit()
            user_dict["telegram_username"] = tg_username
        conn.close()
        return user_dict

    # 2. Check if a user registered on web with this telegram_username and has completed registration
    if tg_username:
        cursor.execute("SELECT * FROM users WHERE LOWER(telegram_username) = ? AND pin_code IS NOT NULL", (tg_username.lower().lstrip('@'),))
        u_match = cursor.fetchone()
        if u_match:
            user_dict = dict(u_match)
            cursor.execute("UPDATE users SET telegram_id = ? WHERE id = ?", (tg_id, user_dict["id"]))
            conn.commit()
            user_dict["telegram_id"] = tg_id
            conn.close()
            return user_dict

    conn.close()
    return None

def find_quiz_by_pin(pin_code):
    clean_pin = pin_code.strip().upper()
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT tq.*, u.full_name as teacher_name, s.name as subject_name
        FROM teacher_quizzes tq
        JOIN users u ON tq.teacher_id = u.id
        JOIN subjects s ON tq.subject_id = s.id
        WHERE UPPER(TRIM(tq.pin_code)) = ?
    """, (clean_pin,))
    row = cursor.fetchone()
    conn.close()
    if not row:
        return None
    q = dict(row)
    if q.get("questions"):
        try:
            q["questions"] = json.loads(q["questions"])
        except:
            q["questions"] = []
    return q

def check_group_invite_code(code):
    clean = code.strip().upper()
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT tg.group_name, u.full_name as teacher_name
        FROM teacher_groups tg
        JOIN users u ON tg.teacher_id = u.id
        WHERE UPPER(TRIM(tg.invite_code)) = ?
    """, (clean,))
    row = cursor.fetchone()
    conn.close()
    return dict(row) if row else None

def save_quiz_result(student_id, quiz, correct_count, total_questions, time_spent_sec):
    score_pct = round((correct_count / total_questions) * 100) if total_questions > 0 else 0
    conn = get_db()
    cursor = conn.cursor()

    quiz_id = quiz["id"]
    teacher_id = quiz.get("teacher_id")
    subject_id = quiz.get("subject_id", 1)
    title = quiz.get("title", "Test")

    # 1. Save submission
    cursor.execute("""
        INSERT INTO quiz_submissions (quiz_id, student_id, score, total_questions, correct_count, time_spent_sec)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (quiz_id, student_id, score_pct, total_questions, correct_count, int(time_spent_sec)))

    # 2. Save grade to journal
    cursor.execute("""
        INSERT INTO student_grades (student_id, teacher_id, subject_id, grade_type, score, comment)
        VALUES (?, ?, ?, 'Test', ?, ?)
    """, (student_id, teacher_id, subject_id, score_pct, f"Telegram bot orqali '{title}' testi: {correct_count}/{total_questions} to'g'ri ({int(time_spent_sec)}s)"))

    # 3. Recalculate average grade and XP
    cursor.execute("SELECT AVG(score) as avg_sc FROM student_grades WHERE student_id = ?", (student_id,))
    row = cursor.fetchone()
    if row and row["avg_sc"] is not None:
        new_grade = round(float(row["avg_sc"]))
        cursor.execute("UPDATE users SET grade_score = ?, xp = xp + ? WHERE id = ?", (new_grade, 50 + correct_count * 10, student_id))

    conn.commit()
    conn.close()

    try:
        from backend.app import bump_data_revision
        bump_data_revision()
    except Exception as e:
        pass

    return score_pct

def get_grade_badge(score):
    if score >= 86:
        return "5 (A'lo) ⭐⭐⭐⭐⭐"
    elif score >= 71:
        return "4 (Yaxshi) ⭐⭐⭐⭐"
    elif score >= 56:
        return "3 (Qoniqarli) ⭐⭐⭐"
    elif score > 0:
        return "2 (Qoniqarsiz) ⚠️"
    else:
        return "0 (Boshlang'ich) 🆕"

# ----------------- PRO SUBSCRIPTION & BOT PAYMENT LOGIC -----------------

def start_pro_purchase_flow(chat_id, user, deep_param="", user_lang="uz"):
    target_user_id = None
    if deep_param.startswith("buy_pro_"):
        try:
            target_user_id = int(deep_param.replace("buy_pro_", "").strip())
        except:
            pass

    target_user = None
    conn = get_db()
    c = conn.cursor()
    if target_user_id:
        c.execute("SELECT * FROM users WHERE id = ?", (target_user_id,))
        r = c.fetchone()
        if r:
            target_user = dict(r)

    if not target_user and user:
        target_user = user

    # If teacher:
    if target_user and target_user.get("role") == "teacher":
        conn.close()
        send_message(chat_id, "👨‍🏫 <b>Hurmatli ustoz!</b>\n\nO'qituvchilar uchun barcha imkoniyatlar (sinflar, testlar, darsliklar) 100% BEPUL taqdim etiladi! Sizga to'lov qilish shart emas.", reply_markup=get_main_keyboard(user_lang))
        return

    current_price = get_pro_price()
    formatted_price = f"{current_price:,}".replace(",", " ")

    if not target_user:
        conn.close()
        user_states[chat_id] = {"state": "WAITING_USER_ID_FOR_PRO", "data": {}}
        prompt_txt = (
            f"💎 <b>EduBattle PRO Obunasi ({formatted_price} so'm / oy)</b>\n\n"
            "Obunani hisobingizga biriktirish uchun, iltimos, EduBattle platformasidagi <b>Login (ID) raqamingizni</b> kiriting:\n"
            "(Masalan: <code>EB-84841</code> yoki ro'yxatdan o'tgan telefon raqamingiz)"
        )
        send_message(chat_id, prompt_txt, reply_markup=CANCEL_KEYBOARD)
        return

    conn.close()

    # Active status check
    is_active_pro = bool(target_user.get("is_pro"))
    exp_info = ""
    if is_active_pro and target_user.get("pro_expires_at"):
        exp_info = f"\n⏳ <i>Joriy PRO obunangiz amal qilish muddati: <b>{target_user['pro_expires_at'][:16]}</b> gacha. Yangi to'lov uni yana +30 kunga uzaytiradi!</i>\n"

    txt = (
        f"💎 <b>EduBattle O'quvchi PRO Obunasi</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n"
        f"👤 <b>Foydalanuvchi:</b> {target_user['full_name']}\n"
        f"🆔 <b>Login (ID):</b> <code>{target_user.get('username')}</code>\n"
        f"💰 <b>Narxi:</b> <b>{formatted_price} so'm / 1 oy (30 kun)</b>\n"
        f"{exp_info}"
        f"━━━━━━━━━━━━━━━━━━━━━━\n"
        f"<b>PRO tarifidagi imkoniyatlar:</b>\n"
        f"⚔️ Do'stlar bilan 3-5 kishilik jamoaviy batllar\n"
        f"📚 Barcha sinflar darsliklari va manbalariga to'liq kirish\n"
        f"🏆 Respublika va maktablararo bellashuvlar\n"
        f"👑 Profil yonida oltin PRO nishoni\n\n"
        f"To'lovni amalga oshirish uchun qulay usulni tanlang:"
    )

    markup = {
        "inline_keyboard": [
            [
                {"text": "🔹 Click", "callback_data": f"pay_method_click_{target_user['id']}"},
                {"text": "🔹 Payme", "callback_data": f"pay_method_payme_{target_user['id']}"}
            ],
            [
                {"text": "💳 Karta raqam (Uzcard/Humo)", "callback_data": f"pay_method_card_{target_user['id']}"}
            ],
            [
                {"text": "❌ Bekor qilish", "callback_data": "cancel_pro_pay"}
            ]
        ]
    }

    send_message(chat_id, txt, reply_markup=markup)

def show_payment_details(chat_id, user_id, method, message_id=None):
    conn = get_db()
    c = conn.cursor()
    c.execute("SELECT id, username, full_name FROM users WHERE id = ?", (user_id,))
    u = c.fetchone()
    conn.close()
    if not u:
        send_message(chat_id, "⚠️ Foydalanuvchi topilmadi.")
        return

    current_price = get_pro_price()
    formatted_price = f"{current_price:,}".replace(",", " ")

    method_name = {
        "click": "Click orqali to'lov",
        "payme": "Payme orqali to'lov",
        "card": "Bank kartasi orqali to'lov"
    }.get(method, "Karta orqali to'lov")

    pay_text = (
        f"💳 <b>{method_name.upper()}</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n"
        f"👤 <b>Qabul qiluvchi:</b> {PAYMENT_CARD_HOLDER}\n"
        f"🔢 <b>Karta raqami:</b> <code>{PAYMENT_CARD}</code>\n"
        f"💰 <b>To'lov summasi:</b> <b>{formatted_price} so'm</b>\n"
        f"📝 <b>To'lov izohi:</b> <code>{u['username']}</code>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n"
        f"📸 <b>KEYINGI QADAM:</b>\n"
        f"1️⃣ Yuqoridagi karta raqamiga <b>{formatted_price} so'm</b> o'tkazing.\n"
        f"2️⃣ To'lov muvaffaqiyatli chiqqan <b>chekining fotosurati (skrinshot) yoki PDF faylini</b> to'g'ridan-to'g'ri <b>ushbu botga yuboring</b>!\n\n"
        f"⚡️ <i>To'lov cheki admin profiliga tasdiqlash uchun yuboriladi va admin tasdiqlashi bilan PRO obunangiz roppa-rosa <b>1 oyga</b> avtomatik faollashtiriladi.</i>"
    )

    user_states[chat_id] = {
        "state": "WAITING_PAYMENT_RECEIPT",
        "data": {
            "user_id": u["id"],
            "username": u["username"],
            "full_name": u["full_name"],
            "provider": method,
            "amount": current_price
        }
    }

    cancel_btn = {
        "inline_keyboard": [
            [{"text": "❌ To'lovni bekor qilish", "callback_data": "cancel_pro_pay"}]
        ]
    }

    send_message(chat_id, pay_text, reply_markup=cancel_btn)

def handle_payment_receipt(message, file_id, file_type, user):
    chat_id = message.get("chat", {}).get("id")
    from_user = message.get("from", {})
    state_data = user_states.get(chat_id, {}).get("data", {})

    user_id = state_data.get("user_id")
    username = state_data.get("username")
    full_name = state_data.get("full_name")
    provider = state_data.get("provider", "card")
    amount = state_data.get("amount", PRO_PRICE)

    conn = get_db()
    c = conn.cursor()

    if not user_id and user:
        user_id = user["id"]
        username = user["username"]
        full_name = user["full_name"]

    if not user_id:
        conn.close()
        send_message(chat_id, "⚠️ Chek qabul qilinishi uchun avval menyudagi <b>'💎 PRO Obuna sotib olish'</b> tugmasini bosing va hisobingizni tanlang.")
        return

    # Insert pending subscription into DB
    c.execute("""
        INSERT INTO subscriptions (user_id, plan_name, amount, provider, status, receipt_file_id, receipt_type, telegram_chat_id, created_at)
        VALUES (?, 'student_pro', ?, ?, 'pending', ?, ?, ?, datetime('now'))
    """, (user_id, amount, provider, file_id, file_type, chat_id))
    sub_id = c.lastrowid
    conn.commit()
    conn.close()

    user_states.pop(chat_id, None)

    # Confirmation to user
    user_ack = (
        f"✅ <b>To'lov chekingiz muvaffaqiyatli qabul qilindi!</b>\n\n"
        f"📋 <b>To'lov so'rovi raqami:</b> #{sub_id}\n"
        f"👤 <b>Foydalanuvchi:</b> {full_name} (<code>{username}</code>)\n"
        f"💰 <b>Summa:</b> {amount:,} so'm\n"
        f"💳 <b>To'lov usuli:</b> {provider.upper()}\n\n"
        f"To'lov chekingiz tekshirish uchun <b>Administrator profiliga</b> yuborildi. "
        f"Admin to'lovni tasdiqlagan zahoti sizning <b>PRO obunangiz roppa-rosa 1 oyga</b> avtomatik faollashtiriladi va sizga bu yerda xabar keladi! 🔔"
    )
    send_message(chat_id, user_ack, reply_markup=get_main_keyboard("uz"))

    # Forward alert exclusively to dedicated Admin Bot (@admidinsfesefse_bot)
    try:
        from admin_bot import notify_admins_of_new_receipt
        notify_admins_of_new_receipt({
            "sub_id": sub_id,
            "full_name": full_name,
            "username": username,
            "provider": provider,
            "amount": amount,
            "file_id": file_id,
            "file_type": file_type
        })
    except Exception as e:
        logging.warning(f"Failed to forward receipt alert to Admin Bot: {e}")

# NOTE: All Admin operations (dashboard, approvals, price change, pdf upload) 
# have been cleanly moved exclusively to Admin Bot (@admidinsfesefse_bot).

# ----------------- MESSAGE HANDLERS -----------------

def handle_message(message):
    chat_id = message.get("chat", {}).get("id")
    from_user = message.get("from", {})
    text = (message.get("text") or "").strip()

    if not chat_id:
        return

    # Ensure Telegram chat menu button is dynamically pinned to WebApp for this chat
    try:
        tg_request("setChatMenuButton", {
            "chat_id": chat_id,
            "menu_button": {
                "type": "web_app",
                "text": "🎮 EduBattle",
                "web_app": {"url": get_student_app_url()}
            }
        })
    except Exception:
        pass

    # Check user registration (only returns registered users with pin_code)
    user = get_registered_user(from_user)
    user_lang = (user.get("lang") if user else None) or chat_lang_cache.get(chat_id) or "uz"
    user_main_kb = get_main_keyboard(user_lang)

    # Check for incoming payment receipt (photo or document)
    photo = message.get("photo")
    document = message.get("document")
    if photo or document:
        file_id = photo[-1]["file_id"] if photo else document["file_id"]
        file_type = "photo" if photo else "document"
        handle_payment_receipt(message, file_id, file_type, user)
        return

    # Cancel command / button
    if text in ("/cancel", "/bekor", "❌ Bekor qilish", "❌ Отмена", "❌ Cancel"):
        user_states.pop(chat_id, None)
        active_sessions.pop(chat_id, None)
        cancel_msg = {
            "ru": "Действие отменено. Вы в главном меню:",
            "en": "Action cancelled. You are in the main menu:",
            "uz": "Amal bekor qilindi. Bosh menyudasiz:"
        }.get(user_lang, "Amal bekor qilindi. Bosh menyudasiz:")
        send_message(chat_id, cancel_msg, reply_markup=user_main_kb)
        return

    # Telegram Mini App commands & buttons
    t_lower = text.lower().strip()
    is_teacher_app = (
        text in ("👨‍🏫 O'qituvchi Kabineti", "👨‍🏫 Кабинет Учителя", "👨‍🏫 Teacher Portal", "/teacher") or
        "o'qituvchi" in t_lower or "ustoz" in t_lower or "учител" in t_lower
    )
    if is_teacher_app:
        send_message(
            chat_id,
            "👨‍🏫 <b>EduBattle O'qituvchilar Portali</b>\n\n"
            "Hurmatli ustoz! O'qituvchilar kabineti tizimi hozirda tubdan mukammallashtirilmoqda va tez kunda yangi talqinda ishga tushiriladi! 🚀\n\n"
            "Hozircha ilovamizdan o'quvchi sifatida foydalanishingiz mumkin:",
            reply_markup={
                "inline_keyboard": [
                    [
                        {
                            "text": "🚀 EduBattle Ilovasini Ochish",
                            "web_app": {"url": get_student_app_url()}
                        }
                    ]
                ]
            }
        )
        return

    is_mini_app = (
        text in ("/app", "/play", "/webapp", "/game", "/miniapp", "/open", "/startapp", "🚀 EduBattle Ilovasi (O'quvchi)", "🚀 EduBattle Ilovasini Ochish", "🚀 Открыть приложение EduBattle", "🚀 Open EduBattle App") or
        any(k in t_lower for k in ["ilova", "mini app", "miniapp", "o'yin", "oyun", "play", "game", "webapp", "botda", "ochish"]) and "apk" not in t_lower
    )
    if is_mini_app:
        mini_app_text = {
            "ru": "🚀 <b>EduBattle Mini App</b>\n\nПриложение открывается прямо внутри Telegram без установки! Нажмите кнопку ниже для запуска:",
            "en": "🚀 <b>EduBattle Mini App</b>\n\nThe app runs directly inside Telegram with no downloads required! Tap below to launch:",
            "uz": "🚀 <b>EduBattle Mini App</b>\n\nIlovani to'g'ridan-to'g'ri Telegram ichida ochib ishlatishingiz mumkin! Hech qanday dastur o'rnatish shart emas.\n\nBoshlash uchun pastdagi tugmani bosing:"
        }.get(user_lang, "🚀 <b>EduBattle Mini App</b>\n\nIlovani ochish uchun pastdagi tugmani bosing:")

        send_message(
            chat_id,
            mini_app_text,
            reply_markup={
                "inline_keyboard": [
                    [
                        {
                            "text": "🚀 ILOVANI OCHISH (PLAY) 🎮",
                            "web_app": {"url": get_student_app_url()}
                        }
                    ],
                    [
                        {"text": "💎 PRO Obuna sotib olish", "callback_data": "btn_pro"}
                    ]
                ]
            }
        )
        return

    # Strictly redirect all admin commands from User Bot to dedicated Admin Bot
    if text.startswith(("/admin", "/panel", "/stats", "/setadmin", "/pending", "/subscribers", "/addpro", "/setprice", "/narx", "/setdownloadurl", "/setnetlifysite", "/clearquestions")) or text in ("asoee321", "admin2026"):
        send_message(
            chat_id,
            "🛡️ <b>Diqqat: Ushbu bot faqat foydalanuvchilar va o'quvchilar uchun!</b>\n\n"
            "Admin boshqaruv paneli, real vaqtdagi jonli statistika, tarif narxini o'zgartirish, PDF darsliklar va to'lovlarni tasdiqlash uchun maxsus <b>Super Admin Botimizga</b> kiring:\n"
            "👉 @admidinsfesefse_bot\n\n"
            "<i>(Admin botga kirish uchun maxfiy parol talab qilinadi)</i>"
        )
        return

    # Pro subscription commands & menu buttons
    if text in ("/pro", "/buy_pro", "💎 PRO Obuna sotib olish", "💎 Купить подписку PRO", "💎 Purchase PRO Subscription"):
        start_pro_purchase_flow(chat_id, user, user_lang=user_lang)
        return

    # /start command
    if text.startswith("/start"):
        user_states.pop(chat_id, None)
        active_sessions.pop(chat_id, None)
        parts = text.split()
        deep_param = parts[1] if len(parts) > 1 else ""

        # Deep-link buy pro
        if deep_param.startswith("buy_pro") or deep_param.startswith("pro"):
            start_pro_purchase_flow(chat_id, user, deep_param=deep_param, user_lang=user_lang)
            return

        # Deep-link reset link
        if deep_param.startswith("reset_"):
            if not user:
                not_reg_msg = {
                    "ru": (
                        "⚠️ <b>Вы еще не зарегистрированы в системе EduBattle!</b>\n\n"
                        "Сброс пароля доступен только для зарегистрированных пользователей.\n\n"
                        "👉 <b>Сначала зарегистрируйтесь:</b>\n"
                        "1️⃣ Нажмите <b>'🔑 Код подтверждения (OTP)'</b> в меню бота;\n"
                        "2️⃣ Заполните форму регистрации на сайте или в приложении.\n\n"
                        "После регистрации вы сможете в любое время восстанавливать пароль!"
                    ),
                    "en": (
                        "⚠️ <b>You are not registered on EduBattle yet!</b>\n\n"
                        "Password reset is only available for registered users.\n\n"
                        "👉 <b>Please register first:</b>\n"
                        "1️⃣ Tap <b>'🔑 Verification Code (OTP)'</b> in the bot menu;\n"
                        "2️⃣ Use this code in the app or website registration form.\n\n"
                        "Once registered, you can freely reset your password at any time!"
                    ),
                    "uz": (
                        "⚠️ <b>Siz hali EduBattle platformasida ro'yxatdan o'tmagansiz!</b>\n\n"
                        "Parolni tiklash xizmati faqat oldin ro'yxatdan o'tgan foydalanuvchilar uchun ishlaydi.\n\n"
                        "👉 <b>Qanday ro'yxatdan o'tish mumkin?</b>\n"
                        "1️⃣ Menyudan <b>'🔑 Tasdiqlash kodi (OTP)'</b> tugmasini bosing va kod oling;\n"
                        "2️⃣ EduBattle ilovasida yoki saytda ro'yxatdan o'tish formasiga ushbu kodni kiriting.\n\n"
                        "Ro'yxatdan o'tganingizdan so'ng, parolingizni bemalol tiklashingiz mumkin!"
                    )
                }.get(user_lang, "⚠️ Siz hali EduBattle platformasida ro'yxatdan o'tmagansiz!")
                send_message(chat_id, not_reg_msg, reply_markup=user_main_kb)
                return
            else:
                send_password_reset_to_tg_user(chat_id, user, user_lang)
                return

        # Deep-link register link
        if deep_param.startswith("register_"):
            send_otp_to_tg_user(chat_id, user, user_lang)
            return

        if user:
            login_display = user.get("username") or "EB-..."
            if user_lang == "ru":
                welcome_text = (
                    f"Здравствуйте, <b>{user['full_name']}</b>! 🎓\n\n"
                    f"Добро пожаловать в официальный бот образовательной платформы <b>Edubattle</b>!\n\n"
                    f"👤 <b>Ваш Логин (ID):</b> <code>{login_display}</code>\n\n"
                    f"📱 <b>Платформа работает прямо в Telegram 24/7</b> на всех устройствах: <b>iOS (iPhone/iPad)</b> и <b>Android</b>!\n\n"
                    f"Через этот бот вы можете:\n"
                    f"🚀 <b>Открыть EduBattle</b> — Запустить приложение прямо внутри Telegram.\n"
                    f"💎 <b>PRO подписка</b> — Оформить премиум подписку со скидкой.\n"
                    f"🔑 <b>Код подтверждения (OTP)</b> — Безопасный код для входа и регистрации.\n"
                    f"🔐 <b>Сброс пароля</b> — Восстановить доступ в 1 клик.\n\n"
                    f"🌐 Сменить язык: нажмите <b>'Сменить язык'</b> или отправьте /lang.\n\n"
                    f"Нажмите на нужную кнопку ниже:"
                )
            elif user_lang == "en":
                welcome_text = (
                    f"Hello, <b>{user['full_name']}</b>! 🎓\n\n"
                    f"Welcome to the official <b>Edubattle</b> educational platform bot!\n\n"
                    f"👤 <b>Your system Login (ID):</b> <code>{login_display}</code>\n\n"
                    f"📱 <b>Runs directly inside Telegram 24/7</b> on all devices: <b>iOS (iPhone/iPad)</b> and <b>Android</b>!\n\n"
                    f"With this bot you can:\n"
                    f"🚀 <b>Launch EduBattle</b> — Open the app directly in Telegram.\n"
                    f"💎 <b>PRO Subscription</b> — Upgrade to PRO with full privileges.\n"
                    f"🔑 <b>OTP Code</b> — Receive secure instant verification codes.\n"
                    f"🔐 <b>Password Reset</b> — Quickly reset your password.\n\n"
                    f"🌐 Change language: press <b>'Change Language'</b> or send /lang.\n\n"
                    f"Choose an option below to start:"
                )
            else:
                welcome_text = (
                    f"Assalomu alaykum, <b>{user['full_name']}</b>! 🎓\n\n"
                    f"<b>Edubattle</b> ta'limiy platformasining rasmiy botiga xush kelibsiz!\n\n"
                    f"👤 <b>Sizning tizimdagi Loginingiz (ID):</b> <code>{login_display}</code>\n\n"
                    f"📱 <b>Ilova to'g'ridan-to'g'ri Telegram ichida 24/7 ishlaydi!</b>\n"
                    f"Hech qanday fayl yuklab olish shart emas — <b>iOS (iPhone/iPad)</b> va <b>Android</b> qurilmalarida birdek mukammal ochiladi.\n\n"
                    f"Ushbu bot orqali siz:\n"
                    f"🚀 <b>EduBattle Ilovasi</b> — Ilovani to'g'ridan-to'g'ri Telegramda ochish (barcha testlar, baholar va darsliklar ilova ichida).\n"
                    f"💎 <b>PRO Obuna</b> — Cheklovsiz imkoniyatlar uchun PRO tarifini xarid qilish.\n"
                    f"🔑 <b>Tasdiqlash kodi (OTP)</b> — Ro'yxatdan o'tish yoki kirish uchun xavfsiz kod olish.\n"
                    f"🔐 <b>Parolni tiklash</b> — Parolingizni unutgan bo'lsangiz, uni darhol tiklash.\n\n"
                    f"🌐 Tilni o'zgartirish uchun <b>'Tilni tanlash'</b> tugmasini bosing yoki /lang deb yozing.\n\n"
                    f"Boshlash uchun pastdagi tugmalardan birini bosing:"
                )
        else:
            if user_lang == "ru":
                welcome_text = (
                    f"Здравствуйте! 🎓\n\n"
                    f"Добро пожаловать в официальный бот образовательной платформы <b>Edubattle</b>!\n\n"
                    f"📱 <b>Платформа работает прямо в Telegram 24/7!</b>\n"
                    f"Никаких скачиваний файлов не требуется — работает на <b>iOS (iPhone/iPad)</b> и <b>Android</b>.\n\n"
                    f"🚀 <b>Открыть EduBattle</b> — Нажмите кнопку ниже для запуска.\n"
                    f"💎 <b>PRO Подписка</b> — Оформить премиум доступ.\n"
                    f"🔑 <b>Код подтверждения (OTP)</b> — Получить код для регистрации.\n\n"
                    f"<i>Нажмите <b>'🚀 ОТКРЫТЬ ПРИЛОЖЕНИЕ'</b> ниже!</i>"
                )
            elif user_lang == "en":
                welcome_text = (
                    f"Hello! 🎓\n\n"
                    f"Welcome to official <b>Edubattle</b> bot!\n\n"
                    f"📱 <b>Runs directly inside Telegram 24/7!</b>\n"
                    f"No downloads required — works on <b>iOS (iPhone/iPad)</b> and <b>Android</b>.\n\n"
                    f"🚀 <b>Launch EduBattle</b> — Tap below to launch the app.\n"
                    f"💎 <b>PRO Subscription</b> — Upgrade to PRO privileges.\n"
                    f"🔑 <b>OTP Code</b> — Get code to register.\n\n"
                    f"<i>Tap <b>'🚀 OPEN EDUBATTLE APP'</b> below!</i>"
                )
            else:
                welcome_text = (
                    f"Assalomu alaykum! 🎓\n\n"
                    f"<b>Edubattle</b> ta'limiy platformasining rasmiy botiga xush kelibsiz!\n\n"
                    f"📱 <b>Ilova to'liq Telegram ichida 24/7 jonli ishlaydi!</b>\n"
                    f"Hech qanday qo'shimcha fayl yuklab olish shart emas — <b>iOS (iPhone/iPad)</b> va <b>Android</b> tizimlarida bitta tugma orqali ishga tushadi.\n\n"
                    f"Quyidagi xizmatlardan foydalanishingiz mumkin:\n"
                    f"🚀 <b>EduBattle Ilovasi</b> — Ilovani ochish va ro'yxatdan o'tish.\n"
                    f"💎 <b>PRO Obuna</b> — Cheklovsiz PRO imkoniyatlariga ega bo'lish.\n"
                    f"🔑 <b>Tasdiqlash kodi (OTP)</b> — Ro'yxatdan o'tish uchun kod olish.\n"
                    f"🌐 <b>Tilni tanlash</b> — O'zingizga qulay tilni tanlash.\n\n"
                    f"<i>Boshlash uchun pastdagi <b>'🚀 ILOVANI OCHISH'</b> tugmasini bosing!</i>"
                )
        start_inline = {
            "inline_keyboard": [
                [
                    {
                        "text": "🚀 ILOVANI OCHISH (PLAY) 🎮",
                        "web_app": {"url": get_student_app_url()}
                    }
                ],
                [
                    {"text": "💎 PRO Obuna sotib olish", "callback_data": "btn_pro"}
                ]
            ]
        }
        send_message(chat_id, welcome_text, reply_markup=start_inline)
        send_message(chat_id, "Quyidagi tugmalar orqali xizmatlardan foydalanishingiz mumkin:", reply_markup=user_main_kb)
        return

    # Menu: Tasdiqlash kodi (OTP)
    if text in ("🔑 Tasdiqlash kodi (OTP)", "🔑 Код подтверждения (OTP)", "🔑 Verification Code (OTP)", "/code", "/otp", "/tasdiq") or "tasdiqlash kodi" in text.lower() or "код подтверждения" in text.lower() or "verification code" in text.lower():
        send_otp_to_tg_user(chat_id, user, user_lang)
        return

    # Menu: Parolni tiklash (Faqat ro'yxatdan o'tganlar uchun!)
    if text in ("🔐 Parolni tiklash", "🔐 Сброс пароля", "🔐 Password Reset", "/reset", "/parol") or "parolni tiklash" in text.lower() or "сброс пароля" in text.lower() or "reset password" in text.lower():
        if not user:
            not_reg_msg = {
                "ru": (
                    "⚠️ <b>Вы еще не зарегистрированы в EduBattle!</b>\n\n"
                    "Сброс пароля доступен только для зарегистрированных пользователей.\n\n"
                    "👉 <b>Сначала зарегистрируйтесь:</b>\n"
                    "1️⃣ Нажмите <b>'🔑 Код подтверждения (OTP)'</b> и получите код.\n"
                    "2️⃣ Введите его на сайте или в приложении при регистрации.\n\n"
                    "После регистрации вы сможете в любое время восстанавливать пароль!"
                ),
                "en": (
                    "⚠️ <b>You are not registered on EduBattle yet!</b>\n\n"
                    "Password reset is only available for registered users.\n\n"
                    "👉 <b>Please register first:</b>\n"
                    "1️⃣ Tap <b>'🔑 Verification Code (OTP)'</b> to get your code.\n"
                    "2️⃣ Use this code in the app or website registration form.\n\n"
                    "Once registered, you can freely reset your password at any time!"
                ),
                "uz": (
                    "⚠️ <b>Siz hali EduBattle tizimida ro'yxatdan o'tmagansiz!</b>\n\n"
                    "Parolni tiklash xizmati faqat tizimda ro'yxatdan o'tgan foydalanuvchilar uchun ishlaydi.\n\n"
                    "👉 <b>Avval ro'yxatdan o'ting:</b>\n"
                    "1️⃣ Menyudan <b>'🔑 Tasdiqlash kodi (OTP)'</b> tugmasini bosing va kod oling;\n"
                    "2️⃣ Ilova yoki saytda ro'yxatdan o'tish formasiga ushbu kodni kiriting.\n\n"
                    "Ro'yxatdan o'tganingizdan so'ng, parolingizni bemalol tiklashingiz mumkin!"
                )
            }.get(user_lang, "⚠️ Siz hali EduBattle platformasida ro'yxatdan o'tmagansiz!")
            send_message(chat_id, not_reg_msg, reply_markup=user_main_kb)
            return

        send_password_reset_to_tg_user(chat_id, user, user_lang)
        return

    # Menu: Language selector
    if text in ("/lang", "/til", "🌐 Tilni tanlash (Til / Lang)", "🌐 Сменить язык (Til / Lang)", "🌐 Change Language (Til / Lang)") or "til" in text.lower() or "язык" in text.lower() or "language" in text.lower():
        send_language_menu(chat_id)
        return

    # Menu: APK Yuklab olish (faqat Android .apk faylini istaganlar uchun)
    if text.startswith("/apk") or text in (
        "📦 APK Yuklab Olish (Android)", "📦 Скачать APK (Android)", "📦 Download APK (Android)",
        "📲 APK Yuklab olish", "📲 Скачать APK", "📲 Download APK"
    ) or ("apk" in text.lower() and ("yukla" in text.lower() or "skachat" in text.lower() or "fayl" in text.lower())):
        send_apk_to_user(chat_id)
        return

    # Direct iOS command
    if text.lower() in ("/ios", "/iphone", "/apple", "ios", "iphone"):
        send_ios_guide(chat_id)
        return

    # Direct Web / PC command
    if text.lower() in ("/web", "/pc", "/kompyuter", "web", "kompyuter"):
        send_web_guide(chat_id)
        return

    # Menu: Test topshirish (Faqat ro'yxatdan o'tganlar uchun)
    if text in ("📝 Test topshirish (Kod & Parol)", "📝 Пройти тест (Код и Пароль)", "📝 Take a Test (Code & Passcode)", "/test"):
        if not user:
            not_reg_msg = {
                "ru": "⚠️ <b>Вы еще не зарегистрированы!</b>\n\nЧтобы сдать тест и сохранить результат в журнал, сначала зарегистрируйтесь в EduBattle.",
                "en": "⚠️ <b>You are not registered yet!</b>\n\nTo take a test and record your grade, please register on EduBattle first.",
                "uz": "⚠️ <b>Siz hali ro'yxatdan o'tmagansiz!</b>\n\nTest topshirish va natijangiz maktab jurnaliga tushishi uchun avval EduBattle platformasida ro'yxatdan o'ting."
            }.get(user_lang, "⚠️ Siz hali ro'yxatdan o'tmagansiz!")
            send_message(chat_id, not_reg_msg, reply_markup=user_main_kb)
            return

        user_states[chat_id] = {"state": "WAITING_FOR_PIN", "data": {}}
        prompt_text = (
            "🔑 <b>1-QADAM / ШАГ 1:</b> Ustozingiz bergan <b>Test Kodini (PIN)</b> kiriting / Введите код теста:\n\n"
            "<i>Masalan / Пример: <code>TEST-677</code> yoki <code>MATH-739</code></i>"
        )
        send_message(chat_id, prompt_text, reply_markup=CANCEL_KEYBOARD)
        return

    # Menu: Natijalarim & Baholarim (Faqat ro'yxatdan o'tganlar uchun)
    if text in ("📊 Natijalarim & Baholarim", "📊 Мои результаты и оценки", "📊 My Grades", "/grades"):
        if not user:
            not_reg_msg = {
                "ru": "⚠️ <b>Вы еще не зарегистрированы!</b>\n\nЧтобы просматривать журнал оценок, сначала зарегистрируйтесь на платформе.",
                "en": "⚠️ <b>You are not registered yet!</b>\n\nTo view your grade report, please register on the platform first.",
                "uz": "⚠️ <b>Siz hali ro'yxatdan o'tmagansiz!</b>\n\nBaholar kundaligini ko'rish uchun avval platformada ro'yxatdan o'ting."
            }.get(user_lang, "⚠️ Siz hali ro'yxatdan o'tmagansiz!")
            send_message(chat_id, not_reg_msg, reply_markup=user_main_kb)
            return

        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT grade_score, xp, full_name FROM users WHERE id = ?", (user["id"],))
        u_info = cursor.fetchone()

        cursor.execute("""
            SELECT sg.*, s.name as subject_name
            FROM student_grades sg
            JOIN subjects s ON sg.subject_id = s.id
            WHERE sg.student_id = ?
            ORDER BY sg.id DESC LIMIT 5
        """, (user["id"],))
        grades = cursor.fetchall()
        conn.close()

        score = u_info["grade_score"] if (u_info and u_info["grade_score"] is not None) else 0
        xp = u_info["xp"] if u_info else 0
        badge = get_grade_badge(score)

        grades_text = (
            f"📊 <b>{user['full_name']}</b> ning baholari:\n"
            f"━━━━━━━━━━━━━━━━━━━━━━\n"
            f"⭐️ <b>Umumiy O'rtacha Baho:</b> {score} / 100 ball\n"
            f"🎖 <b>Milliy Baho:</b> {badge}\n"
            f"⚡️ <b>Tajriba ballari (XP):</b> {xp} XP\n"
            f"━━━━━━━━━━━━━━━━━━━━━━\n"
            f"<b>So'nggi baholar tarixi:</b>\n"
        )
        if not grades:
            grades_text += "<i>Hozircha baholar mavjud emas. Testlarni topshiring va a'lo baholarga ega bo'ling!</i>\n"
        else:
            for g in grades:
                grades_text += f"• <b>{g['subject_name']}:</b> {g['score']} ball ({g['comment'] or 'Test natijasi'})\n"

        send_message(chat_id, grades_text, reply_markup=user_main_kb)
        return

    # Menu: Kutubxona
    if text in ("📚 Kutubxona", "📚 Библиотека", "📚 Library", "/library"):
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT s.name, s.icon, COUNT(t.id) as b_cnt FROM subjects s LEFT JOIN textbooks t ON s.id = t.subject_id GROUP BY s.id")
        subs = cursor.fetchall()
        conn.close()

        lib_text = "📚 <b>Maktab & Litsey Kutubxonasi / Библиотека:</b>\n\nPlatformadagi mavjud darsliklar va qo'llanmalar:\n"
        for s in subs:
            lib_text += f"{s['icon']} <b>{s['name']}:</b> {s['b_cnt']} ta darslik\n"
        lib_text += "\n<i>To'liq kitoblarni o'qish uchun kompyuter yoki brauzerda platformaga kiring!</i>"
        send_message(chat_id, lib_text, reply_markup=user_main_kb)
        return

    # Menu: Yordam
    if text in ("ℹ️ Yordam / Qo'llanma", "ℹ️ Помощь / Инструкция", "ℹ️ Help & Guide", "/help"):
        help_text = (
            "ℹ️ <b>Edubattle Bot orqali test topshirish yo'riqnomasi:</b>\n\n"
            "1. O'qituvchingizdan <b>Test Kodi</b> (masalan: <code>TEST-677</code>) va <b>Test Paroli</b> (masalan: <code>4821</code>)ni oling.\n"
            "2. Botda <b>'📝 Test topshirish'</b> tugmasini bosing.\n"
            "3. Kod va parolni kiriting.\n"
            "4. Savollarni ketma-ket yechib chiqing.\n"
            "5. Test yakunida 100 ballik tizimda bahongiz chiqariladi va o'qituvchingiz jurnaliga avtomatik yoziladi!\n\n"
            "<i>Muammo bo'lsa, /bekor yoki /cancel buyrug'ini yuboring.</i>"
        )
        send_message(chat_id, help_text, reply_markup=user_main_kb)
        return

    # Check if user is in a state
    state_info = user_states.get(chat_id)
    if state_info:
        cur_state = state_info.get("state")
        
        # Check if user sent code and passcode together, e.g. "TEST-677 4821"
        parts = text.split()
        if len(parts) == 2 and cur_state == "WAITING_FOR_PIN":
            pin_cand = parts[0].strip().upper()
            pass_cand = parts[1].strip()
            quiz = find_quiz_by_pin(pin_cand)
            if quiz:
                expected_pass = str(quiz.get("passcode") or "").strip()
                if not expected_pass or expected_pass == pass_cand:
                    user_states.pop(chat_id, None)
                    launch_quiz_for_user(chat_id, user, quiz)
                    return

        if cur_state == "WAITING_FOR_PIN":
            pin_code = text.strip().upper()
            grp_match = check_group_invite_code(pin_code)
            if grp_match:
                send_message(
                    chat_id,
                    f"⚠️ Siz kiritgan <code>{pin_code}</code> kodi test kodi emas, balki Ustoz <b>{grp_match['teacher_name']}</b>ning <b>'{grp_match['group_name']}'</b> sinf guruhi taklif kodidir!\n\nIltimos, ustoz bergan haqiqiy <b>Test Kodi (PIN)</b>ni kiriting:",
                    reply_markup=CANCEL_KEYBOARD
                )
                return

            quiz = find_quiz_by_pin(pin_code)
            if not quiz:
                send_message(
                    chat_id,
                    f"❌ <b>Bunday Test Kodi topilmadi!</b> (<code>{pin_code}</code>)\n\nIltimos, ustozingiz bergan kodni tekshirib qayta kiriting (yoki /bekor qilish):",
                    reply_markup=CANCEL_KEYBOARD
                )
                return

            # If quiz has passcode
            expected_pass = str(quiz.get("passcode") or "").strip()
            if expected_pass:
                user_states[chat_id] = {
                    "state": "WAITING_FOR_PASSCODE",
                    "data": {"quiz": quiz, "pin_code": pin_code}
                }
                send_message(
                    chat_id,
                    f"✅ Test topildi: <b>{quiz['title']}</b> ({quiz['subject_name']})\n\n"
                    f"🔒 <b>2-QADAM:</b> Ushbu test uchun <b>Test Parolini</b> kiriting:\n"
                    f"<i>(O'qituvchingiz taqdim etgan maxsus parol)</i>",
                    reply_markup=CANCEL_KEYBOARD
                )
                return
            else:
                user_states.pop(chat_id, None)
                launch_quiz_for_user(chat_id, user, quiz)
                return

        elif cur_state == "WAITING_FOR_PASSCODE":
            entered_passcode = text.strip()
            quiz = state_info["data"]["quiz"]
            expected_pass = str(quiz.get("passcode") or "").strip()

            if entered_passcode != expected_pass:
                send_message(
                    chat_id,
                    "❌ <b>Test paroli noto'g'ri!</b>\n\nIltimos, ustozingiz bergan to'g'ri parolni kiriting (yoki bekor qilish uchun /bekor deb yozing):",
                    reply_markup=CANCEL_KEYBOARD
                )
                return

            user_states.pop(chat_id, None)
            launch_quiz_for_user(chat_id, user, quiz)
            return

        elif cur_state == "WAITING_USER_ID_FOR_PRO":
            entered_val = text.strip().upper()
            eb_alt = f"EB-{entered_val}" if (not entered_val.startswith("EB-") and entered_val.isdigit()) else entered_val
            conn = get_db()
            c = conn.cursor()
            c.execute("SELECT * FROM users WHERE UPPER(username) = ? OR UPPER(username) = ? OR LOWER(telegram_username) = ? OR id = ?", (entered_val, eb_alt, text.strip().lower().lstrip('@'), int(text) if text.strip().isdigit() else -1))
            found_user = c.fetchone()
            conn.close()
            if not found_user:
                send_message(chat_id, f"⚠️ '<code>{entered_val}</code>' bo'yicha EduBattle foydalanuvchisi topilmadi.\nIltimos, qaytadan Login raqamingizni (masalan: <code>EB-84841</code>) to'g'ri kiriting yoki /bekor deb yozing.")
                return
            user_states.pop(chat_id, None)
            start_pro_purchase_flow(chat_id, dict(found_user), user_lang=user_lang)
            return

        elif cur_state == "WAITING_PAYMENT_RECEIPT":
            send_message(chat_id, "📸 Iltimos, to'lovni amalga oshirgach, to'lov chekining fotosuratini (skrinshot) yoki PDF faylini to'g'ridan-to'g'ri shu botga yuboring.\n\nAgar bekor qilmoqchi bo'lsangiz: ❌ Bekor qilish tugmasini bosing.", reply_markup=CANCEL_KEYBOARD)
            return

    # If user sent test code directly without pressing button first
    if text.startswith("TEST-") or text.startswith("QZ") or text.startswith("MATH-"):
        quiz = find_quiz_by_pin(text.strip().upper())
        if quiz:
            expected_pass = str(quiz.get("passcode") or "").strip()
            if expected_pass:
                user_states[chat_id] = {
                    "state": "WAITING_FOR_PASSCODE",
                    "data": {"quiz": quiz, "pin_code": text.strip().upper()}
                }
                send_message(
                    chat_id,
                    f"✅ Test topildi: <b>{quiz['title']}</b>\n\n🔒 Iltimos, ushbu test uchun <b>Test Parolini</b> kiriting:",
                    reply_markup=CANCEL_KEYBOARD
                )
                return
            else:
                launch_quiz_for_user(chat_id, user, quiz)
                return

    # Default fallback message
    send_message(
        chat_id,
        "Test topshirish uchun quyidagi <b>'📝 Test topshirish (Kod & Parol)'</b> tugmasini bosing:",
        reply_markup=MAIN_KEYBOARD
    )

# ----------------- TEST LAUNCH & INTERACTIVE QUIZ ENGINE -----------------

def launch_quiz_for_user(chat_id, user, quiz):
    questions = quiz.get("questions") or []
    if not questions:
        send_message(chat_id, "⚠️ Ushbu testda hali savollar mavjud emas. Ustozingizga murojaat qiling.", reply_markup=MAIN_KEYBOARD)
        return

    active_sessions[chat_id] = {
        "user_id": user["id"],
        "user_name": user["full_name"],
        "quiz": quiz,
        "questions": questions,
        "current_index": 0,
        "correct_count": 0,
        "wrong_count": 0,
        "start_time": time.time(),
        "answered_current": False
    }

    q_count = len(questions)
    timer_sec = quiz.get("time_limit_sec", 30)

    start_card = (
        f"🎯 <b>Testga Kirish Muvaffaqiyatli!</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n"
        f"📚 <b>Fan:</b> {quiz.get('subject_name', 'Fan')}\n"
        f"📝 <b>Mavzu:</b> {quiz.get('title', 'Test')}\n"
        f"👨‍🏫 <b>Ustoz:</b> {quiz.get('teacher_name', 'O\'qituvchi')}\n"
        f"❓ <b>Savollar soni:</b> {q_count} ta\n"
        f"⏱ <b>Vaqt:</b> Har bir savolga {timer_sec} soniya\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"🚀 Boshlashga tayyormisiz? <b>'Boshlash'</b> tugmasini bosing:"
    )
    start_markup = {
        "inline_keyboard": [
            [{"text": "🚀 Testni Boshlash ➔", "callback_data": "quiz_start"}]
        ]
    }
    send_message(chat_id, start_card, reply_markup=start_markup)

def send_current_question(chat_id, session):
    idx = session["current_index"]
    questions = session["questions"]
    total = len(questions)

    if idx >= total:
        finish_quiz_session(chat_id, session)
        return

    q = questions[idx]
    q_text = q.get("question_text", "Savol")
    opts = q.get("options", [])

    letters = ["A", "B", "C", "D", "E"]
    inline_keyboard = []

    # Build option buttons
    for opt_idx, opt_text in enumerate(opts):
        letter = letters[opt_idx] if opt_idx < len(letters) else f"{opt_idx+1}"
        inline_keyboard.append([
            {"text": f"{letter}) {opt_text}", "callback_data": f"ans_{idx}_{opt_idx}"}
        ])

    session["answered_current"] = False

    msg_text = (
        f"<b>📝 Savol {idx + 1} / {total}:</b>\n\n"
        f"<b>{q_text}</b>\n\n"
        f"<i>To'g'ri javob variantini tanlang:</i>"
    )

    send_message(chat_id, msg_text, reply_markup={"inline_keyboard": inline_keyboard})

def handle_callback_query(callback_query):
    cq_id = callback_query.get("id")
    from_user = callback_query.get("from", {})
    chat_id = callback_query.get("message", {}).get("chat", {}).get("id")
    message_id = callback_query.get("message", {}).get("message_id")
    data = (callback_query.get("data") or "").strip()

    if not chat_id:
        answer_callback_query(cq_id)
        return

    # Language change callback
    if data.startswith("set_lang_"):
        new_lang = data.replace("set_lang_", "")
        chat_lang_cache[chat_id] = new_lang
        conn = get_db()
        c = conn.cursor()
        c.execute("UPDATE users SET lang = ? WHERE telegram_id = ?", (new_lang, chat_id))
        conn.commit()
        conn.close()
        if new_lang == "ru":
            answer_callback_query(cq_id, "Язык изменен: Русский 🇷🇺")
            send_message(chat_id, "✅ <b>Язык успешно изменен на Русский 🇷🇺!</b>\n\nТеперь бот и интерфейс будут отвечать вам на русском языке.", reply_markup=get_main_keyboard("ru"))
        elif new_lang == "en":
            answer_callback_query(cq_id, "Language changed: English 🇬🇧")
            send_message(chat_id, "✅ <b>Language successfully changed to English 🇬🇧!</b>\n\nNow the bot and system interface will respond in English.", reply_markup=get_main_keyboard("en"))
        else:
            answer_callback_query(cq_id, "Til o'zgartirildi: O'zbekcha 🇺🇿")
            send_message(chat_id, "✅ <b>Til muvaffaqiyatli o'zgartirildi: O'zbekcha 🇺🇿!</b>\n\nEndi bot va tizim sizga o'zbek tilida xizmat ko'rsatadi.", reply_markup=get_main_keyboard("uz"))
        return

    # Start quiz button
    if data == "quiz_start":
        answer_callback_query(cq_id, "Test boshlandi!")
        session = active_sessions.get(chat_id)
        if session:
            session["start_time"] = time.time()
            send_current_question(chat_id, session)
        return

    # Answer submission: ans_{q_idx}_{opt_idx}
    if data.startswith("ans_"):
        session = active_sessions.get(chat_id)
        if not session:
            answer_callback_query(cq_id, "Test sessiyasi yakunlangan.", show_alert=True)
            return

        parts = data.split("_")
        if len(parts) != 3:
            answer_callback_query(cq_id)
            return

        q_idx = int(parts[1])
        chosen_opt = int(parts[2])

        if q_idx != session["current_index"] or session["answered_current"]:
            answer_callback_query(cq_id, "Bu savolga allaqachon javob berildi!")
            return

        session["answered_current"] = True
        questions = session["questions"]
        q = questions[q_idx]
        correct_idx = int(q.get("correct_index", 0))
        opts = q.get("options", [])
        letters = ["A", "B", "C", "D", "E"]

        is_correct = (chosen_opt == correct_idx)
        if is_correct:
            session["correct_count"] += 1
            feedback = "✅ <b>To'g'ri javob!</b> 🎉"
            answer_callback_query(cq_id, "To'g'ri! ✅")
        else:
            session["wrong_count"] += 1
            correct_letter = letters[correct_idx] if correct_idx < len(letters) else str(correct_idx)
            correct_text = opts[correct_idx] if correct_idx < len(opts) else ""
            feedback = f"❌ <b>Noto'g'ri javob!</b>\nTo'g'ri javob: <b>{correct_letter}) {correct_text}</b>"
            answer_callback_query(cq_id, "Noto'g'ri! ❌")

        # Explanation
        expl = (q.get("explanation") or "").strip()
        if expl:
            feedback += f"\n\n💡 <b>Izoh:</b> <i>{expl}</i>"

        total = len(questions)
        is_last = (q_idx + 1 >= total)

        next_markup = {
            "inline_keyboard": [
                [
                    {
                        "text": "🏁 Natijani Ko'rish ➔" if is_last else f"➡️ Keyingi Savol ({q_idx + 2}/{total}) ➔",
                        "callback_data": "quiz_finish" if is_last else f"next_{q_idx + 1}"
                    }
                ]
            ]
        }

        # Edit original message with feedback
        orig_text = (
            f"<b>📝 Savol {q_idx + 1} / {total}:</b>\n\n"
            f"<b>{q.get('question_text')}</b>\n\n"
            f"Tanlovingiz: <b>{letters[chosen_opt] if chosen_opt < len(letters) else chosen_opt}) {opts[chosen_opt] if chosen_opt < len(opts) else ''}</b>\n\n"
            f"{feedback}"
        )
        edit_message_text(chat_id, message_id, orig_text, reply_markup=next_markup)
        return

    # Advance to next question: next_{idx}
    if data.startswith("next_"):
        answer_callback_query(cq_id)
        session = active_sessions.get(chat_id)
        if session:
            next_idx = int(data.split("_")[1])
            session["current_index"] = next_idx
            send_current_question(chat_id, session)
        return

    # Finish quiz
    if data == "quiz_finish":
        answer_callback_query(cq_id)
        session = active_sessions.get(chat_id)
        if session:
            finish_quiz_session(chat_id, session)
        return

    # Restart/New test
    if data == "new_test":
        answer_callback_query(cq_id)
        user_states[chat_id] = {"state": "WAITING_FOR_PIN", "data": {}}
        prompt_text = "🔑 Ustozingiz bergan yangi <b>Test Kodini (PIN)</b> kiriting:\n(Masalan: <code>TEST-677</code>)"
        send_message(chat_id, prompt_text, reply_markup=CANCEL_KEYBOARD)
        return

    if data.startswith("adm_") or data.startswith("admin_"):
        answer_callback_query(cq_id, "Admin amallari faqat @admidinsfesefse_bot orqali bajariladi!", show_alert=True)
        return

    # Download callbacks
    if data == "dl_hub":
        answer_callback_query(cq_id)
        send_download_hub(chat_id)
        return

    if data in ("dl_android", "dl_android_tg"):
        answer_callback_query(cq_id, "APK ma'lumotlari tayyorlanmoqda... ⏳")
        send_apk_to_user(chat_id)
        return

    if data == "dl_ios":
        answer_callback_query(cq_id)
        send_ios_guide(chat_id)
        return

    if data == "dl_web":
        answer_callback_query(cq_id)
        send_web_guide(chat_id)
        return

    # View my grades callback
    if data == "my_grades":
        answer_callback_query(cq_id)
        handle_message({"chat": {"id": chat_id}, "from": from_user, "text": "📊 Natijalarim & Baholarim"})
        return

    # PRO Payment Method Selection
    if data.startswith("pay_method_"):
        answer_callback_query(cq_id)
        parts = data.split("_")
        if len(parts) >= 4:
            method = parts[2]
            u_id = int(parts[3])
            show_payment_details(chat_id, u_id, method, message_id=message_id)
        return

    # Cancel PRO Payment
    if data == "cancel_pro_pay":
        answer_callback_query(cq_id, "To'lov bekor qilindi.")
        user_states.pop(chat_id, None)
        edit_message_text(chat_id, message_id, "❌ To'lov jarayoni bekor qilindi. Bosh menyudasiz:", reply_markup=None)
        return



    answer_callback_query(cq_id)

def finish_quiz_session(chat_id, session):
    active_sessions.pop(chat_id, None)

    user_id = session["user_id"]
    user_name = session["user_name"]
    quiz = session["quiz"]
    questions = session["questions"]
    total_q = len(questions)
    correct = session["correct_count"]
    wrong = session["wrong_count"]
    time_spent = int(time.time() - session["start_time"])

    # Save to database
    score_pct = save_quiz_result(user_id, quiz, correct, total_q, time_spent)
    grade_text = get_grade_badge(score_pct)

    result_card = (
        f"🏆 <b>TEST YAKUNLANDI!</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n"
        f"📚 <b>Test:</b> {quiz.get('title')}\n"
        f"👤 <b>O'quvchi:</b> {user_name}\n\n"
        f"📊 <b>Natija:</b> <b>{score_pct} / 100 ball</b> ⭐\n"
        f"🎖 <b>Milliy Baho:</b> <b>{grade_text}</b>\n"
        f"✅ <b>To'g'ri javoblar:</b> {correct} ta\n"
        f"❌ <b>Noto'g'ri javoblar:</b> {wrong} ta\n"
        f"⏱ <b>Sarflangan vaqt:</b> {time_spent} soniya\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n"
        f"📌 <i>Natijangiz ustozingizning baholar jurnaliga va umumiy maktab reytingiga muvaffaqiyatli saqlandi!</i>"
    )

    action_buttons = {
        "inline_keyboard": [
            [{"text": "📝 Boshqa test topshirish", "callback_data": "new_test"}],
            [{"text": "📊 Baholarim va Reytingim", "callback_data": "my_grades"}]
        ]
    }

    send_message(chat_id, result_card, reply_markup=action_buttons)
    send_message(chat_id, "Asosiy menyuga qaytish uchun tugmalardan foydalanishingiz mumkin:", reply_markup=MAIN_KEYBOARD)

# ----------------- LONG POLLING DAEMON -----------------

def run_bot_polling():
    logging.info("Starting Telegram Bot long-polling for @edubattleuz_bot...")
    setup_bot_commands()
    offset = 0
    while True:
        try:
            updates_res = tg_request("getUpdates", {"offset": offset, "timeout": 25})
            if updates_res and updates_res.get("ok"):
                updates = updates_res.get("result", [])
                for u in updates:
                    offset = u["update_id"] + 1
                    if "message" in u:
                        handle_message(u["message"])
                    elif "callback_query" in u:
                        handle_callback_query(u["callback_query"])
            else:
                time.sleep(2)
        except Exception as e:
            logging.error(f"Polling loop exception: {e}")
            time.sleep(3)

def start_telegram_bot_thread():
    t = threading.Thread(target=run_bot_polling, daemon=True, name="TelegramBotWorker")
    t.start()
    logging.info("Telegram Bot background thread spawned successfully.")
    return t

if __name__ == "__main__":
    run_bot_polling()
