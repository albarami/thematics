# Foundation Verification Appendix

This appendix shows the exact aggregation logic, calculation methods, and verification procedures used to confirm internal consistency of the D1-D4 corpus refresh foundation. Every number below is derived programmatically from the source CSV files or actual workbook files.

---

## 1. File count aggregation logic

**Source**: `file_inventory_refresh.csv` (65 rows)

**Method**: Group rows by `case_id` and `file_type`, count occurrences.

**CSV-derived results**:

| case_id | transcript | note | recommendation_workbook | temp_lock | auxiliary | total |
|---------|-----------|------|----------------------|-----------|-----------|-------|
| CASE_D1 | 7 | 8 | 1 | 1 | 0 | 17 |
| CASE_D2 | 7 | 10 | 1 | 0 | 0 | 18 |
| CASE_D3 | 5 | 11 | 1 | 0 | 0 | 17 |
| CASE_D4 | 5 | 7 | 1 | 0 | 0 | 13 |
| **Total** | **24** | **36** | **4** | **1** | **0** | **65** |

**Cross-check against `case_register_refresh.csv`**: All 20 field-level comparisons (5 fields x 4 cases) returned MATCH.

**Cross-check against filesystem**: Recursive scan of the four day folders returned exactly 65 files. Set difference between inventory relative paths and filesystem relative paths was empty in both directions.

**Cases present in inventory**: CASE_D1, CASE_D2, CASE_D3, CASE_D4.

---

## 2. Moderator count calculation

**Source**: `moderator_register_refresh.csv` (45 rows)

**Method**: Group rows by `case_id` and `transcript_match_confidence`, count occurrences.

**CSV-derived results**:

| case_id | total | confirmed | probable | unclear | no_transcript_available |
|---------|-------|-----------|----------|---------|------------------------|
| CASE_D1 | 11 | 0 | 6 | 1 | 4 |
| CASE_D2 | 12 | 0 | 3 | 4 | 5 |
| CASE_D3 | 12 | 1 | 3 | 1 | 7 |
| CASE_D4 | 10 | 2 | 3 | 0 | 5 |
| **Total** | **45** | **3** | **15** | **6** | **21** |

**Verification**: 3 + 15 + 6 + 21 = 45. Matches total row count.

**Cases present**: CASE_D1, CASE_D2, CASE_D3, CASE_D4.

**Cross-check against narrative files**:
- `Corpus_Refresh_Report.md` D1 section states "0 confirmed by name, 6 probable, 1 unclear, 4 no transcript available" → matches CSV.
- `Corpus_Refresh_Report.md` D2 section states "0 confirmed by name, 3 probable, 4 unclear, 5 no transcript available" → matches CSV.
- `Corpus_Refresh_Report.md` D3 section states "1 confirmed by name, 3 probable, 1 unclear, 7 no transcript available" → matches CSV.
- `Corpus_Refresh_Report.md` D4 section states "2 confirmed by name, 3 probable, 5 no transcript available" → matches CSV.
- `Foundation_Verification_Report.md` states "confirmed (3), probable (15), unclear (6), no_transcript_available (21)" → matches CSV.

---

## 3. Pairing count calculation

**Source**: `source_map_refresh.csv` (39 rows)

**Method**: Group rows by `case_id` and `pairing_confidence`, count occurrences.

**CSV-derived results**:

| case_id | total_entries | confirmed | probable | ambiguous | none |
|---------|--------------|-----------|----------|-----------|------|
| CASE_D1 | 9 | 7 | 0 | 0 | 2 |
| CASE_D2 | 11 | 6 | 0 | 0 | 5 |
| CASE_D3 | 11 | 2 | 1 | 0 | 8 |
| CASE_D4 | 8 | 4 | 0 | 0 | 4 |
| **Total** | **39** | **19** | **1** | **0** | **19** |

**Verification**: 19 + 1 + 0 + 19 = 39. Matches total row count.

**Exact composition of the 19 `none` entries** (verified from `pairing_basis` field):
- 11 note-only entries (note file has no transcript with the same prefix)
- 4 transcript-only entries (transcript has no note file with the same prefix)
- 4 standalone auxiliary recommendation workbook entries (1 per day, keyed as `CASE_Dx_AUX_REC`)

**Cross-check against narrative files**:
- `Foundation_Verification_Report.md` states "19 pairings across D1-D4" confirmed, "1 pairing" probable, "19 entries" none → matches CSV.
- `Corpus_Refresh_Report.md` per-day pairing tables: manually counted rows per confidence level in each table match the CSV per-case breakdown.

---

## 4. Recommendation workbook dimension verification

**Source**: Actual `.xlsx` files opened with `openpyxl`

**Method**: For each workbook, read `ws.max_row`, `ws.max_column`, row 1 headers, and count non-empty cells per column across all rows. Also detect rows where columns A and B are empty but column C is populated (irregular rows), and columns where all cells are empty (empty columns).

**Verified results from actual files**:

| Case | Path | Sheet | max_row | max_col | Headers | Non-empty by col | Empty cols | Irregular rows |
|------|------|-------|---------|---------|---------|-----------------|------------|----------------|
| D1 | Day1_Childhood/Recommendations_Data/Health_Workshop_Suggestions Day 1.xlsx | First_Day_01_02_2026 | 41 | 3 | No \| User \| Suggestion | 39 \| 39 \| 41 | none | rows 40, 41 |
| D2 | Day2_Youth/Recommendations_Data/Health_Workshop_Suggestions Day 2.xlsx | Second_Day_02_02_2026 | 58 | 4 | No \| User \| Suggestion \| (empty) | 58 \| 58 \| 58 \| 0 | col 4 | none |
| D3 | Day3_Adults/Recommendations_Data/Health_Workshop_Suggestions Day 3.xlsx | Third_Day_03_02_2026 | 65 | 3 | No \| User \| Suggestion | 65 \| 65 \| 65 | none | none |
| D4 | Day4_Elderly/Recommendations_Data/Health_Workshop_Suggestions Day 4.xlsx | Forth_Day_04_02_2026 | 40 | 3 | No \| User \| Suggestion | 40 \| 40 \| 40 | none | none |

**Cross-check against `recommendation_workbook_initial_assessment.md`**:
- D1: sheet name, max_row, max_column, headers, irregular rows (40-41) all match.
- D2: sheet name, max_row, max_column (4 physical, 3 effective), headers, empty column D all match.
- D3: sheet name, max_row, max_column, headers all match.
- D4: sheet name, max_row, max_column, headers all match.

---

## 5. Corrections applied during machine verification

During the machine-checked verification pass, the following mismatches were detected between the CSV ground truth and the narrative markdown files, and corrected:

| File | Field | Was (incorrect) | Corrected to (CSV truth) |
|------|-------|-----------------|--------------------------|
| Corpus_Refresh_Report.md | D1 probable moderators | 5 | 6 |
| Corpus_Refresh_Report.md | D1 unclear moderators | 2 | 1 |
| Corpus_Refresh_Report.md | D2 unclear moderators | 3 | 4 |
| Foundation_Verification_Report.md | Total probable moderators | 13 | 15 |
| Foundation_Verification_Report.md | Total no_transcript moderators | 23 | 21 |
| Foundation_Verification_Report.md | Total confirmed pairings | 18 | 19 |
| Foundation_Verification_Report.md | Total none pairing entries | 16 | 19 |
| Foundation_Verification_Report.md | Correction table probable | (13) | (15) |
| Foundation_Verification_Report.md | Correction table no_transcript | (23) | (21) |

All corrections were made by changing the narrative to match the CSV, since the CSVs were generated programmatically from the actual source files and confirmed correct.

---

## 6. Final consistency status

After all corrections:
- **File counts**: inventory CSV = case register CSV = filesystem scan = narrative aggregate table. All match.
- **Moderator totals**: moderator register CSV = per-day narrative sections = FVR summary totals. All match.
- **Pairing totals**: source map CSV = FVR pairing section = per-day pairing tables. All match.
- **Workbook dimensions**: actual .xlsx properties = workbook assessment narrative. All match.
- **Contradictions remaining**: 0.
