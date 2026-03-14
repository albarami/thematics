# CASE_D2 Preparation Checklist

## Case identity
- **Case**: CASE_D2
- **Day**: Day 2 — Youth
- **Stakeholder focus**: Youth wellbeing
- **Status**: Gate 1 and Gate 2 complete; Gate 3 coding layer reviewed, tightened, and documented through the current coding integrity report

## Source inventory confirmation
- [x] 7 transcript files identified (`HWYO0AR`, `HWYO3AR`, `HWYO4AR`, `HWYO7AR`, `HWYO9AR`, `HWYO10AR`, `HWYO11AR`)
- [x] 10 note-taker files identified (`HWYO0NT1`, `HWYO1NT`, `HWYO3NT1`, `HWYO4NT1`, `HWYO5NT1`, `HWYO6NT1`, `HWYO9NT1[7]`, `HWYO9NT2`, `HWYO10NT1`, `HWYO11NT2`)
- [x] 1 recommendation workbook identified (`Health_Workshop_Suggestions Day 2.xlsx`)
- [x] 0 temp/lock files identified in the refreshed foundation
- [x] Total: 18 files (matches refreshed corpus foundation)

## Source register
- [x] `CASE_D2_source_register.csv` created with 18 entries
- [x] Each source classified by `file_type` and `source_role`
- [x] Transcript-note relationships copied from the approved D1-D4 foundation
- [x] Note-only and transcript-only cases explicitly documented

## Participant register
- [x] `CASE_D2_participant_register.csv` created with transcript-backed participant, moderator, and unclear rows
- [x] Transcript content extracted to `_working/d2_transcripts_extracted.json` and `_working/d2_notes_extracted.json`
- [x] Moderator assignments cross-checked against `moderator_register_refresh.csv` and transcript context
- [x] Participant rows restricted to transcript-backed identities or explicitly marked unclear where identity recovery failed

## Moderator exclusion
- [x] Moderator logic source identified: `analysis/corpus_refresh/moderator_register_refresh.csv`
- [x] Allowed `speaker_type` values locked: `participant`, `moderator`, `note_taker_summary`, `unclear`
- [x] Transcript-level moderator identification completed where labels were explicit or transcript openings named the facilitator
- [x] Moderator text must remain contextual only and excluded from participant evidence, quotation counts, and theme support

## Question map
- [x] `CASE_D2_question_map.md` created
- [x] Day 2 guide wording recovered from the repeated Q1–Q7 note templates and supporting transcript prompts
- [x] Question coverage by source documented with explicit `Y`, `?`, `partial`, and `—` boundaries

## Recommendation workbook
- [x] `CASE_D2_recommendation_usage_rule.md` created
- [x] Workbook classified as auxiliary structured recommendation material
- [x] Permitted and prohibited uses documented
- [x] Labeling requirement specified

## Participant workbook
- [x] `CASE_D2_participant_workbook.xlsx` created from the reviewed Day 2 coded base

## Coding integrity report
- [x] `CASE_D2_coding_integrity_report.md` created from the reviewed Day 2 coded base and current linked Gate 3 artifacts

## Known preparation issues
1. **Binary source format**: raw Day 2 transcripts and notes are `.docx` files and require extraction before close reading or participant mapping.
2. **Speaker-label variation**: the refreshed foundation already identified mixed quality across Day 2 transcripts.
3. **No-label transcripts**: `HWYO3AR` and `HWYO7AR` were previously flagged as yielding no extracted speaker labels.
4. **Irregular filename**: `HWYO1NT.docx` uses a non-standard note suffix.
5. **Irregular filename**: `HWYO9NT1[7].docx` contains square brackets and may need special handling in scripts.
6. **Recommendation workbook traceability**: generic user labels prevent transcript-equivalent use.

## Immediate next action
- [x] Run the CASE_D2 `.docx` extraction script in `_working/`
- [x] Read extracted transcripts and notes
- [x] Build the participant register and question map from extracted Day 2 material
- [x] Create the CASE_D2 familiarisation materials: source sensitivity memo, language memo, and case-boundary memo
- [x] Lock Gate 2 with `CASE_D2_schema_check.md`
- [x] Build the CASE_D2 working codebook before segment-level coding begins
- [x] Promote the cleaned Day 2 segment base to `CASE_D2_coded_segments.csv`
- [x] Build `CASE_D2_participant_summary.csv` and `CASE_D2_question_evidence_table.csv` from the promoted coded-segment base
- [x] Apply first-pass codebook-based recoding beyond provisional `general_response` and `moderator_context`
- [x] Manually review and tighten the first-pass Day 2 coding layer
- [x] Build `CASE_D2_participant_workbook.xlsx` from the reviewed Day 2 coded base
- [x] Build `CASE_D2_coding_integrity_report.md` from the reviewed Day 2 coding layer
- [ ] Build the remaining theme-dependent Gate 4 and Gate 5 artifacts after theme development is completed and locked
