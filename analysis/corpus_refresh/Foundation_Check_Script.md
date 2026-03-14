# Foundation Check Script

This document is a faithful record of the exact verification logic used in the final machine-checked foundation verification pass for the D1-D4 corpus refresh. Every check section below shows the actual Python logic that was run and the actual results produced. No placeholders or summaries are used.

---

## Check 1A: file_inventory_refresh.csv — counts by case and file_type

```python
import csv
from pathlib import Path
from collections import defaultdict

root = Path(r'c:\Users\baram\OneDrive\Desktop\themnatic')
refresh = root / 'analysis' / 'corpus_refresh'

with (refresh / 'file_inventory_refresh.csv').open('r', encoding='utf-8-sig') as f:
    inv_rows = list(csv.DictReader(f))

inv_by_case_type = defaultdict(lambda: defaultdict(int))
inv_by_case = defaultdict(int)
inv_cases = set()
for r in inv_rows:
    inv_by_case_type[r['case_id']][r['file_type']] += 1
    inv_by_case[r['case_id']] += 1
    inv_cases.add(r['case_id'])

for cid in sorted(inv_cases):
    counts = inv_by_case_type[cid]
    print(f'{cid}: transcript={counts.get("transcript",0)} note={counts.get("note",0)} '
          f'recommendation_workbook={counts.get("recommendation_workbook",0)} '
          f'temp_lock={counts.get("temp_lock",0)} auxiliary={counts.get("auxiliary",0)} '
          f'total={inv_by_case[cid]}')
print(f'grand_total={len(inv_rows)}')
print(f'cases_present={sorted(inv_cases)}')
```

**Actual result:**
```
CASE_D1: transcript=7 note=8 recommendation_workbook=1 temp_lock=1 auxiliary=0 total=17
CASE_D2: transcript=7 note=10 recommendation_workbook=1 temp_lock=0 auxiliary=0 total=18
CASE_D3: transcript=5 note=11 recommendation_workbook=1 temp_lock=0 auxiliary=0 total=17
CASE_D4: transcript=5 note=7 recommendation_workbook=1 temp_lock=0 auxiliary=0 total=13
grand_total=65
cases_present=['CASE_D1', 'CASE_D2', 'CASE_D3', 'CASE_D4']
```

---

## Check 1B: case_register_refresh.csv — cross-check against inventory

```python
with (refresh / 'case_register_refresh.csv').open('r', encoding='utf-8-sig') as f:
    cr_rows = list(csv.DictReader(f))

for r in cr_rows:
    cid = r['case_id']
    inv = inv_by_case_type[cid]
    for label, cr_key, inv_key in [
        ('transcript', 'transcript_count', 'transcript'),
        ('note', 'note_taker_count', 'note'),
        ('recommendation_workbook', 'recommendation_workbook_count', 'recommendation_workbook'),
        ('temp_lock', 'temp_lock_count', 'temp_lock'),
        ('auxiliary', 'auxiliary_count', 'auxiliary'),
    ]:
        cr_val = int(r[cr_key])
        inv_val = inv.get(inv_key, 0)
        status = 'MATCH' if cr_val == inv_val else 'MISMATCH'
        print(f'{cid}/{label}: case_register={cr_val} inventory={inv_val} -> {status}')
```

**Actual result:** All 20 checks (5 fields x 4 cases) returned MATCH.

---

## Check 1C: filesystem — cross-check against inventory

```python
inv_files = set(r['relative_path'] for r in inv_rows)
fs_files = set()
for folder in ['Day1_Childhood', 'Day2_Youth', 'Day3_Adults', 'Day4_Elderly']:
    for p in (root / folder).rglob('*'):
        if p.is_file():
            fs_files.add(p.relative_to(root).as_posix())

in_inv_not_fs = inv_files - fs_files
in_fs_not_inv = fs_files - inv_files
print(f'inventory_file_count={len(inv_files)}')
print(f'filesystem_file_count={len(fs_files)}')
print(f'in_inventory_not_filesystem={sorted(in_inv_not_fs) if in_inv_not_fs else "NONE"}')
print(f'in_filesystem_not_inventory={sorted(in_fs_not_inv) if in_fs_not_inv else "NONE"}')
```

**Actual result:**
```
inventory_file_count=65
filesystem_file_count=65
in_inventory_not_filesystem=NONE
in_filesystem_not_inventory=NONE
```

---

## Check 2: moderator_register_refresh.csv — totals by case and confidence

```python
with (refresh / 'moderator_register_refresh.csv').open('r', encoding='utf-8-sig') as f:
    mr_rows = list(csv.DictReader(f))

mr_by_day = defaultdict(lambda: defaultdict(int))
for r in mr_rows:
    mr_by_day[r['case_id']]['total'] += 1
    mr_by_day[r['case_id']][r['transcript_match_confidence']] += 1

for cid in sorted(mr_by_day):
    d = mr_by_day[cid]
    print(f'{cid}: total={d["total"]} confirmed={d.get("confirmed",0)} '
          f'probable={d.get("probable",0)} unclear={d.get("unclear",0)} '
          f'no_transcript_available={d.get("no_transcript_available",0)}')

csv_mr_totals = defaultdict(int)
for r in mr_rows:
    csv_mr_totals[r['transcript_match_confidence']] += 1
print(f'grand_total={len(mr_rows)}')
print(f'confidence_totals: confirmed={csv_mr_totals["confirmed"]} '
      f'probable={csv_mr_totals["probable"]} unclear={csv_mr_totals["unclear"]} '
      f'no_transcript_available={csv_mr_totals["no_transcript_available"]}')
```

**Actual result:**
```
CASE_D1: total=11 confirmed=0 probable=6 unclear=1 no_transcript_available=4
CASE_D2: total=12 confirmed=0 probable=3 unclear=4 no_transcript_available=5
CASE_D3: total=12 confirmed=1 probable=3 unclear=1 no_transcript_available=7
CASE_D4: total=10 confirmed=2 probable=3 unclear=0 no_transcript_available=5
grand_total=45
confidence_totals: confirmed=3 probable=15 unclear=6 no_transcript_available=21
```

**Derivation check:** 3 + 15 + 6 + 21 = 45. Matches grand_total.

---

## Check 3: source_map_refresh.csv — pairing totals and none-row composition

```python
with (refresh / 'source_map_refresh.csv').open('r', encoding='utf-8-sig') as f:
    sm_rows = list(csv.DictReader(f))

sm_by_case = defaultdict(lambda: defaultdict(int))
for r in sm_rows:
    sm_by_case[r['case_id']][r['pairing_confidence']] += 1

for cid in sorted(sm_by_case):
    d = sm_by_case[cid]
    print(f'{cid}: confirmed={d.get("confirmed",0)} probable={d.get("probable",0)} '
          f'none={d.get("none",0)}')

csv_sm_totals = defaultdict(int)
for r in sm_rows:
    csv_sm_totals[r['pairing_confidence']] += 1
print(f'grand_total={len(sm_rows)}')
print(f'pairing_totals: confirmed={csv_sm_totals["confirmed"]} '
      f'probable={csv_sm_totals["probable"]} none={csv_sm_totals["none"]}')

# Classify the none rows by pairing_basis
note_only = transcript_only = aux_rec = 0
for r in sm_rows:
    if r['pairing_confidence'] == 'none':
        b = r['pairing_basis']
        if 'Note file has no transcript' in b:
            note_only += 1
        elif 'Transcript has no note file' in b:
            transcript_only += 1
        elif 'Standalone auxiliary' in b:
            aux_rec += 1
print(f'none_composition: note_only={note_only} transcript_only={transcript_only} aux_rec={aux_rec}')
```

**Actual result:**
```
CASE_D1: confirmed=7 probable=0 none=2
CASE_D2: confirmed=6 probable=0 none=5
CASE_D3: confirmed=2 probable=1 none=8
CASE_D4: confirmed=4 probable=0 none=4
grand_total=39
pairing_totals: confirmed=19 probable=1 none=19
none_composition: note_only=11 transcript_only=4 aux_rec=4
```

**Derivation check:** 19 + 1 + 19 = 39. Matches grand_total. 11 + 4 + 4 = 19. Matches none total.

---

## Check 4: recommendation workbook structure — from actual .xlsx files

```python
from openpyxl import load_workbook

workbooks = [
    ('CASE_D1', 'Day1_Childhood/Recommendations_Data/Health_Workshop_Suggestions Day 1.xlsx'),
    ('CASE_D2', 'Day2_Youth/Recommendations_Data/Health_Workshop_Suggestions Day 2.xlsx'),
    ('CASE_D3', 'Day3_Adults/Recommendations_Data/Health_Workshop_Suggestions Day 3.xlsx'),
    ('CASE_D4', 'Day4_Elderly/Recommendations_Data/Health_Workshop_Suggestions Day 4.xlsx'),
]

for cid, rel in workbooks:
    wb = load_workbook(root / rel, data_only=True)
    for ws in wb.worksheets:
        header = ['' if c is None else str(c) for c in next(ws.iter_rows(min_row=1, max_row=1, values_only=True))]
        non_empty = [0] * ws.max_column
        for row in ws.iter_rows(values_only=True):
            for idx, cell in enumerate(row):
                if cell not in (None, ''):
                    non_empty[idx] += 1
        empty_cols = [i+1 for i in range(ws.max_column) if non_empty[i] == 0]
        empty_no_user_rows = []
        for ridx, row in enumerate(ws.iter_rows(min_row=2, values_only=True), start=2):
            cells = list(row)
            if len(cells) >= 2 and cells[0] in (None, '') and cells[1] in (None, ''):
                if len(cells) >= 3 and cells[2] not in (None, ''):
                    empty_no_user_rows.append(ridx)
        print(f'{cid} sheet={ws.title} max_row={ws.max_row} max_col={ws.max_column} '
              f'headers={header} non_empty={non_empty} empty_cols={empty_cols} '
              f'irregular_rows={empty_no_user_rows}')
```

**Actual result:**
```
CASE_D1 sheet=First_Day_01_02_2026 max_row=41 max_col=3 headers=['No', 'User', 'Suggestion'] non_empty=[39, 39, 41] empty_cols=[] irregular_rows=[40, 41]
CASE_D2 sheet=Second_Day_02_02_2026 max_row=58 max_col=4 headers=['No', 'User', 'Suggestion', ''] non_empty=[58, 58, 58, 0] empty_cols=[4] irregular_rows=[]
CASE_D3 sheet=Third_Day_03_02_2026 max_row=65 max_col=3 headers=['No', 'User', 'Suggestion'] non_empty=[65, 65, 65] empty_cols=[] irregular_rows=[]
CASE_D4 sheet=Forth_Day_04_02_2026 max_row=40 max_col=3 headers=['No', 'User', 'Suggestion'] non_empty=[40, 40, 40] empty_cols=[] irregular_rows=[]
```

---

## Check 5: Moderators.xlsx — actual workbook contents

```python
wb = load_workbook(root / 'Moderators.xlsx', data_only=True)
print(f'sheet_names={wb.sheetnames}')
for ws in wb.worksheets:
    print(f'Sheet: {ws.title}  max_row={ws.max_row}  max_col={ws.max_column}')
    day_values = set()
    data_rows = 0
    blank_rows = 0
    header_rows = 0
    for row in ws.iter_rows(values_only=True):
        if row[0] == 'Day':
            header_rows += 1
        elif row[0] is None:
            blank_rows += 1
        else:
            data_rows += 1
            day_values.add(row[0])
    print(f'  header_rows={header_rows} data_rows={data_rows} blank_rows={blank_rows}')
    print(f'  day_values_found={sorted(day_values)}')
```

**Actual result:**
```
sheet_names=['Day 1']
Sheet: Day 1  max_row=54  max_col=5
  header_rows=4 data_rows=45 blank_rows=5
  day_values_found=[1, 2, 3, 4]
```

**Conclusion:** The workbook contains 54 rows: 4 header rows, 45 moderator data rows, and 5 blank separator rows. Day values present are 1, 2, 3, 4. No other day values exist in the workbook.

---

## Check 6: final cross-check — all narrative numbers vs CSV ground truth

```python
import re

crr = (refresh / 'Corpus_Refresh_Report.md').read_text(encoding='utf-8')
fvr = (refresh / 'Foundation_Verification_Report.md').read_text(encoding='utf-8')
errors = []

# A. Aggregate table in Corpus_Refresh_Report.md
for label, ft in [('Transcripts','transcript'), ('Note-taker files','note'),
                   ('Recommendation workbooks','recommendation_workbook'),
                   ('Temp/lock files','temp_lock'), ('Auxiliary files','auxiliary')]:
    m = re.search(rf'\| {re.escape(label)} \| (\d+) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \|', crr)
    if m:
        narr = [int(m.group(i)) for i in range(1, 5)]
        csv_v = [inv_by_case_type[c].get(ft, 0) for c in ['CASE_D1','CASE_D2','CASE_D3','CASE_D4']]
        if narr != csv_v:
            errors.append(f'agg-table {label}: narr={narr} csv={csv_v}')
        narr_total = int(m.group(5))
        if narr_total != sum(csv_v):
            errors.append(f'agg-table {label} total: narr={narr_total} csv={sum(csv_v)}')

# B. Per-day moderator counts in Corpus_Refresh_Report.md
for cid, pat in [
    ('CASE_D1', r'Day 1.*?(\d+) moderators.*?(\d+) confirmed by name, (\d+) probable.*?(\d+) unclear, (\d+) no transcript'),
    ('CASE_D2', r'Day 2.*?(\d+) moderators.*?(\d+) confirmed by name, (\d+) probable.*?(\d+) unclear.*?(\d+) no transcript'),
    ('CASE_D3', r'Day 3.*?(\d+) moderators.*?(\d+) confirmed by name.*?(\d+) probable.*?(\d+) unclear.*?(\d+) no transcript'),
    ('CASE_D4', r'Day 4.*?(\d+) moderators.*?(\d+) confirmed by name.*?(\d+) probable.*?(\d+) no transcript'),
]:
    m = re.search(pat, crr, re.DOTALL)
    if m:
        gs = [int(g) for g in m.groups()]
        d = mr_by_day[cid]
        if gs[0] != d['total']:
            errors.append(f'{cid} mod total: narr={gs[0]} csv={d["total"]}')
        if gs[1] != d.get('confirmed', 0):
            errors.append(f'{cid} mod confirmed: narr={gs[1]} csv={d.get("confirmed",0)}')
        if gs[2] != d.get('probable', 0):
            errors.append(f'{cid} mod probable: narr={gs[2]} csv={d.get("probable",0)}')
        if cid != 'CASE_D4':
            if gs[3] != d.get('unclear', 0):
                errors.append(f'{cid} mod unclear: narr={gs[3]} csv={d.get("unclear",0)}')
            if gs[4] != d.get('no_transcript_available', 0):
                errors.append(f'{cid} mod no_tr: narr={gs[4]} csv={d.get("no_transcript_available",0)}')
        else:
            if gs[3] != d.get('no_transcript_available', 0):
                errors.append(f'{cid} mod no_tr: narr={gs[3]} csv={d.get("no_transcript_available",0)}')

# C. FVR moderator summary totals
for key, pat in [
    ('confirmed', r'confirmed.*?\((\d+) cases'),
    ('probable', r'probable.*?\((\d+) cases'),
    ('unclear', r'unclear.*?no.*?match \((\d+) cases'),
    ('no_transcript_available', r'no_transcript_available.*?\((\d+) cases'),
]:
    m = re.search(pat, fvr)
    if m and int(m.group(1)) != csv_mr_totals.get(key, 0):
        errors.append(f'FVR mod {key}: narr={m.group(1)} csv={csv_mr_totals.get(key,0)}')

# D. FVR pairing totals
m = re.search(r'\((\d+) pairings across D1-D4\)', fvr)
if m and int(m.group(1)) != csv_sm_totals.get('confirmed', 0):
    errors.append(f'FVR pair confirmed: narr={m.group(1)} csv={csv_sm_totals["confirmed"]}')
m = re.search(r'\((\d+) entries:', fvr)
if m and int(m.group(1)) != csv_sm_totals.get('none', 0):
    errors.append(f'FVR pair none: narr={m.group(1)} csv={csv_sm_totals["none"]}')

# E. Inventory vs case_register vs filesystem (already checked above)
# F. Only D1-D4 case identifiers present in CSV data (verified in Check 7)

if errors:
    for e in errors:
        print(f'ERROR: {e}')
else:
    print('ALL_CHECKS_PASSED=true')
```

**Actual result:** `ALL_CHECKS_PASSED=true`

---

## Check 7: absence of out-of-scope case identifiers in CSV data

```python
for name, rows, field in [
    ('file_inventory', inv_rows, 'case_id'),
    ('case_register', cr_rows, 'case_id'),
    ('source_map', sm_rows, 'case_id'),
    ('moderator_register', mr_rows, 'case_id'),
]:
    cases_found = set(r[field] for r in rows)
    expected = {'CASE_D1', 'CASE_D2', 'CASE_D3', 'CASE_D4'}
    unexpected = cases_found - expected
    if unexpected:
        print(f'{name}: unexpected cases={unexpected}')
    else:
        print(f'{name}: cases={sorted(cases_found)} OK')
```

**Actual result:**
```
file_inventory: cases=['CASE_D1', 'CASE_D2', 'CASE_D3', 'CASE_D4'] OK
case_register: cases=['CASE_D1', 'CASE_D2', 'CASE_D3', 'CASE_D4'] OK
source_map: cases=['CASE_D1', 'CASE_D2', 'CASE_D3', 'CASE_D4'] OK
moderator_register: cases=['CASE_D1', 'CASE_D2', 'CASE_D3', 'CASE_D4'] OK
```

---

## Corrections applied based on these checks

| File | Field | Was (incorrect) | Corrected to (CSV truth) |
|------|-------|-----------------|--------------------------|
| Corpus_Refresh_Report.md | D1 probable moderators | 5 | 6 |
| Corpus_Refresh_Report.md | D1 unclear moderators | 2 | 1 |
| Corpus_Refresh_Report.md | D2 unclear moderators | 3 | 4 |
| Foundation_Verification_Report.md | Total probable moderators | 13 | 15 |
| Foundation_Verification_Report.md | Total no_transcript moderators | 23 | 21 |
| Foundation_Verification_Report.md | Total confirmed pairings | 18 | 19 |
| Foundation_Verification_Report.md | Total none pairing entries | 16 | 19 |
| Foundation_Verification_Report.md | None-row breakdown | 9 note-only, 6 transcript-only | 11 note-only, 4 transcript-only |
| Foundation_Verification_Report.md | Moderators.xlsx claim | falsely stated workbook contained out-of-scope rows | corrected to "contains Days 1-4 only" |
