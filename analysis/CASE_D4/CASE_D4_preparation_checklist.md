# CASE_D4 Preparation Checklist

## Scope
CASE_D4 (Day 4 — Elderly). This checklist tracks the completion of Gate 1 and Gate 2 preparation artifacts before coding begins.
Gate 3 and later status are tracked separately in `TASK.md` and the gate-specific Day 4 reports; this file remains intentionally limited to pre-coding preparation.

---

## Gate 1 — Source and Participant Integrity

### 1.1 Source inventory

- [x] All Day 4 raw files identified from `source_map_refresh.csv`
- [x] 5 transcripts confirmed: HWEL1AR, HWEL3AR, HWEL7AR, HWEL9AR, HWEL10AR
- [x] 7 note files confirmed: HWEL1NT1, HWEL3NT1, HWEL4NT1, HWEL6NT1, HWEL7NT1, HWEL10NT1, HWEL10NT2
- [x] 1 recommendation workbook confirmed: Health_Workshop_Suggestions Day 4.xlsx
- [x] Note-only tables identified: Table 4 (HWEL4NT1), Table 6 (HWEL6NT1)
- [x] Transcript-only table identified: Table 9 (HWEL9AR, no paired note)
- [x] Source register CSV created: `CASE_D4_source_register.csv` (13 rows)

### 1.2 Participant register

- [x] Candidate speaker labels extracted via `case_d4_label_probe.py`
- [x] Speaker labels cross-checked against note rosters (HWEL3NT1, HWEL10NT2)
- [x] Moderator assignments confirmed against `moderator_register_refresh.csv`
- [x] 7 moderators registered (D4_M01–D4_M07), including 2 note-only moderators with zero transcript turns
- [x] 29 participants registered (D4_P01–D4_P29) from 5 transcript sources
- [x] `speaker_type` limited to: participant, moderator (note_taker_summary and unclear not needed at Gate 1)
- [x] Turn and character counts computed from `d4_transcripts_extracted.json`
- [x] Participant register CSV created: `CASE_D4_participant_register.csv` (36 rows)

### 1.3 Question map

- [x] Seven-question structure confirmed from note templates and transcript moderator prompts
- [x] Arabic and English question text recorded for all seven questions
- [x] Question coverage assessed per source, including partial-coverage flags
- [x] Question map created: `CASE_D4_question_map.md`

### 1.4 Recommendation workbook handling

- [x] Day 4 workbook assessed: 39 substantive rows, generic User X labels, No/User/Suggestion structure
- [x] Classification locked as auxiliary structured recommendation material
- [x] Permitted and prohibited uses documented
- [x] Recommendation usage rule created: `CASE_D4_recommendation_usage_rule.md`

### 1.5 Preparation checklist

- [x] This checklist created: `CASE_D4_preparation_checklist.md`

---

## Gate 2 — Structured Artifact Schema Lock

### 2.1 Schema check

- [x] CSV headers locked from CASE_D1 baseline for all downstream structured artifacts
- [x] `speaker_type` rule locked (participant / moderator / note_taker_summary / unclear)
- [x] Working codebook format decision documented (markdown baseline from CASE_D1)
- [x] Source-specific handling notes documented (HWEL10AR summary-style caution, note-only table limits, transcript-only HWEL9AR caveat)
- [x] Schema check created: `CASE_D4_schema_check.md`

### 2.2 Familiarisation memos

- [x] Familiarisation memo created: `CASE_D4_familiarisation_memo.md`
- [x] Source sensitivity memo created: `CASE_D4_source_sensitivity_memo.md`
- [x] Language and translation memo created: `CASE_D4_language_memo.md`
- [x] Boundary memo created: `CASE_D4_boundary_memo.md`

---

## Gate 1 status
**Complete.** All five Gate 1 artifacts are written and grounded in extracted Day 4 evidence.

## Gate 2 status
**Complete.** Schema check and all four familiarisation memos are written and grounded in Day 4 source evidence.
