from __future__ import annotations

from io import BytesIO

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill

from rash_bot.database import SubmissionRecord, TestRecord


GRADE_COLORS = {
    "A+": "C6EFCE",
    "A": "D9EAD3",
    "B+": "DDEBF7",
    "B": "E8F1FA",
    "C+": "FFF2CC",
    "C": "FCE4D6",
    "Darajasiz": "F8CBAD",
}


def build_excel_report(
    test: TestRecord,
    submissions: list[SubmissionRecord],
) -> bytes:
    """
    Generate a 3-sheet Excel report (.xlsx) in memory:
      1. Natijalar (Rasch reytingi)
      2. Savollar tahlili (Item difficulty & % correct)
      3. Javoblar matritsasi (0/1 binary matrix)
    """
    wb = Workbook()

    header_fill = PatternFill("solid", fgColor="1F4E78")
    header_font = Font(bold=True, color="FFFFFF")
    center = Alignment(horizontal="center", vertical="center")

    # ---------- Sheet 1: Natijalar ----------
    ws1 = wb.active
    ws1.title = "Rasch Natijalar"

    ws1.append([f"Test: {test.title} (Kod: {test.code})"])
    ws1.merge_cells("A1:I1")
    ws1["A1"].font = Font(bold=True, size=13)
    ws1.append(
        [
            f"Jami savollar: {test.total_questions} "
            f"(Yopiq: {test.closed_count}, Ochiq: {test.open_count}) | "
            f"Ishtirokchilar: {len(submissions)}"
        ]
    )
    ws1.merge_cells("A2:I2")
    ws1.append([])

    headers1 = [
        "O'rin",
        "Ism Familiya",
        "Username",
        "To'g'ri",
        "Foiz (%)",
        "Logit (θ)",
        "Rasch Ball (T)",
        "Daraja",
        "Xato savollar",
    ]
    ws1.append(headers1)
    for col_idx in range(1, len(headers1) + 1):
        cell = ws1.cell(row=4, column=col_idx)
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = center

    sorted_subs = sorted(
        submissions,
        key=lambda s: (
            s.rasch_rank if s.rasch_rank is not None else 999999,
            -s.raw_score,
            s.id,
        ),
    )

    for idx, sub in enumerate(sorted_subs, start=1):
        pct = round(100.0 * sub.raw_score / max(test.total_questions, 1), 1)
        wrong_str = ", ".join(str(x) for x in sub.wrong_numbers) if sub.wrong_numbers else "Yo'q"
        row_vals = [
            sub.rasch_rank if sub.rasch_rank is not None else idx,
            sub.full_name,
            f"@{sub.username}" if sub.username else "-",
            f"{sub.raw_score}/{test.total_questions}",
            pct,
            sub.rasch_theta if sub.rasch_theta is not None else "-",
            sub.rasch_t_score if sub.rasch_t_score is not None else "-",
            sub.rasch_grade or "-",
            wrong_str,
        ]
        ws1.append(row_vals)
        row_num = ws1.max_row
        for c in (1, 4, 5, 6, 7, 8):
            ws1.cell(row=row_num, column=c).alignment = center
        grade = sub.rasch_grade or ""
        if grade in GRADE_COLORS:
            grade_cell = ws1.cell(row=row_num, column=8)
            grade_cell.fill = PatternFill("solid", fgColor=GRADE_COLORS[grade])
            grade_cell.font = Font(bold=True)

    col_widths_1 = [8, 28, 18, 12, 11, 12, 15, 13, 36]
    for i, width in enumerate(col_widths_1, start=1):
        ws1.column_dimensions[ws1.cell(row=4, column=i).column_letter].width = width

    # ---------- Sheet 2: Savollar tahlili ----------
    ws2 = wb.create_sheet(title="Savollar Tahlili")
    headers2 = [
        "Savol №",
        "Turi",
        "To'g'ri kalit",
        "To'g'ri yechganlar",
        "Foiz (%)",
        "Qiyinlik (β logit)",
        "Toifa",
    ]
    ws2.append(headers2)
    for col_idx in range(1, len(headers2) + 1):
        cell = ws2.cell(row=1, column=col_idx)
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = center

    items_map: dict[int, dict] = {}
    if test.rasch_summary and "items" in test.rasch_summary:
        for item in test.rasch_summary["items"]:
            items_map[int(item["item_number"])] = item

    total_subs = max(len(submissions), 1)
    for q in test.questions:
        info = items_map.get(q.number)
        if info:
            correct_cnt = info["correct_count"]
            pct = round(100.0 * float(info["p_value"]), 1)
            beta_val = info["beta"]
            diff_label = info["difficulty_label"]
        else:
            correct_cnt = sum(s.binary[q.number - 1] for s in submissions if len(s.binary) >= q.number)
            pct = round(100.0 * correct_cnt / total_subs, 1)
            beta_val = "-"
            diff_label = "-"

        ws2.append(
            [
                q.number,
                "Yopiq" if q.q_type == "closed" else "Ochiq",
                q.display_key,
                f"{correct_cnt}/{len(submissions)}",
                pct,
                beta_val,
                diff_label,
            ]
        )
        for c in (1, 2, 3, 4, 5, 6, 7):
            ws2.cell(row=ws2.max_row, column=c).alignment = center

    col_widths_2 = [10, 12, 18, 18, 12, 18, 14]
    for i, width in enumerate(col_widths_2, start=1):
        ws2.column_dimensions[ws2.cell(row=1, column=i).column_letter].width = width

    # ---------- Sheet 3: Javoblar matritsasi ----------
    ws3 = wb.create_sheet(title="Matritsa (0-1)")
    headers3 = ["Ism Familiya"] + [f"Q{q.number}" for q in test.questions] + ["Jami"]
    ws3.append(headers3)
    for col_idx in range(1, len(headers3) + 1):
        cell = ws3.cell(row=1, column=col_idx)
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = center

    for sub in sorted_subs:
        ws3.append([sub.full_name] + sub.binary + [sub.raw_score])
    ws3.column_dimensions["A"].width = 28

    output = BytesIO()
    wb.save(output)
    return output.getvalue()
