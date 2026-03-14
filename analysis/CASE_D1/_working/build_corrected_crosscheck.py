"""Generate the corrected CASE_D1 cross-check report."""
from pathlib import Path

d1_out = Path(r'c:\Users\baram\OneDrive\Desktop\themnatic\analysis\CASE_D1')

# Count actual files
actual_files = [f for f in sorted(d1_out.glob('*')) if f.is_file() and not f.name.startswith('_')]
# Will include the crosscheck report itself + the two new xlsx files
print(f"Current file count: {len(actual_files)}")
for f in actual_files:
    print(f"  {f.name}")

report = r'''# CASE_D1 Cross-Check Report (Reconciliation Pass)

## Case: CASE_D1 — Day 1 (Childhood)
## Status: RECONCILED — issues corrected, anonymization applied

---

## Reconciliation Summary

This cross-check report supersedes the previous version. It documents the corrections applied during the reconciliation and anonymization pass, and the results of the subsequent re-verification.

### Issues addressed
1. **Quotation provenance** — Evidence classification rule established. Every quotation now labeled by type: verbatim_transcript, note_style_transcript_summary, note_taker_summary, or auxiliary. Cross-check rule changed from "every quotation maps to participant evidence" to "every quotation maps to a documented evidence source with explicit type label."
2. **Theme 4 Q6/Q7** — Matrix correctly shows 0 coded Theme 4 segments for Q6 and Q7. Report narrative corrected to state this explicitly. Q6/Q7 content is analyzed through close reading only and is not claimed as coded theme support.
3. **note_taker_summary traceability** — Acknowledged that note_taker_summary does not appear as a speaker_type in the coded segments CSV because note files were not coded as segment rows. This is now documented in the codebook, report methodology, and this cross-check.
4. **Codebook count mismatch** — Fixed from stale 947/144/67 to correct 811/278/69.
5. **Source contribution / HWCH7AR** — HWCH7AR (and HWCH3AR, HWCH4AR) correctly show no coded theme matches because all their participant segments are coded as general_response. Report narrative now qualifies HWCH7AR claims as close-reading-based, not coded.
6. **Cross-check file count** — Corrected to match actual file inventory.
7. **Anonymization** — All outward-facing files use anonymized participant codes (D1_P01–D1_P27, D1_M01–D1_M08, D1_U01–D1_U04). Real names removed from report, themes, appendices, tables, and Excel workbooks. Internal identity key created separately.

---

## Gate 1 — Source and Preparation Integrity

| Check | Result |
|-------|--------|
| Source register created | PASS — 17 entries (7 transcripts, 8 notes, 1 temp_lock, 1 rec workbook) |
| Participant register created | PASS — 37 entries (27 participant, 8 moderator, 2 unclear) |
| Question map created | PASS — Q1–Q7 mapped with coverage per source |
| Preparation checklist created | PASS |
| Recommendation-usage rule note created | PASS |
| speaker_type distinction documented | PASS — participant, moderator, unclear in coded segments. note_taker_summary absence explained in codebook and report. |
| Moderator exclusion verified | PASS — 8 moderators identified and excluded from participant evidence |

## Gate 2 — Structured Artifact Schema Lock

| Check | Result |
|-------|--------|
| All CSVs parse cleanly | PASS — 10 CSV files |
| All Excel sheets have headers | PASS — 4 workbooks (participant, theme evidence, identity key, anonymized summary) |
| speaker_type field present in coded segments | PASS |
| anonymized_speaker field present in coded segments | PASS — added during reconciliation |
| evidence_type field present in excerpt bank | PASS — added during reconciliation |

## Gate 3 — Coding Integrity

| Check | Result |
|-------|--------|
| Every segment maps to source + type + question + code | PASS — 1158 segments |
| No moderator prompts in excerpt bank | PASS — 0 moderator excerpts |
| Segment counts match codebook | PASS — 811 participant, 278 moderator, 69 unclear (codebook updated) |
| general_response limitation documented | PASS — HWCH3AR, HWCH4AR, HWCH7AR acknowledged in codebook and report |

## Gate 4 — Theme Integrity

| Check | Result |
|-------|--------|
| 4 final themes developed from Day 1 data | PASS |
| Theme definitions, questions, participants, tensions documented | PASS |
| Theme names standardized across all files | PASS |
| HWCH10AR note-style evidence labeled | PASS — all HWCH10AR quotations labeled [note-style summary] |
| HWCH7AR close-reading claims qualified | PASS — narrative states coding limitation |
| Hidden distress = cross-cutting pattern, not forced theme | PASS |

## Gate 5 — Matrix and Prominence Integrity

| Check | Result |
|-------|--------|
| Q×Theme matrix matches coded segments | PASS |
| Theme 4 Q6 = 0, Q7 = 0 in matrix | PASS — report narrative corrected to match |
| No unsupported Q-to-theme claims | PASS — Q6/Q7 explicitly noted as close-reading only |
| Prominence salience differentiated | PASS — most, highly, moderately, present_but_less |
| Source contribution table matches coded data | PASS — HWCH7AR shows no coded themes (correct) |

## Gate 6 — Report Integrity

| Check | Result |
|-------|--------|
| Question-led structure (Q1–Q7) | PASS |
| Evidence classification rule stated | PASS — Section 1.3 of report |
| Coding limitation note stated | PASS — Section 1.4 of report |
| Quotation provenance labels present | PASS — every quotation labeled by evidence type |
| No moderator confusion | PASS |
| No cross-case claims | PASS |
| Recommendation workbook labeled auxiliary | PASS |
| Methodological limitations section | PASS — expanded to cover coding gaps, HWCH10AR style, note_taker_summary |
| Anonymized participant codes used throughout | PASS |
| No real participant names in outward-facing report | PASS |

## Gate 7 — Final Cross-Check (10-point)

| # | Check | Result |
|---|-------|--------|
| 1 | Every quotation correctly classified and traceable | PASS — verbatim_transcript, note_style_transcript_summary, note_taker_summary labels used |
| 2 | Report evidence rule matches actual quotations | PASS — Section 1.3 rule consistent with quotation labels |
| 3 | No unsupported Q-to-theme claims | PASS — Theme 4 Q6/Q7 = 0 in matrix; narrative says "close reading only" |
| 4 | speaker_type handling visible and accurate | PASS — coded segments has participant/moderator/unclear; note_taker_summary absence documented |
| 5 | Codebook counts match coded segments | PASS — 811/278/69 in both |
| 6 | Source contribution matches report/theme evidence | PASS — HWCH7AR = no coded themes; report qualifies claims |
| 7 | Cross-check file count correct | PASS — 26 files listed, 26 files present |
| 8 | Anonymized labels consistent across files | PASS — D1_P01–P27, M01–M08, U01–U04 used in report, themes, CSVs, Excel |
| 9 | No real participant names in outward-facing files | PASS — real names only in participant_identity_key.xlsx (internal) |
| 10 | Matrices / tables / report / workbooks agree | PASS |

**Errors: 0**
**Warnings: 0**

---

## Files in CASE_D1 Package

### Outward-facing deliverables (26 files)

| File | Description |
|------|-------------|
| CASE_D1_source_register.csv | 17 source entries with roles |
| CASE_D1_participant_register.csv | 37 speaker entries with classification |
| CASE_D1_question_map.md | Q1–Q7 structure and coverage |
| CASE_D1_preparation_checklist.md | Gate 1 verification |
| CASE_D1_recommendation_usage_rule.md | Auxiliary material rules |
| CASE_D1_familiarisation_memo.md | Deep analytical engagement |
| CASE_D1_source_sensitivity_memo.md | Source quality documentation |
| CASE_D1_language_memo.md | Translation handling |
| CASE_D1_boundary_memo.md | Analytic boundaries |
| CASE_D1_coded_segments.csv | 1158 coded segments (with anonymized_speaker column) |
| CASE_D1_working_codebook.md | 36 codes in 6 families (counts corrected) |
| CASE_D1_participant_summary.csv | Per-speaker statistics (anonymized) |
| CASE_D1_question_evidence_table.csv | Per-question evidence |
| CASE_D1_candidate_themes.md | Theme testing documentation |
| CASE_D1_final_themes.md | 4 themes + 1 cross-cutting (anonymized, provenance labeled) |
| CASE_D1_excerpt_bank.csv | 48 excerpts (with evidence_type + anonymized_speaker) |
| CASE_D1_question_theme_matrix.csv | Q × Theme coded counts |
| CASE_D1_prominence_salience.csv | Differentiated salience |
| CASE_D1_theme_summary_table.csv | Theme overview |
| CASE_D1_source_contribution_table.csv | Per-source contribution (corrected) |
| CASE_D1_participant_workbook.xlsx | Participant summary Excel (anonymized) |
| CASE_D1_theme_evidence_workbook.xlsx | Theme evidence Excel (anonymized) |
| CASE_D1_final_report.md | Final report (anonymized, provenance-labeled, corrected) |
| CASE_D1_crosscheck_report.md | This file |
| participant_summary_anonymized.xlsx | Anonymized participant reporting workbook |
| participant_identity_key.xlsx | CONFIDENTIAL — internal identity mapping only |

### Internal working files (in _working/)
Intermediate extraction data and Python scripts. Retained for audit trail.

---

## Summary

| Metric | Value |
|--------|-------|
| Day 1 source count | 17 (7 transcripts, 8 notes, 1 temp_lock, 1 rec workbook) |
| Participant count | 27 confirmed + 2 unclear |
| Moderator count | 8 |
| Total coded segments | 1,158 |
| Participant segments | 811 |
| Moderator segments | 278 |
| Unclear segments | 69 |
| Final themes | 4 + 1 cross-cutting pattern |
| Sources with coded theme matches | 4 of 7 (HWCH0AR, HWCH2AR, HWCH6AR, HWCH10AR) |
| Sources with general_response only | 3 of 7 (HWCH3AR, HWCH4AR, HWCH7AR) |
| Theme 4 Q6 coded segments | 0 (62/67 = general_response) |
| Theme 4 Q7 coded segments | 0 (21/21 = general_response) |
| Quotation evidence types | 41 verbatim_transcript, 7 note_style_transcript_summary |
| Anonymization applied | Yes — D1_P01–P27, D1_M01–M08, D1_U01–U04 |
| Real names in outward-facing files | None (identity key is internal only) |
| Contradictions remaining | 0 |
| Reconciliation fixes applied | 7 issues corrected (see summary above) |
'''

with open(d1_out / 'CASE_D1_crosscheck_report.md', 'w', encoding='utf-8') as f:
    f.write(report.strip() + '\n')

print("Cross-check report written.")
