# CASE_D1 Cross-Check Report (Reconciliation Pass)

## Case: CASE_D1 — Day 1 (Childhood)
## Status: VERIFIED — outward-facing package rebuilt from stable anonymization map and cleared in final verification

---

## Reconciliation Summary

This cross-check report supersedes the previous version. It documents the structured rebuild of the outward-facing CASE_D1 package from one stable anonymization map, the separation of outward-facing and internal/confidential materials, and the corrections applied to quotation provenance and Theme 4 reporting.
| Check | Result |
|-------|--------|
| Package separation | PASS — outward-facing files are collected in `OUTWARD_FACING_PACKAGE/`; named internal files are retained in `INTERNAL_CONFIDENTIAL/` |
| Stable anonymized codes only | PASS — outward-facing layer uses `D1_P01–D1_P27`, `D1_M01–D1_M08`, and `D1_U01–D1_U04` only |
| Fallback IDs removed | PASS — no provisional or fallback anonymization identifiers remain in outward-facing exports |
| Structured segment counts | PASS — 1,158 total coded segments = 805 participant + 278 moderator + 75 unclear |
| Excerpt-bank evidence types | PASS — 51 rows = 41 `verbatim_transcript`, 7 `note_style_transcript_summary`, 3 `note_taker_summary` |
| Theme 4 Q6/Q7 claim | PASS — 0 coded Theme 4 segments in Q6 and Q7; narrative explicitly says close-reading only |
| Field schema | PASS — coded segments use `speaker_code`, `speaker_type`, `role_label`, and `attribution_status` |
| Report/table agreement | PASS — corrected report quotation placement now matches the outward-facing evidence layer, and coded-theme claims remain aligned with the matrix and source contribution table |

## Separated Package Inventory

### Outward-facing package (`OUTWARD_FACING_PACKAGE/`) — 16 files

| File | Description |
|------|-------------|
| CASE_D1_candidate_themes.md | Candidate-theme audit trail with corrected Theme 4 qualification |
| CASE_D1_coded_segments.csv | Rebuilt coded-segment export with stable anonymized speaker codes |
| CASE_D1_crosscheck_report.md | This verification report |
| CASE_D1_excerpt_bank.csv | Rebuilt excerpt bank with explicit evidence types |
| CASE_D1_final_report.md | Outward-facing final Day 1 academic report |
| CASE_D1_final_themes.md | Final theme definitions and evidential framing |
| CASE_D1_participant_register.csv | Outward-facing anonymized register with safe classification basis |
| CASE_D1_participant_summary.csv | Per-speaker structured summary |
| CASE_D1_participant_workbook.xlsx | Participant workbook |
| CASE_D1_prominence_salience.csv | Theme prominence summary |
| CASE_D1_question_evidence_table.csv | Per-question evidence counts |
| CASE_D1_question_theme_matrix.csv | Q × Theme coded counts |
| CASE_D1_source_contribution_table.csv | Per-source contribution summary |
| CASE_D1_theme_evidence_workbook.xlsx | Theme evidence workbook |
| CASE_D1_theme_summary_table.csv | Theme overview table |
| participant_summary_anonymized.xlsx | Anonymized participant workbook duplicate for reporting use |

### Internal/confidential package (`INTERNAL_CONFIDENTIAL/`) — 5 files

| File | Description |
|------|-------------|
| CASE_D1_familiarisation_memo.md | Internal analytic memo with named source details |
| CASE_D1_participant_register_anonymized.csv | Internal traceability copy of the rebuilt register |
| CASE_D1_preparation_checklist.md | Internal preparation checklist |
| CASE_D1_source_sensitivity_memo.md | Internal source-sensitivity memo with named references |
| participant_identity_key.xlsx | Internal identity key only |

## Structured-Layer Results

| Metric | Value |
|--------|-------|
| Day 1 source count | 17 (7 transcripts, 8 note files, 1 temp-lock file, 1 recommendation workbook) |
| Participant register count | 37 rows (27 participant, 8 moderator, 2 unclear) |
| Participant summary count | 37 rows (27 participant, 8 moderator including zero-turn `D1_M02`, 2 unclear) |
| Total coded segments | 1,158 |
| Participant segments | 805 |
| Moderator segments | 278 |
| Unclear segments | 75 |
| Final themes | 4 + 1 cross-cutting pattern |
| Sources with coded theme matches | 4 of 7 (`HWCH0AR`, `HWCH2AR`, `HWCH6AR`, `HWCH10AR`) |
| Sources with general_response-only participant coding | 3 of 7 (`HWCH3AR`, `HWCH4AR`, `HWCH7AR`) |
| Theme 4 Q6 coded segments | 0 of 65 participant segments |
| Theme 4 Q7 coded segments | 0 of 21 participant segments |
| Quotation evidence types | 41 verbatim + 7 note-style summary + 3 note-taker summary |

## Final 10-Point Cross-Check

| # | Check | Result |
|---|-------|--------|
| 1 | Outward-facing and internal/confidential files are separated | PASS |
| 2 | Outward-facing exports use only stable anonymized speaker codes | PASS |
| 3 | No fallback IDs remain in outward-facing CSV or markdown deliverables | PASS |
| 4 | Quotation provenance is explicit and truthful | PASS |
| 5 | `note_taker_summary` evidence is preserved in the excerpt bank without being falsely claimed as coded transcript rows | PASS |
| 6 | Theme 4 Q6/Q7 narrative matches the matrix (`0` coded segments; close-reading only) | PASS |
| 7 | Source-contribution claims match the rebuilt CSVs (`HWCH2AR` remains coded for Themes 2 and 3 only; `HWCH3AR`, `HWCH4AR`, and `HWCH7AR` have no coded theme matches) | PASS |
| 8 | Report quotation placement, matrix counts, and participant/source summaries now follow one consistent outward-facing rule | PASS |
| 9 | Outward-facing package inventory claims match the separated folders | PASS |
| 10 | Contradictions remaining in outward-facing package | PASS — 0 identified in this reconciliation pass |

**Errors:** 0
**Warnings:** 0
