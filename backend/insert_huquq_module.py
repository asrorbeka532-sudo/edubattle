# -*- coding: utf-8 -*-
"""
EduBattle: Huquq fanini to'liq bazaga kiritish skripti.
- Fan: Huquq (id: 9, code: law, icon: ⚖️)
- Darsliklar: 8, 9, 10, 11-sinf Davlat va huquq asoslari darsliklari hamda Yangi Konstitutsiya kitobi
- Testlar: 216 ta rasmiy savol (Blitz va mavzulashtirilgan testlar uchun)
"""

import sqlite3
import json
import os
import random

DB_PATH = os.path.join(os.path.dirname(__file__), "edubattle.db")

from huquq_questions_data import HUQUQ_QUESTIONS
from huquq_questions_part2 import HUQUQ_QUESTIONS_PART2
from huquq_questions_part3 import HUQUQ_QUESTIONS_PART3

def insert_all_huquq():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # 1. Subject creation / update
    c.execute("SELECT id FROM subjects WHERE code = 'law' OR id = 9")
    row = c.fetchone()
    if row:
        subject_id = row[0]
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

    print(f"1. Subject 'Huquq' (id={subject_id}) tasdiqlandi.")

    # 2. Textbooks
    books_data = [
        (
            subject_id,
            "O'zbekiston Respublikasi Konstitutsiyasi (Yangi tahrir)",
            "Oliy Majlis va O'zbekiston xalqi",
            "Barcha sinflar",
            None,
            "2023-yil 30-apreldagi referendumda umumxalq ovozi bilan qabul qilingan yangi tahrirdagi O'zbekiston Respublikasi Konstitutsiyasi. 6 bo'lim, 27 bob va 155 moddadan iborat oliy yuridik kuchga ega Bosh qomus.",
            json.dumps([
                {"title": "1-bo'lim. Asosiy prinsiplar (1-18 moddalar)", "summary": "Davlat suvereniteti, xalq hokimiyatchiligi, Konstitutsiya va qonun ustunligi hamda tinchliksevar tashqi siyosat."},
                {"title": "2-bo'lim. Inson va fuqaroning asosiy huquqlari, erkinliklari va burchlari (19-64 moddalar)", "summary": "Fuqarolik, shaxsiy, siyosiy, iqtisodiy, ijtimoiy, madaniy va ekologik huquqlar hamda konstitutsiyaviy burchlar."},
                {"title": "3-bo'lim. Jamiyat va shaxs (65-82 moddalar)", "summary": "Bozor iqtisodiyoti asoslari, jamoat birlashmalari, erkin OAV, oila va yoshlarni har tomonlama qo'llab-quvvatlash."},
                {"title": "4-bo'lim. Ma'muriy-hududiy va davlat tuzilishi (83-90 moddalar)", "summary": "Hududiy yaxlitlik va Qoraqalpog'iston Respublikasining Konstitutsiyaviy maqomi."},
                {"title": "5-bo'lim. Davlat hokimiyatining tashkil etilishi (91-153 moddalar)", "summary": "Oliy Majlis Qonunchilik palatasi va Senati, Prezident, Vazirlar Mahkamasi, Mahalliy hokimiyat, Mustaqil Sud hokimiyati va Prokuratura."},
                {"title": "6-bo'lim. Konstitutsiyaga o'zgartirish kiritish tartibi (154-155 moddalar)", "summary": "Konstitutsiyaga tuzatishlar kiritish va boshqaruv shakli hamda hududiy yaxlitlikning daxlsizligi."}
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
            "Umumta'lim maktablarining 8-sinfi uchun darslik: Davlatning kelib chiqishi, suverenitet, boshqaruv va davlat tuzilishi shakllari, huquq normalari strukturasi, yuridik faktlar va huquqiy madaniyat.",
            json.dumps([
                {"title": "1-bob. Davlat tushunchasi va belgilari", "summary": "Davlatning kelib chiqishi nazariyalari, ommaviy hokimiyat, davlat suvereniteti va uning asosiy vazifalari."},
                {"title": "2-bob. Davlat shakllari va siyosiy rejimlar", "summary": "Monarxiya va respublika, unitar va federatsiya, demokratik va antidemokratik siyosiy rejimlar."},
                {"title": "3-bob. Huquq tushunchasi va huquqiy normalar", "summary": "Huquq va axloq munosabati, gipoteza, dispozitsiya, sanksiya va huquq manbalari."},
                {"title": "4-bob. Huquqiy munosabatlar va qonuniylik", "summary": "Huquqiy munosabat elementlari, yuridik faktlar (voqea va harakat), huquqiy ong va huquqiy madaniyat."}
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
            "Umumta'lim maktablarining 9-sinfi uchun darslik: Fuqarolik huquqi, muomala layoqati, emansipatsiya, mulkdorlik huquqi, Oila huquqi va nikoh munosabatlari, yangi Mehnat kodeksi asoslari.",
            json.dumps([
                {"title": "1-bob. Fuqarolik huquqi asoslari", "summary": "Huquq layoqati va muomala layoqati, emansipatsiya, mulk huquqi, oldi-sotdi va hadya shartnomalari, da'vo muddatlari."},
                {"title": "2-bob. Oila huquqi va nikoh munosabatlari", "summary": "Nikoh yoshi, nikoh tuzish tartibi, nikoh shartnomasi, er-xotin mulki, aliment munosabatlari va farzandlikka olish."},
                {"title": "3-bob. Yangi Mehnat kodeksi asoslari", "summary": "Mehnat shartnomasi tuzish, sinov muddati, haftalik ish vaqti, ta'tillar va mehnat intizomi choralari."},
                {"title": "4-bob. Voyaga yetmaganlarning mehnat huquqlari", "summary": "15-18 yoshli o'smirlarning qisqartirilgan ish vaqti, taqiqlangan ishlar va majburiy tibbiy ko'riklar."}
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
            "Umumta'lim maktablarining 10-sinfi uchun darslik: Ma'muriy huquq, ma'muriy javobgarlik va jazo turlari, Jinoyat huquqi, jinoyat tarkibi, jinoiy javobgarlik yoshi hamda Ekologiya huquqi.",
            json.dumps([
                {"title": "1-bob. Ma'muriy huquq va javobgarlik", "summary": "Ma'muriy huquqbuzarlik tushunchasi, 16 yoshdan javobgarlik, ma'muriy jarimalar va 15 sutkagacha ma'muriy qamoq."},
                {"title": "2-bob. Jinoyat huquqi asoslari", "summary": "Jinoyat toifalari, jinoyat tarkibining 4 elementi (obyekt, obyektiv tomon, subyekt, subyektiv tomon), qasd va ehtiyotsizlik."},
                {"title": "3-bob. Jinoiy javobgarlik va jazo tizimi", "summary": "14 va 16 yoshdan javobgarlik, zaruriy mudofaa, jinoiy ishtirokchilik turlari, ozodlikdan mahrum qilish va umrbod qamoq cheklovlari."},
                {"title": "4-bob. Ekologiya huquqi va atrof-muhit muhofazasi", "summary": "Tabiatni muhofaza qilish to'g'risidagi qonun, Qizil kitob, tabiiy resurslar va ekologik huquqbuzarliklar uchun javobgarlik."}
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
            "Umumta'lim maktablarining 11-sinfi uchun darslik: Xalqaro huquq, Inson huquqlari umumjahon deklaratsiyasi, Sud hokimiyati va odil sudlov kafolatlari, Prokuratura va Advokatura institutlari.",
            json.dumps([
                {"title": "1-bob. Xalqaro huquq va inson huquqlari", "summary": "BMT Nizomi, Inson huquqlari umumjahon deklaratsiyasi (1948), Bola huquqlari to'g'risidagi konvensiya va xalqaro gumanitar huquq."},
                {"title": "2-bob. Sud hokimiyati va odil sudlov", "summary": "Konstitutsiyaviy sud, Oliy sud, sudyalarning mustaqilligi, sud ochiqligi (oshkoraligi) va sud qarorlarining majburiyligi."},
                {"title": "3-bob. Prokuratura va tergov organlari", "summary": "Qonunlar ijrosi ustidan Bosh prokuror nazorati, davlat ayblovi va sud qarorlari ijrosi (MIB)."},
                {"title": "4-bob. Advokatura va fuqarolik institutlari", "summary": "Professional yuridik yordam, advokatlik siri, Ombudsman, Bolalar ombudsmani va Korrupsiyaga qarshi kurashish agentligi."}
            ]),
            None,
            "/uploads/textbooks/davlat_va_huquq_asoslari_11_uzb.pdf"
        )
    ]

    for b in books_data:
        c.execute("SELECT id FROM textbooks WHERE subject_id = ? AND title = ?", (b[0], b[1]))
        exist = c.fetchone()
        if exist:
            c.execute("""
                UPDATE textbooks 
                SET author = ?, grade = ?, summary = ?, chapters = ?, file_url = ?
                WHERE id = ?
            """, (b[2], b[3], b[5], b[6], b[8], exist[0]))
        else:
            c.execute("""
                INSERT INTO textbooks (subject_id, title, author, grade, cover_image, summary, chapters, uploaded_by, file_url)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, b)

    print("2. 5 ta rasmiy darslik saqlandi/yangilandi.")

    # 3. Questions: Combine and Shuffle
    all_raw = HUQUQ_QUESTIONS + HUQUQ_QUESTIONS_PART2 + HUQUQ_QUESTIONS_PART3
    print(f"Jami manba savollari: {len(all_raw)}")

    # Clear existing questions for subject 9 to avoid duplicates
    c.execute("DELETE FROM questions WHERE subject_id = ?", (subject_id,))

    inserted_count = 0
    # Seed random for repeatable balance across options
    rng = random.Random(42)

    for item in all_raw:
        ch_title, q_text, raw_opts, correct_idx, expl, grade, diff = item
        correct_answer = raw_opts[correct_idx]

        # Shuffle options so the correct answer is evenly distributed across 0, 1, 2, 3
        shuffled = list(raw_opts)
        rng.shuffle(shuffled)
        new_corr = shuffled.index(correct_answer)

        c.execute("""
            INSERT INTO questions (subject_id, grade, chapter_title, question_text, options, correct_index, explanation, difficulty, created_by, group_id)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, NULL, NULL)
        """, (
            subject_id,
            grade,
            ch_title,
            q_text,
            json.dumps(shuffled, ensure_ascii=False),
            new_corr,
            expl,
            diff
        ))
        inserted_count += 1

    conn.commit()
    conn.close()

    print(f"3. Huquq fanidan bazaga {inserted_count} ta rasmiy test muvaffaqiyatli kiritildi!")
    return inserted_count

if __name__ == "__main__":
    count = insert_all_huquq()
    print("Tayyor: Jami Huquq testlari soni:", count)
