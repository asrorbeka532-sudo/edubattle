import json
import random
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from database import get_db

def make_q(subject_id, chapter_title, question_text, correct_answer, wrong_answers, explanation="", difficulty="orta", grade="9-sinf"):
    # Clean inputs
    correct_str = str(correct_answer).strip()
    wrongs = [str(w).strip() for w in wrong_answers if str(w).strip() != correct_str]
    
    # If not enough distinct wrong answers, generate unique placeholders
    idx = 1
    while len(wrongs) < 3:
        cand = f"Javob {idx}"
        if cand != correct_str and cand not in wrongs:
            wrongs.append(cand)
        idx += 1
    wrongs = wrongs[:3]
    
    # Shuffle options
    all_opts = [correct_str] + wrongs
    random.shuffle(all_opts)
    correct_idx = all_opts.index(correct_str)
    
    if not explanation:
        explanation = f"To'g'ri javob: {correct_str}"
        
    return (
        subject_id,
        chapter_title,
        question_text,
        json.dumps(all_opts, ensure_ascii=False),
        correct_idx,
        explanation,
        difficulty,
        grade
    )

def insert_questions(q_list, commit=True):
    conn = get_db()
    c = conn.cursor()
    c.executemany("""
        INSERT INTO questions (subject_id, chapter_title, question_text, options, correct_index, explanation, difficulty, grade)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, q_list)
    if commit:
        conn.commit()
    inserted = len(q_list)
    conn.close()
    return inserted
