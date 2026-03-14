# CASE_D3 Preparation Checklist

## Case identity
- **Case**: CASE_D3
- **Day**: Day 3 — Adults
- **Stakeholder focus**: Adult wellbeing
- **Status**: Gate 1 control files created from the refreshed Day 3 source base; coding has not started yet.

## Source inventory confirmation
- [x] 5 transcript files identified (`HWAD1AR`, `HWAD3AR`, `HWAD4AR`, `HWAD6AR`, `HWAD10AR`)
- [x] 11 note-taker files identified (`HWAD0NT1`, `HWAD1NT1`, `HWAD1NT2`, `HWAD3NT1`, `HWAD5NT1`, `HWAD7NT1`, `HWAD9NT1`, `HWAD10NT1`, `HWAD10NTI`, `HWAD11NT2`, `HWAD11NT3`)
- [x] 1 recommendation workbook identified (`Health_Workshop_Suggestions Day 3.xlsx`)
- [x] 0 temp/lock files identified in the refreshed foundation
- [x] Total: 17 files (matches refreshed corpus foundation)

## Source register
- [x] `CASE_D3_source_register.csv` created with 17 entries
- [x] Each source classified by `file_type` and `source_role`
- [x] Transcript-note relationships copied from the approved D1-D4 foundation and rechecked against the actual Day 3 raw folder
- [x] Note-only and transcript-only cases explicitly documented

## Participant register
- [x] `CASE_D3_participant_register.csv` created with transcript-backed participant, moderator, and unclear rows
- [x] Transcript content extracted to `_working/d3_transcripts_extracted.json` and `_working/d3_notes_extracted.json`
- [x] Moderator assignments cross-checked against `moderator_register_refresh.csv` and transcript context
- [x] Register currently contains `25` participant rows, `10` moderator rows, and `2` unclear rows
- [x] Additional flowing material in `HWAD3AR` and `HWAD6AR` explicitly retained as `unclear` rather than over-assigned to named participants

## Moderator exclusion
- [x] Moderator logic source identified: `analysis/corpus_refresh/moderator_register_refresh.csv`
- [x] Allowed `speaker_type` values locked: `participant`, `moderator`, `note_taker_summary`, `unclear`
- [x] Transcript-level moderator identification completed where labels were explicit or transcript openings named the facilitator
- [x] Moderator text must remain contextual only and excluded from participant evidence, quotation counts, and theme support

## Question map
- [x] `CASE_D3_question_map.md` created
- [x] Day 3 guide wording recovered from note templates and transcript prompts
- [x] Question coverage by source documented with explicit `Y`, `partial`, and `—` boundaries

## Recommendation workbook
- [x] `CASE_D3_recommendation_usage_rule.md` created
- [x] Workbook classified as auxiliary structured recommendation material
- [x] Permitted and prohibited uses documented
- [x] Labeling requirement specified

## Known preparation issues
1. **Note-only tables**: tables `0`, `5`, `7`, `9`, and `11` have notes but no current transcript file.
2. **Transcript-only tables**: tables `4` and `6` have no paired note file in the current raw folder.
3. **Irregular filename**: `HWAD10NTI.docx` likely belongs with table 10 but requires explicit tooling caution.
4. **Weak speaker traceability**: `HWAD6AR` preserves substantial discussion but only one stable named participant label.
5. **Partial speaker recovery**: `HWAD3AR` contains recoverable short labels plus additional flowing unattributed material.
6. **Recommendation workbook traceability**: generic user labels prevent transcript-equivalent use.

## Gate 1 status
All Gate 1 deliverables created:
- [x] Source register (CSV)
- [x] Participant register (CSV)
- [x] Question map (MD)
- [x] Preparation checklist (this file)
- [x] Recommendation-usage rule note (MD)

## Immediate next action
- [x] Run the CASE_D3 `.docx` extraction script in `_working/`
- [x] Read extracted transcripts and notes
- [x] Build the participant register and question map from extracted Day 3 material
- [ ] Create the CASE_D3 familiarisation materials: source sensitivity memo, language memo, and case-boundary memo
- [ ] Lock Gate 2 with `CASE_D3_schema_check.md`
- [ ] Build the CASE_D3 working codebook before segment-level coding begins
