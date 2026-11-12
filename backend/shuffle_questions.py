# -*- coding: utf-8 -*-
import sqlite3
import json
import random
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "edubattle.db")

def shuffle_all_questions_in_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("SELECT id, subject_id, question_text, options, correct_index FROM questions")
    rows = c.fetchall()

    rng = random.Random(12345)
    updated = 0

    for r in rows:
        qid, sid, qtext, opt_str, corr_idx = r
        try:
            opts = json.loads(opt_str)
            if isinstance(opts, list) and len(opts) == 4 and 0 <= corr_idx < 4:
                corr_text = opts[corr_idx]

                new_opts = list(opts)
                rng.shuffle(new_opts)
                new_idx = new_opts.index(corr_text)

                c.execute(
                    "UPDATE questions SET options = ?, correct_index = ? WHERE id = ?",
                    (json.dumps(new_opts, ensure_ascii=False), new_idx, qid)
                )
                updated += 1
        except Exception as e:
            print(f"Error on question {qid}:", e)

    conn.commit()

    print(f"Barcha {updated} ta test variantlari mukammal aralashtirildi (A, B, C, D ga teng taqsimlandi).")

    c.execute("SELECT correct_index, count(*) FROM questions GROUP BY correct_index ORDER BY correct_index")
    for r in c.fetchall():
        print(f"Variant {chr(65+r[0])} (indeks {r[0]}): {r[1]} ta savol ({r[1]*100/updated:.1f}%)")

    conn.close()

if __name__ == "__main__":
    shuffle_all_questions_in_db()
