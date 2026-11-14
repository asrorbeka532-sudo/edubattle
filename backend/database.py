import sqlite3
import json
import os

def get_db_path():
    data_dir = os.environ.get("DATA_DIR")
    if not data_dir and os.path.exists("/data") and os.path.isdir("/data"):
        data_dir = "/data"

    if data_dir:
        os.makedirs(data_dir, exist_ok=True)
        target = os.path.join(data_dir, "edubattle.db")
        if not os.path.exists(target):
            seed = os.path.join(os.path.dirname(__file__), "edubattle.db")
            if os.path.exists(seed):
                import shutil
                try:
                    shutil.copy2(seed, target)
                    print(f"Initialized persistent database at {target} from bundled seed.")
                except Exception as e:
                    print(f"Error seeding persistent db: {e}")
        return target
    
    custom_path = os.environ.get("SQLITE_PATH")
    if custom_path:
        return custom_path
        
    return os.path.join(os.path.dirname(__file__), "edubattle.db")

DB_PATH = get_db_path()

def get_db():
    conn = sqlite3.connect(DB_PATH, timeout=10.0)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL;")
    conn.execute("PRAGMA synchronous=NORMAL;")
    conn.execute("PRAGMA busy_timeout=5000;")
    return conn

def init_db():
    conn = get_db()
    cursor = conn.cursor()

    # Users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        full_name TEXT NOT NULL,
        role TEXT NOT NULL DEFAULT 'student', -- 'student', 'teacher', 'admin'
        school_lyceum TEXT,
        grade TEXT,
        avatar TEXT,
        xp INTEGER DEFAULT 0,
        grade_score INTEGER DEFAULT 0, -- 100 balli tizimdagi o'rtacha baho (yangi o'quvchi uchun 0 dan boshlanadi)
        streak INTEGER DEFAULT 0,
        is_pro INTEGER DEFAULT 0, -- 0 = free, 1 = pro
        pin_code TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # Subjects table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS subjects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        code TEXT UNIQUE NOT NULL,
        icon TEXT NOT NULL,
        color TEXT NOT NULL,
        description TEXT,
        category TEXT DEFAULT 'aniq' -- 'aniq', 'tabiiy', 'ijtimoiy', 'xorijiy'
    );
    """)

    # Textbooks table (Kutubxona: rasmiy va o'qituvchilar yuklagan kitoblar)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS textbooks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject_id INTEGER NOT NULL,
        title TEXT NOT NULL,
        author TEXT,
        grade TEXT NOT NULL,
        cover_image TEXT,
        summary TEXT,
        chapters TEXT, -- JSON array of chapters with theory content
        uploaded_by INTEGER, -- NULL bo'lsa rasmiy, aks holda o'qituvchi ID
        file_url TEXT, -- PDF yoki havola
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (subject_id) REFERENCES subjects(id),
        FOREIGN KEY (uploaded_by) REFERENCES users(id)
    );
    """)

    # Questions table (Rasmiy va o'qituvchilar o'zlari tuzgan testlar)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject_id INTEGER NOT NULL,
        grade TEXT DEFAULT '9-sinf',
        chapter_title TEXT,
        question_text TEXT NOT NULL,
        options TEXT NOT NULL, -- JSON array of 4 options
        correct_index INTEGER NOT NULL, -- 0, 1, 2, or 3
        explanation TEXT,
        difficulty TEXT DEFAULT 'orta', -- 'oson', 'orta', 'qiyin'
        created_by INTEGER, -- NULL bo'lsa rasmiy, aks holda o'qituvchi ID
        group_id INTEGER, -- Maxsus sinf uchun yoki umumiy
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (subject_id) REFERENCES subjects(id),
        FOREIGN KEY (created_by) REFERENCES users(id)
    );
    """)

    # Teacher Groups table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS teacher_groups (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        teacher_id INTEGER NOT NULL,
        group_name TEXT NOT NULL,
        subject_id INTEGER,
        invite_code TEXT UNIQUE NOT NULL,
        description TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (teacher_id) REFERENCES users(id)
    );
    """)

    # Group Members table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS group_members (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        group_id INTEGER NOT NULL,
        student_id INTEGER NOT NULL,
        joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (group_id) REFERENCES teacher_groups(id),
        FOREIGN KEY (student_id) REFERENCES users(id),
        UNIQUE(group_id, student_id)
    );
    """)

    # Teacher Quizzes table (for classroom live quizzes / homework)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS teacher_quizzes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        teacher_id INTEGER NOT NULL,
        group_id INTEGER,
        title TEXT NOT NULL,
        subject_id INTEGER NOT NULL,
        time_limit_sec INTEGER DEFAULT 20,
        questions TEXT NOT NULL, -- JSON array of question IDs or objects
        is_pro_only INTEGER DEFAULT 1,
        pin_code TEXT,
        status TEXT DEFAULT 'active', -- 'draft', 'active', 'finished'
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (teacher_id) REFERENCES users(id)
    );
    """)

    # Subject Quizzes / Topics table (Fanlar bo'yicha mavzular va testlar)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS subject_quizzes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject_id INTEGER NOT NULL,
        title TEXT NOT NULL,
        grade TEXT DEFAULT 'Barchasi',
        description TEXT,
        time_limit_sec INTEGER DEFAULT 600,
        questions_json TEXT NOT NULL,
        author_id INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (subject_id) REFERENCES subjects(id)
    );
    """)

    # Quiz Submissions table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS quiz_submissions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        quiz_id INTEGER,
        student_id INTEGER NOT NULL,
        score INTEGER NOT NULL,
        total_questions INTEGER NOT NULL,
        correct_count INTEGER NOT NULL,
        time_spent_sec INTEGER DEFAULT 0,
        submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (student_id) REFERENCES users(id)
    );
    """)

    # Battle History table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS battle_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        room_code TEXT NOT NULL,
        mode TEXT NOT NULL, -- '1v1_free' or 'pro_3_5'
        subject_id INTEGER,
        player_count INTEGER NOT NULL,
        winner_id INTEGER,
        scores_json TEXT NOT NULL,
        played_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # Subscriptions & Payments table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS subscriptions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        plan_name TEXT NOT NULL, -- 'pro_monthly' (29 000 so'm) or 'teacher_pro' (49 000 so'm)
        amount INTEGER NOT NULL,
        provider TEXT NOT NULL, -- 'click', 'payme', 'uzum'
        status TEXT DEFAULT 'active', -- 'pending', 'active', 'expired'
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        expires_at TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(id)
    );
    """)

    # Custom Quizzes (Foydalanuvchilar o'zlari tuzgan testlar va login-parollar)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS custom_quizzes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        subject_id INTEGER DEFAULT 1,
        title TEXT NOT NULL,
        login TEXT NOT NULL UNIQUE,
        passcode TEXT NOT NULL,
        questions_json TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(id)
    );
    """)

    # Friendships table (Friends & Follow Requests)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS friendships (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        friend_id INTEGER NOT NULL,
        status TEXT DEFAULT 'accepted', -- 'pending', 'accepted', 'rejected'
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(id),
        FOREIGN KEY (friend_id) REFERENCES users(id),
        UNIQUE(user_id, friend_id)
    );
    """)

    # Direct Chat Messages table (real-time / persistent in-app messaging)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS direct_messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sender_id INTEGER NOT NULL,
        receiver_id INTEGER NOT NULL,
        message TEXT NOT NULL,
        battle_room_code TEXT,
        is_read INTEGER DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (sender_id) REFERENCES users(id),
        FOREIGN KEY (receiver_id) REFERENCES users(id)
    );
    """)

    # User Sessions table for secure token authentication
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_sessions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        token TEXT UNIQUE NOT NULL,
        ip_address TEXT,
        user_agent TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        expires_at TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(id)
    );
    """)

    # Security Audit Logs (Failed logins, suspicious activity)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS security_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        event_type TEXT NOT NULL,
        ip_address TEXT,
        details TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # Student Grades & Evaluation Journal (100 ballik baholash jurnali)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS student_grades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER NOT NULL,
        teacher_id INTEGER,
        subject_id INTEGER,
        grade_type TEXT NOT NULL, -- 'Darsdagi faollik', 'Uyga vazifa', 'Nazorat ishi', 'Choraklik baho', 'Mustaqil ish', 'Test'
        score INTEGER NOT NULL, -- 0-100 ball
        comment TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (student_id) REFERENCES users(id),
        FOREIGN KEY (teacher_id) REFERENCES users(id),
        FOREIGN KEY (subject_id) REFERENCES subjects(id)
    );
    """)

    # Telegram OTP & Verifications Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS telegram_verifications (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        code TEXT NOT NULL,
        telegram_id INTEGER,
        telegram_username TEXT,
        purpose TEXT DEFAULT 'register', -- 'register', 'login', 'reset'
        user_id INTEGER,
        attempt_count INTEGER DEFAULT 0,
        is_used INTEGER DEFAULT 0,
        expires_at TIMESTAMP NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # Safe Migrations for existing databases
    try:
        cursor.execute("ALTER TABLE users ADD COLUMN grade_score INTEGER DEFAULT 0;")
    except:
        pass
    try:
        cursor.execute("ALTER TABLE users ADD COLUMN telegram_id INTEGER;")
    except:
        pass
    try:
        cursor.execute("ALTER TABLE users ADD COLUMN telegram_username TEXT;")
    except:
        pass
    try:
        cursor.execute("ALTER TABLE users ADD COLUMN lang TEXT DEFAULT 'uz';")
    except:
        pass

    try:
        cursor.execute("ALTER TABLE textbooks ADD COLUMN uploaded_by INTEGER;")
    except:
        pass
    try:
        cursor.execute("ALTER TABLE textbooks ADD COLUMN file_url TEXT;")
    except:
        pass

    try:
        cursor.execute("ALTER TABLE questions ADD COLUMN created_by INTEGER;")
    except:
        pass
    try:
        cursor.execute("ALTER TABLE questions ADD COLUMN group_id INTEGER;")
    except:
        pass
    try:
        cursor.execute("ALTER TABLE questions ADD COLUMN grade TEXT DEFAULT '9-sinf';")
    except:
        pass

    try:
        cursor.execute("ALTER TABLE teacher_quizzes ADD COLUMN passcode TEXT;")
    except:
        pass
    try:
        cursor.execute("ALTER TABLE teacher_quizzes ADD COLUMN description TEXT;")
    except:
        pass
    try:
        cursor.execute("ALTER TABLE friendships ADD COLUMN status TEXT DEFAULT 'accepted';")
    except:
        pass

    # PRO Subscription columns & migrations
    try:
        cursor.execute("ALTER TABLE users ADD COLUMN pro_expires_at TIMESTAMP;")
    except:
        pass
    try:
        cursor.execute("ALTER TABLE users ADD COLUMN trial_used INTEGER DEFAULT 0;")
    except:
        pass
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS trial_grants (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        telegram_id INTEGER UNIQUE,
        user_id INTEGER,
        granted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        expires_at TIMESTAMP
    );
    """)
    try:
        cursor.execute("ALTER TABLE subscriptions ADD COLUMN receipt_file_id TEXT;")
    except:
        pass
    try:
        cursor.execute("ALTER TABLE subscriptions ADD COLUMN receipt_type TEXT;")
    except:
        pass
    try:
        cursor.execute("ALTER TABLE subscriptions ADD COLUMN telegram_chat_id INTEGER;")
    except:
        pass
    try:
        cursor.execute("ALTER TABLE subscriptions ADD COLUMN reviewed_at TIMESTAMP;")
    except:
        pass
    try:
        cursor.execute("ALTER TABLE subscriptions ADD COLUMN admin_id INTEGER;")
    except:
        pass

    # Teacher role is completely disabled until user permits
    cursor.execute("UPDATE users SET role = 'student', is_pro = 0 WHERE role = 'teacher';")

    # Auto-seed Huquq subject, books and questions if not present
    try:
        cursor.execute("SELECT count(*) FROM questions WHERE subject_id = 9;")
        row_cnt = cursor.fetchone()
        if not row_cnt or row_cnt[0] < 200:
            from insert_huquq_module import insert_all_huquq
            conn.commit()
            insert_all_huquq()
    except Exception as e:
        print(f"Huquq auto-seed check: {e}")

    # Ensure questions have evenly distributed correct answer choices (A, B, C, D)
    try:
        cursor.execute("SELECT count(*) FROM questions WHERE correct_index = 0;")
        zero_cnt = cursor.fetchone()[0]
        cursor.execute("SELECT count(*) FROM questions;")
        tot_cnt = cursor.fetchone()[0]
        if tot_cnt > 0 and (zero_cnt / tot_cnt) > 0.4:
            from shuffle_questions import shuffle_all_questions_in_db
            conn.commit()
            shuffle_all_questions_in_db()
    except Exception as e:
        print(f"Question shuffle check: {e}")

    # Reset all coins, xp, and student grades as requested
    try:
        cursor.execute("UPDATE users SET coins = 0, xp = 0, grade_score = 0 WHERE coins != 0 OR xp != 0 OR grade_score != 0;")
        cursor.execute("DELETE FROM student_grades;")
    except Exception as e:
        print(f"Reset migration notice: {e}")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("Database initialized successfully.")


