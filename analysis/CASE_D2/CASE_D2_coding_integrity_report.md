# CASE_D2 Coding Integrity Report

## Case: CASE_D2 — Day 2 (Youth)
## Status: VERIFIED FOR CURRENT GATE 3 CODING-LAYER CHECKS — report-quotation traceability deferred until report drafting

---

## Coding Integrity Summary

This report documents the current Gate 3 coding-integrity checks that are verifiable from the reviewed `CASE_D2_coded_segments.csv` layer and the linked structured outputs already regenerated from that reviewed base. The reviewed coding layer was rebuilt through `analysis/CASE_D2/_working/build_case_d2_phase3_phase4.py`, which applies retrieval-oriented heuristic indexing and then regenerates the linked Day 2 summary artifacts. Those heuristic cues are treated as retrieval aids only and were manually tightened during review; they are not treated as automatic proof of thematic support.

## Current Gate 3 Check Table

| Check | Result |
|-------|--------|
| Required coded-segment fields present | PASS — all 321 rows parse cleanly with no missing values across `segment_id`, `source_file`, `table_id`, `speaker_code`, `speaker_type`, `role_label`, `attribution_status`, `question_id`, `segment_text`, `codes`, and `language` |
| Allowed `speaker_type` values only | PASS — all rows use only `participant`, `moderator`, or `unclear`; no invalid speaker types were found |
| Every coded segment maps to source + type + question + code | PASS — 321 of 321 rows have non-empty source, speaker type, question, and code fields |
| Empty or invalid code values | PASS — 0 rows with empty codes and 0 code values outside the active Day 2 coding build vocabulary |
| Moderator prompts isolated from participant evidence | PASS — all 92 moderator rows are coded `moderator_context`, and the linked participant summary contains 31 participant rows with 0 non-participant rows |
| Linked question-evidence counts match coded base | PASS — `CASE_D2_question_evidence_table.csv` matches the reviewed coded layer for participant, moderator, unclear, and unique participant-speaker counts across Q1–Q7 |
| Mixed-language authority preserved | PASS — original-language segment text remains in the coded layer with explicit language tagging (`185` Arabic rows, `136` English rows) |
| Retrieval/pattern cues documented as indexing aids | PASS — retrieval logic lives in `analysis/CASE_D2/_working/build_case_d2_phase3_phase4.py` and was manually reviewed/tightened before this report |
| Report quotation traceability | DEFERRED — no `CASE_D2` final report or excerpt bank exists yet, so quotation-to-segment linkage must be rechecked when those artifacts are built |

## Structured-Layer Results

| Metric | Value |
|--------|-------|
| Total coded segments | 321 |
| Participant segments | 212 |
| Moderator segments | 92 |
| Unclear segments | 17 |
| Participant summary rows | 31 |
| Participant workbook | `CASE_D2_participant_workbook.xlsx` created from the reviewed coded base |
| Question coverage | Q1–Q7 all present in the reviewed coded layer |
| CSV schema integrity | `CASE_D2_coded_segments.csv`, `CASE_D2_participant_summary.csv`, and `CASE_D2_question_evidence_table.csv` all parse cleanly |
| Unused available retrieval labels in current build vocabulary | `intergenerational_disconnect`, `service_recipient_comparison` |

## Notes on Current Scope

- The current Gate 3 report verifies the reviewed coding layer and the linked structured summaries that already exist.
- Theme-dependent artifacts are not yet in scope here. In particular, the following remain deferred until theme development is completed and locked:
  - `CASE_D2_question_theme_matrix.csv`
  - `CASE_D2_prominence_salience.csv`
  - `CASE_D2_theme_summary_table.csv`
  - `CASE_D2_theme_evidence_workbook.xlsx`
  - any theme-integrity, matrix-prominence, report-integrity, and final cross-check reports
- The recommendation workbook remains auxiliary structured recommendation material only and is not treated as transcript-equivalent evidence in this coding-integrity pass.

## Gate 3 Conclusion

The reviewed `CASE_D2` coding base currently passes the coding-layer checks that are testable before theme development. The next explicit artifact should be the theme-independent continuation of the Gate 3/4 chain from this reviewed base, beginning with any later evidence-selection layer or theme-development artifacts that depend on locked Day 2 themes.

**Errors:** 0
**Warnings:** 1 — report quotation traceability remains deferred until the Day 2 report/excerpt layer exists.
