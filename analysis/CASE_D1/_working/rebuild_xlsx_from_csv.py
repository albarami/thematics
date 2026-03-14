"""Rebuild participant xlsx workbooks from the corrected participant_summary CSV."""
import csv
from pathlib import Path

try:
    from openpyxl import Workbook
except ImportError:
    print("ERROR: openpyxl not installed. Run: pip install openpyxl")
    raise SystemExit(1)

PKG = Path(r"c:\Users\baram\OneDrive\Desktop\themnatic\analysis\CASE_D1\OUTWARD_FACING_PACKAGE")
CSV_PATH = PKG / "CASE_D1_participant_summary.csv"

rows = list(csv.reader(CSV_PATH.open(encoding="utf-8-sig")))
header = rows[0]
data = [r for r in rows[1:] if any(cell.strip() for cell in r)]

print(f"CSV rows: {len(data)}")
mods = sum(1 for r in data if r[3] == "moderator")
print(f"Moderator rows: {mods}")
has_m02 = any(r[0] == "D1_M02" for r in data)
print(f"D1_M02 present: {has_m02}")

for xlsx_name in ["CASE_D1_participant_workbook.xlsx", "participant_summary_anonymized.xlsx"]:
    wb = Workbook()
    ws = wb.active
    ws.title = "Participant Summary"
    ws.append(header)
    for r in data:
        ws.append(r)
    out = PKG / xlsx_name
    wb.save(out)
    print(f"Wrote {out.name}: {len(data)} data rows")

print("Done.")
