import os
import re
import json
import random
import asyncio
import hashlib
import secrets
import hmac
import time
from datetime import datetime
from typing import Dict, List, Optional
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, HTTPException, Query, Body, Request, File, UploadFile, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from database import get_db, init_db

app = FastAPI(title="Zukko EduBattle Platform", version="2.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    init_db()
    render_url = os.environ.get("RENDER_EXTERNAL_URL") or "https://edubattle-backend-x0v2.onrender.com"
    render_url = render_url.rstrip("/")

    # Keep-alive daemon: prevents Render free instance from spinning down
    try:
        def keep_alive_daemon():
            import time
            import requests
            time.sleep(30)
            target = render_url or "https://edubattle-backend-x0v2.onrender.com"
            while True:
                try:
                    res = requests.get(f"{target}/api/subjects", timeout=20)
                    print(f"[KeepAlive] Self-ping status: {res.status_code}")
                except Exception as err:
                    print(f"[KeepAlive] Self-ping error: {err}")
                time.sleep(300) # every 5 minutes (Render idle limit is 15 minutes)

        import threading
        threading.Thread(target=keep_alive_daemon, daemon=True, name="RenderKeepAlive").start()
    except Exception as e:
        print(f"Failed to start keep_alive_daemon: {e}")

    # Register Webhooks on Render so Telegram automatically wakes up and delivers messages 24/7
    try:
        import requests
        from telegram_bot import BOT_TOKEN as STUDENT_BOT_TOKEN
        from admin_bot import ADMIN_BOT_TOKEN

        wh_student = f"{render_url}/api/telegram-webhook"
        r1 = requests.post(f"https://api.telegram.org/bot{STUDENT_BOT_TOKEN}/setWebhook", json={"url": wh_student}, timeout=15).json()
        print(f"Student Bot Webhook ({wh_student}): {r1}")

        wh_admin = f"{render_url}/api/admin-telegram-webhook"
        r2 = requests.post(f"https://api.telegram.org/bot{ADMIN_BOT_TOKEN}/setWebhook", json={"url": wh_admin}, timeout=15).json()
        print(f"Admin Bot Webhook ({wh_admin}): {r2}")
    except Exception as e:
        print(f"Failed to set webhook: {e}")
        # Fallback to polling
        try:
            from telegram_bot import start_telegram_bot_thread
            start_telegram_bot_thread()
        except:
            pass
        try:
            from admin_bot import start_admin_bot_thread
            start_admin_bot_thread()
        except:
            pass

# ----------------- TELEGRAM WEBHOOK ENDPOINTS (24/7 CLOUD DISPATCH) -----------------
@app.post("/api/telegram-webhook")
async def telegram_webhook(request: Request):
    try:
        update = await request.json()
        from telegram_bot import handle_message, handle_callback_query
        if "message" in update:
            handle_message(update["message"])
        elif "callback_query" in update:
            handle_callback_query(update["callback_query"])
        return {"ok": True}
    except Exception as e:
        print(f"Telegram webhook error: {e}")
        return {"ok": False, "error": str(e)}

@app.post("/api/admin-telegram-webhook")
async def admin_telegram_webhook(request: Request):
    try:
        update = await request.json()
        from admin_bot import handle_message, handle_callback_query
        if "message" in update:
            handle_message(update["message"])
        elif "callback_query" in update:
            handle_callback_query(update["callback_query"])
        return {"ok": True}
    except Exception as e:
        print(f"Admin webhook error: {e}")
        return {"ok": False, "error": str(e)}

@app.get("/api/setup-webhooks")
def api_setup_webhooks():
    import requests
    render_url = (os.environ.get("RENDER_EXTERNAL_URL") or "https://edubattle-backend-x0v2.onrender.com").rstrip("/")
    from telegram_bot import BOT_TOKEN as STUDENT_BOT_TOKEN
    from admin_bot import ADMIN_BOT_TOKEN
    
    wh_student = f"{render_url}/api/telegram-webhook"
    wh_admin = f"{render_url}/api/admin-telegram-webhook"
    
    r1 = requests.post(f"https://api.telegram.org/bot{STUDENT_BOT_TOKEN}/setWebhook", json={"url": wh_student}, timeout=15).json()
    r2 = requests.post(f"https://api.telegram.org/bot{ADMIN_BOT_TOKEN}/setWebhook", json={"url": wh_admin}, timeout=15).json()
    
    return {
        "student_bot_webhook": r1,
        "admin_bot_webhook": r2,
        "student_url": wh_student,
        "admin_url": wh_admin
    }

# ----------------- SECURITY & NO-CACHE HEADERS MIDDLEWARE -----------------
@app.middleware("http")
async def add_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "SAMEORIGIN"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response

# ----------------- SECURITY UTILITIES (PBKDF2 & RATE LIMITING) -----------------

def hash_password(password: str) -> str:
    salt = secrets.token_hex(16)
    key = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt.encode("utf-8"), 100000).hex()
    return f"{salt}${key}"

def verify_password(password: str, stored_hash: str) -> bool:
    if not stored_hash:
        return False
    if "$" in stored_hash:
        parts = stored_hash.split("$", 1)
        if len(parts) != 2:
            return False
        salt, key = parts
        check = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt.encode("utf-8"), 100000).hex()
        return hmac.compare_digest(key, check)
    return hmac.compare_digest(password, stored_hash)

def create_session(user_id: int, ip_address: str = "127.0.0.1") -> str:
    token = secrets.token_urlsafe(32)
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO user_sessions (user_id, token, ip_address, expires_at)
        VALUES (?, ?, ?, datetime('now', '+30 days'))
    """, (user_id, token, ip_address))
    conn.commit()
    conn.close()
    bump_data_revision()
    return token

def get_current_user_from_token(token: str) -> Optional[dict]:
    if not token:
        return None
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT u.id, u.username, u.full_name, u.role, u.school_lyceum, u.grade, u.avatar, u.xp, u.grade_score, u.streak, u.is_pro, u.pro_expires_at
        FROM user_sessions s
        JOIN users u ON s.user_id = u.id
        WHERE s.token = ? AND s.expires_at > datetime('now')
    """, (token,))
    row = cursor.fetchone()
    if not row:
        conn.close()
        return None

    user_dict = dict(row)
    if user_dict.get("role") == "student" and user_dict.get("is_pro") and user_dict.get("pro_expires_at"):
        try:
            exp_str = user_dict["pro_expires_at"][:19]
            exp_dt = datetime.strptime(exp_str, "%Y-%m-%d %H:%M:%S")
            if exp_dt < datetime.now():
                cursor.execute("UPDATE users SET is_pro = 0 WHERE id = ?", (user_dict["id"],))
                cursor.execute("UPDATE subscriptions SET status = 'expired' WHERE user_id = ? AND status = 'active'", (user_dict["id"],))
                conn.commit()
                user_dict["is_pro"] = 0
        except Exception:
            pass
    conn.close()
    return user_dict

LOGIN_FAILURES: Dict[str, List[float]] = {}

def check_rate_limit(key: str, max_attempts: int = 5, window_sec: int = 300) -> bool:
    now = time.time()
    attempts = [t for t in LOGIN_FAILURES.get(key, []) if now - t < window_sec]
    LOGIN_FAILURES[key] = attempts
    if len(attempts) >= max_attempts:
        return False
    return True

def record_login_failure(key: str):
    now = time.time()
    if key not in LOGIN_FAILURES:
        LOGIN_FAILURES[key] = []
    LOGIN_FAILURES[key].append(now)

def clear_login_failure(key: str):
    LOGIN_FAILURES.pop(key, None)

def log_security_event(event_type: str, ip: str, details: str):
    try:
        conn = get_db()
        c = conn.cursor()
        c.execute("INSERT INTO security_logs (event_type, ip_address, details) VALUES (?, ?, ?)", (event_type, ip, details))
        conn.commit()
        conn.close()
    except Exception:
        pass

def generate_auto_login_sync() -> str:
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

# ----------------- IN-MEMORY BATTLE ROOM MANAGER -----------------
class BattleRoom:
    def __init__(self, room_code: str, mode: str, host_id: int, host_name: str, subject_id: int, max_players: int = 2, question_count: int = 5):
        self.room_code = room_code
        self.mode = mode  # '1v1' or 'pro_3_5'
        self.host_id = host_id
        self.host_name = host_name
        self.subject_id = subject_id
        self.max_players = max_players  # 2 for free, 3 to 5 for pro
        self.question_count = question_count if question_count in (5, 15, 30) else 5
        self.players: Dict[str, dict] = {} # websocket_id -> player info
        self.sockets: Dict[str, WebSocket] = {}
        self.status = "waiting" # 'waiting', 'playing', 'finished'
        self.questions: List[dict] = []
        self.current_q_index = 0
        self.q_start_time = 0
        self.time_limit = 15 # seconds per question
        self.answers_this_round: Dict[str, dict] = {}

    def can_join(self) -> bool:
        return len(self.players) < self.max_players and self.status == "waiting"

class BattleManager:
    def __init__(self):
        self.rooms: Dict[str, BattleRoom] = {}

    def create_room(self, room_code: str, mode: str, host_id: int, host_name: str, subject_id: int, max_players: int, question_count: int = 5) -> BattleRoom:
        room = BattleRoom(room_code, mode, host_id, host_name, subject_id, max_players, question_count)
        self.rooms[room_code] = room
        return room

    def get_room(self, room_code: str) -> Optional[BattleRoom]:
        return self.rooms.get(room_code)

    def remove_room(self, room_code: str):
        if room_code in self.rooms:
            del self.rooms[room_code]

battle_manager = BattleManager()


# ----------------- REAL-TIME SYNC & GLOBAL REVISION -----------------
DATA_REVISION = 1

def bump_data_revision():
    global DATA_REVISION
    DATA_REVISION += 1

@app.get("/api/sync/state")
def get_sync_state():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM subjects")
    sub_cnt = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM textbooks")
    book_cnt = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM teacher_quizzes")
    quiz_cnt = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM group_members")
    member_cnt = cursor.fetchone()[0]
    conn.close()
    return {
        "revision": DATA_REVISION,
        "subjects_count": sub_cnt,
        "textbooks_count": book_cnt,
        "quizzes_count": quiz_cnt,
        "members_count": member_cnt
    }

# ----------------- REST API ROUTES -----------------

@app.get("/api/subjects")
def get_subjects():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM subjects ORDER BY id ASC")
    rows = [dict(r) for r in cursor.fetchall()]
    conn.close()
    return rows


@app.post("/api/admin/add-subject")
def admin_add_subject(payload: dict = Body(...)):
    name = (payload.get("name") or "").strip()
    icon = (payload.get("icon") or "📘").strip()
    category = (payload.get("category") or "aniq").strip()
    description = (payload.get("description") or f"{name} fani").strip()
    color = payload.get("color") or "var(--accent-red)"

    if not name:
        raise HTTPException(status_code=400, detail="Fan nomi talab qilinadi")

    # Generate unique code
    clean_code = re.sub(r'[^a-zA-Z0-9]', '', name.lower())
    if not clean_code:
        clean_code = f"sub_{random.randint(100, 9999)}"

    conn = get_db()
    cursor = conn.cursor()

    # Check if subject with this name or code exists
    cursor.execute("SELECT id FROM subjects WHERE UPPER(name) = ? OR code = ?", (name.upper(), clean_code))
    existing = cursor.fetchone()
    if existing:
        conn.close()
        raise HTTPException(status_code=400, detail=f"'{name}' fani allaqachon mavjud!")

    cursor.execute("""
        INSERT INTO subjects (name, code, icon, color, description, category)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (name, clean_code, icon, color, description, category))
    new_id = cursor.lastrowid
    conn.commit()
    conn.close()
    bump_data_revision()

    bump_data_revision()

    return {
        "success": True,
        "id": new_id,
        "name": name,
        "code": clean_code,
        "icon": icon,
        "color": color,
        "description": description,
        "category": category,
        "message": f"'{name}' fani barcha o'quvchilar va ustozlar uchun muvaffaqiyatli qo'shildi!"
    }

@app.get("/api/auth/generate-login")
def get_auto_login():
    return {"login": generate_auto_login_sync()}

@app.post("/api/auth/telegram-otp/request")
def request_telegram_otp(payload: dict = Body(...), request: Request = None):
    client_ip = request.client.host if request and request.client else "127.0.0.1"
    
    # Honeypot check
    if payload.get("website_url"):
        log_security_event("HONEYPOT_TRIGGERED", client_ip, "Bot caught in OTP request")
        return {"success": False, "message": "Xatolik"}

    # Rate limiting: max 5 requests per 180s
    if not check_rate_limit(f"otp:{client_ip}", max_attempts=5, window_sec=180):
        log_security_event("RATE_LIMIT_EXCEEDED", client_ip, "Too many OTP requests")
        raise HTTPException(status_code=429, detail="⚠️ Kiber-nazorat: Juda ko'p so'rov yuborildi! Iltimos 3 daqiqadan so'ng qayta urinib ko'ring.")

    telegram_raw = (payload.get("telegram") or "").strip()
    login_cand = (payload.get("login") or "").strip()
    purpose = payload.get("purpose", "register")
    if purpose not in ("register", "reset"):
        purpose = "register"

    clean_tg_user = telegram_raw.lstrip("@").strip().lower()
    
    conn = get_db()
    cursor = conn.cursor()

    target_tg_id = None
    target_user_id = None
    user_name = None

    # Check if this telegram or login matches existing registered user
    if clean_tg_user:
        cursor.execute("SELECT id, telegram_id, full_name, username, pin_code FROM users WHERE (LOWER(telegram_username) = ? OR LOWER(username) = ?) AND pin_code IS NOT NULL", (clean_tg_user, clean_tg_user))
        matched = cursor.fetchone()
        if matched:
            target_user_id = matched["id"]
            target_tg_id = matched["telegram_id"]
            user_name = matched["full_name"]

    if not target_user_id and login_cand:
        cursor.execute("SELECT id, telegram_id, full_name, username, pin_code FROM users WHERE LOWER(username) = ? AND pin_code IS NOT NULL", (login_cand.lower(),))
        matched2 = cursor.fetchone()
        if matched2:
            target_user_id = matched2["id"]
            target_tg_id = matched2["telegram_id"]
            user_name = matched2["full_name"]

    # Ro'yxatdan o'tmagan odam uchun parolni tiklash taqiqlanadi!
    if purpose == "reset":
        if not target_user_id:
            conn.close()
            raise HTTPException(
                status_code=404,
                detail="❌ Ushbu login yoki Telegram orqali ro'yxatdan o'tgan foydalanuvchi topilmadi! Parolni tiklash faqat oldin ro'yxatdan o'tgan foydalanuvchilar uchun mumkin. Iltimos, avval ro'yxatdan o'ting."
            )

    # Generate cryptographically secure 6-digit code
    code = f"{secrets.randbelow(900000) + 100000}"
    
    # Save verification record (expires in 10 minutes)
    cursor.execute("""
        INSERT INTO telegram_verifications (code, telegram_id, telegram_username, purpose, user_id, expires_at)
        VALUES (?, ?, ?, ?, ?, datetime('now', '+10 minutes'))
    """, (code, target_tg_id, clean_tg_user or None, purpose, target_user_id))
    conn.commit()
    conn.close()

    sent_direct = False
    if target_tg_id:
        try:
            from telegram_bot import send_message
            if purpose == "reset":
                msg = (
                    f"🔐 <b>EduBattle Parolni Tiklash:</b>\n\n"
                    f"Sizning bir martalik tiklash kodingiz:\n\n"
                    f"👉 <code>{code}</code> 👈\n\n"
                    f"⏳ Ushbu kod <b>10 daqiqa</b> amal qiladi. Agar buni siz so'ramagan bo'lsangiz, xabarga e'tibor bermang."
                )
            else:
                msg = (
                    f"🔑 <b>EduBattle Ro'yxatdan o'tish kodi:</b>\n\n"
                    f"Sizning tasdiqlash kodingiz:\n\n"
                    f"👉 <code>{code}</code> 👈\n\n"
                    f"⏳ Ushbu kod <b>10 daqiqa</b> amal qiladi."
                )
            res = send_message(target_tg_id, msg)
            if res and res.get("ok"):
                sent_direct = True
        except Exception as e:
            pass

    return {
        "success": True,
        "sent_direct": sent_direct,
        "bot_url": f"https://t.me/edubattleuz_bot?start={purpose}_{code}",
        "bot_username": "edubattleuz_bot",
        "message": (
            "✅ 6-xonali tasdiqlash kodi Telegram akkauntingizga yuborildi!" 
            if sent_direct else 
            "Telegram botimizga kiring (@edubattleuz_bot) va '🔑 Tasdiqlash kodi' tugmasini bosing yoki /code deb yozing!"
        )
    }

@app.post("/api/auth/register")
def register_user(payload: dict = Body(...), request: Request = None):
    client_ip = request.client.host if request and request.client else "127.0.0.1"
    
    # Honeypot anti-bot check
    if payload.get("website_url"):
        log_security_event("HONEYPOT_TRIGGERED", client_ip, "Bot caught in register")
        return {"success": False, "detail": "Xatolik"}

    username = (payload.get("username") or "").strip().lower()
    full_name = (payload.get("full_name") or "").strip()
    role = "student" # Teacher registration is disabled until further notice
    password = (payload.get("password") or "").strip()
    school_lyceum = (payload.get("school_lyceum") or "Maktab / Litsey").strip()
    grade = (payload.get("grade") or "9-sinf").strip()
    verification_code = (payload.get("verification_code") or "").strip()
    telegram_raw = (payload.get("telegram") or "").strip().lstrip("@")

    if not full_name:
        raise HTTPException(status_code=400, detail="F.I.Sh (Ism va Familiya) talab qilinadi")
    if len(password) < 4:
        raise HTTPException(status_code=400, detail="Parol kamida 4 ta belgidan iborat bo'lishi kerak")

    # If username is empty, auto-generate unique login
    if not username:
        username = generate_auto_login_sync().lower()

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM users WHERE LOWER(username) = ?", (username,))
    if cursor.fetchone():
        # Auto-resolve collision if auto-generated
        username = generate_auto_login_sync().lower()

    # Check Telegram OTP verification if provided
    matched_tg_id = None
    matched_tg_user = telegram_raw or None
    if verification_code:
        cursor.execute("""
            SELECT id, telegram_id, telegram_username 
            FROM telegram_verifications 
            WHERE code = ? AND purpose = 'register' AND is_used = 0 AND expires_at > datetime('now')
            ORDER BY id DESC LIMIT 1
        """, (verification_code,))
        v_row = cursor.fetchone()
        if v_row:
            cursor.execute("UPDATE telegram_verifications SET is_used = 1 WHERE id = ?", (v_row["id"],))
            if v_row["telegram_id"]:
                matched_tg_id = v_row["telegram_id"]
            if v_row["telegram_username"]:
                matched_tg_user = v_row["telegram_username"]

    avatar = "teacher_1.png" if role == "teacher" else "avatar_1.png"
    is_pro = 1 if role == "teacher" else 0
    hashed_pwd = hash_password(password)

    cursor.execute("""
        INSERT INTO users (username, full_name, role, school_lyceum, grade, avatar, pin_code, xp, grade_score, streak, is_pro, telegram_id, telegram_username)
        VALUES (?, ?, ?, ?, ?, ?, ?, 0, 0, 0, ?, ?, ?)
    """, (username, full_name, role, school_lyceum, grade, avatar, hashed_pwd, is_pro, matched_tg_id, matched_tg_user))
    user_id = cursor.lastrowid
    conn.commit()

    cursor.execute("SELECT id, username, full_name, role, school_lyceum, grade, avatar, xp, coins, grade_score, streak, is_pro, telegram_id, telegram_username FROM users WHERE id = ?", (user_id,))
    user = dict(cursor.fetchone())
    conn.close()

    log_security_event("REGISTER_SUCCESS", client_ip, f"User {username} registered successfully")
    token = create_session(user_id, client_ip)
    return {"success": True, "user": user, "token": token, "auto_login": username}

@app.post("/api/auth/reset-password")
def reset_password(payload: dict = Body(...), request: Request = None):
    client_ip = request.client.host if request and request.client else "127.0.0.1"

    # Honeypot check
    if payload.get("website_url"):
        log_security_event("HONEYPOT_TRIGGERED", client_ip, "Bot caught in reset-password")
        return {"success": False, "detail": "Xatolik"}

    # Rate limiting: max 5 attempts per 300s
    if not check_rate_limit(f"reset:{client_ip}", max_attempts=5, window_sec=300):
        log_security_event("RATE_LIMIT_EXCEEDED", client_ip, "Too many password reset attempts")
        raise HTTPException(status_code=429, detail="⚠️ Kiber-nazorat: Juda ko'p urinish! 5 daqiqadan so'ng qayta urinib ko'ring.")

    login_cand = (payload.get("login") or "").strip().lower()
    code = (payload.get("code") or "").strip()
    new_password = (payload.get("new_password") or "").strip()

    if not login_cand or not code or not new_password:
        raise HTTPException(status_code=400, detail="Login, tasdiqlash kodi va yangi parol kiritilishi shart!")

    if len(new_password) < 4:
        raise HTTPException(status_code=400, detail="Yangi parol kamida 4 ta belgidan iborat bo'lishi kerak")

    conn = get_db()
    cursor = conn.cursor()

    # Verify code in telegram_verifications
    cursor.execute("""
        SELECT id, telegram_id, user_id, telegram_username
        FROM telegram_verifications
        WHERE code = ? AND purpose = 'reset' AND is_used = 0 AND expires_at > datetime('now')
        ORDER BY id DESC LIMIT 1
    """, (code,))
    v_row = cursor.fetchone()

    if not v_row:
        conn.close()
        record_login_failure(f"reset:{client_ip}")
        raise HTTPException(status_code=400, detail="❌ Tasdiqlash kodi noto'g'ri yoki eskirgan (10 daqiqa)!")

    # Find target user by login or by telegram_id / user_id
    cursor.execute("""
        SELECT id, username, pin_code FROM users 
        WHERE (LOWER(username) = ? OR id = ? OR (telegram_id IS NOT NULL AND telegram_id = ?)) AND pin_code IS NOT NULL
    """, (login_cand, v_row["user_id"] or 0, v_row["telegram_id"] or 0))
    user_row = cursor.fetchone()

    if not user_row:
        conn.close()
        raise HTTPException(status_code=404, detail="❌ Bunday ro'yxatdan o'tgan foydalanuvchi hisobi topilmadi! Iltimos, avval ro'yxatdan o'ting.")

    user_id = user_row["id"]
    new_hash = hash_password(new_password)

    cursor.execute("UPDATE users SET pin_code = ? WHERE id = ?", (new_hash, user_id))
    cursor.execute("UPDATE telegram_verifications SET is_used = 1 WHERE id = ?", (v_row["id"],))
    conn.commit()
    conn.close()

    clear_login_failure(f"reset:{client_ip}")
    log_security_event("PASSWORD_RESET_SUCCESS", client_ip, f"User {user_row['username']} reset password")

    return {"success": True, "message": "Parolingiz muvaffaqiyatli yangilandi! Endi yangi parolingiz bilan tizimga kirishingiz mumkin."}


@app.post("/api/auth/telegram-webapp-login")
def telegram_webapp_login(payload: dict = Body(...), request: Request = None):
    client_ip = request.client.host if request and request.client else "127.0.0.1"
    tg_id = payload.get("id")
    if not tg_id:
        raise HTTPException(status_code=400, detail="Telegram ID yetishmayapti")

    first_name = (payload.get("first_name") or "").strip()
    last_name = (payload.get("last_name") or "").strip()
    full_name = f"{first_name} {last_name}".strip() or "Telegram Foydalanuvchi"
    tg_username = (payload.get("username") or "").strip()
    requested_role = "student" # Teacher role completely disabled

    conn = get_db()
    c = conn.cursor()
    c.execute("SELECT id, username, full_name, role, school_lyceum, grade, avatar, xp, coins, grade_score, streak, is_pro, telegram_id FROM users WHERE telegram_id = ?", (tg_id,))
    row = c.fetchone()

    if not row and tg_username:
        c.execute("SELECT id, username, full_name, role, school_lyceum, grade, avatar, xp, coins, grade_score, streak, is_pro, telegram_id FROM users WHERE LOWER(telegram_username) = ? OR LOWER(username) = ?", (tg_username.lower().lstrip('@'), tg_username.lower().lstrip('@')))
        row = c.fetchone()
        if row:
            c.execute("UPDATE users SET telegram_id = ?, telegram_username = ? WHERE id = ?", (tg_id, tg_username, row["id"]))
            conn.commit()

    if row:
        user_data = dict(row)
        # Ensure user has official EB- ID format (except admin)
        if not (user_data.get("username") and user_data["username"].startswith("EB-")) and user_data["role"] != "admin":
            new_eb = f"EB-{secrets.randbelow(90000) + 10000}"
            c.execute("UPDATE users SET username = ? WHERE id = ?", (new_eb, user_data["id"]))
            conn.commit()
            user_data["username"] = new_eb

        # Ensure teacher role is disabled - convert back to student
        if user_data["role"] == "teacher":
            c.execute("UPDATE users SET role = 'student', is_pro = 0 WHERE id = ?", (user_data["id"],))
            conn.commit()
            user_data["role"] = "student"
            user_data["is_pro"] = 0

        token = create_session(user_data["id"], client_ip)
        conn.close()
        return {"success": True, "user": user_data, "token": token}

    # Auto-register new user from Telegram with official EB-XXXXX ID
    new_username = f"EB-{secrets.randbelow(90000) + 10000}"
    while True:
        c.execute("SELECT id FROM users WHERE UPPER(username) = ?", (new_username,))
        if not c.fetchone():
            break
        new_username = f"EB-{secrets.randbelow(90000) + 10000}"

    c.execute("""
        INSERT INTO users (username, full_name, role, school_lyceum, grade, avatar, xp, coins, streak, is_pro, pin_code, created_at, grade_score, telegram_id, telegram_username)
        VALUES (?, ?, ?, 'EduBattle Online', '9-sinf', 'avatar1.png', 0, 0, 1, ?, ?, datetime('now'), 0, ?, ?)
    """, (new_username, full_name, requested_role, 1 if requested_role == 'teacher' else 0, hash_password("tg_pass_12345"), tg_id, tg_username))
    conn.commit()
    new_id = c.lastrowid
    c.execute("SELECT id, username, full_name, role, school_lyceum, grade, avatar, xp, coins, grade_score, streak, is_pro, telegram_id FROM users WHERE id = ?", (new_id,))
    new_row = c.fetchone()
    conn.close()

    user_data = dict(new_row)
    token = create_session(new_id, client_ip)
    return {"success": True, "user": user_data, "token": token}

    # Auto-register new student user from Telegram
    new_username = f"tg_{tg_id}" if not tg_username else tg_username.lower()
    c.execute("SELECT id FROM users WHERE LOWER(username) = ?", (new_username,))
    if c.fetchone():
        new_username = f"EB-{secrets.randbelow(90000) + 10000}"

    c.execute("""
        INSERT INTO users (username, full_name, role, school_lyceum, grade, avatar, xp, coins, streak, is_pro, pin_code, created_at, grade_score, telegram_id, telegram_username)
        VALUES (?, ?, 'student', 'EduBattle Online', '9-sinf', 'avatar1.png', 0, 0, 1, 0, ?, datetime('now'), 0, ?, ?)
    """, (new_username, full_name, hash_password("tg_pass_12345"), tg_id, tg_username))
    conn.commit()
    new_id = c.lastrowid
    c.execute("SELECT id, username, full_name, role, school_lyceum, grade, avatar, xp, coins, grade_score, streak, is_pro, telegram_id FROM users WHERE id = ?", (new_id,))
    new_row = c.fetchone()
    conn.close()

    user_data = dict(new_row)
    token = create_session(new_id, client_ip)
    return {"success": True, "user": user_data, "token": token}

@app.post("/api/auth/login")
def login_user(payload: dict = Body(...), request: Request = None):
    client_ip = request.client.host if request and request.client else "127.0.0.1"
    username = (payload.get("username") or "").strip().lower()
    password = (payload.get("password") or "").strip()
    
    rate_key = f"{client_ip}:{username}"
    if not check_rate_limit(rate_key, max_attempts=5, window_sec=300):
        raise HTTPException(
            status_code=429, 
            detail="⚠️ Kiber-xavfsizlik nazorati: Juda ko'p muvaffaqiyatsiz urinish! 5 daqiqadan so'ng qayta urinib ko'ring."
        )

    if not username or not password:
        raise HTTPException(status_code=400, detail="Login va parol kiritilishi shart!")

    conn = get_db()
    cursor = conn.cursor()
    
    # Super Admin secure check with constant-time comparison
    if username in ("admin", "superadmin") and (hmac.compare_digest(password, "asoee321") or hmac.compare_digest(password, "admin2026")):
        cursor.execute("SELECT id, username, full_name, role, school_lyceum, grade, avatar, xp, grade_score, streak, is_pro FROM users WHERE role = 'admin'")
        admin_row = cursor.fetchone()
        conn.close()
        if admin_row:
            admin_data = dict(admin_row)
            clear_login_failure(rate_key)
            token = create_session(admin_data["id"], client_ip)
            return {"success": True, "user": admin_data, "token": token}

    eb_variant = f"eb-{username}" if (not username.startswith("eb-") and username.isdigit()) else username
    cursor.execute("""
        SELECT id, username, full_name, role, school_lyceum, grade, avatar, xp, grade_score, streak, is_pro, pin_code 
        FROM users 
        WHERE LOWER(username) = ? OR LOWER(username) = ? OR LOWER(telegram_username) = ?
    """, (username, eb_variant, username.lstrip('@')))
    row = cursor.fetchone()
    
    if not row:
        conn.close()
        record_login_failure(rate_key)
        raise HTTPException(status_code=404, detail="Bunday foydalanuvchi topilmadi! Iltimos, ro'yxatdan o'ting.")
    
    user_dict = dict(row)
    stored_pin = user_dict.get("pin_code") or ""
    
    if not verify_password(password, stored_pin):
        conn.close()
        record_login_failure(rate_key)
        raise HTTPException(status_code=400, detail="Parol noto'g'ri!")
        
    # Auto-upgrade plain passwords to secure PBKDF2
    if "$" not in stored_pin:
        new_hash = hash_password(password)
        cursor.execute("UPDATE users SET pin_code = ? WHERE id = ?", (new_hash, user_dict["id"]))
        conn.commit()

    conn.close()
    clear_login_failure(rate_key)

    token = create_session(user_dict["id"], client_ip)
    del user_dict["pin_code"]
    return {"success": True, "user": user_dict, "token": token}

@app.get("/api/auth/me")
def get_auth_me(token: str = Query("", alias="token")):
    user = get_current_user_from_token(token)
    if not user:
        raise HTTPException(status_code=401, detail="Sessiya eskirgan yoki yaroqsiz")
    return {"success": True, "user": user}

@app.post("/api/user/language")
def update_user_language(payload: dict = Body(...), token: str = Query("", alias="token")):
    lang = (payload.get("lang") or "uz").strip().lower()
    if lang not in ("uz", "ru", "en"):
        lang = "uz"
    user = get_current_user_from_token(token)
    if user:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET lang = ? WHERE id = ?", (lang, user["id"]))
        conn.commit()
        conn.close()
    return {"success": True, "lang": lang}

@app.get("/api/textbooks")
def get_textbooks(subject_id: Optional[int] = None, grade: Optional[str] = None):
    conn = get_db()
    cursor = conn.cursor()
    query = """
        SELECT t.*, s.name as subject_name, s.icon as subject_icon, s.color as subject_color 
        FROM textbooks t 
        JOIN subjects s ON t.subject_id = s.id 
        WHERE 1=1
    """
    params = []
    if subject_id:
        query += " AND t.subject_id = ?"
        params.append(subject_id)
    if grade:
        query += " AND (t.grade LIKE ? OR t.grade LIKE '%litsey%')"
        params.append(f"%{grade}%")
    query += " ORDER BY t.id ASC"

    cursor.execute(query, tuple(params))
    rows = []
    for r in cursor.fetchall():
        item = dict(r)
        if item.get("chapters"):
            try:
                item["chapters"] = json.loads(item["chapters"])
            except:
                item["chapters"] = []
        rows.append(item)
    conn.close()
    return rows


@app.get("/api/textbooks/{book_id}")
def get_textbook_detail(book_id: int):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT t.*, s.name as subject_name, s.icon as subject_icon, s.color as subject_color 
        FROM textbooks t 
        JOIN subjects s ON t.subject_id = s.id 
        WHERE t.id = ?
    """, (book_id,))
    row = cursor.fetchone()
    conn.close()
    if not row:
        raise HTTPException(status_code=404, detail="Darslik topilmadi")
    item = dict(row)
    if item.get("chapters"):
        try:
            item["chapters"] = json.loads(item["chapters"])
        except:
            item["chapters"] = []
    return item

@app.get("/api/questions")
def get_questions(subject_id: Optional[int] = None, grade: Optional[str] = None, count: int = 10, difficulty: Optional[str] = None):
    conn = get_db()
    cursor = conn.cursor()
    query = "SELECT * FROM questions WHERE 1=1"
    params = []
    if subject_id:
        query += " AND subject_id = ?"
        params.append(subject_id)
    if grade:
        cursor.execute("SELECT COUNT(*) FROM questions WHERE subject_id = ? AND (grade = ? OR grade LIKE ?)", (subject_id or 0, grade, f"%{grade}%"))
        has_grade_q = cursor.fetchone()[0] > 0
        if has_grade_q:
            query += " AND (grade = ? OR grade LIKE ?)"
            params.append(grade)
            params.append(f"%{grade}%")
    if difficulty:
        query += " AND difficulty = ?"
        params.append(difficulty)
    query += " ORDER BY RANDOM() LIMIT ?"
    params.append(count)

    cursor.execute(query, tuple(params))
    rows = []
    for r in cursor.fetchall():
        item = dict(r)
        if item.get("options"):
            try:
                item["options"] = json.loads(item["options"])
            except:
                item["options"] = []
        rows.append(item)
    conn.close()
    return rows

# ----------------- SUBJECT QUIZZES (MAVZULAR VA TESTLAR) -----------------
@app.get("/api/subject-quizzes/{subject_id}")
def get_subject_quizzes(subject_id: int):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, subject_id, title, grade, description, time_limit_sec, questions_json, created_at 
        FROM subject_quizzes 
        WHERE subject_id = ? 
        ORDER BY id DESC
    """, (subject_id,))
    quizzes = []
    for r in cursor.fetchall():
        item = dict(r)
        try:
            qs = json.loads(item["questions_json"])
            item["question_count"] = len(qs)
        except:
            item["question_count"] = 0
        del item["questions_json"]
        quizzes.append(item)
    conn.close()
    return quizzes

@app.get("/api/subject-quizzes/quiz/{quiz_id}")
def get_subject_quiz_detail(quiz_id: int):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT sq.*, s.name as subject_name, s.icon as subject_icon, s.color as subject_color
        FROM subject_quizzes sq
        JOIN subjects s ON sq.subject_id = s.id
        WHERE sq.id = ?
    """, (quiz_id,))
    r = cursor.fetchone()
    if not r:
        conn.close()
        raise HTTPException(status_code=404, detail="Test topilmadi")
    quiz = dict(r)
    try:
        quiz["questions"] = json.loads(quiz["questions_json"])
    except:
        quiz["questions"] = []
    del quiz["questions_json"]
    conn.close()
    return quiz

@app.post("/api/subject-quizzes/create")
def create_subject_quiz(payload: dict = Body(...)):
    subject_id = payload.get("subject_id")
    title = (payload.get("title") or "").strip()
    grade = payload.get("grade") or "Barchasi"
    description = (payload.get("description") or "").strip()
    time_limit_sec = int(payload.get("time_limit_sec") or 600)
    questions = payload.get("questions") or []
    author_id = payload.get("author_id")

    if not subject_id or not title:
        raise HTTPException(status_code=400, detail="Fan va test/mavzu nomi kiritilishi shart")
    if not questions or not isinstance(questions, list) or len(questions) == 0:
        raise HTTPException(status_code=400, detail="Kamida bitta test savoli kiritilishi shart")

    cleaned_questions = []
    for q in questions:
        q_text = (q.get("question_text") or q.get("text") or "").strip()
        opts = q.get("options") or []
        correct = int(q.get("correct_index", 0))
        expl = (q.get("explanation") or "").strip()
        if not q_text or len(opts) < 2:
            continue
        cleaned_questions.append({
            "question_text": q_text,
            "options": opts,
            "correct_index": correct,
            "explanation": expl
        })

    if not cleaned_questions:
        raise HTTPException(status_code=400, detail="Yaroqli test savollari topilmadi")

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO subject_quizzes (subject_id, title, grade, description, time_limit_sec, questions_json, author_id)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (subject_id, title, grade, description, time_limit_sec, json.dumps(cleaned_questions, ensure_ascii=False), author_id))
    quiz_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return {"ok": True, "quiz_id": quiz_id, "message": "Test muvaffaqiyatli saqlandi!"}

@app.delete("/api/subject-quizzes/{quiz_id}")
def delete_subject_quiz(quiz_id: int):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM subject_quizzes WHERE id = ?", (quiz_id,))
    conn.commit()
    conn.close()
    return {"ok": True, "message": "Test o'chirildi"}



@app.get("/api/users")
def get_users(role: Optional[str] = None):
    conn = get_db()
    cursor = conn.cursor()
    if role:
        cursor.execute("SELECT id, username, full_name, role, school_lyceum, grade, avatar, xp, coins, grade_score, streak, is_pro FROM users WHERE role = ?", (role,))
    else:
        cursor.execute("SELECT id, username, full_name, role, school_lyceum, grade, avatar, xp, coins, grade_score, streak, is_pro FROM users ORDER BY id ASC")
    rows = [dict(r) for r in cursor.fetchall()]
    conn.close()
    return rows


@app.get("/api/users/{user_id}")
@app.get("/api/user/{user_id}")
def get_user_detail(user_id: int):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, username, full_name, role, school_lyceum, grade, avatar, xp, coins, grade_score, streak, is_pro, pro_expires_at, created_at FROM users WHERE id = ?", (user_id,))
    row = cursor.fetchone()
    if not row:
        conn.close()
        raise HTTPException(status_code=404, detail="Foydalanuvchi topilmadi")
    u = dict(row)
    if u.get("role") == "student" and u.get("is_pro") and u.get("pro_expires_at"):
        try:
            exp_str = u["pro_expires_at"][:19]
            exp_dt = datetime.strptime(exp_str, "%Y-%m-%d %H:%M:%S")
            if exp_dt < datetime.now():
                cursor.execute("UPDATE users SET is_pro = 0 WHERE id = ?", (u["id"],))
                cursor.execute("UPDATE subscriptions SET status = 'expired' WHERE user_id = ? AND status = 'active'", (u["id"],))
                conn.commit()
                u["is_pro"] = 0
        except Exception:
            pass
    conn.close()
    return u

@app.get("/api/leaderboard")
def get_leaderboard(period: str = "weekly", user_id: Optional[int] = None):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS coin_transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            amount INTEGER NOT NULL,
            reason TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()

    if period == "weekly":
        cursor.execute("""
            SELECT u.id, u.username, u.full_name, u.school_lyceum, u.grade, u.avatar, u.xp,
                   COALESCE(SUM(ct.amount), 0) as weekly_coins,
                   u.coins as total_coins,
                   u.grade_score, u.streak, u.is_pro
            FROM users u
            LEFT JOIN coin_transactions ct ON ct.user_id = u.id AND ct.created_at >= datetime('now', '-7 days')
            WHERE u.role = 'student'
            GROUP BY u.id
            ORDER BY weekly_coins DESC, total_coins DESC
            LIMIT 50
        """)
    else:  # all_time
        cursor.execute("""
            SELECT u.id, u.username, u.full_name, u.school_lyceum, u.grade, u.avatar, u.xp,
                   COALESCE((SELECT SUM(amount) FROM coin_transactions WHERE user_id = u.id AND created_at >= datetime('now', '-7 days')), 0) as weekly_coins,
                   u.coins as total_coins,
                   u.grade_score, u.streak, u.is_pro
            FROM users u
            WHERE u.role = 'student'
            ORDER BY u.coins DESC
            LIMIT 50
        """)

    rows = []
    for idx, r in enumerate(cursor.fetchall(), 1):
        d = dict(r)
        d["rank"] = idx
        d["coins"] = d["weekly_coins"] if period == "weekly" else d["total_coins"]
        rows.append(d)

    # Compute current user rank if user_id is provided
    user_rank = None
    if user_id:
        for r in rows:
            if r["id"] == user_id:
                user_rank = {
                    "rank": r["rank"],
                    "coins": r["coins"],
                    "weekly_coins": r["weekly_coins"],
                    "total_coins": r["total_coins"]
                }
                break
        if not user_rank:
            cursor.execute("SELECT id, coins, xp FROM users WHERE id = ?", (user_id,))
            u_self = cursor.fetchone()
            if u_self:
                if period == "weekly":
                    cursor.execute("SELECT COALESCE(SUM(amount), 0) FROM coin_transactions WHERE user_id = ? AND created_at >= datetime('now', '-7 days')", (user_id,))
                    my_wcoins = cursor.fetchone()[0] or 0
                    cursor.execute("""
                        SELECT COUNT(*) + 1 FROM (
                            SELECT u.id, COALESCE(SUM(ct.amount), 0) as w
                            FROM users u
                            LEFT JOIN coin_transactions ct ON ct.user_id = u.id AND ct.created_at >= datetime('now', '-7 days')
                            WHERE u.role = 'student'
                            GROUP BY u.id
                            HAVING w > ?
                        )
                    """, (my_wcoins,))
                    my_rank = cursor.fetchone()[0] or 1
                    user_rank = {"rank": my_rank, "coins": my_wcoins, "weekly_coins": my_wcoins, "total_coins": u_self["coins"]}
                else:
                    cursor.execute("SELECT COUNT(*) + 1 FROM users WHERE role = 'student' AND coins > ?", (u_self["coins"],))
                    my_rank = cursor.fetchone()[0] or 1
                    user_rank = {"rank": my_rank, "coins": u_self["coins"], "weekly_coins": 0, "total_coins": u_self["coins"]}

    conn.close()
    return {
        "period": period,
        "leaderboard": rows,
        "user_rank": user_rank
    }

@app.post("/api/submit-test")
def submit_test(payload: dict = Body(...)):
    user_id = payload.get("user_id", 1)
    quiz_id = payload.get("quiz_id")
    total_questions = payload.get("total_questions", 5)
    correct_count = payload.get("correct_count", 0)
    time_spent_sec = payload.get("time_spent_sec", 0)

    conn = get_db()
    cursor = conn.cursor()

    # Strict role guard: verify user and check PRO status
    cursor.execute("SELECT role, is_pro FROM users WHERE id = ?", (user_id,))
    u_row = cursor.fetchone()
    if not u_row or u_row["role"] != "student":
        conn.close()
        return {
            "success": True,
            "xp_earned": 0,
            "coins_earned": 0,
            "score": round((correct_count / total_questions) * 100) if total_questions > 0 else 100,
            "grade_score": 100,
            "message": "O'qituvchi yoki admin sinovi (o'quvchi sifatida baholanmaydi)"
        }

    is_pro = bool(u_row["is_pro"])

    # Check daily test limit for Free users (Max 2 tests/day)
    cursor.execute("""
        SELECT COUNT(*) FROM quiz_submissions 
        WHERE student_id = ? AND date(submitted_at) = date('now')
    """, (user_id,))
    today_count = cursor.fetchone()[0] or 0
    if not is_pro and today_count >= 2:
        conn.close()
        return {
            "success": False,
            "limit_reached": True,
            "today_count": today_count,
            "max_limit": 2,
            "message": "Bugungi bepul test limitingiz tugadi (2/2)! Cheklovsiz testlar va 2x bonuslar uchun PRO tarifiga o'ting."
        }

    # 100 balli tizimda hisoblash + PRO 2x Multiplier
    score_pct = round((correct_count / total_questions) * 100) if total_questions > 0 else 0
    base_xp = correct_count * 20 + (40 if correct_count == total_questions else 0)
    xp_earned = base_xp * 2 if is_pro else base_xp
    coins_earned = (correct_count * 5 * 2) if is_pro else (correct_count * 2)

    cursor.execute("""
        INSERT INTO quiz_submissions (quiz_id, student_id, score, total_questions, correct_count, time_spent_sec)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (quiz_id, user_id, score_pct, total_questions, correct_count, time_spent_sec))

    # O'quvchining o'rtacha bahosini hisoblash (100 balli tizim)
    cursor.execute("SELECT AVG(score) FROM quiz_submissions WHERE student_id = ?", (user_id,))
    avg_res = cursor.fetchone()[0] or score_pct
    avg_grade = min(100, max(0, round(avg_res)))

    cursor.execute("""
        UPDATE users 
        SET coins = coins + ? 
        WHERE id = ?
    """, (coins_earned, user_id))

    if coins_earned > 0:
        cursor.execute("""
            INSERT INTO coin_transactions (user_id, amount, reason, created_at)
            VALUES (?, ?, 'Mavzulashtirilgan test', datetime('now'))
        """, (user_id, coins_earned))

    conn.commit()
    cursor.execute("SELECT coins FROM users WHERE id = ?", (user_id,))
    u_updated = cursor.fetchone()
    new_coins = u_updated["coins"] if u_updated else 0
    conn.close()
    bump_data_revision()

    return {
        "success": True,
        "xp_earned": 0,
        "coins_earned": coins_earned,
        "new_coins": new_coins,
        "new_xp": 0,
        "score": score_pct,
        "grade_score": 0,
        "is_pro": is_pro,
        "today_count": today_count + 1,
        "remaining_free": max(0, 2 - (today_count + 1)) if not is_pro else 999
    }

# ----------------- TEACHER PORTAL API -----------------

@app.get("/api/teacher/{teacher_id}/groups")
def get_teacher_groups(teacher_id: int):
    conn = get_db()
    cursor = conn.cursor()

    # Strict role guard: verify teacher role
    cursor.execute("SELECT role FROM users WHERE id = ?", (teacher_id,))
    u = cursor.fetchone()
    if not u or u["role"] not in ("teacher", "admin"):
        conn.close()
        raise HTTPException(status_code=403, detail="Faqat o'qituvchilar va administratorlar kirishi mumkin")

    cursor.execute("""
        SELECT g.*, s.name as subject_name, s.icon as subject_icon,
               (SELECT COUNT(*) FROM group_members gm WHERE gm.group_id = g.id) as student_count
        FROM teacher_groups g
        LEFT JOIN subjects s ON g.subject_id = s.id
        WHERE g.teacher_id = ?
        ORDER BY g.id DESC
    """, (teacher_id,))
    groups = [dict(r) for r in cursor.fetchall()]
    conn.close()
    return groups

@app.post("/api/teacher/groups")
def create_teacher_group(payload: dict = Body(...)):
    teacher_id = payload.get("teacher_id")
    group_name = (payload.get("group_name") or "").strip()
    subject_id = payload.get("subject_id", 1)
    description = payload.get("description", "")
    invite_code = (payload.get("invite_code") or f"EDUGROUP{random.randint(100, 999)}").strip().upper()

    if not teacher_id or not group_name:
        raise HTTPException(status_code=400, detail="O'qituvchi ID va Guruh nomi talab qilinadi")

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, role FROM users WHERE id = ?", (teacher_id,))
    user = cursor.fetchone()
    if not user or user["role"] not in ("teacher", "admin"):
        conn.close()
        raise HTTPException(status_code=403, detail="Faqat o'qituvchilar yangi sinf ochishi mumkin!")

    try:
        cursor.execute("""
            INSERT INTO teacher_groups (teacher_id, group_name, subject_id, invite_code, description)
            VALUES (?, ?, ?, ?, ?)
        """, (teacher_id, group_name, subject_id, invite_code, description))
        new_id = cursor.lastrowid
        conn.commit()
    except Exception as e:
        conn.close()
        raise HTTPException(status_code=400, detail=f"Guruh kodi band yoki xatolik: {str(e)}")

    conn.close()
    bump_data_revision()
    return {"success": True, "group_id": new_id, "invite_code": invite_code}

@app.delete("/api/teacher/groups/{group_id}")
def delete_teacher_group(group_id: int, teacher_id: int = Query(...)):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM teacher_groups WHERE id = ? AND teacher_id = ?", (group_id, teacher_id))
    grp = cursor.fetchone()
    if not grp:
        conn.close()
        raise HTTPException(status_code=404, detail="Guruh topilmadi yoki sizga tegishli emas")
    cursor.execute("DELETE FROM group_members WHERE group_id = ?", (group_id,))
    cursor.execute("DELETE FROM teacher_groups WHERE id = ?", (group_id,))
    conn.commit()
    conn.close()
    bump_data_revision()
    return {"success": True, "message": "Sinf muvaffaqiyatli o'chirildi"}

@app.delete("/api/teacher/groups/{group_id}/students/{student_id}")
def remove_student_from_group(group_id: int, student_id: int, teacher_id: int = Query(...)):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM teacher_groups WHERE id = ? AND teacher_id = ?", (group_id, teacher_id))
    grp = cursor.fetchone()
    if not grp:
        conn.close()
        raise HTTPException(status_code=404, detail="Guruh topilmadi yoki sizga tegishli emas")
    cursor.execute("DELETE FROM group_members WHERE group_id = ? AND student_id = ?", (group_id, student_id))
    conn.commit()
    conn.close()
    bump_data_revision()
    return {"success": True, "message": "O'quvchi guruhdan chiqarildi"}

@app.get("/api/teacher/groups/{group_id}/students")
def get_group_students(group_id: int):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT u.id, u.username, u.full_name, u.school_lyceum, u.grade, u.avatar, u.xp, u.grade_score, u.streak, u.is_pro,
               gm.joined_at,
               (SELECT COUNT(*) FROM quiz_submissions qs WHERE qs.student_id = u.id) as tests_completed,
               (SELECT ROUND(AVG(score), 1) FROM quiz_submissions qs WHERE qs.student_id = u.id) as avg_score
        FROM group_members gm
        JOIN users u ON gm.student_id = u.id
        WHERE gm.group_id = ?
        ORDER BY u.grade_score DESC, u.xp DESC
    """, (group_id,))
    students = [dict(r) for r in cursor.fetchall()]
    conn.close()
    return students

@app.get("/api/teacher/{teacher_id}/all-students")
def get_teacher_all_students(teacher_id: int):
    conn = get_db()
    cursor = conn.cursor()

    # Strict role guard: verify teacher role
    cursor.execute("SELECT role FROM users WHERE id = ?", (teacher_id,))
    u = cursor.fetchone()
    if not u or u["role"] not in ("teacher", "admin"):
        conn.close()
        raise HTTPException(status_code=403, detail="Faqat o'qituvchilar va administratorlar kirishi mumkin")

    cursor.execute("""
        SELECT DISTINCT u.id, u.username, u.full_name, u.school_lyceum, u.grade, u.avatar, u.xp, u.grade_score, u.streak, u.is_pro,
               tg.id as group_id, tg.group_name,
               (SELECT COUNT(*) FROM quiz_submissions qs WHERE qs.student_id = u.id) as tests_completed,
               (SELECT ROUND(AVG(score), 1) FROM quiz_submissions qs WHERE qs.student_id = u.id) as avg_score
        FROM teacher_groups tg
        JOIN group_members gm ON tg.id = gm.group_id
        JOIN users u ON gm.student_id = u.id
        WHERE tg.teacher_id = ?
        ORDER BY u.grade_score DESC, u.xp DESC
    """, (teacher_id,))
    students = [dict(r) for r in cursor.fetchall()]
    conn.close()
    return students

# ----------------- STUDENT JOIN TEACHER GROUP API -----------------
@app.post("/api/student/join-group")
def student_join_group(payload: dict = Body(...)):
    student_id = payload.get("student_id")
    invite_code = (payload.get("invite_code") or "").strip().upper()

    if not student_id:
        raise HTTPException(status_code=400, detail="Iltimos, avval akkauntingizga kiring!")
    if not invite_code:
        raise HTTPException(status_code=400, detail="Iltimos, ustozingiz bergan guruh kodi yoki parolini kiriting!")

    conn = get_db()
    cursor = conn.cursor()

    # Verify student exists and strictly enforce student role
    cursor.execute("SELECT id, full_name, role FROM users WHERE id = ?", (student_id,))
    student = cursor.fetchone()
    if not student:
        conn.close()
        raise HTTPException(status_code=404, detail="O'quvchi akkaunti topilmadi!")

    if student["role"] != "student":
        conn.close()
        raise HTTPException(status_code=400, detail="Faqat o'quvchilar sinf guruhiga qo'shila oladi! O'qituvchilar o'quvchi sifatida a'zo bo'la olmaydi.")

    # Find group by invite_code
    cursor.execute("""
        SELECT tg.*, u.full_name as teacher_name, s.name as subject_name
        FROM teacher_groups tg
        JOIN users u ON tg.teacher_id = u.id
        LEFT JOIN subjects s ON tg.subject_id = s.id
        WHERE UPPER(TRIM(tg.invite_code)) = ?
    """, (invite_code,))
    grp = cursor.fetchone()

    # If not found by invite code, also check if it might match group_name case-insensitively
    if not grp:
        cursor.execute("""
            SELECT tg.*, u.full_name as teacher_name, s.name as subject_name
            FROM teacher_groups tg
            JOIN users u ON tg.teacher_id = u.id
            LEFT JOIN subjects s ON tg.subject_id = s.id
            WHERE UPPER(TRIM(tg.group_name)) = ?
        """, (invite_code,))
        grp = cursor.fetchone()

    if not grp:
        # Check if they entered a Quiz PIN by mistake
        cursor.execute("SELECT title FROM teacher_quizzes WHERE UPPER(TRIM(pin_code)) = ?", (invite_code,))
        qz = cursor.fetchone()
        conn.close()
        if qz:
            raise HTTPException(status_code=400, detail=f"Siz kiritgan '{invite_code}' kodi guruh kodi emas, balki '{qz['title']}' testining PIN kodidir! Uni 'Testga Kirish' bo'limida kiriting.")
        raise HTTPException(status_code=404, detail=f"Bunday guruh kodi yoki paroli ('{invite_code}') topilmadi! Iltimos, ustozingiz bergan to'g'ri kodni tekshiring.")

    group_id = grp["id"]

    # Check if student is already in the group
    cursor.execute("SELECT id FROM group_members WHERE group_id = ? AND student_id = ?", (group_id, student_id))
    existing = cursor.fetchone()
    if existing:
        conn.close()
        return {
            "success": True,
            "already_member": True,
            "group_id": group_id,
            "group_name": grp["group_name"],
            "teacher_name": grp["teacher_name"],
            "subject_name": grp["subject_name"],
            "message": f"Siz allaqachon '{grp['group_name']}' sinf guruhiga a'zosiz!"
        }

    # Add to group
    cursor.execute("INSERT INTO group_members (group_id, student_id) VALUES (?, ?)", (group_id, student_id))
    conn.commit()
    conn.close()
    bump_data_revision()
    bump_data_revision()

    return {
        "success": True,
        "group_id": group_id,
        "group_name": grp["group_name"],
        "teacher_name": grp["teacher_name"],
        "subject_name": grp["subject_name"],
        "message": f"Tabriklaymiz! Siz Ustoz {grp['teacher_name']}ning '{grp['group_name']}' sinf guruhiga muvaffaqiyatli a'zo bo'ldingiz!"
    }

@app.get("/api/student/{student_id}/groups")
def get_student_groups(student_id: int):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT tg.id as group_id, tg.group_name, tg.invite_code, tg.description,
               u.full_name as teacher_name, s.name as subject_name, s.icon as subject_icon,
               gm.joined_at,
               (SELECT COUNT(*) FROM group_members WHERE group_id = tg.id) as total_students
        FROM group_members gm
        JOIN teacher_groups tg ON gm.group_id = tg.id
        JOIN users u ON tg.teacher_id = u.id
        LEFT JOIN subjects s ON tg.subject_id = s.id
        WHERE gm.student_id = ?
        ORDER BY gm.id DESC
    """, (student_id,))
    rows = [dict(r) for r in cursor.fetchall()]
    conn.close()
    return rows


# ----------------- STUDENT EVALUATION & GRADING JOURNAL API -----------------

def get_letter_grade(score: int) -> dict:
    if score >= 86:
        return {"grade": 5, "label": "A'lo", "color": "green", "stars": "⭐⭐⭐⭐⭐"}
    elif score >= 71:
        return {"grade": 4, "label": "Yaxshi", "color": "blue", "stars": "⭐⭐⭐⭐"}
    elif score >= 56:
        return {"grade": 3, "label": "Qoniqarli", "color": "amber", "stars": "⭐⭐⭐"}
    elif score > 0:
        return {"grade": 2, "label": "Qoniqarsiz", "color": "red", "stars": "⭐⭐"}
    else:
        return {"grade": 0, "label": "Boshlang'ich (0 ball)", "color": "gray", "stars": "⚪"}

@app.post("/api/teacher/grade-student")
def teacher_grade_student(payload: dict = Body(...)):
    raise HTTPException(
        status_code=400,
        detail="O'quvchilarni baholash faqat tizim orqali avtomatik ravishda ishlagan testlari natijasiga qarab amalga oshiriladi!"
    )

@app.get("/api/student/{student_id}/grades")
def get_student_grades(student_id: int):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT id, full_name, grade_score, xp, school_lyceum, grade FROM users WHERE id = ?", (student_id,))
    student = cursor.fetchone()
    if not student:
        conn.close()
        raise HTTPException(status_code=404, detail="O'quvchi topilmadi")

    cursor.execute("""
        SELECT g.*, u.full_name as teacher_name, s.name as subject_name, s.icon as subject_icon
        FROM student_grades g
        LEFT JOIN users u ON g.teacher_id = u.id
        LEFT JOIN subjects s ON g.subject_id = s.id
        WHERE g.student_id = ?
        ORDER BY g.created_at DESC, g.id DESC
    """, (student_id,))

    grades = []
    breakdown = {"alo": 0, "yaxshi": 0, "qoniqarli": 0, "qoniqarsiz": 0}

    for r in cursor.fetchall():
        item = dict(r)
        item["letter"] = get_letter_grade(item["score"])
        grades.append(item)
        if item["score"] >= 86:
            breakdown["alo"] += 1
        elif item["score"] >= 71:
            breakdown["yaxshi"] += 1
        elif item["score"] >= 56:
            breakdown["qoniqarli"] += 1
        else:
            breakdown["qoniqarsiz"] += 1

    if grades:
        overall_avg = round(sum(g["score"] for g in grades) / len(grades))
    else:
        overall_avg = student["grade_score"] if (student["grade_score"] is not None) else 0
    overall_letter = get_letter_grade(overall_avg)

    conn.close()
    return {
        "student": dict(student),
        "overall_average": overall_avg,
        "overall_letter": overall_letter,
        "total_grades": len(grades),
        "breakdown": breakdown,
        "grades": grades
    }

# ----------------- TEACHER TEXTBOOK & QUESTION UPLOAD API -----------------

@app.post("/api/teacher/textbooks")
def teacher_upload_textbook(payload: dict = Body(...)):
    teacher_id = payload.get("teacher_id")
    subject_id = payload.get("subject_id")
    title = (payload.get("title") or "").strip()
    author = (payload.get("author") or "Ustoz").strip()
    grade = (payload.get("grade") or "9-sinf").strip()
    summary = (payload.get("summary") or "").strip()
    file_url = (payload.get("file_url") or "").strip()
    chapters = payload.get("chapters") or []

    if not teacher_id or not title or not subject_id:
        raise HTTPException(status_code=400, detail="Darslik nomi va fani talab qilinadi")

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT role FROM users WHERE id = ?", (teacher_id,))
    u = cursor.fetchone()
    if not u or u["role"] not in ("teacher", "admin"):
        conn.close()
        raise HTTPException(status_code=403, detail="Faqat o'qituvchilar va administratorlar darslik yuklay oladi")

    cursor.execute("""
        INSERT INTO textbooks (subject_id, title, author, grade, summary, chapters, uploaded_by, file_url)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (subject_id, title, author, grade, summary, json.dumps(chapters, ensure_ascii=False), teacher_id, file_url))
    new_id = cursor.lastrowid
    conn.commit()
    conn.close()
    bump_data_revision()
    bump_data_revision()
    return {"success": True, "id": new_id, "message": "Darslik kutubxonaga muvaffaqiyatli qo'shildi!"}

@app.get("/api/library")
def get_library(subject_id: Optional[int] = None, grade: Optional[str] = None, teacher_id: Optional[int] = None):
    conn = get_db()
    cursor = conn.cursor()
    query = """
        SELECT t.*, s.name as subject_name, s.icon as subject_icon, s.color as subject_color,
               u.full_name as uploader_name, u.role as uploader_role
        FROM textbooks t
        JOIN subjects s ON t.subject_id = s.id
        LEFT JOIN users u ON t.uploaded_by = u.id
        WHERE 1=1
    """
    params = []
    if subject_id:
        query += " AND t.subject_id = ?"
        params.append(subject_id)
    if grade and grade.lower() != 'barchasi':
        query += " AND (t.grade LIKE ? OR t.grade LIKE '%litsey%')"
        params.append(f"%{grade}%")
    if teacher_id:
        query += " AND t.uploaded_by = ?"
        params.append(teacher_id)
        
    query += " ORDER BY t.id DESC"
    cursor.execute(query, tuple(params))
    rows = []
    for r in cursor.fetchall():
        item = dict(r)
        if item.get("chapters"):
            try:
                item["chapters"] = json.loads(item["chapters"])
            except:
                item["chapters"] = []
        rows.append(item)
    conn.close()
    return rows


@app.post("/api/teacher/questions")
def teacher_create_question(payload: dict = Body(...)):
    teacher_id = payload.get("teacher_id")
    subject_id = payload.get("subject_id", 1)
    grade = (payload.get("grade") or "9-sinf").strip()
    chapter_title = (payload.get("chapter_title") or "Umumiy mavzu").strip()
    question_text = (payload.get("question_text") or "").strip()
    options = payload.get("options") or []
    correct_index = int(payload.get("correct_index", 0))
    explanation = (payload.get("explanation") or "").strip()
    group_id = payload.get("group_id")

    if not teacher_id or not question_text or len(options) < 2:
        raise HTTPException(status_code=400, detail="Savol matni va kamida 2 ta javob varianti kiritilishi shart")

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT role FROM users WHERE id = ?", (teacher_id,))
    u = cursor.fetchone()
    if not u or u["role"] not in ("teacher", "admin"):
        conn.close()
        raise HTTPException(status_code=403, detail="Faqat o'qituvchilar test tuza oladi")

    cursor.execute("""
        INSERT INTO questions (subject_id, grade, chapter_title, question_text, options, correct_index, explanation, created_by, group_id)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (subject_id, grade, chapter_title, question_text, json.dumps(options, ensure_ascii=False), correct_index, explanation, teacher_id, group_id))
    new_id = cursor.lastrowid
    conn.commit()
    conn.close()
    bump_data_revision()
    return {"success": True, "id": new_id, "message": "Test savoli muvaffaqiyatli saqlandi!"}

@app.get("/api/teacher/{teacher_id}/questions")
def get_teacher_questions(teacher_id: int):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT role FROM users WHERE id = ?", (teacher_id,))
    u = cursor.fetchone()
    if not u or u["role"] not in ("teacher", "admin"):
        conn.close()
        raise HTTPException(status_code=403, detail="Faqat o'qituvchilar va administratorlar kirishi mumkin")
    cursor.execute("""
        SELECT q.*, s.name as subject_name, s.icon as subject_icon, g.group_name
        FROM questions q
        JOIN subjects s ON q.subject_id = s.id
        LEFT JOIN teacher_groups g ON q.group_id = g.id
        WHERE q.created_by = ?
        ORDER BY q.id DESC
    """, (teacher_id,))
    rows = []
    for r in cursor.fetchall():
        item = dict(r)
        if item.get("options"):
            try:
                item["options"] = json.loads(item["options"])
            except:
                pass
        rows.append(item)
    conn.close()
    return rows


@app.get("/api/student/{student_id}/available-tests")
def get_student_available_tests(student_id: int):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT tg.teacher_id, tg.group_name, tg.id as group_id, u.full_name as teacher_name
        FROM group_members gm
        JOIN teacher_groups tg ON gm.group_id = tg.id
        JOIN users u ON tg.teacher_id = u.id
        WHERE gm.student_id = ?
    """, (student_id,))
    groups = [dict(r) for r in cursor.fetchall()]

    teacher_ids = list(set([g["teacher_id"] for g in groups]))
    questions = []
    if teacher_ids:
        placeholders = ",".join("?" for _ in teacher_ids)
        cursor.execute(f"""
            SELECT q.*, s.name as subject_name, s.icon as subject_icon, u.full_name as teacher_name
            FROM questions q
            JOIN subjects s ON q.subject_id = s.id
            JOIN users u ON q.created_by = u.id
            WHERE q.created_by IN ({placeholders})
            ORDER BY q.id DESC
        """, tuple(teacher_ids))
        for r in cursor.fetchall():
            item = dict(r)
            if item.get("options"):
                try:
                    item["options"] = json.loads(item["options"])
                except:
                    pass
            questions.append(item)
    conn.close()
    return {"groups": groups, "questions": questions}

# ----------------- TEZKOR TEST VA VIKTORINA TIZIMI -----------------

@app.post("/api/teacher/create-quiz")
def create_teacher_quiz(payload: dict = Body(...)):
    teacher_id = payload.get("teacher_id")
    group_id = payload.get("group_id")
    title = (payload.get("title") or "").strip()
    subject_id = payload.get("subject_id", 1)
    grade = (payload.get("grade") or "9-sinf").strip()
    time_limit_sec = int(payload.get("time_limit_sec", 30))
    questions_list = payload.get("questions", [])
    passcode = str(payload.get("passcode") or random.randint(1000, 9999)).strip()
    description = (payload.get("description") or f"{title} mavzusidagi maxsus test").strip()
    pin_code = (payload.get("pin_code") or f"TEST-{random.randint(100, 999)}").strip().upper()

    if not teacher_id or not title:
        raise HTTPException(status_code=400, detail="Test / Mavzu nomi va o'qituvchi ID talab qilinadi")

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, role, full_name FROM users WHERE id = ?", (teacher_id,))
    teacher = cursor.fetchone()
    if not teacher or teacher["role"] not in ("teacher", "admin"):
        conn.close()
        raise HTTPException(status_code=403, detail="Faqat o'qituvchilar test yarata oladi!")

    # Agar savollar berilmagan bo'lsa, mavjud bazadan olinadi
    if not questions_list:
        cursor.execute("""
            SELECT id, question_text, options, correct_index, explanation 
            FROM questions 
            WHERE (created_by = ? OR subject_id = ?) 
            ORDER BY RANDOM() LIMIT 5
        """, (teacher_id, subject_id))
        for r in cursor.fetchall():
            q_dict = dict(r)
            if isinstance(q_dict.get("options"), str):
                try:
                    q_dict["options"] = json.loads(q_dict["options"])
                except:
                    pass
            questions_list.append(q_dict)
    else:
        # Savollarni kelajakda ham foydalanish uchun questions jadvaliga ham saqlab qo'yamiz
        for q in questions_list:
            q_text = (q.get("question_text") or "").strip()
            q_opts = q.get("options") or []
            q_correct = int(q.get("correct_index", 0))
            q_expl = (q.get("explanation") or "").strip()
            if q_text and len(q_opts) >= 2:
                cursor.execute("""
                    INSERT INTO questions (subject_id, grade, chapter_title, question_text, options, correct_index, explanation, created_by, group_id)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (subject_id, grade, title, q_text, json.dumps(q_opts, ensure_ascii=False), q_correct, q_expl, teacher_id, group_id))

    # 100% BEPUL o'qituvchilar uchun test yaratish
    cursor.execute("""
        INSERT INTO teacher_quizzes (teacher_id, group_id, title, subject_id, time_limit_sec, questions, is_pro_only, pin_code, status, passcode, description)
        VALUES (?, ?, ?, ?, ?, ?, 0, ?, 'active', ?, ?)
    """, (teacher_id, group_id, title, subject_id, time_limit_sec, json.dumps(questions_list, ensure_ascii=False), pin_code, passcode, description))
    new_quiz_id = cursor.lastrowid
    conn.commit()
    conn.close()
    bump_data_revision()
    bump_data_revision()

    share_text = f"📚 Test: {title}\n🔑 Test KODI: {pin_code}\n🔒 PAROL: {passcode}\n⏱ Vaqt: har bir savolga {time_limit_sec} soniya\n📝 Jami savollar: {len(questions_list)} ta"

    return {
        "success": True,
        "quiz_id": new_quiz_id,
        "title": title,
        "pin_code": pin_code,
        "passcode": passcode,
        "total_questions": len(questions_list),
        "time_limit_sec": time_limit_sec,
        "share_text": share_text
    }

@app.get("/api/teacher/{teacher_id}/quizzes")
def get_teacher_quizzes(teacher_id: int):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT role FROM users WHERE id = ?", (teacher_id,))
    u = cursor.fetchone()
    if not u or u["role"] not in ("teacher", "admin"):
        conn.close()
        raise HTTPException(status_code=403, detail="Faqat o'qituvchilar va administratorlar kirishi mumkin")
    cursor.execute("""
        SELECT tq.*, tg.group_name, s.name as subject_name
        FROM teacher_quizzes tq
        LEFT JOIN teacher_groups tg ON tq.group_id = tg.id
        LEFT JOIN subjects s ON tq.subject_id = s.id
        WHERE tq.teacher_id = ?
        ORDER BY tq.id DESC
    """, (teacher_id,))
    rows = []
    for r in cursor.fetchall():
        item = dict(r)
        if item.get("questions"):
            try:
                item["questions"] = json.loads(item["questions"])
            except:
                pass
        rows.append(item)
    conn.close()
    return rows


@app.get("/api/quiz/info/{pin_code}")
def get_quiz_info(pin_code: str):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT tq.*, u.full_name as teacher_name, s.name as subject_name
        FROM teacher_quizzes tq
        JOIN users u ON tq.teacher_id = u.id
        JOIN subjects s ON tq.subject_id = s.id
        WHERE UPPER(tq.pin_code) = ?
    """, (pin_code.strip().upper(),))
    row = cursor.fetchone()
    conn.close()
    if not row:
        raise HTTPException(status_code=404, detail="Bunday Test Kodi topilmadi!")
    q = dict(row)
    if q.get("questions"):
        try:
            q["questions"] = json.loads(q["questions"])
        except:
            q["questions"] = []
    return q

@app.post("/api/quiz/verify-access")
def verify_quiz_access(payload: dict = Body(...)):
    pin_code = (payload.get("pin_code") or "").strip().upper()
    passcode = (payload.get("passcode") or "").strip()

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT tq.*, u.full_name as teacher_name, s.name as subject_name
        FROM teacher_quizzes tq
        JOIN users u ON tq.teacher_id = u.id
        JOIN subjects s ON tq.subject_id = s.id
        WHERE UPPER(tq.pin_code) = ?
    """, (pin_code,))
    row = cursor.fetchone()
    if not row:
        cursor.execute("""
            SELECT tg.group_name, u.full_name as teacher_name
            FROM teacher_groups tg
            JOIN users u ON tg.teacher_id = u.id
            WHERE UPPER(TRIM(tg.invite_code)) = ?
        """, (pin_code,))
        grp_match = cursor.fetchone()
        conn.close()
        if grp_match:
            raise HTTPException(
                status_code=400,
                detail=f"Siz kiritgan '{pin_code}' kodi test kodi emas, balki Ustoz {grp_match['teacher_name']}ning '{grp_match['group_name']}' sinf guruhi taklif kodidir! Iltimos, 'Guruhga Qo'shilish' tugmasi orqali a'zo bo'ling."
            )
        raise HTTPException(status_code=404, detail="Bunday Test Kodi topilmadi! Iltimos, kodni tekshiring.")
    conn.close()

    q = dict(row)
    if q.get("passcode") and q["passcode"].strip():
        if passcode.strip() != q["passcode"].strip():
            raise HTTPException(status_code=403, detail="Test paroli noto'g'ri! Iltimos, ustoz bergan to'g'ri parolni kiriting.")

    if q.get("questions"):
        try:
            q["questions"] = json.loads(q["questions"])
        except:
            q["questions"] = []

    return {"success": True, "quiz": q}

@app.post("/api/quiz/submit-result")
def submit_quiz_result(payload: dict = Body(...)):
    student_id = payload.get("student_id")
    quiz_id = payload.get("quiz_id")
    correct_count = int(payload.get("correct_count", 0))
    total_questions = int(payload.get("total_questions", 1))
    time_spent_sec = float(payload.get("time_spent_sec", 0))

    score_pct = round((correct_count / total_questions) * 100) if total_questions > 0 else 0

    conn = get_db()
    cursor = conn.cursor()

    # Quiz metadata
    cursor.execute("SELECT title, subject_id, teacher_id FROM teacher_quizzes WHERE id = ?", (quiz_id,))
    qz_meta = cursor.fetchone()
    qz_title = qz_meta["title"] if qz_meta else "Test"
    qz_sub_id = qz_meta["subject_id"] if qz_meta else 1
    qz_teacher_id = qz_meta["teacher_id"] if qz_meta else None

    # Save to quiz_submissions
    cursor.execute("""
        INSERT INTO quiz_submissions (quiz_id, student_id, score, total_questions, correct_count, time_spent_sec)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (quiz_id, student_id, score_pct, total_questions, correct_count, int(time_spent_sec)))

    # Save to student_grades if student is registered
    if student_id:
        cursor.execute("""
            INSERT INTO student_grades (student_id, teacher_id, subject_id, grade_type, score, comment)
            VALUES (?, ?, ?, 'Test', ?, ?)
        """, (student_id, qz_teacher_id, qz_sub_id, score_pct, f"'{qz_title}' testi: {correct_count}/{total_questions} to'g'ri ({int(time_spent_sec)} soniya)"))

        # Recalculate cumulative average grade score (100-point scale)
        cursor.execute("""
            SELECT ROUND(AVG(val), 1) FROM (
                SELECT score as val FROM student_grades WHERE student_id = ?
                UNION ALL
                SELECT score as val FROM quiz_submissions WHERE student_id = ?
            )
        """, (student_id, student_id))
        avg_row = cursor.fetchone()
        new_avg = round(avg_row[0]) if (avg_row and avg_row[0] is not None) else score_pct

        xp_bonus = 0
        cursor.execute("UPDATE users SET grade_score = 0 WHERE id = ?", (student_id,))
    else:
        new_avg = score_pct

    conn.commit()
    conn.close()
    bump_data_revision()

    letter = get_letter_grade(score_pct)
    return {
        "success": True,
        "score": score_pct,
        "correct_count": correct_count,
        "total_questions": total_questions,
        "time_spent_sec": int(time_spent_sec),
        "new_grade_score": new_avg,
        "letter_grade": letter
    }

@app.get("/api/bot/info")
def get_bot_info():
    return {
        "ok": True,
        "bot_username": "edubattleuz_bot",
        "bot_link": "https://t.me/edubattleuz_bot"
    }

@app.get("/api/quiz/{quiz_id}/leaderboard")
def get_quiz_leaderboard(quiz_id: int):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT qs.*, u.full_name, u.username, u.school_lyceum, u.grade, u.avatar
        FROM quiz_submissions qs
        LEFT JOIN users u ON qs.student_id = u.id
        WHERE qs.quiz_id = ?
        ORDER BY qs.correct_count DESC, qs.time_spent_sec ASC
    """, (quiz_id,))
    subs = [dict(r) for r in cursor.fetchall()]
    conn.close()
    return subs

# ----------------- FRIENDS & SOCIAL CHAT API (Follow / Podpiska & Chat) -----------------

@app.get("/api/friends/search")
def search_users(q: str = Query(""), query: str = Query(""), current_user_id: int = Query(0)):
    term = (q or query).strip()
    if not term:
        return []
    clean_term = term.upper()
    eb_variant = f"EB-{clean_term}" if (not clean_term.startswith("EB-") and clean_term.isdigit()) else clean_term
    like_term = f"%{term.lower()}%"
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT u.id, u.username, u.full_name, u.role, u.school_lyceum, u.grade, u.xp, u.coins, u.is_pro,
               (SELECT status FROM friendships WHERE user_id = ? AND friend_id = u.id) as outgoing_status,
               (SELECT status FROM friendships WHERE user_id = u.id AND friend_id = ?) as incoming_status
        FROM users u
        WHERE u.id != ? AND (
            UPPER(u.username) = ? OR
            UPPER(u.username) = ? OR
            LOWER(u.username) LIKE ? OR
            LOWER(u.full_name) LIKE ? OR
            LOWER(u.telegram_username) LIKE ?
        )
        LIMIT 25
    """, (current_user_id, current_user_id, current_user_id, clean_term, eb_variant, like_term, like_term, like_term))
    raw_results = [dict(r) for r in cursor.fetchall()]
    conn.close()

    results = []
    for r in raw_results:
        out_s = r.get("outgoing_status")
        in_s = r.get("incoming_status")
        if out_s == "accepted" or in_s == "accepted":
            r["friend_status"] = "friends"
        elif out_s == "pending":
            r["friend_status"] = "pending_sent"
        elif in_s == "pending":
            r["friend_status"] = "pending_received"
        else:
            r["friend_status"] = "none"
        results.append(r)
    return results

@app.get("/api/friends/{user_id}")
def get_user_friends(user_id: int):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT DISTINCT u.id, u.username, u.full_name, u.role, u.school_lyceum, u.grade, u.xp, u.coins, u.is_pro,
               f.created_at as followed_at
        FROM friendships f
        JOIN users u ON (f.friend_id = u.id AND f.user_id = ?) OR (f.user_id = u.id AND f.friend_id = ?)
        WHERE f.status = 'accepted' AND u.id != ?
        ORDER BY f.id DESC
    """, (user_id, user_id, user_id))
    friends = [dict(r) for r in cursor.fetchall()]
    conn.close()
    return friends

@app.get("/api/friends/requests/{user_id}")
def get_friend_requests(user_id: int):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT f.id as request_id, f.created_at,
               u.id as requester_id, u.username, u.full_name, u.role, u.school_lyceum, u.grade, u.xp, u.is_pro
        FROM friendships f
        JOIN users u ON f.user_id = u.id
        WHERE f.friend_id = ? AND f.status = 'pending'
        ORDER BY f.id DESC
    """, (user_id,))
    incoming = [dict(r) for r in cursor.fetchall()]

    cursor.execute("""
        SELECT f.id as request_id, f.created_at,
               u.id as target_id, u.username, u.full_name, u.role, u.school_lyceum, u.grade, u.xp, u.is_pro
        FROM friendships f
        JOIN users u ON f.friend_id = u.id
        WHERE f.user_id = ? AND f.status = 'pending'
        ORDER BY f.id DESC
    """, (user_id,))
    outgoing = [dict(r) for r in cursor.fetchall()]
    conn.close()
    return {"incoming": incoming, "outgoing": outgoing}

@app.post("/api/friends/send-request")
def send_friend_request(payload: dict = Body(...)):
    user_id = payload.get("user_id")
    target_id = payload.get("target_id") or payload.get("friend_id")

    if not user_id or not target_id or user_id == target_id:
        raise HTTPException(status_code=400, detail="Noto'g'ri foydalanuvchi ma'lumotlari")

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, user_id, friend_id, status FROM friendships 
        WHERE (user_id = ? AND friend_id = ?) OR (user_id = ? AND friend_id = ?)
    """, (user_id, target_id, target_id, user_id))
    existing = cursor.fetchone()

    if existing:
        e = dict(existing)
        if e["status"] == "accepted":
            conn.close()
            return {"success": True, "status": "friends", "message": "Siz allaqachon do'stsiz!"}
        elif e["user_id"] == user_id and e["status"] == "pending":
            cursor.execute("DELETE FROM friendships WHERE id = ?", (e["id"],))
            conn.commit()
            conn.close()
            bump_data_revision()
            return {"success": True, "status": "none", "message": "Do'stlik so'rovi bekor qilindi"}
        elif e["friend_id"] == user_id and e["status"] == "pending":
            cursor.execute("UPDATE friendships SET status = 'accepted' WHERE id = ?", (e["id"],))
            cursor.execute("INSERT OR REPLACE INTO friendships (user_id, friend_id, status) VALUES (?, ?, 'accepted')", (user_id, target_id))
            conn.commit()
            conn.close()
            bump_data_revision()
            return {"success": True, "status": "friends", "message": "Do'stlik so'rovi qabul qilindi!"}

    cursor.execute("""
        INSERT OR REPLACE INTO friendships (user_id, friend_id, status)
        VALUES (?, ?, 'pending')
    """, (user_id, target_id))
    conn.commit()
    conn.close()
    bump_data_revision()
    return {"success": True, "status": "pending_sent", "message": "Do'stlik so'rovi muvaffaqiyatli yuborildi!"}

@app.post("/api/friends/respond-request")
def respond_friend_request(payload: dict = Body(...)):
    user_id = payload.get("user_id")
    requester_id = payload.get("requester_id")
    action = payload.get("action")

    if not user_id or not requester_id or action not in ("accept", "reject"):
        raise HTTPException(status_code=400, detail="Noto'g'ri parametrlar")

    conn = get_db()
    cursor = conn.cursor()

    if action == "accept":
        cursor.execute("""
            UPDATE friendships SET status = 'accepted' 
            WHERE user_id = ? AND friend_id = ?
        """, (requester_id, user_id))
        cursor.execute("""
            INSERT OR REPLACE INTO friendships (user_id, friend_id, status)
            VALUES (?, ?, 'accepted')
        """, (user_id, requester_id))
        msg = "Do'stlik so'rovi qabul qilindi!"
    else:
        cursor.execute("""
            DELETE FROM friendships 
            WHERE user_id = ? AND friend_id = ?
        """, (requester_id, user_id))
        msg = "Do'stlik so'rovi rad etildi."

    conn.commit()
    conn.close()
    bump_data_revision()
    return {"success": True, "action": action, "message": msg}

@app.post("/api/friends/remove")
def remove_friend(payload: dict = Body(...)):
    user_id = payload.get("user_id")
    friend_id = payload.get("friend_id")

    if not user_id or not friend_id:
        raise HTTPException(status_code=400, detail="Noto'g'ri parametrlar")

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        DELETE FROM friendships 
        WHERE (user_id = ? AND friend_id = ?) OR (user_id = ? AND friend_id = ?)
    """, (user_id, friend_id, friend_id, user_id))
    conn.commit()
    conn.close()
    bump_data_revision()
    return {"success": True, "message": "Do'stlik bekor qilindi"}

@app.post("/api/friends/toggle-follow")
def toggle_follow(payload: dict = Body(...)):
    return send_friend_request(payload)

@app.get("/api/chat/messages")
def get_chat_messages(user_id: int = Query(...), friend_id: int = Query(...)):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, sender_id, receiver_id, message, battle_room_code, created_at
        FROM direct_messages
        WHERE (sender_id = ? AND receiver_id = ?) OR (sender_id = ? AND receiver_id = ?)
        ORDER BY id ASC
        LIMIT 100
    """, (user_id, friend_id, friend_id, user_id))
    msgs = [dict(r) for r in cursor.fetchall()]
    conn.close()
    return msgs

@app.post("/api/chat/send")
def send_chat_message(payload: dict = Body(...)):
    sender_id = payload.get("sender_id")
    receiver_id = payload.get("receiver_id")
    message = (payload.get("message") or "").strip()
    battle_room_code = payload.get("battle_room_code")

    if not sender_id or not receiver_id or (not message and not battle_room_code):
        raise HTTPException(status_code=400, detail="Xabar matni kiritilmadi")

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO direct_messages (sender_id, receiver_id, message, battle_room_code)
        VALUES (?, ?, ?, ?)
    """, (sender_id, receiver_id, message, battle_room_code))
    msg_id = cursor.lastrowid
    conn.commit()
    conn.close()
    bump_data_revision()

    return {"success": True, "id": msg_id, "message": message, "battle_room_code": battle_room_code}

# ----------------- TARIFF & PAYMENT SYSTEM (Click, Payme, Uzum) -----------------

DEFAULT_PRO_PRICE = 29000

def get_pro_price() -> int:
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS app_settings (key TEXT PRIMARY KEY, value TEXT, updated_at TIMESTAMP)")
        cursor.execute("SELECT value FROM app_settings WHERE key = 'pro_price'")
        row = cursor.fetchone()
        conn.close()
        if row and row["value"]:
            return int(row["value"])
    except Exception as e:
        logger.error(f"Error fetching pro_price: {e}")
    return DEFAULT_PRO_PRICE

TARIFF_PLANS = {
    "student_pro": {
        "id": "student_pro",
        "title": "O'quvchi PRO",
        "amount": 29000,
        "currency": "so'm",
        "period": "oylik",
        "features": [
            "3-5 kishilik guruhli do'stlar batli",
            "Barcha sinflar darsliklari va testlariga cheksiz kirish",
            "O'qituvchi guruhlariga kirish va jonli sinf viktorinalarida qatnashish",
            "Shaxsiy reyting tahlili va 100 balli tizimdagi baho",
            "VIP profil va cheksiz jonli bahslar"
        ]
    }
}

@app.get("/api/tariffs")
def get_tariffs():
    price = get_pro_price()
    plan = dict(TARIFF_PLANS["student_pro"])
    plan["amount"] = price
    return [plan]

@app.post("/api/payments/checkout")
def process_payment(payload: dict = Body(...)):
    user_id = payload.get("user_id")
    plan_id = payload.get("plan_id", "student_pro")
    provider = payload.get("provider", "click") # click, payme, uzum
    card_number = (payload.get("card_number") or "").replace(" ", "")

    if not user_id:
        raise HTTPException(status_code=400, detail="Foydalanuvchi aniqlanmadi")

    plan = dict(TARIFF_PLANS.get(plan_id, TARIFF_PLANS["student_pro"]))
    amount = get_pro_price()
    plan["amount"] = amount

    conn = get_db()
    cursor = conn.cursor()

    # Check user existence
    cursor.execute("SELECT id, role, full_name FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()
    if not user:
        conn.close()
        raise HTTPException(status_code=404, detail="Foydalanuvchi topilmadi")

    # Record subscription
    cursor.execute("""
        INSERT INTO subscriptions (user_id, plan_name, amount, provider, status, expires_at)
        VALUES (?, ?, ?, ?, 'active', datetime('now', '+30 days'))
    """, (user_id, plan_id, amount, provider))

    # Activate PRO for user
    cursor.execute("UPDATE users SET is_pro = 1 WHERE id = ?", (user_id,))
    conn.commit()

    cursor.execute("SELECT id, username, full_name, role, school_lyceum, grade, avatar, xp, coins, streak, is_pro FROM users WHERE id = ?", (user_id,))
    updated_user = dict(cursor.fetchone())
    conn.close()

    return {
        "success": True,
        "message": f"To'lov muvaffaqiyatli qabul qilindi! {plan['title']} tarifi 30 kunga faollashtirildi.",
        "provider": provider.upper(),
        "amount": amount,
        "user": updated_user
    }

# ----------------- SUPER ADMIN API -----------------

@app.get("/api/admin/stats")
def get_admin_stats(secret: Optional[str] = Query(None)):
    if secret not in ("asoee321", "admin2026"):
        raise HTTPException(status_code=403, detail="Ruxsat berilmadi. Faqat Super Admin uchun!")
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM users WHERE role = 'student'")
    student_count = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM users WHERE role = 'teacher'")
    teacher_count = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM users WHERE is_pro = 1")
    pro_count = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM questions")
    question_count = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM textbooks")
    book_count = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM quiz_submissions")
    test_sub_count = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM teacher_groups")
    group_count = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*), COALESCE(SUM(amount), 0) FROM subscriptions WHERE status = 'approved'")
    sub_row = cursor.fetchone()
    cursor.execute("SELECT COUNT(*) FROM subscriptions WHERE status = 'pending'")
    pending_count = cursor.fetchone()[0]
    conn.close()

    return {
        "students": student_count,
        "teachers": teacher_count,
        "pro_users": pro_count,
        "pro_price": get_pro_price(),
        "questions": question_count,
        "textbooks": book_count,
        "tests_taken": test_sub_count,
        "groups": group_count,
        "active_subscriptions": sub_row[0],
        "total_revenue": sub_row[1],
        "pending_receipts": pending_count
    }

@app.post("/api/admin/set-price")
def admin_set_price(payload: dict = Body(...)):
    secret = payload.get("secret")
    price = payload.get("price")
    if secret not in ("asoee321", "admin2026"):
        raise HTTPException(status_code=403, detail="Faqat Super Admin uchun!")
    
    try:
        price_int = int(str(price).replace(" ", "").replace(",", ""))
        if price_int <= 0 or price_int > 10000000:
            raise HTTPException(status_code=400, detail="Narx 0 dan katta va 10 000 000 so'mdan oshmasligi kerak")
    except (ValueError, TypeError):
        raise HTTPException(status_code=400, detail="Yaroqsiz summa formati")

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS app_settings (key TEXT PRIMARY KEY, value TEXT, updated_at TIMESTAMP)")
    cursor.execute("""
        INSERT INTO app_settings (key, value, updated_at)
        VALUES ('pro_price', ?, datetime('now'))
        ON CONFLICT(key) DO UPDATE SET value = excluded.value, updated_at = excluded.updated_at
    """, (str(price_int),))
    conn.commit()
    conn.close()
    bump_data_revision()

    formatted_price = f"{price_int:,}".replace(",", " ")
    return {
        "success": True,
        "price": price_int,
        "formatted": f"{formatted_price} so'm",
        "message": f"PRO tarifi narxi muvaffaqiyatli {formatted_price} so'm qilib belgilandi!"
    }

@app.post("/api/admin/toggle-pro")
def toggle_user_pro(payload: dict = Body(...)):
    user_id = payload.get("user_id")
    secret = payload.get("secret")
    if secret not in ("asoee321", "admin2026"):
        raise HTTPException(status_code=403, detail="Faqat Super Admin uchun!")

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT is_pro FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()
    if not user:
        conn.close()
        raise HTTPException(status_code=404, detail="Foydalanuvchi topilmadi")
    new_status = 0 if user["is_pro"] else 1
    cursor.execute("UPDATE users SET is_pro = ? WHERE id = ?", (new_status, user_id))
    conn.commit()
    conn.close()
    bump_data_revision()
    return {"success": True, "is_pro": new_status}

@app.post("/api/admin/upload-pdf")
async def admin_upload_pdf(file: UploadFile = File(...), folder: str = Form("textbooks")):
    ext = os.path.splitext(file.filename)[1].lower()
    if ext not in (".pdf", ".epub", ".djvu", ".doc", ".docx", ".txt"):
        raise HTTPException(status_code=400, detail="Faqat PDF yoki hujjat fayllarini yuklash mumkin")
    
    target_dir = os.path.join(FRONTEND_DIR, "uploads", folder)
    os.makedirs(target_dir, exist_ok=True)
    
    clean_name = re.sub(r'[^a-zA-Z0-9_\.-]', '_', file.filename)
    safe_filename = f"{int(time.time())}_{clean_name}"
    file_path = os.path.join(target_dir, safe_filename)
    
    contents = await file.read()
    with open(file_path, "wb") as f:
        f.write(contents)
        
    file_url = f"/uploads/{folder}/{safe_filename}"
    return {
        "success": True, 
        "file_url": file_url, 
        "filename": safe_filename, 
        "size": len(contents),
        "message": "Fayl muvaffaqiyatli yuklandi!"
    }

@app.post("/api/admin/add-question")
def admin_add_question(payload: dict = Body(...)):
    subject_id = payload.get("subject_id", 1)
    grade = payload.get("grade", "9-sinf")
    chapter_title = payload.get("chapter_title", "Umumiy mavzu")
    question_text = (payload.get("question_text") or "").strip()
    options = payload.get("options", [])
    correct_index = int(payload.get("correct_index", 0))
    explanation = (payload.get("explanation") or "").strip()
    difficulty = payload.get("difficulty", "orta")

    if not question_text or len(options) < 2:
        raise HTTPException(status_code=400, detail="Savol matni va kamida 2 ta variant kerak")

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO questions (subject_id, grade, chapter_title, question_text, options, correct_index, explanation, difficulty)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (subject_id, grade, chapter_title, question_text, json.dumps(options, ensure_ascii=False), correct_index, explanation, difficulty))
    new_id = cursor.lastrowid
    conn.commit()
    conn.close()
    bump_data_revision()
    return {"success": True, "id": new_id, "message": "Yangi test savoli muvaffaqiyatli saqlandi!"}

@app.get("/api/admin/questions-list")
def admin_get_questions_list(secret: Optional[str] = Query(None)):
    if secret not in ("asoee321", "admin2026"):
        raise HTTPException(status_code=403, detail="Faqat Super Admin uchun!")
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT q.*, s.name as subject_name, s.icon as subject_icon
        FROM questions q
        LEFT JOIN subjects s ON q.subject_id = s.id
        ORDER BY q.id DESC
    """)
    rows = []
    for r in cursor.fetchall():
        item = dict(r)
        if item.get("options"):
            try:
                item["options"] = json.loads(item["options"])
            except:
                pass
        rows.append(item)
    conn.close()
    return rows


@app.delete("/api/admin/questions/{q_id}")
def admin_delete_question(q_id: int, secret: Optional[str] = Query(None)):
    if secret and secret not in ("asoee321", "admin2026"):
        raise HTTPException(status_code=403, detail="Faqat Super Admin uchun!")
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM questions WHERE id = ?", (q_id,))
    conn.commit()
    conn.close()
    bump_data_revision()
    return {"success": True, "message": "Savol o'chirildi"}

@app.post("/api/admin/clear-all-questions")
def admin_clear_all_questions(payload: dict = Body(...)):
    secret = payload.get("secret")
    if secret not in ("asoee321", "admin2026"):
        raise HTTPException(status_code=403, detail="Faqat Super Admin uchun!")
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM questions")
    cursor.execute("DELETE FROM teacher_quizzes")
    cursor.execute("DELETE FROM quiz_submissions")
    cursor.execute("DELETE FROM battle_history")
    conn.commit()
    conn.close()
    bump_data_revision()
    return {"success": True, "message": "Barcha testlar va batl natijalari to'liq o'chirildi!"}

@app.post("/api/admin/add-book")
def admin_add_book(payload: dict = Body(...)):
    subject_id = payload.get("subject_id", 1)
    title = (payload.get("title") or "").strip()
    author = (payload.get("author") or "Bosh Administrator").strip()
    grade = (payload.get("grade") or "Barcha sinflar").strip()
    summary = (payload.get("summary") or "").strip()
    content = (payload.get("content") or "").strip()
    file_url = (payload.get("file_url") or "").strip()
    chapters = payload.get("chapters") or []
    if content and not chapters:
        chapters = [{"title": "1-Bob / Asosiy Qoidalar", "summary": content[:80] + "...", "content": content}]

    if not title:
        raise HTTPException(status_code=400, detail="Kitob nomi talab qilinadi")

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO textbooks (subject_id, title, author, grade, cover_image, summary, chapters, uploaded_by, file_url)
        VALUES (?, ?, ?, ?, 'book_generic.png', ?, ?, 3, ?)
    """, (subject_id, title, author, grade, summary, json.dumps(chapters, ensure_ascii=False), file_url))
    new_id = cursor.lastrowid
    conn.commit()
    conn.close()
    bump_data_revision()
    return {
        "success": True, 
        "id": new_id, 
        "file_url": file_url,
        "message": f"'{title}' darsligi barcha foydalanuvchilar kutubxonasiga muvaffaqiyatli qo'shildi!"
    }


# ----------------- REAL-TIME BATTLE WEBSOCKET -----------------

@app.websocket("/ws/battle/{room_code}")
async def battle_websocket(websocket: WebSocket, room_code: str):
    await websocket.accept()
    room = battle_manager.get_room(room_code)
    player_id = None
    player_key = str(id(websocket))

    if not room:
        await websocket.send_json({"type": "error", "message": "Bunday batl xonasi mavjud emas yoki yakunlangan!"})
        await websocket.close()
        return

    try:
        while True:
            data = await websocket.receive_json()
            action = data.get("action")

            if action == "join":
                # Check limits
                if len(room.players) >= room.max_players:
                    await websocket.send_json({"type": "error", "message": f"Bu xona to'lgan! Maksimal {room.max_players} kishi qatnasha oladi."})
                    await websocket.close()
                    return

                player_id = data.get("user_id")
                player_name = data.get("name", "O'yinchi")
                is_pro = bool(data.get("is_pro", False))
                avatar = data.get("avatar", "avatar_1.png")

                # If room mode is 'pro_3_5', require either host or joining user or allow if room created as PRO
                room.players[player_key] = {
                    "key": player_key,
                    "id": player_id,
                    "name": player_name,
                    "avatar": avatar,
                    "is_pro": is_pro,
                    "score": 0,
                    "ready": True,
                    "is_bot": False
                }
                room.sockets[player_key] = websocket

                # Broadcast room update
                await broadcast_room_state(room)

            elif action == "add_bot":
                # Add intelligent simulated bot competitor for instant action
                if len(room.players) < room.max_players:
                    bot_names = ["Olimpiada_Chempioni", "Zukko_Talaba", "Shahzod_Pro", "Malika_Iqtidor", "Aziz_Fast"]
                    bot_name = random.choice(bot_names)
                    bot_key = f"bot_{random.randint(1000, 9999)}"
                    room.players[bot_key] = {
                        "key": bot_key,
                        "id": random.randint(900, 999),
                        "name": f"🤖 {bot_name}",
                        "avatar": f"avatar_{random.randint(1, 4)}.png",
                        "is_pro": True,
                        "score": 0,
                        "ready": True,
                        "is_bot": True
                    }
                    await broadcast_room_state(room)

            elif action == "start":
                # Fetch questions for this battle (5, 15, or 30 questions)
                limit_cnt = getattr(room, "question_count", 5)
                if limit_cnt not in (5, 15, 30):
                    limit_cnt = 5

                conn = get_db()
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT id, question_text, options, correct_index, explanation, difficulty 
                    FROM questions 
                    WHERE subject_id = ? 
                    ORDER BY RANDOM() LIMIT ?
                """, (room.subject_id, limit_cnt))
                q_rows = list(cursor.fetchall())

                # If subject has fewer questions than requested, top up with other subjects
                if len(q_rows) < limit_cnt:
                    needed = limit_cnt - len(q_rows)
                    existing_ids = [r["id"] for r in q_rows] or [-1]
                    placeholders = ",".join("?" for _ in existing_ids)
                    cursor.execute(f"""
                        SELECT id, question_text, options, correct_index, explanation, difficulty 
                        FROM questions 
                        WHERE id NOT IN ({placeholders})
                        ORDER BY RANDOM() LIMIT ?
                    """, (*existing_ids, needed))
                    more_rows = cursor.fetchall()
                    q_rows.extend(more_rows)
                conn.close()

                questions = []
                for q in q_rows:
                    item = dict(q)
                    try:
                        item["options"] = json.loads(item["options"])
                    except:
                        item["options"] = []
                    questions.append(item)

                if not questions:
                    for ws in list(room.sockets.values()):
                        try:
                            await ws.send_json({
                                "type": "error",
                                "message": "Ushbu fan bo'yicha rasmiy testlar hali kiritilmagan. Kitob va testlar yuklangach, to'liq batl boshlanadi!"
                            })
                        except:
                            pass
                    continue

                room.questions = questions
                room.status = "playing"
                room.current_q_index = 0

                await send_next_question(room)

            elif action == "answer":
                q_idx = data.get("question_index")
                chosen_opt = data.get("selected_option")
                time_left = data.get("time_left", 10)

                if q_idx == room.current_q_index and player_key in room.players:
                    current_q = room.questions[q_idx]
                    is_correct = (chosen_opt == current_q["correct_index"])
                    # Speed bonus: faster answer yields more points (max 1000)
                    points = 0
                    if is_correct:
                        points = 500 + int(time_left * 35)
                        room.players[player_key]["score"] += points

                    room.answers_this_round[player_key] = {
                        "correct": is_correct,
                        "points": points,
                        "chosen": chosen_opt
                    }

                    # If bots exist in room, simulate bot answer
                    for b_key, b_info in list(room.players.items()):
                        if b_info.get("is_bot") and b_key not in room.answers_this_round:
                            bot_correct = random.random() > 0.35 # 65% correct
                            bot_points = 500 + random.randint(200, 450) if bot_correct else 0
                            b_info["score"] += bot_points
                            room.answers_this_round[b_key] = {
                                "correct": bot_correct,
                                "points": bot_points,
                                "chosen": current_q["correct_index"] if bot_correct else (current_q["correct_index"] + 1) % 4
                            }

                    # Check if all players answered
                    if len(room.answers_this_round) >= len(room.players):
                        await reveal_round_results(room)

            elif action == "reaction":
                emoji = data.get("emoji", "🔥")
                sticker_text = data.get("text", "")
                sticker_type = data.get("sticker_type", "fire")
                sender_info = room.players.get(player_key, {})
                sender_name = sender_info.get("name", "O'yinchi")
                sender_avatar = sender_info.get("avatar", "avatar_1.png")
                for ws in list(room.sockets.values()):
                    try:
                        await ws.send_json({
                            "type": "reaction",
                            "sender_key": player_key,
                            "sender_id": sender_info.get("id"),
                            "sender": sender_name,
                            "avatar": sender_avatar,
                            "emoji": emoji,
                            "text": sticker_text,
                            "sticker_type": sticker_type
                        })
                    except Exception:
                        pass

    except WebSocketDisconnect:
        pass
    finally:
        if player_key in room.players:
            del room.players[player_key]
        if player_key in room.sockets:
            del room.sockets[player_key]

        if len(room.players) == 0:
            battle_manager.remove_room(room_code)
        else:
            await broadcast_room_state(room)

async def broadcast_room_state(room: BattleRoom):
    players_list = list(room.players.values())
    payload = {
        "type": "room_state",
        "room_code": room.room_code,
        "mode": room.mode,
        "max_players": room.max_players,
        "question_count": getattr(room, "question_count", 5),
        "status": room.status,
        "player_count": len(players_list),
        "players": players_list,
        "can_start": len(players_list) >= 2
    }
    for ws in list(room.sockets.values()):
        try:
            await ws.send_json(payload)
        except:
            pass

async def send_next_question(room: BattleRoom):
    room.answers_this_round = {}
    if room.current_q_index >= len(room.questions):
        # Game finished!
        await finish_game(room)
        return

    q = room.questions[room.current_q_index]
    # Hide correct index from client during round
    client_q = {
        "index": room.current_q_index,
        "total": len(room.questions),
        "question_text": q["question_text"],
        "options": q["options"],
        "difficulty": q.get("difficulty", "orta"),
        "time_limit": room.time_limit
    }

    for ws in list(room.sockets.values()):
        try:
            await ws.send_json({
                "type": "question",
                "question": client_q,
                "current_index": room.current_q_index,
                "total": len(room.questions),
                "leaderboard": sorted(room.players.values(), key=lambda p: p["score"], reverse=True)
            })
        except:
            pass

    # Auto round timer: if round isn't finished within time_limit + 1 sec, force reveal
    asyncio.create_task(round_timer_task(room, room.current_q_index))

async def round_timer_task(room: BattleRoom, q_idx: int):
    await asyncio.sleep(room.time_limit + 1)
    if room.status == "playing" and room.current_q_index == q_idx and len(room.answers_this_round) < len(room.players):
        # Auto-fill unanswered players with 0
        for p_key, p_info in room.players.items():
            if p_key not in room.answers_this_round:
                room.answers_this_round[p_key] = {"correct": False, "points": 0, "chosen": -1}
        await reveal_round_results(room)

async def reveal_round_results(room: BattleRoom):
    q = room.questions[room.current_q_index]
    round_payload = {
        "type": "round_result",
        "correct_index": q["correct_index"],
        "explanation": q.get("explanation", ""),
        "answers": room.answers_this_round,
        "leaderboard": sorted(room.players.values(), key=lambda p: p["score"], reverse=True)
    }

    for ws in list(room.sockets.values()):
        try:
            await ws.send_json(round_payload)
        except:
            pass

    # Bot stickers/emotions occasionally
    for b_key, b_info in list(room.players.items()):
        if b_info.get("is_bot") and random.random() < 0.45:
            bot_ans = room.answers_this_round.get(b_key, {})
            if bot_ans.get("correct"):
                bot_stickers = [
                    ("😎", "Oson ekan!", "flex"),
                    ("🔥", "Yonamiz!", "fire"),
                    ("⚡", "Tezkor javob!", "fire"),
                    ("🧠", "Katta miya!", "flex"),
                    ("🎯", "Aniq nishon!", "fire")
                ]
            else:
                bot_stickers = [
                    ("🤯", "Miya portladi!", "shock"),
                    ("😱", "Adashdim-ku!", "shock"),
                    ("😭", "Eh attang!", "shock"),
                    ("🤦‍♂️", "Qanday qilib?!", "shock")
                ]
            chosen_st = random.choice(bot_stickers)
            for ws in list(room.sockets.values()):
                try:
                    await ws.send_json({
                        "type": "reaction",
                        "sender_key": b_key,
                        "sender_id": b_info.get("id"),
                        "sender": b_info.get("name"),
                        "avatar": b_info.get("avatar"),
                        "emoji": chosen_st[0],
                        "text": chosen_st[1],
                        "sticker_type": chosen_st[2]
                    })
                except Exception:
                    pass

    # Wait 3.5 seconds before advancing to next question
    await asyncio.sleep(3.5)
    room.current_q_index += 1
    await send_next_question(room)

async def finish_game(room: BattleRoom):
    room.status = "finished"
    standings = sorted(room.players.values(), key=lambda p: p["score"], reverse=True)
    winner = standings[0] if standings else None

    # Save to database
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO battle_history (room_code, mode, subject_id, player_count, winner_id, scores_json)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            room.room_code, room.mode, room.subject_id, len(room.players),
            winner["id"] if winner else None,
            json.dumps(standings, ensure_ascii=False)
        ))
        conn.commit()
        conn.close()
    except Exception as e:
        print("Save battle error:", e)

    payload = {
        "type": "game_over",
        "winner": winner,
        "standings": standings
    }

    for ws in list(room.sockets.values()):
        try:
            await ws.send_json(payload)
        except:
            pass

@app.post("/api/battle/create-room")
def create_battle_room(payload: dict = Body(...)):
    host_id = payload.get("host_id", 1)
    host_name = payload.get("host_name", "O'yinchi")
    subject_id = payload.get("subject_id", 1)
    mode = payload.get("mode", "1v1") # '1v1' or 'pro_3_5'
    requested_max = int(payload.get("max_players", 2))
    question_count = int(payload.get("question_count", 5))
    if question_count not in (5, 15, 30):
        question_count = 5

    # Free users can do 2 players. PRO users can select 3, 4, or 5 players!
    if mode == "pro_3_5":
        max_players = min(max(requested_max, 3), 5)
    else:
        max_players = 2

    # Generate 6-digit room code
    room_code = f"BATL{random.randint(1000, 9999)}"
    battle_manager.create_room(room_code, mode, host_id, host_name, subject_id, max_players, question_count)

    return {
        "success": True,
        "room_code": room_code,
        "mode": mode,
        "max_players": max_players,
        "question_count": question_count
    }

# ----------------- STATIC FILES & FRONTEND -----------------

FRONTEND_DIR = os.path.join(os.path.dirname(__file__), "..", "frontend")
@app.post("/api/user/role")
def update_user_role(payload: dict = Body(...)):
    user_id = payload.get("user_id")
    role = payload.get("role")
    if role == "teacher":
        raise HTTPException(status_code=403, detail="O'qituvchi paneli yopilgan! Hech kim o'qituvchi bo'la olmaydi.")
    conn = get_db()
    c = conn.cursor()
    c.execute("UPDATE users SET role = 'student', is_pro = 0 WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()
    return {"ok": True, "role": "student"}

# ----------------- TEACHER SEARCH & ADD STUDENT BY ID -----------------
@app.get("/api/teacher/search-students")
def teacher_search_students(q: str = Query(""), teacher_id: int = Query(0)):
    term = q.strip()
    if not term:
        return []
    clean_term = term.upper()
    eb_variant = f"EB-{clean_term}" if (not clean_term.startswith("EB-") and clean_term.isdigit()) else clean_term
    like_term = f"%{term.lower()}%"
    
    conn = get_db()
    c = conn.cursor()
    c.execute("""
        SELECT u.id, u.username, u.full_name, u.role, u.school_lyceum, u.grade, u.xp, u.grade_score, u.is_pro
        FROM users u
        WHERE u.role = 'student' AND (
            UPPER(u.username) = ? OR
            UPPER(u.username) = ? OR
            LOWER(u.username) LIKE ? OR
            LOWER(u.full_name) LIKE ?
        )
        LIMIT 20
    """, (clean_term, eb_variant, like_term, like_term))
    students = [dict(r) for r in c.fetchall()]
    conn.close()
    return students

@app.post("/api/teacher/groups/{group_id}/add-student")
def teacher_add_student_to_group(group_id: int, payload: dict = Body(...)):
    teacher_id = payload.get("teacher_id")
    student_id = payload.get("student_id")
    student_eb = (payload.get("student_eb") or "").strip().upper()
    
    conn = get_db()
    c = conn.cursor()
    c.execute("SELECT id, group_name FROM teacher_groups WHERE id = ? AND teacher_id = ?", (group_id, teacher_id))
    grp = c.fetchone()
    if not grp:
        conn.close()
        raise HTTPException(status_code=403, detail="Guruh topilmadi yoki sizga tegishli emas!")
    
    if not student_id and student_eb:
        if not student_eb.startswith("EB-") and student_eb.isdigit():
            student_eb = f"EB-{student_eb}"
        c.execute("SELECT id FROM users WHERE UPPER(username) = ? AND role = 'student'", (student_eb,))
        st_row = c.fetchone()
        if st_row:
            student_id = st_row["id"]
        else:
            conn.close()
            raise HTTPException(status_code=404, detail=f"'{student_eb}' ID raqamli o'quvchi topilmadi!")

    if not student_id:
        conn.close()
        raise HTTPException(status_code=400, detail="O'quvchi tanlanmadi!")

    c.execute("SELECT id FROM group_members WHERE group_id = ? AND student_id = ?", (group_id, student_id))
    if c.fetchone():
        conn.close()
        return {"success": True, "message": "O'quvchi allaqachon ushbu guruhga a'zo!"}

    c.execute("INSERT INTO group_members (group_id, student_id, joined_at) VALUES (?, ?, datetime('now'))", (group_id, student_id))
    conn.commit()
    conn.close()
    return {"success": True, "message": f"O'quvchi '{grp['group_name']}' guruhiga muvaffaqiyatli qo'shildi!"}



# ----------------- PRO DAILY TEST LIMIT & BLITZ API -----------------

@app.get("/api/user-test-limit/{user_id}")
def check_user_test_limit(user_id: int):
    if not user_id:
        return {"allowed": True, "today_count": 0, "max_limit": 2, "is_pro": False}
    
    conn = get_db()
    c = conn.cursor()
    c.execute("SELECT id, role, is_pro FROM users WHERE id = ?", (user_id,))
    u = c.fetchone()
    if not u:
        conn.close()
        return {"allowed": True, "today_count": 0, "max_limit": 2, "is_pro": False}
    
    is_pro = bool(u["is_pro"]) or (u["role"] in ("teacher", "admin"))
    
    # Check submissions today
    c.execute("""
        SELECT COUNT(*) FROM quiz_submissions 
        WHERE student_id = ? AND date(submitted_at) = date('now')
    """, (user_id,))
    today_count = c.fetchone()[0] or 0
    conn.close()
    
    allowed = is_pro or (today_count < 2)
    return {
        "allowed": allowed,
        "today_count": today_count,
        "max_limit": 2,
        "is_pro": is_pro,
        "remaining": max(0, 2 - today_count) if not is_pro else 999
    }

@app.get("/api/blitz/current")
def get_current_blitz_question(subject_id: int = Query(1), user_id: int = Query(0)):
    now = time.time()
    current_minute = int(now // 60)
    seconds_left = max(0, 60 - int(now % 60))
    
    conn = get_db()
    c = conn.cursor()
    
    # Ensure blitz table exists
    c.execute("""
        CREATE TABLE IF NOT EXISTS blitz_submissions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            subject_id INTEGER NOT NULL,
            minute_epoch INTEGER NOT NULL,
            selected_index INTEGER,
            is_correct INTEGER NOT NULL,
            coins_earned INTEGER NOT NULL,
            submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(user_id, subject_id, minute_epoch)
        )
    """)
    conn.commit()
    
    # Get all questions for subject
    c.execute("SELECT * FROM questions WHERE subject_id = ? ORDER BY id ASC", (subject_id,))
    q_rows = c.fetchall()
    
    if not q_rows:
        # Fallback to any questions
        c.execute("SELECT * FROM questions ORDER BY id ASC LIMIT 20")
        q_rows = c.fetchall()
        
    if not q_rows:
        conn.close()
        return JSONResponse(
            content={"error": "Savollar topilmadi", "seconds_left": seconds_left},
            headers={"Cache-Control": "no-cache, no-store, must-revalidate", "Pragma": "no-cache"}
        )
        
    # Deterministic sequential index per minute: advances by 1 every minute across the large pool
    q_idx = current_minute % len(q_rows)
    q = dict(q_rows[q_idx])
    
    if q.get("options") and isinstance(q["options"], str):
        try:
            q["options"] = json.loads(q["options"])
        except:
            q["options"] = []
            
    # Check if user already submitted for this minute
    already_answered = False
    submission_data = None
    if user_id:
        c.execute("""
            SELECT selected_index, is_correct, coins_earned 
            FROM blitz_submissions 
            WHERE user_id = ? AND subject_id = ? AND minute_epoch = ?
        """, (user_id, subject_id, current_minute))
        sub = c.fetchone()
        if sub:
            already_answered = True
            submission_data = dict(sub)
            
    conn.close()
    
    return JSONResponse(
        content={
            "subject_id": subject_id,
            "minute_epoch": current_minute,
            "seconds_left": seconds_left,
            "question_id": q["id"],
            "chapter_title": q.get("chapter_title", "Blitz Savol"),
            "question_text": q["question_text"],
            "options": q["options"],
            "already_answered": already_answered,
            "user_answer": submission_data["selected_index"] if submission_data else None,
            "is_correct": bool(submission_data["is_correct"]) if submission_data else None,
            "explanation": q.get("explanation") if already_answered else None
        },
        headers={
            "Cache-Control": "no-cache, no-store, must-revalidate",
            "Pragma": "no-cache",
            "Expires": "0"
        }
    )

@app.post("/api/blitz/submit")
def submit_blitz_answer(payload: dict = Body(...)):
    user_id = payload.get("user_id", 0)
    subject_id = payload.get("subject_id", 1)
    minute_epoch = payload.get("minute_epoch", 0)
    selected_index = payload.get("selected_index", -1)
    
    now = time.time()
    real_minute = int(now // 60)
    
    # Allow submission within 5s grace of minute transition
    if abs(real_minute - minute_epoch) > 1:
        raise HTTPException(status_code=400, detail="Vaqt tugadi! Yangi daqiqa savoliga o'ting.")
        
    conn = get_db()
    c = conn.cursor()
    
    # Get user by id or telegram_id
    c.execute("SELECT id, is_pro, coins FROM users WHERE id = ? OR telegram_id = ?", (user_id, user_id))
    u = c.fetchone()
    if not u:
        new_eb = f"EB-{secrets.randbelow(90000) + 10000}"
        c.execute("""
            INSERT INTO users (username, full_name, role, school_lyceum, grade, avatar, xp, coins, streak, is_pro, pin_code, created_at, grade_score)
            VALUES (?, 'EduBattle Foydalanuvchi', 'student', 'EduBattle Online', '9-sinf', 'avatar1.png', 0, 0, 1, 0, ?, datetime('now'), 0)
        """, (new_eb, hash_password("pass_12345")))
        conn.commit()
        actual_user_id = c.lastrowid
        is_pro = False
    else:
        actual_user_id = u["id"]
        is_pro = bool(u["is_pro"])

    # Check duplicate
    c.execute("SELECT id FROM blitz_submissions WHERE user_id = ? AND subject_id = ? AND minute_epoch = ?", (actual_user_id, subject_id, minute_epoch))
    if c.fetchone():
        conn.close()
        return {"success": False, "message": "Ushbu daqiqadagi savolga allaqachon javob berdingiz!"}
    
    # Get question for this minute
    c.execute("SELECT * FROM questions WHERE subject_id = ? ORDER BY id ASC", (subject_id,))
    q_rows = c.fetchall()
    if not q_rows:
        c.execute("SELECT * FROM questions ORDER BY id ASC LIMIT 20")
        q_rows = c.fetchall()
        
    q_idx = minute_epoch % len(q_rows)
    q = dict(q_rows[q_idx])
    
    is_correct = (selected_index == q["correct_index"])
    coins_earned = (25 if is_pro else 10) if is_correct else 0
    xp_earned = 0
    
    c.execute("""
        INSERT INTO blitz_submissions (user_id, subject_id, minute_epoch, selected_index, is_correct, coins_earned)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (actual_user_id, subject_id, minute_epoch, selected_index, 1 if is_correct else 0, coins_earned))
    
    c.execute("""
        UPDATE users 
        SET coins = coins + ? 
        WHERE id = ?
    """, (coins_earned, actual_user_id))

    if coins_earned > 0:
        c.execute("""
            INSERT INTO coin_transactions (user_id, amount, reason, created_at)
            VALUES (?, ?, '1 daqiqalik Blitz turniri', datetime('now'))
        """, (actual_user_id, coins_earned))
    
    conn.commit()
    
    c.execute("SELECT coins FROM users WHERE id = ?", (actual_user_id,))
    new_stats = dict(c.fetchone())
    conn.close()
    
    return {
        "success": True,
        "is_correct": is_correct,
        "correct_index": q["correct_index"],
        "coins_earned": coins_earned,
        "xp_earned": 0,
        "is_pro": is_pro,
        "explanation": q.get("explanation") or "To'g'ri javob qayd etildi.",
        "new_coins": new_stats["coins"],
        "new_xp": 0,
        "user_id": actual_user_id
    }


if os.path.exists(FRONTEND_DIR):
    UPLOADS_DIR = os.path.join(FRONTEND_DIR, "uploads")
os.makedirs(UPLOADS_DIR, exist_ok=True)
app.mount("/uploads", StaticFiles(directory=UPLOADS_DIR), name="uploads")
app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")

@app.get("/download/android")
@app.get("/download/edubattle.apk")
def download_android_apk():
    apk_path = os.path.join(FRONTEND_DIR, "downloads", "EduBattle.apk")
    if not os.path.exists(apk_path):
        apk_path = os.path.join(os.path.dirname(__file__), "EduBattle.apk")
    if os.path.exists(apk_path):
        return FileResponse(
            apk_path,
            media_type="application/vnd.android.package-archive",
            filename="EduBattle.apk"
        )
    return JSONResponse(status_code=404, content={"detail": "APK topilmadi"})

@app.get("/download")
@app.get("/app")
def serve_download_page():
    page_path = os.path.join(FRONTEND_DIR, "download.html")
    if os.path.exists(page_path):
        return FileResponse(
            page_path,
            headers={
                "Cache-Control": "no-cache, no-store, must-revalidate",
                "Pragma": "no-cache",
                "Expires": "0"
            }
        )
    return FileResponse(os.path.join(FRONTEND_DIR, "index.html"))

@app.get("/admin")
@app.get("/admin-portal")
def serve_admin():
    admin_path = os.path.join(FRONTEND_DIR, "admin-portal.html")
    if os.path.exists(admin_path):
        return FileResponse(
            admin_path,
            headers={
                "Cache-Control": "no-cache, no-store, must-revalidate",
                "Pragma": "no-cache",
                "Expires": "0"
            }
        )
    return JSONResponse(status_code=404, content={"detail": "Admin portal topilmadi"})

@app.get("/")
def serve_index():
    index_path = os.path.join(FRONTEND_DIR, "index.html")
    if os.path.exists(index_path):
        return FileResponse(
            index_path,
            headers={
                "Cache-Control": "no-cache, no-store, must-revalidate",
                "Pragma": "no-cache",
                "Expires": "0"
            }
        )
    return {"message": "EduBattle API Running"}

@app.get("/{catchall:path}")
def serve_static(catchall: str):
    if catchall.startswith("api/"):
        return JSONResponse(status_code=404, content={"detail": "API endpoint not found"})
    file_path = os.path.join(FRONTEND_DIR, catchall)
    if os.path.exists(file_path) and os.path.isfile(file_path):
        return FileResponse(
            file_path,
            headers={
                "Cache-Control": "no-cache, no-store, must-revalidate",
                "Pragma": "no-cache",
                "Expires": "0"
            }
        )
    # Fallback to index.html for SPA/PWA routing
    index_path = os.path.join(FRONTEND_DIR, "index.html")
    if os.path.exists(index_path):
        return FileResponse(
            index_path,
            headers={
                "Cache-Control": "no-cache, no-store, must-revalidate",
                "Pragma": "no-cache",
                "Expires": "0"
            }
        )
    return JSONResponse(status_code=404, content={"detail": "Not found"})


