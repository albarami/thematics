# Foundation Verification Report

## Purpose
This report documents the explicit verification steps taken during the corrected D1-D4-only corpus refresh pass. It records how each item was verified, what was corrected from the previous pass, and where uncertainty remains.

## Machine-verification status
All numbers in this report and in `Corpus_Refresh_Report.md` were machine-checked against the CSV ground truth files. A full cross-check script was run comparing every narrative number to the corresponding CSV-derived aggregation. After corrections, the final verification pass returned **zero mismatches**.

**Supporting documents:**
- `Foundation_Verification_Appendix.md` — exact aggregation tables and cross-check results
- `Foundation_Check_Script.md` — exact Python logic and commands used for all checks

---

## 1. How D1-D4 were verified

### File counts
Every file count was verified by programmatic recursive scan of the raw day folders (`Day1_Childhood`, `Day2_Youth`, `Day3_Adults`, `Day4_Elderly`). Files were classified by subfolder path and filename prefix:
- `Audio Recordings _Transcripts/*.docx` -> transcript
- `NoteTakers_Notes/*.docx` (excluding `_$*` and `~$*`) -> note
- `NoteTakers_Notes/_$*` or `NoteTakers_Notes/~$*` -> temp_lock
- `Recommendations_Data/*.xlsx` -> recommendation_workbook
- Everything else -> auxiliary

Classification was applied to every file individually. No counts were estimated or carried over from the previous pass.

### Exact filenames
All filenames were extracted by the same recursive scan and listed explicitly per type per day. No filenames were inferred or assumed. Irregular filenames were flagged:
- `HWYO1NT.docx` (non-standard NT suffix without number)
- `HWYO9NT1[7].docx` (square brackets in filename)
- `HWAD10NTI.docx` (NTI instead of NT + number)

### Recommendation workbook structure
Each of the four recommendation workbooks was opened with `openpyxl` and verified for:
- Exact sheet names (read from workbook, not assumed)
- Exact max_row and max_column (read from worksheet properties)
- Exact column headers (read from row 1)
- Non-empty cell count per column (counted programmatically across all rows)
- Sample rows inspected to assess row type (raw, grouped, cleaned)

Key findings:
- All four workbooks have a consistent `No | User | Suggestion` structure
- Day 2 has a phantom empty column D (max_column=4 but column D has 0 non-empty cells)
- Day 1 has 2 supplementary rows (40-41) with empty No/User but populated Suggestion
- Days 3 and 4 have fully populated rows with no irregularities

### Moderator workbook verification
`Moderators.xlsx` was opened and every row was read programmatically. The workbook has a single sheet named `Day 1`. It contains 54 rows total: 4 header rows (one per day section), 45 moderator data rows (Days 1-4), and 5 blank separator rows. Each data row was verified for:
- Day number (values found: 1, 2, 3, 4)
- Stakeholder group label
- Table ID
- Moderator name

The workbook contains moderator assignments for Days 1-4 only. No other day values are present in the workbook.

### Moderator-transcript matching
For each moderator row (Days 1-4), the corresponding transcript file was identified by matching the table ID to the filename pattern `HW[prefix][table_id]AR.docx`. Three levels of matching were attempted:
1. **Exact name match**: moderator name appears verbatim in transcript text
2. **Normalized match**: moderator name matches a transcript speaker label after case-folding and punctuation removal
3. **Role label match**: transcript contains generic moderator/session-manager labels (`Moderator`, `مدير الجلسة`, `المحاور`, `موديريتر`)

Each moderator row was assigned a transcript match confidence level based on the strongest available evidence:
- `confirmed`: name or close variant appears in transcript with moderator role context (3 cases total: هنادي أحمد أبو بكر in HWAD1AR, Diana Hassan in HWEL1AR, د. عبد اللطيف سلامي in HWEL9AR)
- `probable`: transcript has a generic moderator role label and workbook assigns this person, but no name confirmation (15 cases)
- `unclear`: transcript has no moderator role label and no name match (6 cases)
- `no_transcript_available`: no transcript file exists for that table (21 cases)

### Pairing verification
Transcript-note pairings were determined by extracting the source code prefix (e.g. `HWCH0` from `HWCH0AR.docx` and `HWCH0NT1.docx`) and checking whether both transcript and note files exist for each prefix. Confidence levels:
- `confirmed`: exact prefix match with both file types present (19 pairings across D1-D4)
- `probable`: prefix match but irregular filename (1 pairing: HWAD10)
- `none`: only one file type present for the prefix, or a standalone auxiliary recommendation workbook entry (19 entries: 11 note-only, 4 transcript-only, 4 standalone auxiliary recommendation workbook entries)

No pairings were forced based on loose similarity. Every `none` entry was explicitly documented with the reason.

### Participant/source-role assessment
For each transcript, speaker labels were extracted by scanning for `Label: content` patterns in the DOCX XML. This extraction is a first-pass approximation only. Known limitations:
- Some transcripts embed speaker labels inline without colon separators
- Some transcripts use paragraph-level formatting (bold, color) rather than text-pattern labels
- Two Day 2 transcripts (HWYO3AR, HWYO7AR) yielded zero extracted labels
- Several Day 3 transcripts use descriptive role labels rather than names

These limitations are documented in the participant register logic note and will need to be resolved during the derived-text preparation stage.

---

## 2. Which counts were directly verified

| Item | Verification method |
|------|-------------------|
| Transcript file count per day | Programmatic recursive glob of `Audio Recordings _Transcripts/*.docx` |
| Note-taker file count per day | Programmatic recursive glob of `NoteTakers_Notes/*.docx` minus temp/lock prefixes |
| Temp/lock file count per day | Programmatic recursive glob of `NoteTakers_Notes/_$*` and `NoteTakers_Notes/~$*` |
| Recommendation workbook count per day | Programmatic recursive glob of `Recommendations_Data/*.xlsx` |
| Auxiliary file count per day | All remaining files after the above classifications |
| Recommendation workbook sheet names | Read from `openpyxl` `wb.sheetnames` |
| Recommendation workbook max_row | Read from `openpyxl` `ws.max_row` |
| Recommendation workbook max_column | Read from `openpyxl` `ws.max_column` |
| Recommendation workbook column headers | Read from `openpyxl` row 1 |
| Recommendation workbook non-empty cells per column | Counted programmatically across all rows |
| Moderator names per day | Read from `openpyxl` row-by-row from `Moderators.xlsx` |
| Moderator-transcript name matching | Programmatic full-text search of each transcript DOCX |
| Moderator-transcript role-label matching | Programmatic search for moderator-related terms in each transcript DOCX |
| Speaker label extraction per transcript | Programmatic regex extraction of `Label:` patterns from DOCX XML |

---

## 3. Which items required normalization or judgment

| Item | Nature of judgment |
|------|-------------------|
| Moderator transcript match confidence | Judgment required to distinguish `confirmed` (name + role) from `probable` (role label only) from `unclear` (no evidence). Applied conservatively: only 3 of 45 moderator rows rated `confirmed`. |
| HWAD10 pairing confidence | Rated `probable` instead of `confirmed` because the note file `HWAD10NTI.docx` uses an irregular suffix pattern. |
| Recommendation workbook row type | Assessed as "grouped/cleaned" based on inspection of sample rows showing generic user labels and bundled multi-recommendation entries. This is a provisional assessment, not a certainty. |
| Day 1 rows 40-41 treatment | Assessed as manually aggregated supplementary notes based on the row 40 prefix text "نقاط إضافية من مداخلات الحضور تم جمعها بشكل يدوي" (= "Additional points from audience interventions collected manually"). |
| Speaker label extraction completeness | The regex-based extraction is known to miss inline labels, paragraph-formatted labels, and non-colon-delimited speakers. The extracted label sets are lower bounds, not complete inventories. |
| D1 moderator "Kulood" / "Dr. Kholoud" | Rated `probable` rather than `confirmed` because "Kulood" is a plausible spelling variant of "Kholoud" but the transcript does not explicitly label this speaker as a moderator. |
| D1 moderator "نور الوتاري" / "نور أحمد الوتادي" | Rated `probable` because "الوتاري" vs "الوتادي" is a plausible variant but the transcript does not use a moderator role label for this speaker. |
| D4 moderator "هالة" / "هالة فايد حسن فتحي" | Rated `probable` because transcript HWEL3AR has "أستاذة هالة" and "أ.هالة" (first-name match) but no moderator role label. |

---

## 4. Where uncertainty still exists

1. **Transcripts with no extracted speaker labels** (HWYO3AR, HWYO7AR): It is unknown whether these transcripts contain speaker labels in a non-standard format that the extraction missed, or whether they genuinely lack speaker attribution. This must be resolved during derived-text preparation by manual inspection.

2. **Moderators rated `unclear`** (6 rows): These moderators are assigned by the workbook but have no transcript-level confirmation. It is possible that (a) the moderator is present under a different name/label, (b) the transcript format does not preserve moderator attribution, or (c) the workbook assignment is incorrect. Resolution requires manual transcript reading during preparation.

3. **Moderators with `no_transcript_available`** (21 rows): These tables have no transcript file in the current raw folder. The moderator assignment from `Moderators.xlsx` cannot be verified or denied. If transcripts are later added, these rows should be re-verified.

4. **HWAD10NTI.docx naming**: The `NTI` suffix is irregular. It is unknown whether this is a typo for `NT1` or an intentional variant. Treated as probably part of the HWAD10 cluster.

5. **HWYO9NT1[7].docx naming**: The square brackets are unusual and may cause issues with some tools. The file's relationship to HWYO9 is confirmed by prefix, but the bracket suffix is unexplained.

6. **Recommendation workbook `User X` label consistency**: It is unknown whether `User 1` in Day 1 refers to the same person as `User 1` in Day 2. This should not be assumed.

7. **Day 2 column D**: The empty fourth column in the Day 2 workbook is unexplained. It has no analytical significance but its origin is unknown.

8. **Speaker labels that look like sentence fragments**: Some "labels" extracted by the regex (e.g. long Arabic sentence fragments ending with a colon) are not true speaker labels. These false positives must be filtered during derived-text preparation.

---

## 5. What was corrected from the previous refresh pass

| Correction | Detail |
|-----------|--------|
| **Scope reduced to D1-D4** | Previous pass included additional day folders. Corrected pass covers D1-D4 only: 65 inventory rows, 4 case register rows. |
| **Moderator confidence levels added** | Previous pass used a single `confirmed` confidence for all workbook-listed moderators. Corrected pass uses 4-level evidence-based confidence: `confirmed` (3), `probable` (15), `unclear` (6), `no_transcript_available` (21). |
| **Recommendation workbook assessment expanded** | Previous pass assessed only the Day 1 workbook. Corrected pass verifies all four D1-D4 workbooks with exact metadata (sheet names, row counts, column counts, non-empty cell counts, structural notes). |
| **Day 2 phantom column documented** | Previous pass did not note the empty column D in the Day 2 workbook. Now documented. |
| **Day 1 supplementary rows documented** | Previous pass did not distinguish the manually aggregated rows 40-41 from user-attributed rows. Now documented with exact row numbers and content assessment. |
| **Pairing basis made explicit** | Previous pass described pairings narratively. Corrected pass provides per-entry confidence with explicit basis text in the source map CSV. |
| **Participant-availability caveats added** | Previous pass stated participant extraction was "feasible" generically. Corrected pass documents specific transcript-level limitations including zero-label transcripts and descriptive-label transcripts. |
| **Report headings fixed** | Previous pass used non-ASCII dash characters in headings. Corrected pass uses plain ASCII. |

---

## 6. Verification conclusion

The D1-D4 foundation is now based on:
- Directly verified file counts (no assumptions, no carryover)
- Directly verified workbook metadata (no guesses)
- Evidence-based moderator confidence levels (not blanket "confirmed")
- Explicit pairing logic with per-entry basis statements
- Documented filename irregularities
- Documented remaining uncertainties

The foundation is clean enough to begin CASE_D1 preparation and Gate 1 work, provided the remaining uncertainties (especially zero-label transcripts and unclear moderator assignments) are resolved during the derived-text preparation stage rather than assumed away.

## 7. Machine-checked consistency confirmation

The following cross-checks were run programmatically after all corrections:

| Check | Source A | Source B | Result |
|-------|----------|----------|--------|
| File counts | file_inventory_refresh.csv | case_register_refresh.csv | 20/20 fields MATCH |
| File counts | file_inventory_refresh.csv | filesystem recursive scan | 65/65 files MATCH |
| File counts | case_register_refresh.csv | Corpus_Refresh_Report.md aggregate table | ALL MATCH |
| Moderator totals | moderator_register_refresh.csv | Corpus_Refresh_Report.md per-day sections | ALL MATCH |
| Moderator totals | moderator_register_refresh.csv | Foundation_Verification_Report.md summary | ALL MATCH |
| Pairing totals | source_map_refresh.csv | Foundation_Verification_Report.md summary | ALL MATCH |
| Pairing totals | source_map_refresh.csv | Corpus_Refresh_Report.md per-day tables | ALL MATCH |
| Workbook structure | actual .xlsx files | recommendation_workbook_initial_assessment.md | ALL MATCH |

**Final status after machine-checked verification: all narrative numbers match CSV ground truth.**
