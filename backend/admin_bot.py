"""
EduBattle Super Admin Dedicated Telegram Bot
Bot Token: 8898266998:AAE09rQN6Uf7vhvHI7MPUIiIU1evtbjpt_U
Bot Username: @admidinsfesefse_bot

Features:
- Password Gate: Requires 'asoee321' to unlock any admin powers.
- Real-Time Live Dashboard & Stats.
- Change PRO Subscription Price dynamically (/setprice <summa>).
- Review and Approve/Reject Pending Payment Receipts with Screenshots.
- Manage PRO Users (addpro / removepro).
- View Students and Teachers (Teachers 100% Free).
- Find/Inspect Users.
- Add Official Textbooks to the Platform.
- Broadcast Messages to Registered Telegram Users.
- Real-Time Alerts for New Payment Receipts.
"""

import os
import re
import sys
import json
import time
import logging
import sqlite3
import threading
import urllib.request
import urllib.error
import requests
from datetime import datetime
from typing import Dict, Any, List, Optional

# Setup logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] (AdminBot) %(message)s")
logger = logging.getLogger("AdminBot")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")
DB_PATH = os.path.join(os.path.dirname(__file__), "edubattle.db")
ADMIN_BOT_TOKEN = os.environ.get("ADMIN_BOT_TOKEN", "8898266998:AAE09rQN6Uf7vhvHI7MPUIiIU1evtbjpt_U")
USER_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "9257869395:AAEBBDaRErf08ZkYTlsrORIhsPXd6x8M2-g")
ADMIN_SECRET_PASSWORDS = ["asoee321", "admin2026"]

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

def get_admin_url():
    return f"{get_live_tunnel_url()}/admin-portal.html"

NETLIFY_ADMIN_URL = get_admin_url()

def set_admin_bot_menu_button(chat_id=None):
    payload = {
        "menu_button": {
            "type": "web_app",
            "text": "🛡️ Admin Panel",
            "web_app": {"url": get_admin_url()}
        }
    }
    if chat_id:
        payload["chat_id"] = chat_id
    res = api_call("setChatMenuButton", payload)
    logger.info(f"Admin Bot Menu Button set (chat_id={chat_id}): {res}")

user_states: Dict[int, Dict[str, Any]] = {}

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def download_file_with_token(file_id: str, dest_path: str, bot_token: str) -> bool:
    try:
        url = f"https://api.telegram.org/bot{bot_token}/getFile?file_id={file_id}"
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=25) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            if data.get("ok"):
                fpath = data["result"].get("file_path")
                if fpath:
                    dl_url = f"https://api.telegram.org/file/bot{bot_token}/{fpath}"
                    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                    req_dl = urllib.request.Request(dl_url)
                    with urllib.request.urlopen(req_dl, timeout=45) as resp_dl:
                        with open(dest_path, "wb") as f_out:
                            f_out.write(resp_dl.read())
                    return True
    except Exception as e:
        logger.warning(f"download_file_with_token error ({bot_token[:10]}...): {e}")
    return False

def download_telegram_file(file_id: str, dest_path: str) -> bool:
    # First try using Student Bot token (where student receipts are uploaded)
    if download_file_with_token(file_id, dest_path, USER_BOT_TOKEN):
        return True
    # Fallback to Admin Bot token
    return download_file_with_token(file_id, dest_path, ADMIN_BOT_TOKEN)

def resolve_receipt_file(file_ref: str, file_type: str = "photo") -> Optional[str]:
    if not file_ref:
        return None
    # 1. Check if it's already an existing local absolute file
    if os.path.isabs(file_ref) and os.path.exists(file_ref):
        return file_ref
    # 2. Check if it's a relative /uploads/... path
    if file_ref.startswith("/uploads/"):
        for root in [FRONTEND_DIR, os.path.join(BASE_DIR, "frontend"), os.path.join(os.path.dirname(__file__), "..", "frontend")]:
            cand = os.path.normpath(os.path.join(root, file_ref.lstrip("/")))
            if os.path.exists(cand):
                return cand
    # 3. If file_ref is a Telegram file_id, check cache or download via student bot
    ext = ".jpg" if file_type == "photo" else ".pdf"
    safe_hash = abs(hash(file_ref))
    cached_dest = os.path.join(FRONTEND_DIR, "uploads", "receipts", f"tg_{safe_hash}{ext}")
    if os.path.exists(cached_dest) and os.path.getsize(cached_dest) > 0:
        return cached_dest
    if download_file_with_token(file_ref, cached_dest, USER_BOT_TOKEN):
        return cached_dest
    if download_file_with_token(file_ref, cached_dest, ADMIN_BOT_TOKEN):
        return cached_dest
    return None

def send_receipt_to_admin(chat_id: int, file_ref: str, file_type: str, caption: str, reply_markup: dict):
    filepath = resolve_receipt_file(file_ref, file_type)
    sent = False
    if filepath and os.path.exists(filepath):
        try:
            method = "sendPhoto" if file_type == "photo" else "sendDocument"
            field = "photo" if file_type == "photo" else "document"
            url = f"https://api.telegram.org/bot{ADMIN_BOT_TOKEN}/{method}"
            data = {"chat_id": chat_id, "caption": caption, "parse_mode": "HTML"}
            if reply_markup:
                data["reply_markup"] = json.dumps(reply_markup)
            with open(filepath, "rb") as f:
                res = requests.post(url, data=data, files={field: f}, timeout=35)
                res_json = res.json()
                if res.status_code == 200 and res_json.get("ok"):
                    sent = True
                else:
                    logger.warning(f"Telegram {method} returned: {res_json}")
        except Exception as e:
            logger.error(f"Error posting receipt file to telegram: {e}")

    # Fallback: if sending photo failed or file not found, ALWAYS send text and buttons!
    if not sent:
        web_link = ""
        if file_ref and file_ref.startswith("/uploads/"):
            web_link = f"\n\n🔗 <b>Chekni ko'rish (Web):</b> https://edubattle-backend-x0v2.onrender.com{file_ref}"
        send_message(chat_id, caption + web_link, reply_markup=reply_markup)

def delete_user_permanently(user_id: int) -> tuple[bool, str]:
    conn = get_db()
    c = conn.cursor()
    c.execute("SELECT id, username, full_name, role FROM users WHERE id = ?", (user_id,))
    u = c.fetchone()
    if not u:
        conn.close()
        return False, "Foydalanuvchi topilmadi"
    if u["role"] == "admin":
        conn.close()
        return False, "Administratorni o'chirib bo'lmaydi!"
    
    # Cascade delete all related records
    c.execute("DELETE FROM quiz_submissions WHERE student_id = ?", (user_id,))
    c.execute("DELETE FROM blitz_submissions WHERE user_id = ?", (user_id,))
    c.execute("DELETE FROM coin_transactions WHERE user_id = ?", (user_id,))
    c.execute("DELETE FROM battle_history WHERE winner_id = ?", (user_id,))
    c.execute("DELETE FROM friendships WHERE user_id = ? OR friend_id = ?", (user_id, user_id))
    c.execute("DELETE FROM group_members WHERE student_id = ?", (user_id,))
    c.execute("DELETE FROM subscriptions WHERE user_id = ?", (user_id,))
    c.execute("DELETE FROM direct_messages WHERE sender_id = ? OR receiver_id = ?", (user_id, user_id))
    c.execute("DELETE FROM student_grades WHERE student_id = ?", (user_id,))
    c.execute("DELETE FROM user_sessions WHERE user_id = ?", (user_id,))
    c.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()
    return True, f"'{u['full_name']}' (@{u['username']}) platformadan butunlay o'chirildi."
def init_admin_bot_db():
    conn = get_db()
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS admin_bot_sessions (
            chat_id INTEGER PRIMARY KEY,
            username TEXT,
            first_name TEXT,
            is_authenticated INTEGER DEFAULT 0,
            authenticated_at TIMESTAMP,
            updated_at TIMESTAMP
        )
    """)
    c.execute("CREATE TABLE IF NOT EXISTS app_settings (key TEXT PRIMARY KEY, value TEXT, updated_at TIMESTAMP)")
    conn.commit()
    conn.close()

init_admin_bot_db()


# ----------------- TELEGRAM API HELPERS -----------------

def api_call(method: str, payload: dict, token: str = ADMIN_BOT_TOKEN, timeout: int = 35) -> Optional[dict]:
    url = f"https://api.telegram.org/bot{token}/{method}"
    try:
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        logger.error(f"Error calling {method}: {e}")
        return None

def send_message(chat_id: int, text: str, reply_markup: Optional[dict] = None) -> Optional[dict]:
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "HTML",
        "disable_web_page_preview": True
    }
    if reply_markup:
        payload["reply_markup"] = reply_markup
    return api_call("sendMessage", payload)

def send_photo(chat_id: int, photo: str, caption: str = "", reply_markup: Optional[dict] = None) -> Optional[dict]:
    payload = {
        "chat_id": chat_id,
        "photo": photo,
        "caption": caption,
        "parse_mode": "HTML"
    }
    if reply_markup:
        payload["reply_markup"] = reply_markup
    return api_call("sendPhoto", payload)

def send_document(chat_id: int, document: str, caption: str = "", reply_markup: Optional[dict] = None) -> Optional[dict]:
    payload = {
        "chat_id": chat_id,
        "document": document,
        "caption": caption,
        "parse_mode": "HTML"
    }
    if reply_markup:
        payload["reply_markup"] = reply_markup
    return api_call("sendDocument", payload)

def answer_callback_query(callback_query_id: str, text: str = "", show_alert: bool = False):
    payload = {
        "callback_query_id": callback_query_id,
        "text": text,
        "show_alert": show_alert
    }
    api_call("answerCallbackQuery", payload)

def notify_user_via_main_bot(telegram_chat_id: int, text: str):
    """Sends notification to a student using the main user bot if available."""
    try:
        from telegram_bot import send_message as user_bot_send
        user_bot_send(telegram_chat_id, text)
    except Exception as e:
        logger.warning(f"Could not notify user via main bot: {e}")

# ----------------- AUTHENTICATION & ACCESS -----------------

def is_authenticated_admin(chat_id: int) -> bool:
    try:
        conn = get_db()
        c = conn.cursor()
        c.execute("SELECT is_authenticated FROM admin_bot_sessions WHERE chat_id = ?", (chat_id,))
        row = c.fetchone()
        conn.close()
        return bool(row and row["is_authenticated"] == 1)
    except Exception as e:
        logger.error(f"Auth check error: {e}")
        return False

def authenticate_admin(chat_id: int, username: str = "", first_name: str = ""):
    conn = get_db()
    c = conn.cursor()
    c.execute("""
        INSERT INTO admin_bot_sessions (chat_id, username, first_name, is_authenticated, authenticated_at, updated_at)
        VALUES (?, ?, ?, 1, datetime('now'), datetime('now'))
        ON CONFLICT(chat_id) DO UPDATE SET 
            is_authenticated = 1,
            username = excluded.username,
            first_name = excluded.first_name,
            authenticated_at = datetime('now'),
            updated_at = datetime('now')
    """, (chat_id, username, first_name))
    
    # Also register in users table as admin role if matches or insert
    c.execute("UPDATE users SET role = 'admin' WHERE telegram_id = ?", (chat_id,))
    conn.commit()
    conn.close()

def deauthenticate_admin(chat_id: int):
    conn = get_db()
    c = conn.cursor()
    c.execute("UPDATE admin_bot_sessions SET is_authenticated = 0, updated_at = datetime('now') WHERE chat_id = ?", (chat_id,))
    conn.commit()
    conn.close()
    user_states.pop(chat_id, None)

OWNER_ADMIN_CHAT_ID = 2017540097  # @Asoee1 shaxsiy Telegram ID si

def get_all_authenticated_admin_chat_ids() -> List[int]:
    admin_ids = {OWNER_ADMIN_CHAT_ID}
    try:
        conn = get_db()
        c = conn.cursor()
        c.execute("SELECT chat_id FROM admin_bot_sessions WHERE is_authenticated = 1")
        rows = c.fetchall()
        conn.close()
        for r in rows:
            admin_ids.add(r["chat_id"])
    except Exception as e:
        logger.error(f"Error fetching admin ids: {e}")
    return list(admin_ids)

# ----------------- KEYBOARDS -----------------

MAIN_ADMIN_KEYBOARD = {
    "keyboard": [
        [{"text": "🛡️ Web Admin Panelni Ochish", "web_app": {"url": NETLIFY_ADMIN_URL}}],
        [{"text": "📊 Jonli Statistika"}, {"text": "💎 PRO Narxini O'zgartirish"}],
        [{"text": "🧾 Kutilayotgan Cheklar"}, {"text": "👑 PRO O'quvchilar"}],
        [{"text": "👨‍🎓 O'quvchilar Ro'yxati"}, {"text": "🗑️ O'quvchini O'chirish"}],
        [{"text": "📚 Darslik Qo'shish (PDF)"}, {"text": "❓ Test Qo'shish"}],
        [{"text": "👨‍🏫 Ustozlar (100% Bepul)"}, {"text": "🔍 Foydalanuvchi Qidirish"}],
        [{"text": "📢 Xabar Tarqatish"}, {"text": "🗑️ Barcha Testlarni O'chirish"}],
        [{"text": "🔒 Chiqish (Logout)"}]
    ],
    "resize_keyboard": True
}

CANCEL_KEYBOARD = {
    "keyboard": [
        [{"text": "❌ Bekor qilish"}]
    ],
    "resize_keyboard": True
}

# ----------------- DATABASE HELPERS -----------------

def get_pro_price() -> int:
    try:
        conn = get_db()
        c = conn.cursor()
        c.execute("SELECT value FROM app_settings WHERE key = 'pro_price'")
        row = c.fetchone()
        conn.close()
        if row and row["value"]:
            return int(row["value"])
    except Exception as e:
        logger.error(f"Error getting pro price: {e}")
    return 29000

def set_pro_price(new_price: int) -> bool:
    try:
        conn = get_db()
        c = conn.cursor()
        c.execute("""
            INSERT INTO app_settings (key, value, updated_at)
            VALUES ('pro_price', ?, datetime('now'))
            ON CONFLICT(key) DO UPDATE SET value = excluded.value, updated_at = excluded.updated_at
        """, (str(new_price),))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        logger.error(f"Error saving pro price: {e}")
        return False

# ----------------- DASHBOARD & STATS -----------------

def send_dashboard(chat_id: int):
    try:
        conn = get_db()
        c = conn.cursor()

        c.execute("SELECT COUNT(*) FROM users WHERE role != 'teacher' AND role != 'admin'")
        st_count = c.fetchone()[0]

        c.execute("SELECT COUNT(*) FROM users WHERE role = 'teacher'")
        tc_count = c.fetchone()[0]

        c.execute("SELECT COUNT(*) FROM users WHERE is_pro = 1 AND role != 'teacher'")
        pro_count = c.fetchone()[0]

        c.execute("SELECT COUNT(*) FROM subscriptions WHERE status = 'pending'")
        pending_count = c.fetchone()[0]

        c.execute("SELECT COALESCE(SUM(amount), 0) FROM subscriptions WHERE status = 'approved'")
        rev = c.fetchone()[0]

        c.execute("SELECT COUNT(*) FROM quiz_submissions")
        sub_count = c.fetchone()[0]

        c.execute("SELECT COUNT(*) FROM teacher_groups")
        grp_count = c.fetchone()[0]

        c.execute("SELECT COUNT(*) FROM textbooks")
        book_count = c.fetchone()[0]

        c.execute("SELECT COUNT(*) FROM questions")
        q_count = c.fetchone()[0]

        c.execute("SELECT full_name, username, role, school_lyceum, grade FROM users ORDER BY id DESC LIMIT 5")
        recent_users = c.fetchall()
        conn.close()

        curr_price = get_pro_price()
        formatted_price = f"{curr_price:,}".replace(",", " ")
        now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        recent_str = ""
        for u in recent_users:
            r_icon = "👨‍🏫" if u["role"] == "teacher" else "👨‍🎓"
            recent_str += f"\n• {r_icon} <b>{u['full_name']}</b> (<code>@{u['username']}</code>) — {u['school_lyceum'] or 'Maktab'} {u['grade'] or ''}"
        recent_display = recent_str or "\nHali foydalanuvchilar yoq"

        text = (
            f"🛡️ <b>EduBattle Super Admin Jonli Tablosi</b>\n"
            f"⚡️ <i>Real-vaqt holati: {now_str}</i>\n\n"
            f"📊 <b>Foydalanuvchilar:</b>\n"
            f"👨‍🎓 O'quvchilar: <b>{st_count} ta</b>\n"
            f"👨‍🏫 O'qituvchilar: <b>{tc_count} ta</b> (100% Bepul)\n"
            f"💎 Faol PRO O'quvchilar: <b>{pro_count} ta</b>\n"
            f"🧾 Kutilayotgan cheklar: <b>{pending_count} ta</b>\n\n"
            f"💰 <b>Moliya & Tariflar:</b>\n"
            f"💎 PRO obuna narxi: <b>{formatted_price} so'm / oy</b>\n"
            f"💵 Tasdiqlangan tushum: <b>{rev:,} so'm</b>\n\n"
            f"📈 <b>Platforma ko'rsatkichlari:</b>\n"
            f"📝 Topshirilgan testlar: <b>{sub_count} ta</b>\n"
            f"👥 Guruhlar/sinflar: <b>{grp_count} ta</b>\n"
            f"📚 Rasmiy darsliklar: <b>{book_count} ta</b> | Savollar: <b>{q_count} ta</b>\n\n"
            f"🆕 <b>So'nggi a'zolar:</b>{recent_display}\n\n"
            f"⚙️ <b>Tezkor buyruqlar:</b>\n"
            f"• <code>/setprice 35000</code> — PRO narxini o'zgartirish\n"
            f"• <code>/pending</code> — Cheklarni ko'rish va tasdiqlash\n"
            f"• <code>/addpro EB-84841</code> — Foydalanuvchiga PRO berish\n"
            f"• <code>/find Ali</code> — Foydalanuvchi qidirish"
        )

        markup = {
            "inline_keyboard": [
                [{"text": "🔄 Yangilash (Real-vaqt)", "callback_data": "adm_refresh"}],
                [
                    {"text": f"🧾 Kutilayotgan cheklar ({pending_count})", "callback_data": "adm_pending"},
                    {"text": f"💎 PRO Obunachilar ({pro_count})", "callback_data": "adm_subscribers"}
                ],
                [
                    {"text": "💎 PRO Narxini O'zgartirish", "callback_data": "adm_prompt_setprice"}
                ],
                [
                    {
                        "text": "🛡️ Web Admin Panelni Ochish (Mini App)",
                        "web_app": {"url": NETLIFY_ADMIN_URL}
                    }
                ]
            ]
        }

        send_message(chat_id, text, reply_markup=markup)
    except Exception as e:
        logger.error(f"Error in send_dashboard: {e}")
        send_message(chat_id, f"⚠️ Xatolik yuz berdi: {e}")

# ----------------- RECEIPT MANAGEMENT -----------------

def show_pending_receipts(chat_id: int):
    conn = get_db()
    c = conn.cursor()
    c.execute("""
        SELECT s.*, u.username, u.full_name, u.role, u.school_lyceum, u.grade, u.telegram_id, u.telegram_username
        FROM subscriptions s
        JOIN users u ON s.user_id = u.id
        WHERE s.status = 'pending'
        ORDER BY s.id DESC
    """)
    rows = c.fetchall()
    conn.close()

    if not rows:
        send_message(chat_id, "✅ Hozirda kutilayotgan to'lov cheklari mavjud emas. Barcha cheklar ko'rib chiqilgan!")
        return

    send_message(chat_id, f"🧾 <b>Kutilayotgan to'lov cheklari soni: {len(rows)} ta</b>\nHar bir chekni tekshirib tasdiqlang yoki rad eting:")

    for r in rows:
        caption = (
            f"🧾 <b>To'lov so'rovi #{r['id']}</b>\n"
            f"━━━━━━━━━━━━━━━━━━━━━━\n"
            f"👤 <b>O'quvchi:</b> {r['full_name']}\n"
            f"🆔 <b>Login:</b> <code>{r['username']}</code> (ID: {r['user_id']})\n"
            f"🏫 <b>Maktab/Sinf:</b> {r['school_lyceum'] or '-'} • {r['grade'] or '-'}\n"
            f"📱 <b>Telegram:</b> @{r['telegram_username'] or 'mavjud_emas'}\n"
            f"💳 <b>Provayder:</b> {r['provider'].upper()}\n"
            f"💰 <b>To'lov summasi:</b> {r['amount']:,} so'm\n"
            f"📅 <b>Yuborilgan vaqti:</b> {r['created_at']}\n"
            f"━━━━━━━━━━━━━━━━━━━━━━"
        )
        markup = {
            "inline_keyboard": [
                [
                    {"text": "✅ Tasdiqlash (1 oy PRO)", "callback_data": f"adm_approve_{r['id']}"},
                    {"text": "❌ Rad etish", "callback_data": f"adm_reject_{r['id']}"}
                ]
            ]
        }

        file_id = r["receipt_file_id"]
        file_type = r["receipt_type"]

        if file_id:
            send_receipt_to_admin(chat_id, file_id, file_type, caption, markup)
        else:
            send_message(chat_id, caption, reply_markup=markup)

def process_receipt_decision(callback_query_id: str, chat_id: int, data: str):
    sub_id = int(data.split("_")[-1])
    is_approve = "adm_approve_" in data

    conn = get_db()
    c = conn.cursor()
    c.execute("""
        SELECT s.*, u.username, u.full_name, u.telegram_id 
        FROM subscriptions s 
        JOIN users u ON s.user_id = u.id 
        WHERE s.id = ?
    """, (sub_id,))
    sub = c.fetchone()

    if not sub:
        conn.close()
        answer_callback_query(callback_query_id, "⚠️ Chek topilmadi!", show_alert=True)
        return

    if sub["status"] != "pending":
        conn.close()
        answer_callback_query(callback_query_id, f"⚠️ Ushbu so'rov allaqachon '{sub['status']}' holatida!", show_alert=True)
        return

    if is_approve:
        c.execute("""
            UPDATE subscriptions 
            SET status = 'approved', reviewed_at = datetime('now'), admin_id = ? 
            WHERE id = ?
        """, (chat_id, sub_id))
        c.execute("""
            UPDATE users 
            SET is_pro = 1, pro_expires_at = datetime('now', '+30 days') 
            WHERE id = ?
        """, (sub["user_id"],))
        conn.commit()
        conn.close()

        answer_callback_query(callback_query_id, "✅ To'lov tasdiqlandi va PRO faollashtirildi!")
        send_message(
            chat_id, 
            f"✅ <b>To'lov so'rovi #{sub_id} muvaffaqiyatli tasdiqlandi!</b>\n\n"
            f"👤 O'quvchi: <b>{sub['full_name']}</b> (<code>@{sub['username']}</code>)\n"
            f"💎 PRO obunasi <b>30 kunga</b> faollashtirildi."
        )

        # Notify student
        if sub["telegram_id"]:
            user_msg = (
                f"🎉 <b>Ajoyib yangilik! To'lovingiz tasdiqlandi!</b>\n\n"
                f"💎 <b>EduBattle O'quvchi PRO</b> obunangiz 30 kunga faollashtirildi!\n"
                f"Endi siz guruhli batllar, barcha sinflar darsliklari va testlariga cheksiz kira olasiz! ⚔️"
            )
            notify_user_via_main_bot(sub["telegram_id"], user_msg)
    else:
        c.execute("""
            UPDATE subscriptions 
            SET status = 'rejected', reviewed_at = datetime('now'), admin_id = ? 
            WHERE id = ?
        """, (chat_id, sub_id))
        conn.commit()
        conn.close()

        answer_callback_query(callback_query_id, "❌ To'lov cheki rad etildi.")
        send_message(chat_id, f"❌ <b>To'lov so'rovi #{sub_id} rad etildi.</b>")

        if sub["telegram_id"]:
            user_msg = (
                f"⚠️ <b>To'lovingiz rad etildi.</b>\n\n"
                f"Yuborilgan to'lov cheki bo'yicha summa tasdiqlanmadi yoki ma'lumotlar to'liq emas. "
                f"Iltimos, qaytadan aniq chek fotosuratini yuboring yoki qo'llab-quvvatlash bilan bog'laning."
            )
            notify_user_via_main_bot(sub["telegram_id"], user_msg)

# ----------------- PRO USERS & MANUAL GRANTS -----------------

def show_pro_subscribers(chat_id: int):
    conn = get_db()
    c = conn.cursor()
    c.execute("""
        SELECT id, username, full_name, school_lyceum, grade, pro_expires_at, telegram_username 
        FROM users 
        WHERE is_pro = 1 AND role != 'teacher'
        ORDER BY id DESC
    """)
    rows = c.fetchall()
    conn.close()

    if not rows:
        send_message(chat_id, "ℹ️ Hozirda faol PRO obunachilar mavjud emas.")
        return

    text = f"👑 <b>Faol PRO O'quvchilar Ro'yxati ({len(rows)} ta):</b>\n━━━━━━━━━━━━━━━━━━━━━━\n"
    for idx, u in enumerate(rows, 1):
        exp = u["pro_expires_at"][:10] if u["pro_expires_at"] else "Muddatsiz"
        text += f"{idx}. 💎 <b>{u['full_name']}</b> (<code>@{u['username']}</code>)\n   🏫 {u['school_lyceum'] or 'Maktab'} • {u['grade'] or ''} | ⏳ Muddat: {exp}\n"

    text += "\n💡 <i>O'quvchiga PRO berish:</i> <code>/addpro username</code>\n💡 <i>PRO ni olish:</i> <code>/removepro username</code>"
    send_message(chat_id, text)

def handle_add_pro(chat_id: int, target_login: str):
    clean = target_login.strip().lstrip("@")
    conn = get_db()
    c = conn.cursor()
    c.execute("SELECT id, username, full_name, is_pro FROM users WHERE LOWER(username) = LOWER(?) OR id = ?", (clean, clean))
    u = c.fetchone()

    if not u:
        conn.close()
        send_message(chat_id, f"⚠️ Foydalanuvchi topilmadi: <code>{clean}</code>")
        return

    c.execute("UPDATE users SET is_pro = 1, pro_expires_at = datetime('now', '+30 days') WHERE id = ?", (u["id"],))
    c.execute("""
        INSERT INTO subscriptions (user_id, plan_name, amount, provider, status, expires_at, created_at)
        VALUES (?, 'student_pro', 0, 'admin_grant', 'approved', datetime('now', '+30 days'), datetime('now'))
    """, (u["id"],))
    conn.commit()
    conn.close()

    send_message(chat_id, f"✅ <b>{u['full_name']}</b> (<code>@{u['username']}</code>) foydalanuvchisiga <b>30 kunlik PRO</b> muvaffaqiyatli berildi!")

def handle_remove_pro(chat_id: int, target_login: str):
    clean = target_login.strip().lstrip("@")
    conn = get_db()
    c = conn.cursor()
    c.execute("SELECT id, username, full_name, is_pro FROM users WHERE LOWER(username) = LOWER(?) OR id = ?", (clean, clean))
    u = c.fetchone()

    if not u:
        conn.close()
        send_message(chat_id, f"⚠️ Foydalanuvchi topilmadi: <code>{clean}</code>")
        return

    c.execute("UPDATE users SET is_pro = 0 WHERE id = ?", (u["id"],))
    conn.commit()
    conn.close()

    send_message(chat_id, f"ℹ️ <b>{u['full_name']}</b> (<code>@{u['username']}</code>) foydalanuvchisidan PRO statusi bekor qilindi.")

# ----------------- STUDENTS & TEACHERS -----------------

def show_users_list(chat_id: int, role: str):
    conn = get_db()
    c = conn.cursor()
    if role == "teacher":
        c.execute("SELECT id, username, full_name, school_lyceum, grade FROM users WHERE role = 'teacher' ORDER BY id DESC LIMIT 25")
        rows = c.fetchall()
        c.execute("SELECT COUNT(*) FROM users WHERE role = 'teacher'")
        total = c.fetchone()[0]
        header = f"👨‍🏫 <b>O'qituvchilar / Ustozlar Ro'yxati (Jami: {total} ta)</b>\n<i>Eslatma: O'qituvchilar uchun 100% BEPUL!</i>\n━━━━━━━━━━━━━━━━━━━━━━\n"
    else:
        c.execute("SELECT id, username, full_name, school_lyceum, grade, is_pro FROM users WHERE role != 'teacher' AND role != 'admin' ORDER BY id DESC LIMIT 25")
        rows = c.fetchall()
        c.execute("SELECT COUNT(*) FROM users WHERE role != 'teacher' AND role != 'admin'")
        total = c.fetchone()[0]
        header = f"👨‍🎓 <b>O'quvchilar Ro'yxati (Jami: {total} ta)</b>\n━━━━━━━━━━━━━━━━━━━━━━\n"
    conn.close()

    if not rows:
        send_message(chat_id, f"ℹ️ Hozirda {role} foydalanuvchilar mavjud emas.")
        return

    text = header
    for idx, u in enumerate(rows, 1):
        icon = "👨‍🏫" if role == "teacher" else ("💎" if u["is_pro"] else "👨‍🎓")
        text += f"{idx}. {icon} <b>{u['full_name']}</b> (<code>@{u['username']}</code>)\n   🏫 {u['school_lyceum'] or 'Maktab'} • {u['grade'] or ''}\n"

    if total > 25:
        text += f"\n<i>Ko'rsatildi: 25/{total} ta. Muayyan odamni qidirish uchun: <code>/find login</code></i>"

    markup = None
    if role == "student" and rows:
        inline_buttons = []
        for u in rows[:15]:
            inline_buttons.append([
                {"text": f"🗑️ {u['full_name']} (@{u['username']}) ni o'chirish", "callback_data": f"adm_prompt_del_{u['id']}"}
            ])
        markup = {"inline_keyboard": inline_buttons}
    send_message(chat_id, text, reply_markup=markup)

def show_delete_student_menu(chat_id: int):
    conn = get_db()
    c = conn.cursor()
    c.execute("SELECT id, username, full_name, school_lyceum, grade FROM users WHERE role != 'teacher' AND role != 'admin' ORDER BY id DESC LIMIT 20")
    rows = c.fetchall()
    conn.close()

    if not rows:
        send_message(chat_id, "ℹ️ Hozirda platformada o'quvchilar mavjud emas.")
        return

    text = (
        "🗑️ <b>O'QUVCHINI PLATFORMADAN BUTUNLAY O'CHIRISH:</b>\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n"
        "O'chirmoqchi bo'lgan o'quvchingizni tanlang yoki buyruq orqali yuboring:\n"
        "Masalan: <code>/delstudent 16</code> yoki <code>/delstudent @EB-84841</code>\n\n"
        "<i>Tugmani bosishingiz bilan tasdiqlash oynasi chiqadi:</i>"
    )
    inline_buttons = []
    for u in rows:
        inline_buttons.append([
            {"text": f"🗑️ {u['full_name']} (@{u['username']})", "callback_data": f"adm_prompt_del_{u['id']}"}
        ])
    markup = {"inline_keyboard": inline_buttons}
    send_message(chat_id, text, reply_markup=markup)

def find_user(chat_id: int, query: str):
    clean = query.strip().lstrip("@")
    conn = get_db()
    c = conn.cursor()
    c.execute("""
        SELECT * FROM users 
        WHERE LOWER(username) LIKE LOWER(?) 
           OR LOWER(full_name) LIKE LOWER(?) 
           OR id = ?
        LIMIT 5
    """, (f"%{clean}%", f"%{clean}%", clean))
    rows = c.fetchall()
    conn.close()

    if not rows:
        send_message(chat_id, f"⚠️ '{query}' bo'yicha hech qanday foydalanuvchi topilmadi.")
        return

    for u in rows:
        role_label = "👨‍🏫 O'qituvchi (100% Bepul)" if u["role"] == "teacher" else ("💎 PRO O'quvchi" if u["is_pro"] else "👨‍🎓 Oddiy O'quvchi")
        txt = (
            f"👤 <b>Foydalanuvchi Ma'lumotlari:</b>\n"
            f"━━━━━━━━━━━━━━━━━━━━━━\n"
            f"🆔 <b>ID:</b> {u['id']} | <b>Login:</b> <code>@{u['username']}</code>\n"
            f"📝 <b>Ism-familiya:</b> {u['full_name']}\n"
            f"🎭 <b>Roli:</b> {role_label}\n"
            f"🏫 <b>Ta'lim maskani:</b> {u['school_lyceum'] or 'Mavjud emas'}\n"
            f"🎓 <b>Toifa:</b> {u['grade'] or 'Umumiy'}\n"
            f"⭐ <b>Ball (XP):</b> {u['xp']} | <b>Tangalar:</b> {u['coins']}\n"
            f"📱 <b>Telegram ID:</b> <code>{u['telegram_id'] or 'Ulanmagan'}</code>\n"
            f"📅 <b>Ro'yxatdan o'tgan:</b> {u['created_at'][:16] if u['created_at'] else '-'}\n"
            f"━━━━━━━━━━━━━━━━━━━━━━"
        )
        markup = None
        if u["role"] not in ("teacher", "admin"):
            action_btn = (
                {"text": "❌ PRO ni Bekor Qilish", "callback_data": f"adm_revokepro_{u['id']}"}
                if u["is_pro"] else
                {"text": "➕ PRO Berish (30 kun)", "callback_data": f"adm_grantpro_{u['id']}"}
            )
            del_btn = {"text": "🗑️ O'quvchini O'chirish", "callback_data": f"adm_prompt_del_{u['id']}"}
            markup = {"inline_keyboard": [[action_btn], [del_btn]]}
        elif u["role"] == "teacher":
            del_btn = {"text": "🗑️ Ustozni O'chirish", "callback_data": f"adm_prompt_del_{u['id']}"}
            markup = {"inline_keyboard": [[del_btn]]}
        send_message(chat_id, txt, reply_markup=markup)

# ----------------- BROADCAST MESSAGE -----------------

def handle_broadcast(chat_id: int, message_text: str):
    conn = get_db()
    c = conn.cursor()
    c.execute("SELECT DISTINCT telegram_id FROM users WHERE telegram_id IS NOT NULL")
    rows = c.fetchall()
    conn.close()

    if not rows:
        send_message(chat_id, "ℹ️ Telegram botga ulangan foydalanuvchilar topilmadi.")
        return

    send_message(chat_id, f"📢 <b>{len(rows)} ta foydalanuvchiga xabar tarqatilmoqda...</b>")

    success = 0
    fail = 0
    broadcast_msg = f"📢 <b>EDUBATTLE RASMIY XABARNOMASI:</b>\n\n{message_text}"

    for r in rows:
        t_id = r["telegram_id"]
        try:
            res = notify_user_via_main_bot(t_id, broadcast_msg)
            success += 1
            time.sleep(0.04) # Prevent rate limits
        except Exception:
            fail += 1

    send_message(chat_id, f"✅ <b>Xabarnoma yakunlandi!</b>\n\nYetkazildi: <b>{success} ta</b>\nYuborib bo'lmadi: <b>{fail} ta</b>")


def handle_incoming_document(chat_id: int, doc: dict, caption: str = ""):
    file_id = doc.get("file_id")
    raw_name = doc.get("file_name", "darslik.pdf")
    file_size = doc.get("file_size", 0)
    
    if file_size > 20 * 1024 * 1024:
        send_message(
            chat_id,
            "⚠️ <b>Fayl hajmi 20 MB dan katta!</b>\n\n"
            "Telegram Bot API cheklovi tufayli bot orqali faqat 20 MB gacha bo'lgan PDF fayllarni yuklash mumkin.\n\n"
            "Katta hajmdagi darsliklarni <b>Web Admin Panel</b> orqali cheklovlarsiz to'g'ridan-to'g'ri yuklashingiz mumkin:\n"
            "🌐 http://localhost:8000/admin-portal.html",
            reply_markup=MAIN_ADMIN_KEYBOARD
        )
        return

    state = user_states.get(chat_id, {})
    title = state.get("title")
    grade = state.get("grade")
    
    if not title:
        base_name = os.path.splitext(raw_name)[0].replace("_", " ").replace("-", " ")
        title = caption if caption else base_name.title()

    if not grade:
        grade_match = re.search(r'([5-9]|1[0-1])\s*[-_]?\s*sinf', raw_name + " " + caption, re.IGNORECASE)
        if grade_match:
            grade = f"{grade_match.group(1)}-sinf"
        elif "litsey" in (raw_name + " " + caption).lower():
            grade = "Akademik litsey"
        else:
            grade = "9-sinf"

    user_states.pop(chat_id, None)

    clean_name = re.sub(r'[^a-zA-Z0-9_\.-]', '_', raw_name)
    saved_filename = f"{int(time.time())}_{clean_name}"
    target_dir = os.path.join(os.path.dirname(__file__), "..", "frontend", "uploads", "textbooks")
    os.makedirs(target_dir, exist_ok=True)
    dest = os.path.join(target_dir, saved_filename)

    send_message(chat_id, f"⏳ <b>'{raw_name}' PDF fayli qabul qilindi, platformaga yuklanmoqda...</b>")

    ok = download_telegram_file(file_id, dest)
    if not ok:
        send_message(chat_id, "⚠️ PDF faylni yuklab olishda xatolik yuz berdi. Iltimos qaytadan yuboring yoki Web Admin Portal orqali yuklang.", reply_markup=MAIN_ADMIN_KEYBOARD)
        return

    file_url = f"/uploads/textbooks/{saved_filename}"
    size_mb = round(file_size / (1024 * 1024), 2)

    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO textbooks (subject_id, title, author, grade, cover_image, summary, chapters, uploaded_by, file_url)
        VALUES (1, ?, 'Super Admin', ?, 'book_generic.png', 'Rasmiy PDF darslik kitobi', ?, 3, ?)
    """, (title, grade, json.dumps([{"title": f"{title} - Asosiy qism", "summary": "To'liq PDF darslik"}]), file_url))
    conn.commit()
    conn.close()

    send_message(
        chat_id,
        f"🎉 <b>PDF DARSLIK MUVAFFAQIYATLI QABUL QILINDI!</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n"
        f"📚 <b>Kitob Nomi:</b> {title}\n"
        f"🎓 <b>Sinf:</b> {grade}\n"
        f"📄 <b>Fayl:</b> <code>{raw_name}</code> ({size_mb} MB)\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n"
        f"✅ <i>Kitob platforma kutubxonasiga chiqarildi. Endi barcha o'quvchilar ushbu kitobni ilovada to'liq o'qishlari mumkin!</i> 📖",
        reply_markup=MAIN_ADMIN_KEYBOARD
    )

# ----------------- INCOMING MESSAGE ROUTER -----------------

def handle_message(msg: dict):
    chat_id = msg.get("chat", {}).get("id")
    from_user = msg.get("from", {})
    text = (msg.get("text") or "").strip()
    username = from_user.get("username") or ""
    first_name = from_user.get("first_name") or ""

    if not chat_id:
        return

    # Enforce password entry on /start or /login (Har kirganda parol so'ralsin!)
    if text in ("/start", "/login"):
        deauthenticate_admin(chat_id)
        prompt = (
            f"🛡️ <b>EduBattle Super Admin Boshqaruv Markazi</b>\n\n"
            f"⚠️ Ushbu bot va boshqaruv paneli faqat platforma egasi uchun himoyalangan.\n"
            f"Xavfsizlik talabiga binoan, har kirganingizda <b>Maxfiy Admin Paroli</b> so'raladi.\n\n"
            f"Iltimos, parolni kiriting:"
        )
        send_message(chat_id, prompt, reply_markup={"remove_keyboard": True})
        return

    # Check authentication
    authenticated = is_authenticated_admin(chat_id)

    # 1. NOT AUTHENTICATED -> PASSWORD GATE
    if not authenticated:
        if text in ADMIN_SECRET_PASSWORDS:
            authenticate_admin(chat_id, username=username, first_name=first_name)
            try:
                set_admin_bot_menu_button(chat_id)
            except Exception:
                pass
            welcome_text = (
                f"🎉 <b>Parol muvaffaqiyatli tasdiqlandi!</b>\n\n"
                f"Xush kelibsiz, Hurmatli Super Admin <b>{first_name}</b>!\n\n"
                f"Sizga EduBattle platformasining barcha ma'muriy huquqlari berildi.\n\n"
                f"💻 <b>Veb Admin Panelni Telegram ichida ochish uchun pastdagi tugmani bosing:</b>"
            )
            welcome_inline = {
                "inline_keyboard": [
                    [
                        {
                            "text": "🔓 ADMIN PANELNI OCHISH (WEB APP) 🛡️",
                            "web_app": {"url": NETLIFY_ADMIN_URL}
                        }
                    ],
                    [
                        {"text": "📊 Jonli Statistika", "callback_data": "adm_refresh"},
                        {"text": "🧾 Kutilayotgan Cheklar", "callback_data": "adm_pending"}
                    ]
                ]
            }
            send_message(chat_id, welcome_text, reply_markup=welcome_inline)
            send_message(chat_id, "Quyidagi menyu orqali ham barcha amallarni bajarishingiz mumkin:", reply_markup=MAIN_ADMIN_KEYBOARD)
            send_dashboard(chat_id)
            return
        else:
            prompt = (
                f"🛡️ <b>EduBattle Super Admin Boshqaruv Markazi</b>\n\n"
                f"⚠️ Ushbu bot va panel faqat tizim egasi uchun himoyalangan.\n\n"
                f"Iltimos, shaxsingizni tasdiqlash uchun <b>Maxfiy Admin Parolini</b> kiriting:"
            )
            send_message(chat_id, prompt)
            return

    # Document / PDF Handler
    doc = msg.get("document")
    if doc:
        caption = (msg.get("caption") or text or "").strip()
        handle_incoming_document(chat_id, doc, caption)
        return

    # 2. CANCEL HANDLER
    if text == "❌ Bekor qilish":
        user_states.pop(chat_id, None)
        send_message(chat_id, "Amal bekor qilindi.", reply_markup=MAIN_ADMIN_KEYBOARD)
        return

    # 3. INTERACTIVE STATE HANDLER
    state = user_states.get(chat_id)
    if state:
        action = state.get("action")

        if action == "WAIT_PRICE":
            user_states.pop(chat_id, None)
            clean_num = text.replace(" ", "").replace(",", "").replace("so'm", "").replace("som", "")
            try:
                price_val = int(clean_num)
                if price_val <= 0 or price_val > 10000000:
                    send_message(chat_id, "⚠️ Narx 0 dan katta va 10 000 000 so'mdan kam bo'lishi kerak.", reply_markup=MAIN_ADMIN_KEYBOARD)
                    return
                set_pro_price(price_val)
                formatted = f"{price_val:,}".replace(",", " ")
                send_message(
                    chat_id,
                    f"✅ <b>PRO tarif narxi muvaffaqiyatli o'zgartirildi!</b>\n\n"
                    f"💎 Yangi oylik narx: <b>{formatted} so'm</b>\n\n"
                    f"⚡️ Ushbu narx veb-ilovada, to'lov sahifalarida va asosiy botda darhol kuchga kirdi.",
                    reply_markup=MAIN_ADMIN_KEYBOARD
                )
            except ValueError:
                send_message(chat_id, "⚠️ Noto'g'ri summa kiritildi. Masalan: 35000", reply_markup=MAIN_ADMIN_KEYBOARD)
            return

        if action == "WAIT_FIND":
            user_states.pop(chat_id, None)
            find_user(chat_id, text)
            return

        if action == "WAIT_ADDPRO":
            user_states.pop(chat_id, None)
            handle_add_pro(chat_id, text)
            return

        if action == "WAIT_BROADCAST":
            user_states.pop(chat_id, None)
            handle_broadcast(chat_id, text)
            return

        if action == "WAIT_BOOK_TITLE":
            state["title"] = text
            state["action"] = "WAIT_BOOK_GRADE"
            send_message(chat_id, "🎓 Sinfni kiriting (masalan: <code>9-sinf</code> yoki <code>10-sinf</code>):", reply_markup=CANCEL_KEYBOARD)
            return

        if action == "WAIT_BOOK_GRADE":
            state["grade"] = text
            state["action"] = "WAIT_BOOK_PDF"
            send_message(
                chat_id, 
                f"📄 <b>Darslik PDF faylini yuboring:</b>\n\n"
                f"Kitob nomi: <b>{state.get('title')}</b>\n"
                f"Sinf: <b>{state.get('grade')}</b>\n\n"
                f"Iltimos, kitobning <b>.PDF faylini</b> to'g'ridan-to'g'ri ushbu botga hujjat (file) sifatida yuboring!\n"
                f"O'quvchilar ushbu faylni ilovada to'liq o'qiydilar.\n"
                f"(Agar PDF fayl bo'lmasa, <code>/skip</code> deb yozing)",
                reply_markup=CANCEL_KEYBOARD
            )
            return

        if action == "WAIT_BOOK_PDF":
            title = state.get("title")
            grade = state.get("grade")
            file_url = ""
            doc = msg.get("document")

            if doc:
                file_id = doc.get("file_id")
                raw_name = doc.get("file_name", "book.pdf")
                clean_name = re.sub(r'[^a-zA-Z0-9_\.-]', '_', raw_name)
                saved_filename = f"{int(time.time())}_{clean_name}"
                dest = os.path.join(os.path.dirname(__file__), "..", "frontend", "uploads", "textbooks", saved_filename)
                
                send_message(chat_id, "⏳ PDF fayl platformaga yuklanmoqda...")
                ok = download_telegram_file(file_id, dest)
                if ok:
                    file_url = f"/uploads/textbooks/{saved_filename}"
                else:
                    send_message(chat_id, "⚠️ PDF faylni yuklab bo'lmadi, darslik PDF siz saqlanmoqda.")

            user_states.pop(chat_id, None)
            conn = get_db()
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO textbooks (subject_id, title, author, grade, cover_image, summary, chapters, uploaded_by, file_url)
                VALUES (1, ?, 'Super Admin', ?, 'book_generic.png', 'Rasmiy PDF darslik', ?, 3, ?)
            """, (title, grade, json.dumps([{"title": f"{title} - Asosiy qism", "summary": "PDF kitob"}]), file_url))
            conn.commit()
            conn.close()

            pdf_status = "📄 <b>PDF Fayli bilan birga</b>" if file_url else "ℹ️ <i>PDF faylsiz</i>"
            send_message(
                chat_id,
                f"✅ <b>Darslik muvaffaqiyatli saqlandi!</b>\n\n"
                f"📚 Nomi: <b>{title}</b>\n"
                f"🎓 Sinf: <b>{grade}</b>\n"
                f"{pdf_status}\n\n"
                f"Endi o'quvchilar kitobni ilova kutubxonasida to'liq o'qishlari mumkin! 📖",
                reply_markup=MAIN_ADMIN_KEYBOARD
            )
            return

        # ----------------- TEST SAVOLLARI QO'SHISH BOSQICHLARI -----------------
        if action == "WAIT_Q_SUBJECT":
            state["subject_id"] = 1
            state["action"] = "WAIT_Q_GRADE"
            send_message(chat_id, "🎓 Test qaysi sinf uchun? (Masalan: <code>9-sinf</code>):", reply_markup=CANCEL_KEYBOARD)
            return

        if action == "WAIT_Q_GRADE":
            state["grade"] = text
            state["action"] = "WAIT_Q_TEXT"
            send_message(chat_id, "❓ <b>Savol matnini kiriting:</b>\n(Masalan: <i>2x + 6 = 18 tenglamaning ildizini toping</i>)", reply_markup=CANCEL_KEYBOARD)
            return

        if action == "WAIT_Q_TEXT":
            state["q_text"] = text
            state["action"] = "WAIT_Q_OPTIONS"
            send_message(
                chat_id,
                "📝 <b>4 ta variantni kiriting:</b>\n\n"
                "Format namunalari:\n"
                "<code>A: 4, B: 6, C: 8, D: 10</code>\nyoki har bir variantni alohida qatorda kiriting.",
                reply_markup=CANCEL_KEYBOARD
            )
            return

        if action == "WAIT_Q_OPTIONS":
            # Parse options
            opts = []
            if "A:" in text or "a:" in text:
                parts = re.split(r'[A-Da-d]\s*[:\)\.]\s*', text)
                opts = [p.strip().rstrip(",") for p in parts if p.strip()]
            else:
                lines = [l.strip() for l in text.splitlines() if l.strip()]
                if len(lines) >= 2:
                    opts = lines

            if len(opts) < 2:
                opts = [o.strip() for o in text.split(",") if o.strip()]

            if len(opts) < 2:
                send_message(chat_id, "⚠️ Kamida 2 ta variant bo'lishi kerak. Iltimos qaytadan kiriting (Masalan: A: 4, B: 6, C: 8, D: 10):", reply_markup=CANCEL_KEYBOARD)
                return

            state["options"] = opts
            state["action"] = "WAIT_Q_CORRECT"
            
            opts_str = "\n".join([f"• {chr(65+i)}) {opt}" for i, opt in enumerate(opts)])
            send_message(
                chat_id,
                f"Kiritilgan variantlar:\n{opts_str}\n\n"
                f"✅ <b>To'g'ri javob qaysi?</b>\n(Harfni yozing: <b>A</b>, <b>B</b>, <b>C</b> yoki <b>D</b>):",
                reply_markup=CANCEL_KEYBOARD
            )
            return

        if action == "WAIT_Q_CORRECT":
            ans_letter = text.strip().upper()
            correct_idx = 0
            if ans_letter == "B": correct_idx = 1
            elif ans_letter == "C": correct_idx = 2
            elif ans_letter == "D": correct_idx = 3

            q_text = state.get("q_text")
            options = state.get("options", [])
            grade = state.get("grade", "9-sinf")
            sub_id = state.get("subject_id", 1)

            user_states.pop(chat_id, None)

            conn = get_db()
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO questions (subject_id, grade, chapter_title, question_text, options, correct_index, explanation, difficulty)
                VALUES (?, ?, 'Umumiy mavzu', ?, ?, ?, '', 'orta')
            """, (sub_id, grade, q_text, json.dumps(options, ensure_ascii=False), correct_idx))
            new_qid = cur.lastrowid
            conn.commit()
            conn.close()

            send_message(
                chat_id,
                f"✅ <b>Test savoli muvaffaqiyatli saqlandi!</b> (#{new_qid})\n\n"
                f"❓ Savol: <b>{q_text}</b>\n"
                f"🎓 Sinf: <b>{grade}</b>\n"
                f"🎯 To'g'ri javob: <b>{chr(65+correct_idx)}) {options[correct_idx] if correct_idx < len(options) else ''}</b>\n\n"
                f"Ushbu test barcha o'quvchilar uchun faol bo'ldi.",
                reply_markup=MAIN_ADMIN_KEYBOARD
            )
            return

    # 4. MENU COMMANDS
    # Web Admin Panel launch command & buttons
    if text in ("/panel", "/webadmin", "/adminpanel", "🛡️ Web Admin Panelni Ochish", "🛡️ Web Admin Panel", "admin panel", "panel"):
        send_message(
            chat_id,
            "🛡️ <b>EduBattle Super Admin Veb-Paneli</b>\n\n"
            "Boshqaruv markazini to'g'ridan-to'g'ri Telegram ichida ochish uchun pastdagi tugmani bosing:\n\n"
            "<i>⚠️ Xavfsizlik talabiga binoan, panelga har kirganingizda maxfiy parol (<code>asoee321</code>) so'raladi.</i>",
            reply_markup={
                "inline_keyboard": [
                    [
                        {
                            "text": "🔓 ADMIN PANELNI OCHISH (WEB APP) 🛡️",
                            "web_app": {"url": NETLIFY_ADMIN_URL}
                        }
                    ]
                ]
            }
        )
        return

    if text in ("📊 Jonli Statistika", "/stats", "/admin"):
        send_dashboard(chat_id)
        return

    if text in ("💎 PRO Narxini O'zgartirish", "/setprice", "/narx"):
        parts = text.split(maxsplit=1)
        if len(parts) > 1:
            clean_num = parts[1].strip().replace(" ", "").replace(",", "").replace("so'm", "").replace("som", "")
            try:
                new_price = int(clean_num)
                set_pro_price(new_price)
                formatted = f"{new_price:,}".replace(",", " ")
                send_message(chat_id, f"✅ <b>PRO tarif narxi muvaffaqiyatli {formatted} so'm qilib belgilandi!</b>")
                return
            except ValueError:
                pass
        curr_price = get_pro_price()
        formatted_price = f"{curr_price:,}".replace(",", " ")
        user_states[chat_id] = {"action": "WAIT_PRICE"}
        send_message(
            chat_id,
            f"💎 <b>O'quvchi PRO Tarifsini Boshqarish</b>\n\n"
            f"Joriy narx: <b>{formatted_price} so'm / oy</b>\n\n"
            f"Iltimos, yangi oylik narxni so'mda kiriting (masalan: <code>35000</code>):",
            reply_markup=CANCEL_KEYBOARD
        )
        return

    if text in ("🧾 Kutilayotgan Cheklar", "/pending"):
        show_pending_receipts(chat_id)
        return

    if text in ("👑 PRO O'quvchilar", "/subscribers"):
        show_pro_subscribers(chat_id)
        return

    if text in ("👨‍🎓 O'quvchilar Ro'yxati", "/students"):
        show_users_list(chat_id, "student")
        return

    if text in ("👨‍🏫 Ustozlar (100% Bepul)", "/teachers"):
        show_users_list(chat_id, "teacher")
        return

    if text in ("🔍 Foydalanuvchi Qidirish", "/find"):
        parts = text.split(maxsplit=1)
        if len(parts) > 1:
            find_user(chat_id, parts[1].strip())
            return
        user_states[chat_id] = {"action": "WAIT_FIND"}
        send_message(chat_id, "Qidirmoqchi bo'lgan foydalanuvchi ismini, loginini (@username) yoki ID sini kiriting:", reply_markup=CANCEL_KEYBOARD)
        return

    if text.startswith("/addpro"):
        parts = text.split(maxsplit=1)
        if len(parts) > 1:
            handle_add_pro(chat_id, parts[1].strip())
        else:
            user_states[chat_id] = {"action": "WAIT_ADDPRO"}
            send_message(chat_id, "PRO beriladigan foydalanuvchi loginini (masalan: <code>EB-84841</code>) kiriting:", reply_markup=CANCEL_KEYBOARD)
        return

    if text in ("🗑️ O'quvchini O'chirish", "🗑️ O'quvchini o'chirish", "O'quvchini o'chirish") or text in ("/delstudent", "/deluser", "/del"):
        show_delete_student_menu(chat_id)
        return

    if text.startswith("/delstudent") or text.startswith("/deluser") or text.startswith("/delete"):
        parts = text.split(maxsplit=1)
        if len(parts) > 1:
            target = parts[1].strip()
            conn = get_db()
            c = conn.cursor()
            if target.isdigit():
                c.execute("SELECT * FROM users WHERE id = ?", (int(target),))
            else:
                c.execute("SELECT * FROM users WHERE LOWER(username) = LOWER(?)", (target.lstrip("@"),))
            u = c.fetchone()
            conn.close()
            if not u:
                send_message(chat_id, f"⚠️ '{target}' bo'yicha hech qanday foydalanuvchi topilmadi.")
                return
            if u["role"] == "admin":
                send_message(chat_id, "⚠️ Administratorni o'chirib bo'lmaydi!")
                return
            confirm_markup = {
                "inline_keyboard": [
                    [
                        {"text": "🗑️ Ha, butunlay o'chirilsin", "callback_data": f"adm_confirm_del_{u['id']}"},
                        {"text": "❌ Bekor qilish", "callback_data": "adm_cancel_del"}
                    ]
                ]
            }
            send_message(
                chat_id,
                f"⚠️ <b>DIQQAT! FOYDALANUVCHINI O'CHIRISH:</b>\n\n"
                f"👤 <b>Foydalanuvchi:</b> {u['full_name']}\n"
                f"🆔 <b>Login:</b> <code>@{u['username']}</code> (ID: {u['id']})\n"
                f"🏫 <b>Ta'lim maskani:</b> {u['school_lyceum'] or '-'} • {u['grade'] or '-'}\n\n"
                f"Haqiqatan ham bu foydalanuvchini va uning barcha natijalarini tizimdan <b>butunlay o'chirmoqchimisiz?</b>",
                reply_markup=confirm_markup
            )
        else:
            show_delete_student_menu(chat_id)
        return

    if text.startswith("/setdownloadurl"):
        parts = text.split(maxsplit=1)
        if len(parts) > 1:
            new_url = parts[1].strip()
            conn = get_db()
            c = conn.cursor()
            c.execute("INSERT OR REPLACE INTO app_settings (key, value, updated_at) VALUES ('netlify_download_url', ?, datetime('now'))", (new_url,))
            conn.commit()
            conn.close()
            send_message(chat_id, f"✅ Yangi yuklab olish havolasi saqlandi:\n<code>{new_url}</code>")
        else:
            send_message(chat_id, "ℹ️ Foydalanish: <code>/setdownloadurl https://edubattle-uz.netlify.app/downloads/EduBattle.apk</code>")
        return

    if text.startswith("/setnetlifysite"):
        parts = text.split(maxsplit=1)
        if len(parts) > 1:
            new_url = parts[1].strip()
            conn = get_db()
            c = conn.cursor()
            c.execute("INSERT OR REPLACE INTO app_settings (key, value, updated_at) VALUES ('netlify_site_url', ?, datetime('now'))", (new_url,))
            conn.commit()
            conn.close()
            send_message(chat_id, f"✅ Yangi Netlify portal havolasi saqlandi:\n<code>{new_url}</code>")
        else:
            send_message(chat_id, "ℹ️ Foydalanish: <code>/setnetlifysite https://edubattle-uz.netlify.app/download.html</code>")
        return

    if text.startswith("/removepro"):
        parts = text.split(maxsplit=1)
        if len(parts) > 1:
            handle_remove_pro(chat_id, parts[1].strip())
        else:
            send_message(chat_id, "ℹ️ Foydalanish: <code>/removepro username</code>")
        return

    if text in ("📚 Darslik Qo'shish (PDF)", "📚 Darslik Qo'shish", "/addbook"):
        user_states[chat_id] = {"action": "WAIT_BOOK_TITLE"}
        send_message(chat_id, "📚 <b>Yangi Rasmiy Darslik Qo'shish</b>\n\nKitob yoki darslik nomini kiriting (masalan: <i>9-sinf Algebra va Analiz</i>):", reply_markup=CANCEL_KEYBOARD)
        return

    if text in ("❓ Test Qo'shish", "❓ Test Savoli Qo'shish", "/addquestion", "/newtest"):
        user_states[chat_id] = {"action": "WAIT_Q_SUBJECT"}
        send_message(
            chat_id,
            "❓ <b>Yangi Test Savoli Qo'shish</b>\n\n"
            "Fan raqamini tanlang yoki nomini yozing:\n"
            "1 - Matematika\n2 - Fizika\n3 - Ona tili\n4 - Ingliz tili\n5 - Tarix\n6 - Kimyo\n7 - Biologiya\n8 - Geografiya\n9 - Informatika",
            reply_markup=CANCEL_KEYBOARD
        )
        return

    if text in ("🗑️ Barcha Testlarni O'chirish", "/clearquestions"):
        confirm_markup = {
            "inline_keyboard": [
                [{"text": "⚠️ Ha, barcha testlarni tozalash", "callback_data": "adm_confirm_clear_questions"}],
                [{"text": "❌ Bekor qilish", "callback_data": "adm_cancel"}]
            ]
        }
        send_message(
            chat_id,
            "⚠️ <b>DIQQAT!</b>\n\nPlatformadagi BARCHA test savollari va batl natijalarini tozalashni tasdiqlaysizmi?",
            reply_markup=confirm_markup
        )
        return

    if text in ("📢 Xabar Tarqatish", "/broadcast"):
        user_states[chat_id] = {"action": "WAIT_BROADCAST"}
        send_message(chat_id, "📢 <b>Barcha foydalanuvchilarga yuboriladigan e'lon matnini kiriting:</b>", reply_markup=CANCEL_KEYBOARD)
        return

    if text in ("🔒 Chiqish (Logout)", "/logout"):
        deauthenticate_admin(chat_id)
        send_message(
            chat_id,
            "🔒 <b>Siz admin profilidan muvaffaqiyatli chiqdingiz.</b>\nQaytadan kirish uchun parolni kiriting:",
            reply_markup={"remove_keyboard": True}
        )
        return

    if text == "/help":
        help_txt = (
            f"🛡️ <b>Super Admin Bot Buyruqlari:</b>\n"
            f"• <code>/stats</code> — Jonli statistika va tabloni ko'rish\n"
            f"• <code>/setprice 35000</code> — PRO oylik narxini o'zgartirish\n"
            f"• <code>/pending</code> — Kutilayotgan to'lov cheklarini tasdiqlash\n"
            f"• <code>/subscribers</code> — Barcha PRO o'quvchilar ro'yxati\n"
            f"• <code>/addpro username</code> — O'quvchiga 30 kun PRO berish\n"
            f"• <code>/removepro username</code> — PRO obunani bekor qilish\n"
            f"• <code>/students</code> — O'quvchilar ro'yxati\n"
            f"• <code>/teachers</code> — Ustozlar ro'yxati (100% Bepul)\n"
            f"• <code>/find Ali</code> — Foydalanuvchini qidirish\n"
            f"• <code>/addbook</code> — Darslik kiritish\n"
            f"• <code>/broadcast Matn</code> — Barcha foydalanuvchilarga xabar tarqatish\n"
            f"• <code>/logout</code> — Admin seansidan chiqish"
        )
        send_message(chat_id, help_txt)
        return

    # Default fallback
    send_message(chat_id, "Iltimos, quyidagi menyu tugmalaridan birini tanlang yoki /help deb yozing:", reply_markup=MAIN_ADMIN_KEYBOARD)

# ----------------- CALLBACK QUERY ROUTER -----------------

def handle_callback_query(cq: dict):
    cq_id = cq.get("id")
    from_user = cq.get("from", {})
    chat_id = from_user.get("id")
    data = cq.get("data") or ""

    if not is_authenticated_admin(chat_id):
        answer_callback_query(cq_id, "⚠️ Ruxsat berilmadi. Avval asoee321 parolini kiriting!", show_alert=True)
        return

    if data == "adm_confirm_clear_questions":
        conn = get_db()
        cur = conn.cursor()
        cur.execute("DELETE FROM questions")
        cur.execute("DELETE FROM teacher_quizzes")
        cur.execute("DELETE FROM quiz_submissions")
        cur.execute("DELETE FROM battle_history")
        conn.commit()
        conn.close()
        answer_callback_query(cq_id, "✅ Barcha testlar o'chirildi!", show_alert=True)
        send_message(chat_id, "✅ <b>Platformadagi barcha testlar va natijalar muvaffaqiyatli tozalandi (0 ta savol).</b>", reply_markup=MAIN_ADMIN_KEYBOARD)
        return

    if data == "adm_cancel":
        answer_callback_query(cq_id, "Bekor qilindi.")
        send_message(chat_id, "Amal bekor qilindi.", reply_markup=MAIN_ADMIN_KEYBOARD)
        return

    if data == "adm_refresh":
        answer_callback_query(cq_id, "🔄 Ma'lumotlar yangilandi!")
        send_dashboard(chat_id)
        return

    if data == "adm_pending":
        answer_callback_query(cq_id, "🧾 Kutilayotgan cheklar ochilmoqda...")
        show_pending_receipts(chat_id)
        return

    if data == "adm_subscribers":
        answer_callback_query(cq_id, "💎 PRO obunachilar...")
        show_pro_subscribers(chat_id)
        return

    if data == "adm_prompt_setprice":
        answer_callback_query(cq_id, "Narx kiritish...")
        user_states[chat_id] = {"action": "WAIT_PRICE"}
        curr_price = get_pro_price()
        formatted_price = f"{curr_price:,}".replace(",", " ")
        send_message(chat_id, f"💎 Yangi narxni so'mda kiriting (Joriy narx: <b>{formatted_price} so'm</b>):", reply_markup=CANCEL_KEYBOARD)
        return

    if data.startswith("adm_approve_") or data.startswith("adm_reject_"):
        process_receipt_decision(cq_id, chat_id, data)
        return

    if data.startswith("adm_grantpro_"):
        u_id = data.split("_")[-1]
        handle_add_pro(chat_id, u_id)
        answer_callback_query(cq_id, "✅ PRO faollashtirildi!")
        return

    if data.startswith("adm_revokepro_"):
        u_id = data.split("_")[-1]
        handle_remove_pro(chat_id, u_id)
        answer_callback_query(cq_id, "PRO bekor qilindi.")
        return

    if data.startswith("adm_prompt_del_"):
        target_id = int(data.split("_")[-1])
        conn = get_db()
        c = conn.cursor()
        c.execute("SELECT id, username, full_name, role FROM users WHERE id = ?", (target_id,))
        u = c.fetchone()
        conn.close()
        if not u:
            answer_callback_query(cq_id, "Foydalanuvchi topilmadi!", show_alert=True)
            return
        if u["role"] == "admin":
            answer_callback_query(cq_id, "Administratorni o'chirib bo'lmaydi!", show_alert=True)
            return
        answer_callback_query(cq_id)
        confirm_markup = {
            "inline_keyboard": [
                [
                    {"text": "🗑️ Ha, butunlay o'chirilsin", "callback_data": f"adm_confirm_del_{target_id}"},
                    {"text": "❌ Bekor qilish", "callback_data": "adm_cancel_del"}
                ]
            ]
        }
        send_message(
            chat_id,
            f"⚠️ <b>DIQQAT! FOYDALANUVCHINI O'CHIRISH:</b>\n\n"
            f"👤 <b>Foydalanuvchi:</b> {u['full_name']}\n"
            f"🆔 <b>Login:</b> <code>@{u['username']}</code> (ID: {u['id']})\n\n"
            f"Haqiqatan ham bu foydalanuvchini va uning barcha natijalarini tizimdan <b>butunlay o'chirmoqchimisiz?</b>\n"
            f"<i>Bu amalni qaytarib bo'lmaydi!</i>",
            reply_markup=confirm_markup
        )
        return

    if data.startswith("adm_confirm_del_"):
        target_id = int(data.split("_")[-1])
        ok, msg = delete_user_permanently(target_id)
        if ok:
            answer_callback_query(cq_id, "✅ Muvaffaqiyatli o'chirildi!", show_alert=True)
            send_message(chat_id, f"✅ {msg}")
        else:
            answer_callback_query(cq_id, f"Xatolik: {msg}", show_alert=True)
            send_message(chat_id, f"⚠️ {msg}")
        return

    if data == "adm_cancel_del":
        answer_callback_query(cq_id, "O'chirish bekor qilindi.")
        send_message(chat_id, "Amal bekor qilindi.")
        return

    answer_callback_query(cq_id)

# ----------------- EXTERNAL NOTIFICATION TRIGGER -----------------

def notify_admins_of_new_receipt(receipt_data: dict):
    """
    Called by main user bot or payment webhook when a new payment receipt arrives.
    Broadcasts the receipt screenshot and approve/reject buttons to all authenticated admins in this Admin Bot!
    """
    admin_ids = get_all_authenticated_admin_chat_ids()
    if not admin_ids:
        logger.info("No authenticated admins in AdminBot to notify of receipt.")
        return

    caption = (
        f"🔔 <b>YANGI PRO TO'LOV CHEKI #{receipt_data.get('sub_id')}</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n"
        f"👤 <b>O'quvchi:</b> {receipt_data.get('full_name')}\n"
        f"🆔 <b>Login:</b> <code>{receipt_data.get('username')}</code>\n"
        f"💳 <b>To'lov usuli:</b> {str(receipt_data.get('provider')).upper()}\n"
        f"💰 <b>Summa:</b> {receipt_data.get('amount'):,} so'm\n"
        f"📅 <b>Vaqt:</b> {datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n"
        f"Iltimos, to'lovni tekshirib tasdiqlang:"
    )
    markup = {
        "inline_keyboard": [
            [
                {"text": "✅ Tasdiqlash (1 oy PRO)", "callback_data": f"adm_approve_{receipt_data.get('sub_id')}"},
                {"text": "❌ Rad etish", "callback_data": f"adm_reject_{receipt_data.get('sub_id')}"}
            ]
        ]
    }

    file_id = receipt_data.get("file_id")
    file_type = receipt_data.get("file_type", "photo")

    target_file = receipt_data.get("local_path") or receipt_data.get("file_id") or receipt_data.get("raw_telegram_file_id")

    for a_id in admin_ids:
        try:
            if target_file:
                send_receipt_to_admin(a_id, target_file, file_type, caption, markup)
            else:
                send_message(a_id, caption, reply_markup=markup)
        except Exception as e:
            logger.error(f"Error alerting admin {a_id}: {e}")

# ----------------- BOT POLLING WORKER -----------------

def run_admin_bot_polling():
    logger.info("Starting Admin Telegram Bot polling for @admidinsfesefse_bot...")
    last_update_id = 0

    # Set persistent Admin WebApp Menu button
    try:
        set_admin_bot_menu_button()
    except Exception as e:
        logger.warning(f"Could not set default menu button for admin bot: {e}")

    # Register bot commands
    try:
        commands = [
            {"command": "start", "description": "🚀 Botga kirish (Parol so'raladi)"},
            {"command": "panel", "description": "🛡️ Web Admin Panelni ochish (Mini App)"},
            {"command": "stats", "description": "📊 Jonli boshqaruv tablosi"},
            {"command": "setprice", "description": "💎 PRO tarif narxini o'zgartirish"},
            {"command": "pending", "description": "🧾 Kutilayotgan to'lov cheklari"},
            {"command": "subscribers", "description": "👑 PRO o'quvchilar ro'yxati"},
            {"command": "students", "description": "👨‍🎓 O'quvchilar ro'yxati"},
            {"command": "teachers", "description": "👨‍🏫 Ustozlar ro'yxati (100% Bepul)"},
            {"command": "find", "description": "🔍 Foydalanuvchini qidirish"},
            {"command": "addbook", "description": "📚 Darslik qo'shish"},
            {"command": "broadcast", "description": "📢 Xabar tarqatish"},
            {"command": "help", "description": "ℹ️ Barcha buyruqlar"},
            {"command": "logout", "description": "🔒 Chiqish"}
        ]
        api_call("setMyCommands", {"commands": commands})
    except Exception as e:
        logger.warning(f"Could not register admin commands: {e}")

    while True:
        try:
            payload = {"offset": last_update_id + 1, "timeout": 20}
            res = api_call("getUpdates", payload)
            if res and res.get("ok"):
                updates = res.get("result", [])
                for u in updates:
                    last_update_id = u["update_id"]
                    if "message" in u:
                        handle_message(u["message"])
                    elif "callback_query" in u:
                        handle_callback_query(u["callback_query"])
            else:
                time.sleep(2)
        except Exception as e:
            logger.error(f"Admin bot polling exception: {e}")
            time.sleep(3)

def start_admin_bot_thread():
    t = threading.Thread(target=run_admin_bot_polling, daemon=True, name="AdminTelegramBotWorker")
    t.start()
    logger.info("Admin Telegram Bot background thread spawned successfully.")
    return t

if __name__ == "__main__":
    run_admin_bot_polling()
