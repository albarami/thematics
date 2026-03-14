# Master Day-by-Day Case Analysis Workflow

## Purpose
This document is the master step-by-step workflow for completing one stakeholder case analysis without missing any required analytic or documentation step.

It is designed to be reused for each day-based case in the project.

## Current assessed scope
The current active assessment scope covers CASE_D1 through CASE_D4 only:

- `CASE_D1` - Day 1 Childhood
- `CASE_D2` - Day 2 Youth
- `CASE_D3` - Day 3 Adults
- `CASE_D4` - Day 4 Elderly

The workflow captures the end-to-end case process established through the completed Day 1 analysis and turns it into a reusable case checklist.

## How to use this workflow
Apply the steps below to one case at a time.

Do not skip ahead. Complete the case in sequence from boundary definition through final reporting, correction pass, and project-level documentation updates.

Within-case integrity must be preserved until a later cross-case stage. This means that one case should not be interpreted through another case while the case-level analysis is still being built.

## Non-negotiable rules for every case
- Treat one day folder as one stakeholder case.
- Treat transcript files as primary verbal data.
- Treat note-taker files as contextual and triangulation data.
- Keep raw files unchanged.
- Keep all derived analytic files inside the `analysis/` workspace.
- Preserve provenance from source file to later analytic outputs.
- Treat original-language material as authoritative where mixed-language content exists.
- Use salience or prevalence only as a supplementary layer after theme development.
- Use participant summaries, question matrices, theme evidence sheets, tables, and visuals only as reporting-support layers after coding and theme development.
- Derive charts, graphs, and tables from structured sheets rather than impressionistic judgement.
- Use quotations from multiple participants where feasible so reporting does not rely on a narrow range of voices.
- Treat moderator prompts, facilitator probes, and discussion-guide wording as contextual framing only, not as participant evidence.
- Do not make cross-case claims inside the case-level analysis outputs.
- Update `TASK.md` when a major workflow stage is completed.

## Required case-level outputs
The following outputs form the standard case artifact set.

| Area | Required output |
|---|---|
| Context | `[CASE_ID]_question_map.csv` |
| Coding | `[CASE_ID]_coded_segments.csv` |
| Coding | `[CASE_ID]_working_codebook.csv` |
| Memos | `[CASE_ID]_coding_reflection_memo.md` |
| Memos | `[CASE_ID]_source_sensitivity_memo.md` |
| Memos | `[CASE_ID]_language_translation_memo.md` |
| Memos | `[CASE_ID]_boundary_memo.md` |
| Themes | `[CASE_ID]_candidate_theme_development.csv` |
| Themes | `[CASE_ID]_final_themes.md` |
| Themes | `[CASE_ID]_excerpt_bank.csv` |
| Themes | `[CASE_ID]_salience_matrix.csv` |
| Reporting outputs | update `analysis/reporting_outputs/Participants_Master.xlsx` |
| Reporting outputs | update `analysis/reporting_outputs/Question_Matrices.xlsx` |
| Reporting outputs | update `analysis/reporting_outputs/Theme_Evidence.xlsx` |
| Reporting outputs | create or update case tables in `analysis/reporting_outputs/tables/` |
| Reporting outputs | create or update case visuals in `analysis/reporting_outputs/visuals/` |
| Reporting outputs | keep `analysis/reporting_outputs/reporting_output_method_note.md` aligned with the active reporting framework |
| Reports | `[CASE_ID]_within_case_thematic_report.md` |
| Reports | `[CASE_ID]_final_academic_report.md` |
| Reports | `[CASE_ID]_final_academic_report_revised.md` when a formal revision pass is required |
| Reports | `[CASE_ID]_methodology.md` |
| Validation | `[CASE_ID]_csv_validation_report.md` |
| Context / Validation | `[CASE_ID]_guide_reconciliation_note.md` when guide clarification or late reconciliation is required |
| Project logs | update `analysis/04_prepared_data/processing_log.csv` |
| Project logs | update `analysis/04_prepared_data/audit_trail.csv` |
| Project logs | update translation decision records when language handling requires it |
| Project tracking | update `TASK.md` |

## Step-by-step workflow

### Step 1. Confirm the case boundary and source set
Define the target case clearly before beginning analytic work.

Checklist:
- Confirm the `CASE_ID`.
- Confirm the day folder and stakeholder group.
- Confirm which prepared transcript files belong to the case.
- Confirm which prepared note files belong to the case.
- Confirm any auxiliary files that are excluded or require a separate documented decision.
- Confirm that the case will be analysed on its own before any cross-case comparison.

Output expectation:
- a clearly bounded case workspace and a defensible source set for that case

### Step 2. Review the governing method documents
Before starting the case analysis, review the project-level source-of-truth documents.

Checklist:
- Review `analysis/00_protocol/thematic_analysis_protocol.md`.
- Review `analysis/03_methods/full_project_methodology.md`.
- Review `analysis/03_methods/methods_skeleton.md`.
- Review this workflow file.
- Review `TASK.md` so the case work is tracked correctly.

Output expectation:
- the case analysis is anchored to the current documented method rather than memory alone

### Step 3. Create or verify the case analysis workspace
Make sure the case analysis folder contains the working structure needed for the full workflow.

Checklist:
- Confirm or create the case folder.
- Confirm or create subfolders for `context`, `coding`, `memos`, `themes`, `reports`, and `validation`.
- Confirm that filenames will use the correct `CASE_ID`.
- Confirm that the workspace remains separate from the raw source folders.

Output expectation:
- a stable case workspace ready for the full end-to-end process

### Step 4. Re-read the prepared case materials closely
Re-read the prepared sources within the case only.

Checklist:
- Read all prepared transcript files for the case.
- Read all prepared note files for the case.
- Note repeated concerns, tensions, emphases, gaps, and uncertainties.
- Note where the notes are more compressed than the transcripts.
- Note any source pairing ambiguity.
- Note any language or translation issues that will need careful handling.

Output expectation:
- grounded familiarity with the case material before coding begins

### Step 5. Build the question-context map
Create a case-specific question map so excerpts can be interpreted in relation to the discussion sequence.

Checklist:
- Identify the discussion questions for the target day.
- Map the questions in sequence.
- Preserve both wording and question function where possible.
- Use the map as contextual support only.
- Do not turn questions into themes.
- If guide wording is uncertain or clarified later, document the reconciliation explicitly.

Required output:
- `context/[CASE_ID]_question_map.csv`

Conditional output:
- `context/[CASE_ID]_guide_reconciliation_note.md` if reconciliation is needed

### Step 6. Segment the case material into coded meaning units
Create the coded segments dataset directly from the prepared case sources.

Checklist:
- Segment the case material into meaning units.
- Keep segments flexible in length according to interpretive relevance.
- Preserve provenance to source file and question context where available.
- Capture concerns, meanings, tensions, descriptions, and proposed solutions.
- Avoid coding by mechanical line count.

Required output:
- `coding/[CASE_ID]_coded_segments.csv`

### Step 7. Build the working codebook
Turn the developing coding logic into a usable case-level codebook.

Checklist:
- Consolidate recurring codes.
- Keep code labels clear and analytically useful.
- Record short definitions or analytic comments where needed.
- Allow both close-to-data codes and more interpretive codes.
- Treat indicator terms or pattern cues as retrieval and indexing aids, not as automatic proof of thematic support.
- Revise the codebook as coding understanding develops.

Required output:
- `coding/[CASE_ID]_working_codebook.csv`

### Step 8. Write the four required reflexive and methodological memos
Memoing is mandatory, not optional.

Checklist:
- Write the coding reflection memo.
- Write the source sensitivity memo.
- Write the language and translation memo.
- Write the boundary memo.
- Record uncertainties, assumptions, tensions, and risks of overreach.
- Record how source compression or mixed-language content affects interpretation.

Required outputs:
- `memos/[CASE_ID]_coding_reflection_memo.md`
- `memos/[CASE_ID]_source_sensitivity_memo.md`
- `memos/[CASE_ID]_language_translation_memo.md`
- `memos/[CASE_ID]_boundary_memo.md`

### Step 9. Develop candidate themes
Move from codes to broader patterned meanings within the case.

Checklist:
- Group related codes into candidate themes.
- Test whether grouped segments express a broader shared meaning in context, not just repeated topic words.
- Check whether the candidate theme is coherent across case materials.
- Use keyword or pattern hits only to retrieve candidate material for review, never as an automatic theme-assignment rule.
- Allow segments to support a theme even where no expected keyword is present if close reading, question context, speaker role, discussion flow, or memoed interpretation justify inclusion.
- Interpret Arabic concepts, local cultural meanings, tensions, and contradictions in context rather than by literal term matching alone.
- Separate major themes from tensions, divergences, and lower-level observations.
- Do not use salience counts to generate themes.

Required output:
- `themes/[CASE_ID]_candidate_theme_development.csv`

### Step 10. Refine final themes and supporting evidence
Refine candidate themes into defensible final themes and link them to evidence.

Checklist:
- Define the final themes clearly.
- Check theme boundaries so themes remain distinct.
- Identify supporting excerpts.
- Record source spread and divergent material.
- Confirm that supporting evidence reflects contextual interpretation and memo-based reasoning rather than keyword repetition alone.
- Confirm that the final themes explain the case better than a list of topics would.

Required outputs:
- `themes/[CASE_ID]_final_themes.md`
- `themes/[CASE_ID]_excerpt_bank.csv`

### Step 11. Add the supplementary salience layer
Create the salience layer only after the final themes exist.

Checklist:
- Rate relative prominence only after theme development.
- Keep the salience layer descriptive rather than determinative.
- Avoid treating frequency as proof of validity.
- Explain why some retained themes are broader, more concentrated, or more central than others.
- Keep the salience judgement case-bounded.

Required output:
- `themes/[CASE_ID]_salience_matrix.csv`

### Step 12. Build the participant-level summary sheet
Create the participant register entries for the case where participant identity information or defensible role labels are available in the source material.

Checklist:
- Record the participant identifier or role label.
- Record the case and day label.
- Record the source file.
- Record the question or questions contributed to.
- Write a short summary of what the participant mainly said.
- Link the participant summary to the relevant codes and themes.
- Record notable quotations.
- Record language notes where relevant.
- Exclude moderator or question-like framing from participant-summary content.
- Use the participant sheet to strengthen quotation diversity and balanced reporting.

Required output:
- update `analysis/reporting_outputs/Participants_Master.xlsx`

### Step 13. Build the question-level analytic matrices
Create a matrix for each discussion question so the reporting chain from question to response pattern to theme is explicit.

Checklist:
- Record the question ID.
- Record the case ID.
- Record the participant identifier or role where available.
- Record the source file.
- Summarise the response pattern.
- Link the response to the relevant code.
- Link the response to the relevant final theme.
- Record relative prominence within the question.
- Record a quotation reference.
- Record divergence or tension notes where relevant.
- Keep moderator prompts and guide wording in contextual notes only, not in participant-response or quotation fields.

Required output:
- update `analysis/reporting_outputs/Question_Matrices.xlsx`

### Step 14. Build the theme evidence workbook and reporting tables
Consolidate theme evidence into structured workbook entries and reporting tables.

Checklist:
- Record the theme name.
- Record the case ID.
- Record the linked question ID where relevant.
- Record the participant identifier or role.
- Record source file and source type.
- Record excerpt reference and quotation.
- Summarise the analytic point supported by the quotation.
- Record prominence notes.
- Record divergence or tension where relevant.
- Exclude moderator prompts from participant quotation counts and theme-evidence counts.
- Build reporting tables from the structured sheets rather than ad hoc judgement.

Required outputs:
- update `analysis/reporting_outputs/Theme_Evidence.xlsx`
- create or update case tables in `analysis/reporting_outputs/tables/`

### Step 15. Generate descriptive visuals from structured sheets
Create charts or heatmaps only after the structured reporting sheets are in place.

Checklist:
- Generate a case-level theme prominence chart where useful.
- Generate a theme-by-question chart where useful.
- Generate a question-to-theme table or heatmap where useful.
- Generate a source-spread table or heatmap where useful.
- Confirm that each visual is derived from the structured workbook layer.
- Confirm that visuals are descriptive and explanatory only.
- Confirm that visuals do not replace thematic interpretation.

Required output:
- create or update case visuals in `analysis/reporting_outputs/visuals/`

### Step 16. Write the within-case thematic report
Produce the first formal case report grounded in the case artifact set and the reporting-output layer.

Checklist:
- Write the case purpose and scope.
- State the within-case boundary clearly.
- Describe the data used and source roles.
- Explain the analytic process.
- Present the final themes with supporting evidence.
- Include question-by-question analysis.
- Include richer quotation support from multiple participants where feasible.
- Distinguish transcript-derived quotations from note-derived quotations.
- Keep moderator or facilitator wording in contextual framing only rather than in evidentiary quotation lists.
- Include tensions, limitations, and the boundary statement.
- Avoid cross-case claims.

Required output:
- `reports/[CASE_ID]_within_case_thematic_report.md`

### Step 17. Write the final academic report
Produce the fuller academic report for the case.

Checklist:
- Write the case report in a form suitable for academic use.
- Keep the interpretation within the case boundary.
- Link the reporting clearly to the case evidence.
- Make sure the report aligns with the theme set, excerpt bank, salience layer, participant sheet, question matrices, and theme evidence workbook.
- Include a matrix for each question.
- Include tables summarising major response patterns.
- Include a theme prominence table.
- Include charts or graphs where useful.

Required output:
- `reports/[CASE_ID]_final_academic_report.md`

### Step 18. Write the revised final report when revision is required
If the case report needs structural, analytic, or presentation revision, preserve that work as a revised report rather than silently overwriting the earlier file.

Checklist:
- Apply the requested revisions systematically.
- Re-check theme consistency after revision.
- Re-check wording around prominence, boundaries, interpretation, and quotation support.
- Make sure revised sections remain aligned with the case artifacts and reporting-output sheets.
- Preserve the distinction between findings and supplementary salience or visual layers.

Conditional output:
- `reports/[CASE_ID]_final_academic_report_revised.md`

### Step 19. Write the case-level methodology file
Create a standalone methodology file for the case.

Checklist:
- Describe the method as applied to the case.
- Keep the methodology focused on approach, data basis, procedure, reporting infrastructure, language handling, transparency, and limitations.
- Keep it as methodology rather than a progress note.
- Make sure it is consistent with the project-level methodology.

Required output:
- `reports/[CASE_ID]_methodology.md`

### Step 20. Run the correction and consistency pass
A full correction pass is required before the case is considered complete.

Checklist:
- Validate all case CSV files for parse integrity.
- Repair malformed quoting or broken fields where necessary.
- Confirm that the question map is accurate.
- Reconcile the question map against the guide if needed.
- Confirm that reports, themes, excerpts, salience records, participant sheets, question matrices, and theme evidence records are mutually consistent.
- Confirm that quotation coverage is not concentrated narrowly where broader participant support is available.
- Confirm that no cross-case language has slipped into the case outputs.
- Confirm that mixed-language handling remains methodologically consistent.

Required output:
- `validation/[CASE_ID]_csv_validation_report.md`

Conditional output:
- `context/[CASE_ID]_guide_reconciliation_note.md`

### Step 21. Update project-level documentation
The case is not complete until the project-level documentation has been updated.

Checklist:
- Add the relevant entry to `analysis/04_prepared_data/processing_log.csv`.
- Add the relevant entry to `analysis/04_prepared_data/audit_trail.csv`.
- Update translation decision records when language handling decisions have been made.
- Keep `analysis/reporting_outputs/reporting_output_method_note.md` aligned with any reporting-structure changes.
- Update `TASK.md` immediately for completed major case milestones.

Output expectation:
- the case work is integrated into the live project documentation layer

### Step 22. Run the final completion check
Before moving to the next case, confirm that the full workflow has been completed.

Final completion checklist:
- Every required case artifact exists.
- The case boundary has been maintained throughout.
- The source roles remain consistent with the protocol.
- The memos exist and reflect real analytic judgement.
- The final themes are supported by the case evidence.
- The salience layer is present and remains supplementary.
- The participant sheet, question matrices, and theme evidence workbook entries exist.
- The tables and visuals are derived from structured sheets.
- The reports and methodology file are internally consistent.
- The validation and reconciliation records exist where needed.
- The processing log, audit trail, reporting note, and task tracker are updated.

## Minimum completion gate for any new case
Do not call a case complete unless all of the following are true:

- the case artifact set is complete
- the participant sheet, question matrices, and theme evidence records exist
- the reporting tables and visuals exist where appropriate
- the correction pass is complete
- the project logs are updated
- the case methodology exists
- the case report exists
- the final theme set exists
- the workflow has been checked step by step against this file

## Summary
This workflow is the master checklist for repeating the full case-analysis process from Day 1 across the remaining stakeholder cases. It now requires structured reporting sheets, question matrices, participant summaries, stronger quotation diversity, tables, and descriptive visuals so that future case work can be completed without skipping required analytic or reporting steps.
