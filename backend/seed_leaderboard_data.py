import sqlite3
import random
from datetime import datetime, timedelta

conn = sqlite3.connect('backend/edubattle.db')
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS coin_transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    amount INTEGER NOT NULL,
    reason TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')
c.execute('CREATE INDEX IF NOT EXISTS idx_coin_tx_user_created ON coin_transactions(user_id, created_at)')

# 1. Backfill transactions for existing students
c.execute("SELECT id, coins FROM users WHERE role = 'student'")
existing_students = c.fetchall()
for uid, ucoins in existing_students:
    c.execute("SELECT COUNT(*) FROM coin_transactions WHERE user_id = ?", (uid,))
    if c.fetchone()[0] == 0 and ucoins > 0:
        # Give weekly portion (70%) and past portion (30%)
        weekly_amt = int(ucoins * 0.7)
        past_amt = ucoins - weekly_amt
        if past_amt > 0:
            c.execute("""
                INSERT INTO coin_transactions (user_id, amount, reason, created_at)
                VALUES (?, ?, 'Mavzulashtirilgan test', datetime('now', '-10 days'))
            """, (uid, past_amt))
        if weekly_amt > 0:
            c.execute("""
                INSERT INTO coin_transactions (user_id, amount, reason, created_at)
                VALUES (?, ?, '1 daqiqalik Blitz turniri', datetime('now', '-2 days'))
            """, (uid, weekly_amt))

# 2. Add realistic top students if not present
sample_students = [
    ("Jasurbek Raxmatov", "Qorako'l Xalqaro Matematika Maktabi", "11-sinf", "🦁", 1, 1420, 480, 4200),
    ("Malika Qosimova", "Toshkent Prezident Maktabi", "10-sinf", "🌟", 1, 1260, 420, 3850),
    ("Diyorbek Ismoilov", "Al-Xorazmiy nomidagi IT Maktabi", "10-sinf", "🚀", 1, 1150, 390, 3500),
    ("Madinabonu Alimova", "Samarqand 1-sonli Akademik Litsey", "AL 2-bosqich", "🎓", 0, 980, 310, 2900),
    ("Shahzod Normatov", "Farg'ona 2-sonli IDUM", "9-sinf", "🦅", 1, 890, 290, 2650),
    ("Zuhra Karimova", "Namangan 1-son Prezident Ijod Maktabi", "11-sinf", "🦉", 0, 810, 260, 2400),
    ("Behzod Abdullayev", "Buxoro Davlat Universiteti qoshidagi AL", "AL 1-bosqich", "⚡", 1, 750, 230, 2200),
    ("Sevara Rustamova", "Andijon 24-sonli Ixtisoslashgan Maktab", "10-sinf", "🌺", 0, 680, 210, 2050),
    ("Bobur Mirzayev", "Xorazm Urganch 1-son IDUM", "10-sinf", "🏆", 1, 620, 190, 1900),
    ("Gulnoza Ahmedova", "Toshkent 178-sonli IDUM", "9-sinf", "🌸", 0, 540, 170, 1750),
    ("Ulug'bek Fayzullayev", "Navoiy 1-sonli Ixtisoslashgan Maktab-internat", "11-sinf", "🎯", 1, 480, 150, 1600),
    ("Kamola Yo'ldosheva", "Qashqadaryo Qarshi 2-sonli AL", "AL 2-bosqich", "✨", 0, 410, 130, 1450)
]

for name, school, grade, avatar, is_pro, total_coins, weekly_coins, xp in sample_students:
    c.execute("SELECT id FROM users WHERE full_name = ? AND role = 'student'", (name,))
    row = c.fetchone()
    if not row:
        eb_id = f"EB-{random.randint(10000, 99999)}"
        c.execute("""
            INSERT INTO users (username, full_name, role, school_lyceum, grade, avatar, xp, coins, streak, is_pro, grade_score, created_at)
            VALUES (?, ?, 'student', ?, ?, ?, ?, ?, ?, ?, 95, datetime('now', '-30 days'))
        """, (eb_id, name, school, grade, avatar, xp, total_coins, random.randint(3, 15), is_pro))
        user_id = c.lastrowid
    else:
        user_id = row[0]
        c.execute("""
            UPDATE users SET school_lyceum = ?, grade = ?, avatar = ?, xp = ?, coins = ?, is_pro = ?
            WHERE id = ?
        """, (school, grade, avatar, xp, total_coins, is_pro, user_id))

    # Seed transactions for this student
    c.execute("DELETE FROM coin_transactions WHERE user_id = ?", (user_id,))
    # Past coins (older than 7 days)
    past_coins = total_coins - weekly_coins
    if past_coins > 0:
        c.execute("""
            INSERT INTO coin_transactions (user_id, amount, reason, created_at)
            VALUES (?, ?, 'Mavzulashtirilgan testlar', datetime('now', '-12 days'))
        """, (user_id, past_coins))
    
    # Weekly coins distributed across past 5 days
    days = [1, 2, 3, 4, 5]
    remaining = weekly_coins
    for i, d in enumerate(days):
        if i == len(days) - 1:
            chunk = remaining
        else:
            chunk = max(10, remaining // (len(days) - i))
        remaining -= chunk
        if chunk > 0:
            reasons = ["1 daqiqalik Blitz turniri", "Fanlararo test", "PvP Battle g'olibi"]
            reason = random.choice(reasons)
            c.execute("""
                INSERT INTO coin_transactions (user_id, amount, reason, created_at)
                VALUES (?, ?, ?, datetime('now', ? || ' days', ? || ' hours'))
            """, (user_id, chunk, reason, f"-{d}", f"-{random.randint(1, 10)}"))

conn.commit()
conn.close()
print("Seeding complete successfully!")
