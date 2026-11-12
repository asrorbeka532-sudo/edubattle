# -*- coding: utf-8 -*-
import sqlite3
import json
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "edubattle.db")

def create_huquq_subject_and_books(conn):
    c = conn.cursor()
    # 1. Subject: Huquq
    c.execute("SELECT id FROM subjects WHERE code = 'law' OR id = 9")
    existing_sub = c.fetchone()
    if existing_sub:
        subject_id = existing_sub[0]
        c.execute("""
            UPDATE subjects 
            SET name = 'Huquq', code = 'law', icon = '⚖️', color = '#8b5cf6', 
                description = 'Konstitutsiya, Davlat va Huquq asoslari, Fuqarolik va Inson huquqlari',
                category = 'ijtimoiy'
            WHERE id = ?
        """, (subject_id,))
    else:
        c.execute("""
            INSERT INTO subjects (id, name, code, icon, color, description, category)
            VALUES (9, 'Huquq', 'law', '⚖️', '#8b5cf6', 
                    'Konstitutsiya, Davlat va Huquq asoslari, Fuqarolik va Inson huquqlari', 'ijtimoiy')
        """)
        subject_id = 9

    # 2. Textbooks: 8, 9, 10, 11-sinflar va Konstitutsiya
    books_data = [
        (
            subject_id,
            "O'zbekiston Respublikasi Konstitutsiyasi (Yangi tahrir)",
            "Oliy Majlis va O'zbekiston xalqi",
            "Barcha sinflar",
            None,
            "2023-yil 30-aprel referendumida qabul qilingan yangi tahrirdagi Konstitutsiya. 6 bo'lim, 27 bob va 155 moddadan iborat rasmiy qonunlar to'plami.",
            json.dumps([
                {"title": "1-bo'lim. Asosiy prinsiplar (1-18 moddalar)", "summary": "Davlat suvereniteti, xalq hokimiyatchiligi, qonun ustunligi va tashqi siyosat."},
                {"title": "2-bo'lim. Inson va fuqaroning asosiy huquqlari, erkinliklari va burchlari (19-64 moddalar)", "summary": "Fuqarolik, shaxsiy, siyosiy, iqtisodiy, ijtimoiy, madaniy va ekologik huquqlar."},
                {"title": "3-bo'lim. Jamiyat va shaxs (65-82 moddalar)", "summary": "Iqtisodiy asoslar, jamoat birlashmalari, OAV, oila va yoshlar siyosati."},
                {"title": "4-bo'lim. Ma'muriy-hududiy va davlat tuzilishi (83-90 moddalar)", "summary": "Hududiy tuzilish va Qoraqalpog'iston Respublikasining suveren maqomi."},
                {"title": "5-bo'lim. Davlat hokimiyatining tashkil etilishi (91-153 moddalar)", "summary": "Oliy Majlis, Prezident, Vazirlar Mahkamasi, Mahalliy hokimiyat, Sud hokimiyati va Prokuratura."},
                {"title": "6-bo'lim. Konstitutsiyaga o'zgartirish kiritish tartibi (154-155 moddalar)", "summary": "Konstitutsiyaga tuzatishlar kiritish va uning daxlsizligi."}
            ]),
            None,
            "/uploads/textbooks/ozbekiston_respublikasi_konstitutsiyasi_yangi_tahrir.pdf"
        ),
        (
            subject_id,
            "8-sinf Davlat va huquq asoslari",
            "A. Saidov, V. Qo'chqorov",
            "8-sinf",
            None,
            "Davlat va jamiyat qurilishi, davlatning kelib chiqishi, boshqaruv va tuzilish shakllari, huquq normalari strukturasi hamda huquqiy ong.",
            json.dumps([
                {"title": "1-bob. Davlat tushunchasi va uning belgilari", "summary": "Davlat kelib chiqishi nazariyalari, suverenitet, davlatning ichki va tashqi vazifalari."},
                {"title": "2-bob. Davlat shakllari va siyosiy rejim", "summary": "Monarxiya va respublika, unitar va federatsiya, demokratik va antidemokratik rejimlar."},
                {"title": "3-bob. Huquq tushunchasi va huquq normalari", "summary": "Huquq va axloq, gipoteza, dispozitsiya va sanksiya, huquq manbalari."},
                {"title": "4-bob. Huquqiy munosabatlar va yuridik javobgarlik", "summary": "Huquqiy munosabat elementlari, yuridik faktlar va huquqbuzarliklar."}
            ]),
            None,
            "/uploads/textbooks/davlat_va_huquq_asoslari_8_uzb.pdf"
        ),
        (
            subject_id,
            "9-sinf Davlat va huquq asoslari",
            "A. Saidov, U. Tojixonov",
            "9-sinf",
            None,
            "Fuqarolik huquqi asoslari, mulk huquqi, shartnomalar, oila huquqi va nikoh munosabatlari, yangi Mehnat kodeksi qoidalari.",
            json.dumps([
                {"title": "1-bob. Fuqarolik huquqi va muomala layoqati", "summary": "Huquq layoqati va muomala layoqati, emansipatsiya, mulkdorlik huquqi va meros."},
                {"title": "2-bob. Majburiyatlar va fuqarolik-huquqiy shartnomalar", "summary": "Oldi-sotdi, hadya, ijara, da'vo muddatlari va zararni qoplash."},
                {"title": "3-bob. Oila huquqi va nikoh munosabatlari", "summary": "Nikoh yoshi, nikoh shartnomasi, er-xotin mulki, aliment majburiyatlari."},
                {"title": "4-bob. Mehnat huquqi va voyaga yetmaganlar mehnati", "summary": "Mehnat shartnomasi, ish vaqti, ta'tillar, mehnat intizomi va jazolari."}
            ]),
            None,
            "/uploads/textbooks/davlat_va_huquq_asoslari_9_uzb.pdf"
        ),
        (
            subject_id,
            "10-sinf Davlat va huquq asoslari",
            "O'. Tojixonov, A. Saidov",
            "10-sinf",
            None,
            "Ma'muriy huquq va javobgarlik, Jinoyat huquqi prinsiplari, jinoiy javobgarlik yoshi, jazo turlari hamda Ekologiya huquqi normalari.",
            json.dumps([
                {"title": "1-bob. Ma'muriy huquq va ma'muriy huquqbuzarlik", "summary": "Ma'muriy javobgarlik yoshi, jazo turlari, jarima va ma'muriy qamoq."},
                {"title": "2-bob. Jinoyat huquqi tushunchasi va jinoyat tarkibi", "summary": "Obyekt, obyektiv tomon, subyekt va subyektiv tomon, qasd va ehtiyotsizlik."},
                {"title": "3-bob. Jinoiy javobgarlik va jazo choralari", "summary": "14 va 16 yoshdan javobgarlik, zaruriy mudofaa, jinoiy ishtirokchilik va jazo turlari."},
                {"title": "4-bob. Ekologiya huquqi va tabiatni muhofaza qilish", "summary": "Qizil kitob, tabiiy resurslardan foydalanish, brakonyerlikka qarshi kurash."}
            ]),
            None,
            "/uploads/textbooks/davlat_va_huquq_asoslari_10_uzb.pdf"
        ),
        (
            subject_id,
            "11-sinf Davlat va huquq asoslari",
            "A. Saidov, B. Ahmedov",
            "11-sinf",
            None,
            "Xalqaro huquq, Inson huquqlari umumjahon deklaratsiyasi, Sud hokimiyati va odil sudlov, Prokuratura, Advokatura va huquqni muhofaza qiluvchi organlar.",
            json.dumps([
                {"title": "1-bob. Xalqaro huquq va inson huquqlari", "summary": "BMT nizomi, Inson huquqlari deklaratsiyasi, Bola huquqlari to'g'risidagi konvensiya."},
                {"title": "2-bob. Sud hokimiyati va odil sudlov kafolatlari", "summary": "Konstitutsiyaviy sud, Oliy sud, sudyalar mustaqilligi, apellyatsiya va kassatsiya."},
                {"title": "3-bob. Prokuratura va tergov organlari", "summary": "Bosh prokuror nazorati, davlat ayblovi, qonuniylikni ta'minlash."},
                {"title": "4-bob. Advokatura va inson huquqlari himoyasi", "summary": "Advokatlik faoliyati, malakali yuridik yordam, Ombudsman va huquqiy institutlar."}
            ]),
            None,
            "/uploads/textbooks/davlat_va_huquq_asoslari_11_uzb.pdf"
        )
    ]

    for b in books_data:
        c.execute("SELECT id FROM textbooks WHERE subject_id = ? AND title = ?", (b[0], b[1]))
        row = c.fetchone()
        if not row:
            c.execute("""
                INSERT INTO textbooks (subject_id, title, author, grade, cover_image, summary, chapters, uploaded_by, file_url)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, b)

    conn.commit()
    print("Huquq fani va 5 ta rasmiy darsliklar (8-11 sinf + Konstitutsiya) bazaga muvaffaqiyatli saqlandi.")
    return subject_id

if __name__ == "__main__":
    conn = sqlite3.connect(DB_PATH)
    create_huquq_subject_and_books(conn)
    conn.close()
