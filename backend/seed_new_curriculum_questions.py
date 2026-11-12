# -*- coding: utf-8 -*-
"""
EduBattle - 2020-2023 Yangi darsliklar asosidagi savollar bankini bazaga kiritish skripti.
Barcha 8 ta umumta'lim fani (50 tadan = 400 ta savol) yangi 2020-2023 darsliklariga asoslangan holda yangilanadi.
9-fan (Huquq - 2023 Yangi Konstitutsiya asosidagi 216 ta savol) saqlab qolinadi.
Jami: 616 ta mukammal va to'liq savollar banki.
"""

import sys
import os
import sqlite3
import json
import random

# Workspace yo'lini qo'shish
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
WORKSPACE_ROOT = os.path.abspath(os.path.join(CURRENT_DIR, ".."))
if WORKSPACE_ROOT not in sys.path:
    sys.path.insert(0, WORKSPACE_ROOT)

from backend.curriculum_questions_math_physics import MATEMATIKA_QUESTIONS, FIZIKA_QUESTIONS
from backend.curriculum_questions_chem_bio import KIMYO_QUESTIONS, BIOLOGIYA_QUESTIONS
from backend.curriculum_questions_lang_hist import ONA_TILI_ADABIYOT_QUESTIONS, TARIX_QUESTIONS
from backend.curriculum_questions_eng_it import INGLIZ_TILI_QUESTIONS, INFORMATIKA_QUESTIONS

DB_PATH = os.path.join(CURRENT_DIR, "edubattle.db")
BUNDLED_PATH = os.path.join(CURRENT_DIR, "bundled_questions.json")

def process_and_distribute_options(questions_list, seed=42):
    """
    Savol variantlarini aralashtiradi, to'g'ri javobni (dastlab 0-indeksdagi)
    har xil pozitsiyalarga (A, B, C, D) taqsimlaydi va correct_index ni to'g'rilaydi.
    """
    rng = random.Random(seed)
    processed = []
    
    for q in questions_list:
        orig_opts = list(q["options"])
        correct_text = orig_opts[q["correct_index"]]
        
        # Variantlarni aralashtirish
        shuffled = list(orig_opts)
        rng.shuffle(shuffled)
        new_correct_idx = shuffled.index(correct_text)
        
        item = {
            "subject_id": q["subject_id"],
            "grade": q["grade"],
            "chapter_title": q["chapter_title"],
            "question_text": q["question_text"],
            "options": json.dumps(shuffled, ensure_ascii=False),
            "correct_index": new_correct_idx,
            "explanation": q["explanation"],
            "difficulty": q.get("difficulty", "orta")
        }
        processed.append(item)
        
    return processed

def main():
    print("=" * 60)
    print("EduBattle yangi darsliklar (2020-2023) savollar bankini yuklash...")
    print("=" * 60)
    
    # 8 ta fan savollari to'plami
    subject_question_map = {
        1: ("Matematika", MATEMATIKA_QUESTIONS),
        2: ("Fizika", FIZIKA_QUESTIONS),
        3: ("Kimyo", KIMYO_QUESTIONS),
        4: ("Biologiya", BIOLOGIYA_QUESTIONS),
        5: ("Ona tili va Adabiyot", ONA_TILI_ADABIYOT_QUESTIONS),
        6: ("Tarix", TARIX_QUESTIONS),
        7: ("Ingliz tili", INGLIZ_TILI_QUESTIONS),
        8: ("Informatika va IT", INFORMATIKA_QUESTIONS)
    }
    
    all_new_questions = []
    
    for sub_id, (sub_name, q_list) in subject_question_map.items():
        count = len(q_list)
        print(f"Fan {sub_id} ({sub_name}): {count} ta savol tayyorlandi.")
        if count != 50:
            raise ValueError(f"Xatolik: Fan {sub_name} savollari soni {count} ta, 50 ta bo'lishi kerak!")
        processed = process_and_distribute_options(q_list, seed=100 + sub_id)
        all_new_questions.extend(processed)
        
    print(f"\nJami 8 ta fandan {len(all_new_questions)} ta yangi tahrirdagi savol tayyorlandi.")
    
    # Bazaga yozish
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    
    # 9-fan (Huquq) dan tashqari eski savollarni o'chirish
    cur.execute("DELETE FROM questions WHERE subject_id != 9")
    deleted_count = cur.rowcount
    print(f"Eski savollar o'chirildi: {deleted_count} ta.")
    
    # Yangi savollarni kiritish
    insert_sql = """
        INSERT INTO questions (subject_id, grade, chapter_title, question_text, options, correct_index, explanation, difficulty)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """
    for q in all_new_questions:
        cur.execute(insert_sql, (
            q["subject_id"],
            q["grade"],
            q["chapter_title"],
            q["question_text"],
            q["options"],
            q["correct_index"],
            q["explanation"],
            q["difficulty"]
        ))
        
    conn.commit()
    print(f"{len(all_new_questions)} ta yangi savol muvaffaqiyatli bazaga kiritildi.")
    
    # Yakuniy statistika
    print("\n--- Bazadagi jami savollar statistikasi ---")
    cur.execute("""
        SELECT s.id, s.name, COUNT(q.id)
        FROM subjects s
        LEFT JOIN questions q ON s.id = q.subject_id
        GROUP BY s.id, s.name
        ORDER BY s.id
    """)
    totals = cur.fetchall()
    total_q = 0
    for sid, sname, count in totals:
        print(f"[{sid}] {sname}: {count} ta savol")
        total_q += count
    print(f"UMUMIY BAZADAGI SAVOLLAR: {total_q} ta.")
    
    # Barcha savollarni bundled_questions.json ga eksport qilish (zaxira va Render deployment uchun)
    cur.execute("SELECT subject_id, grade, chapter_title, question_text, options, correct_index, explanation, difficulty FROM questions ORDER BY subject_id, id")
    all_db_rows = cur.fetchall()
    bundled_data = []
    for r in all_db_rows:
        bundled_data.append({
            "subject_id": r[0],
            "grade": r[1],
            "chapter_title": r[2],
            "question_text": r[3],
            "options": json.loads(r[4]) if isinstance(r[4], str) else r[4],
            "correct_index": r[5],
            "explanation": r[6],
            "difficulty": r[7]
        })
        
    with open(BUNDLED_PATH, "w", encoding="utf-8") as f:
        json.dump(bundled_data, f, ensure_ascii=False, indent=2)
    print(f"Barcha {len(bundled_data)} ta savol '{BUNDLED_PATH}' fayliga saqlandi.")
    
    conn.close()
    print("\nSavollar bankini yangilash to'liq yakunlandi!")

if __name__ == "__main__":
    main()
