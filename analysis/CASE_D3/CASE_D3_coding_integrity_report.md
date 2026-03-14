# CASE_D3 Coding Integrity Report

## Case: CASE_D3 — Day 3 (Adults)
## Status: VERIFIED FOR CURRENT PROMOTED GATE 3 STRUCTURED CHECKS — full Gate 3 closure deferred pending first-pass recoding review and manual tightening

---

## Coding Integrity Summary

This report documents the current Gate 3 checks that can be verified from the current promoted `CASE_D3_coded_segments.csv` layer and the linked structured outputs already regenerated from that same promoted base. The current Day 3 coded layer was produced from `analysis/CASE_D3/_working/CASE_D3_segment_candidates.csv` via `analysis/CASE_D3/_working/build_case_d3_phase3_phase4.py`.

This report is **not** a claim that `CASE_D3` is package-ready or that Gate 3 is fully closed. It records what is verifiable now, what remains caveated, and what is still deferred before Gate 4 theme work.

## Current Gate 3 Check Table

| Check | Result |
|-------|--------|
| Required coded-segment fields present | PASS — all 1,234 rows parse cleanly with no missing values across `segment_id`, `source_file`, `table_id`, `speaker_code`, `speaker_type`, `role_label`, `attribution_status`, `question_id`, `segment_text`, `codes`, and `language` |
| Allowed `speaker_type` values only | PASS — all rows use only `participant`, `moderator`, or `unclear`; no invalid `speaker_type` values were found; `note_taker_summary` is not present in the current transcript-derived promoted layer |
| Every coded segment maps to source + type + question + code | PASS — all 1,234 rows have non-empty source, speaker type, question, and code fields |
| Empty or invalid code values | PASS — 0 rows have empty `codes`, and all moderator rows remain coded `moderator_context` |
| Moderator prompts isolated from participant evidence | PASS — all 307 moderator rows are coded `moderator_context`, and `CASE_D3_participant_summary.csv` contains 23 participant rows with 0 non-participant rows |
| Linked question-evidence counts match coded base | PASS — `CASE_D3_question_evidence_table.csv` matches participant, moderator, unclear, and unique participant-speaker counts for `Q1`–`Q7`, with 0 mismatches |
| Source linkage preserved | PASS — all 1,234 rows retain `source_file` and `table_id` linkage across `HWAD10AR.docx`, `HWAD1AR.docx`, `HWAD3AR.docx`, `HWAD4AR.docx`, and `HWAD6AR.docx` |
| Question coverage recorded with current caveats | PASS WITH CAVEAT — `Q1`–`Q7` are present in the promoted coded layer, but `HWAD1AR` still has weak `Q2`/`Q3` boundaries, `HWAD10AR` does not preserve a clean standalone `Q6` section, and later recommendation material may survive as moderator-led summary structure |
| Mixed-language authority preserved | PASS — original-language segment text remains in the coded layer with explicit language tagging (`832` Arabic rows, `402` English rows) |
| Manual code review closure | DEFERRED — first-pass codebook-based recoding and manual tightening have not yet been completed |
| Gate 4 / Gate 6 quotation traceability | DEFERRED — no locked Day 3 theme/report layer exists yet, so quotation-to-segment linkage is not yet testable |

## Structured-Layer Results

| Metric | Value |
|--------|-------|
| Total coded segments | 1,234 |
| Participant segments | 489 |
| Moderator segments | 307 |
| Unclear segments | 438 |
| Participant summary rows | 23 |
| Question evidence rows | 7 |
| Participant workbook | `CASE_D3_participant_workbook.xlsx` created from the current promoted base |
| Languages | `832` Arabic / `402` English |
| Question coverage | `Q1`–`Q7` present in the current promoted coded layer |
| Transcript source coverage | `HWAD10AR.docx`, `HWAD1AR.docx`, `HWAD3AR.docx`, `HWAD4AR.docx`, `HWAD6AR.docx` |

## Current Limitations That Remain Explicit

- `HWAD1AR` retains weak `Q2`/`Q3` transcript boundaries, so its promoted coverage remains partial and later questions dominate the surviving structured rows.
- `HWAD10AR` does not preserve a clean standalone `Q6` section in the current transcript extraction; its later recommendation material is present mainly as moderator-led summary or recommendation context.
- Later sections in some sources preserve moderator-led summary structure; these rows remain moderator context or unattributed material rather than being smoothed into participant evidence.
- `HWAD3AR` and `HWAD6AR` still contain substantial flowing unattributed discussion that is retained as `unclear` instead of being over-assigned to named participants.
- The recommendation workbook remains auxiliary structured recommendation material only and is not treated as transcript-equivalent evidence in this coding-integrity pass.

## Notes on Current Scope

- This report verifies the current promoted Gate 3 structured layer and the linked outputs already regenerated from it.
- It does not close Day 3 manual coding review.
- Theme-dependent artifacts remain deferred until Gate 4 and later work:
  - `CASE_D3_question_theme_matrix.csv`
  - `CASE_D3_prominence_salience.csv`
  - `CASE_D3_theme_summary_table.csv`
  - `CASE_D3_theme_evidence_workbook.xlsx`
  - any theme-integrity, matrix-prominence, report-integrity, and final cross-check reports
- Note files and the recommendation workbook continue to serve as contextual or auxiliary materials only; they are not being converted into transcript-equivalent participant evidence here.

## Gate 3 Conclusion

The current promoted `CASE_D3` coding base passes the structured Gate 3 checks that are testable from the repo now, and the current limitations are explicitly documented. Gate 3 is now documented truthfully enough to support the next controlled step, but it is **not** fully closed yet. Full Gate 3 closure still depends on first-pass codebook-based recoding/manual tightening and any follow-up integrity recheck after that review.

**Errors:** 0
**Warnings:** 4 — weak `HWAD1AR` `Q2`/`Q3` boundaries; weak `HWAD10AR` `Q6` preservation; later moderator-led summary structure; manual review closure still deferred.
