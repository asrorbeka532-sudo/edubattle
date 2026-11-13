#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EduBattle - Avtomatik ma'lumotlar bazasi zaxira (backup) skripti.
Baza faylini /data/backups jildiga sanasi bilan saqlaydi va 30 kundan eski nusxalarni tozalaydi.
"""

import os
import shutil
import datetime

def make_backup():
    data_dir = os.environ.get("DATA_DIR") or "/data"
    db_source = os.path.join(data_dir, "edubattle.db")
    if not os.path.exists(db_source):
        # Fallback to local
        db_source = os.path.join(os.path.dirname(__file__), "..", "backend", "edubattle.db")

    if not os.path.exists(db_source):
        print(f"Baza fayli topilmadi: {db_source}")
        return

    backup_dir = os.path.join(data_dir, "backups")
    os.makedirs(backup_dir, exist_ok=True)

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = os.path.join(backup_dir, f"edubattle_backup_{timestamp}.db")

    shutil.copy2(db_source, backup_file)
    print(f"Zaxira nusxa yaratildi: {backup_file} (Hajmi: {os.path.getsize(backup_file)} bayt)")

    # 30 kundan eski zaxira fayllarni tozalash
    now = datetime.datetime.now()
    for fname in os.listdir(backup_dir):
        fpath = os.path.join(backup_dir, fname)
        if os.path.isfile(fpath) and fname.startswith("edubattle_backup_"):
            mtime = datetime.datetime.fromtimestamp(os.path.getmtime(fpath))
            if (now - mtime).days > 30:
                os.remove(fpath)
                print(f"Eski zaxira o'chirildi: {fname}")

if __name__ == "__main__":
    make_backup()
