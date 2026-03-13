---
description: 7-gate controlled workflow for within-case day-level thematic analysis (CASE_D2 onward)
---

# Within-Case Day-Level Thematic Analysis — 7-Gate Controlled Workflow

This workflow applies to CASE_D2 and every subsequent day-case (CASE_D3, CASE_D4, CASE_D5).
No case may be marked complete until all 7 gates pass.
The CASE_D1 reconciliation pass established the standard; this workflow is stricter.

## Variables

- `{CASE}` = case ID, e.g. `CASE_D2`
- `{DAY}` = day label, e.g. `Day 2`
- `{ANALYSIS_DIR}` = `analysis/0X_{DAY_LOWER}_thematic_analysis`
- `{BUNDLE_DIR}` = `analysis/case_bundles/{CASE}_bundle`
- `{SUBMISSION_DIR}` = `{BUNDLE_DIR}/submission_data`

---

## PRE-CHECK — Corpus Amendment Trigger

Before Gate 1, confirm whether `{CASE}` has received any corpus amendment since the last approved inventory or case analysis.

Check specifically:
- new transcript files
- new note-taker files
- removed or superseded raw files
- new structured recommendation sheets or other post-workshop summary artifacts
- changed filename irregularities or pairing assumptions

If materially expanded core data were added, DO NOT patch the earlier case outputs. Refresh the inventory and rerun the case from Gate 1. Earlier outputs remain archived for audit only and the rerun becomes the superseding version.

If only auxiliary structured recommendation material was added, document the treatment decision explicitly before continuing. Auxiliary recommendation sheets do not generate themes and do not count as transcript-equivalent participant evidence unless row-level traceability is demonstrated.

---

## GATE 1 — Source and Preparation Integrity

**When:** Before any coding begins.

Confirm:
1. Final source list for {CASE} (all raw files → derived files)
2. Which files are transcripts vs notes
3. Participant list / role list if available from transcript speaker labels
4. Moderator vs participant distinction for every speaker
5. Question map reconciled against the actual discussion guide
6. Prepared files, source map, and provenance links are complete

**Required outputs:**
- `{CASE}_source_register.csv`
- `{CASE}_participant_register.csv`
- `{CASE}_question_map.csv`
- `{CASE}_preparation_checklist.md`

**Gate passes when:** All 4 outputs exist and are internally consistent. No coding may begin before this.

---

## GATE 2 — Structured Artifact Schema Lock

**When:** After Gate 1, before analysis begins.

Confirm:
1. Exact same column schema as CASE_D1 for:
   - coded segments CSV
   - working codebook CSV
   - question-by-theme matrix CSV
   - excerpt bank CSV
   - salience/prominence CSV
   - participant summary CSV/Excel
2. `speaker_type` field added everywhere relevant, with values:
   - `participant`
   - `moderator`
   - `note_taker_summary`
   - `unclear`
3. Moderator rows must NEVER count as participant evidence
4. All CSVs must parse cleanly (no broken quoting, no missing columns)

**Required output:**
- `{CASE}_schema_check.md`

**Gate passes when:** Schema check confirms identical structure to CASE_D1 with speaker_type field added.

---

## GATE 3 — Coding Integrity

**When:** After coding is complete, before theme writing.

Confirm:
1. Every segment ID maps to: source file, source type, question context, code
2. Every quoted line in the report maps back to a coded segment
3. No moderator prompt appears in participant quotation evidence
4. Mixed-language excerpts preserve original-language authority
5. No orphan segments (segments not linked to any code)
6. No orphan codes (codes with no segments)

**Required output:**
- `{CASE}_coding_integrity_report.md`

**Gate passes when:** Zero integrity failures found, or all failures are resolved before proceeding.

---

## GATE 4 — Theme Integrity

**When:** After theme development, before final report writing.

Confirm:
1. Every final theme is traceable to coded segments
2. Every theme has:
   - definition
   - contributing questions
   - contributing participants
   - supporting quotations (from multiple participants)
   - divergence/tension note
3. No theme-question claim is made without segment support
4. Final theme names are locked and used identically across all files
5. Theme names include any essential qualifiers (e.g. "around children")

**Required output:**
- `{CASE}_theme_integrity_report.md`

**Gate passes when:** All themes are fully traceable and named consistently.

---

## GATE 5 — Matrix and Prominence Integrity

**When:** After themes are locked, before final report writing.

Confirm:
1. Question-by-theme matrix matches:
   - coded segments
   - theme file
   - summary tables
2. Prominence table matches:
   - salience CSV
   - summary tables
   - report wording
3. No all-high pattern unless justified explicitly per theme
4. Each theme's prominence level is explained clearly:
   - most prominent
   - strong
   - more focused / less prominent
5. Every Q×Theme cell is evidence-backed or explicitly marked Absent

**Required output:**
- `{CASE}_matrix_prominence_check.md`

**Gate passes when:** Matrix, prominence table, and report wording are fully aligned.

---

## GATE 6 — Report Integrity

**When:** After report draft, before final export.

Confirm:
1. Report is question-led (Q-by-Q sections before cross-question themes)
2. Each question section includes:
   - what participants said
   - deeper meaning
   - why it matters
   - key supporting evidence
   - tensions/nuances
   - link to final themes
3. Report includes:
   - richer quotations from multiple participants
   - question-by-theme matrix reference
   - theme prominence table
   - charts/tables or references to them
4. Report does NOT:
   - confuse moderator prompts with participant evidence
   - make cross-case claims
   - use D1SEG-style IDs for a different day
5. Appendices include: method note, data sources, theme definitions, prominence note, translation note

**Required output:**
- `{CASE}_report_integrity_check.md`

**Gate passes when:** All structural and evidentiary checks pass.

---

## GATE 7 — Final Cross-Check

**When:** After all fixes from Gates 1–6, before marking complete.

Cross-check ALL of these against each other:
- final report
- methodology
- coded segments CSV
- codebook CSV
- question-by-theme matrix CSV
- excerpt bank CSV
- salience/prominence CSV
- participant summary CSV/Excel
- summary tables
- charts/tables

Check specifically:
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

**Required output:**
- `{CASE}_final_crosscheck_report.md`

**Gate passes when:** Zero contradictions remain, or all contradictions are resolved and the report is regenerated.

---

## COMPLETION RULE

{CASE} is NOT complete until:
- All 7 gates pass
- All CSVs validate
- All files are internally consistent
- Final exported report is regenerated after the last fixes
- Submission folder is created with the full reviewer package

## FINAL DELIVERABLES

Before marking {CASE} complete, the following must exist:

In `{BUNDLE_DIR}/submission_data/`:
- `00_README.md`
- `01_{CASE}_final_report.md`
- `02_{CASE}_methodology.md`
- `03_{CASE}_key_quotations.csv`
- `04_{CASE}_question_by_theme_matrix.csv`
- `05_{CASE}_theme_prominence.csv`
- `06_{CASE}_participant_summary.csv`
- `07_{CASE}_summary_tables.md`

In `{BUNDLE_DIR}/`:
- All analysis artifacts (coding, themes, memos, context, validation, reporting_outputs)

## FINAL STATUS REPORT

Do NOT say "done" until providing:
1. Exact files created
2. Exact checks run
3. Contradictions found
4. Fixes applied
5. Confirmation that the final exported report reflects the corrected files
