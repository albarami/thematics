# Case-Level QA Gate Specification

## Purpose
This document defines the mandatory quality-assurance gates that must pass before any within-case day-level thematic analysis (CASE_D2 onward) can be marked complete. These gates were established after the CASE_D1 reconciliation pass revealed three cross-file inconsistencies that required correction. The specification is stricter than the CASE_D1 process to prevent similar issues from recurring.

## Applicability
- CASE_D1 refresh reruns after material corpus amendment
- CASE_D2, CASE_D3, CASE_D4
- If a previously completed case receives materially expanded core data, this specification applies to the rerun and superseding version of that case

## Current assessed scope
The current active assessment scope covers CASE_D1 through CASE_D4 only. All gate checks, registers, and deliverables are bounded to D1-D4.

## Pre-Check — Corpus Amendment Trigger

Before Gate 1, confirm whether the raw case corpus has changed since the last approved inventory or analysis.

If the case has received materially expanded core data such as additional transcripts or additional note-taker files, stop and rerun the case from Gate 1 rather than patching earlier outputs. If the change is auxiliary only, document the treatment decision explicitly and continue only if the case's primary and contextual evidence base is unchanged.

## Gate Summary

| Gate | Name | When | Key Output |
|------|------|------|------------|
| 1 | Source and Preparation Integrity | Before coding | Source register, participant register, question map, preparation checklist |
| 2 | Structured Artifact Schema Lock | Before analysis | Schema check report |
| 3 | Coding Integrity | Before theme writing | Coding integrity report |
| 4 | Theme Integrity | Before final report writing | Theme integrity report |
| 5 | Matrix and Prominence Integrity | Before final report writing | Matrix prominence check report |
| 6 | Report Integrity | Before final export | Report integrity check report |
| 7 | Final Cross-Check | Before marking complete | Final cross-check report |

## Gate 1 — Source and Preparation Integrity

Before any coding begins, confirm:

1. Final source list for the case (all raw files mapped to derived files)
2. Classification of each file as transcript or notes
3. Participant list or role list extracted from transcript speaker labels
4. Moderator vs participant distinction for every identified speaker
5. Question map reconciled against the actual discussion guide
6. Prepared files, source map, and provenance links are complete and match the Phase 1 manifest

Required outputs:
- `{CASE}_source_register.csv`
- `{CASE}_participant_register.csv`
- `{CASE}_question_map.csv`
- `{CASE}_preparation_checklist.md`

## Gate 2 — Structured Artifact Schema Lock

Before analysis begins, confirm:

1. Exact same column schema as CASE_D1 for all structured artifacts:
   - coded segments CSV
   - working codebook CSV
   - question-by-theme matrix CSV
   - excerpt bank CSV
   - salience/prominence CSV
   - participant summary CSV and Excel sheet
2. A `speaker_type` field is present everywhere relevant, using only these values: `participant`, `moderator`, `note_taker_summary`, `unclear`
3. Moderator rows are flagged and never counted as participant evidence
4. All CSVs parse cleanly with no broken quoting or missing columns

Required output:
- `{CASE}_schema_check.md`

## Gate 3 — Coding Integrity

After coding is complete and before theme writing, confirm:

1. Every segment ID maps to a source file, source type, question context, and code
2. Every quoted line in the report maps back to a coded segment
3. No moderator prompt appears in participant quotation evidence
4. Mixed-language excerpts preserve original-language authority
5. No orphan segments (unlinked to any code) or orphan codes (with no segments)

Required output:
- `{CASE}_coding_integrity_report.md`

## Gate 4 — Theme Integrity

After theme development and before final report writing, confirm:

1. Every final theme is traceable to coded segments
2. Every theme has: definition, contributing questions, contributing participants, supporting quotations from multiple participants, and a divergence or tension note
3. No theme-question claim is made without segment support
4. Final theme names are locked and used identically across all files, including any essential qualifiers

Required output:
- `{CASE}_theme_integrity_report.md`

## Gate 5 — Matrix and Prominence Integrity

After themes are locked and before final report writing, confirm:

1. The question-by-theme matrix matches coded segments, the theme file, and the summary tables
2. The prominence table matches the salience CSV, summary tables, and report wording
3. No all-high prominence pattern unless each high rating is individually justified
4. Each theme's prominence level is explicitly explained (most prominent, strong, or more focused / less prominent)
5. Every question-by-theme cell is either evidence-backed or explicitly marked Absent

Required output:
- `{CASE}_matrix_prominence_check.md`

## Gate 6 — Report Integrity

After the report draft and before final export, confirm:

1. The report is question-led with Q-by-Q sections before cross-question themes
2. Each question section includes: what participants said, deeper meaning, why it matters, key evidence, tensions/nuances, and link to final themes
3. The report includes richer quotations from multiple participants, a question-by-theme matrix, a theme prominence table, and charts or tables
4. The report does not confuse moderator prompts with participant evidence
5. The report does not make cross-case claims
6. Appendices include a method note, data sources, theme definitions, a prominence note, and a translation note

Required output:
- `{CASE}_report_integrity_check.md`

## Gate 7 — Final Cross-Check

After all fixes from Gates 1–6 and before marking the case complete, cross-check all artifacts against each other:

1. Theme names identical everywhere
2. Theme definitions aligned everywhere
3. Every quotation maps to a segment
4. Every segment maps to a source
5. Question-theme links are evidence-backed
6. Participant counts consistent
7. Source counts consistent
8. No moderator lines counted as participant evidence
9. All CSVs parse cleanly
10. No contradiction between report text and matrix/table outputs

Required output:
- `{CASE}_final_crosscheck_report.md`

## Completion Rule

A case is NOT complete until:
- All 7 gates pass
- All CSVs validate
- All files are internally consistent
- The final exported report is regenerated after the last fixes
- The submission folder is created with the full reviewer package

## Final Deliverables

The submission folder (`{CASE}_bundle/submission_data/`) must contain:
- `00_README.md`
- `01_{CASE}_final_report.md`
- `02_{CASE}_methodology.md`
- `03_{CASE}_key_quotations.csv`
- `04_{CASE}_question_by_theme_matrix.csv`
- `05_{CASE}_theme_prominence.csv`
- `06_{CASE}_participant_summary.csv`
- `07_{CASE}_summary_tables.md`

## Final Status Report

A case cannot be marked done without providing:
1. Exact files created
2. Exact checks run
3. Contradictions found
4. Fixes applied
5. Confirmation that the final exported report reflects the corrected files

## Origin
This specification was created on 2026-03-12 after the CASE_D1 reconciliation pass identified and corrected:
- Truncated Theme 3 name in 3 source CSVs
- Q3 × Theme 1 mismatch between report and matrix
- Unsupported Q4 claim in Theme 2 cross-question mapping
