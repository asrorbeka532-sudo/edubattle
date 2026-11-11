import json
from database import get_db, init_db

def seed_all():
    init_db()
    conn = get_db()
    cursor = conn.cursor()

    # Clear existing questions - user requested: "O'zing sun'iy tarzda qo'shgan testlaringni olib tashlagin. Men o'zim senga test beraman"
    cursor.execute("DELETE FROM questions")
    cursor.execute("DELETE FROM battle_history")
    cursor.execute("DELETE FROM quiz_submissions")
    cursor.execute("DELETE FROM teacher_quizzes")
    cursor.execute("DELETE FROM group_members")
    cursor.execute("DELETE FROM teacher_groups")
    cursor.execute("DELETE FROM textbooks")
    cursor.execute("DELETE FROM subjects")
    cursor.execute("DELETE FROM users")
    cursor.execute("DELETE FROM subscriptions")

    # 1. Base Users (admin + demo student + demo teacher)
    users_data = [
        (1, "sardor_9a", "Sardor Aliyev", "student", "172-maktab", "9-sinf", "avatar_1.png", 0, 0, 0, 0, "1111"),
        (2, "ustoz_olimjon", "Ustoz Olimjon Yo'ldoshev", "teacher", "21-maktab & Litsey", "Oliy toifa", "teacher_1.png", 850, 0, 15, 0, "teacher123"),
        (3, "admin", "Bosh Administrator", "admin", "EduBattle Markazi", "Super Admin", "admin.png", 9999, 0, 99, 1, "admin2026")
    ]
    cursor.executemany("""
    INSERT INTO users (id, username, full_name, role, school_lyceum, grade, avatar, xp, coins, streak, is_pro, pin_code)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, users_data)

    # 2. Real Subjects
    subjects_data = [
        (1, "Matematika", "math", "📐", "#ef4444", "Algebra, Geometriya va Mantiqiy masalalar", "aniq"),
        (2, "Fizika", "physics", "⚡", "#6366f1", "Mexanika, Elektr, Optika va Kvant fizikasi", "aniq"),
        (3, "Kimyo", "chemistry", "🧪", "#10b981", "Anorganik va Organik kimyo, Davriy qonun", "tabiiy"),
        (4, "Biologiya", "biology", "🧬", "#22c55e", "Sitologiya, Anatomiya va Genetika", "tabiiy"),
        (5, "Ona tili va Adabiyot", "uzbek", "📚", "#f59e0b", "Fonetika, Sintaksis va Badiiy adabiyot", "ijtimoiy"),
        (6, "Tarix", "history", "🏛️", "#ec4899", "O'zbekiston tarixi va Jahon sivilizatsiyalari", "ijtimoiy"),
        (7, "Ingliz tili", "english", "🌍", "#3b82f6", "Grammar, Lexicon, CEFR B1-B2 & IELTS", "xorijiy"),
        (8, "Informatika va IT", "cs", "💻", "#06b6d4", "Algoritmlar, Dasturlash va Kiberxavfsizlik", "aniq")
    ]
    cursor.executemany("""
    INSERT INTO subjects (id, name, code, icon, color, description, category)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, subjects_data)

    # 3. Base Group for Teacher
    cursor.execute("""
    INSERT INTO teacher_groups (id, teacher_id, group_name, subject_id, invite_code, description)
    VALUES (1, 2, "9-A Sinf Matematika Guruxi", 1, "MATH9A", "9-A sinf o'quvchilari uchun maxsus guruh")
    """)
    cursor.execute("""
    INSERT INTO group_members (group_id, student_id)
    VALUES (1, 1)
    """)

    conn.commit()
    conn.close()
    print("Database cleaned and initialized! Fake questions cleared. Ready for user's official materials.")

if __name__ == "__main__":
    seed_all()
