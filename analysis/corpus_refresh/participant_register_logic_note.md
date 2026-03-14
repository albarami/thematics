# Participant Register Logic Note (D1-D4 Only)

## Scope
This note defines the refreshed participant-register logic, moderator-register logic, and source-role rules for the D1-D4 assessment scope. The assessed cases are CASE_D1, CASE_D2, CASE_D3, and CASE_D4.

## Foundation rule
No old participant assumptions, speaker counts, or prior case outputs are reused. Every participant and role decision must be rebuilt from the refreshed raw corpus, the restored method baseline, and transcript context.

## Source-role rules
- **Transcript files** (`*AR.docx`) are the primary verbal data source for participant and moderator extraction.
- **Note-taker files** (`*NT*.docx`) are contextual and triangulation data. They may preserve role clues but do not override transcript speaker attribution.
- **Recommendation workbooks** (`Health_Workshop_Suggestions Day X.xlsx`) are auxiliary structured recommendation material. They may support Q6/Q7 and policy-facing reporting but are not transcript-equivalent participant evidence and must not generate themes.
- **Temp/lock files** (`_$*`, `~$*`) are excluded from analysis entirely.

## Allowed `speaker_type` values
- `participant`
- `moderator`
- `note_taker_summary`
- `unclear`

## Moderator logic
1. Use `analysis/corpus_refresh/moderator_register_refresh.csv` as the first-pass moderator roster for Days 1-4.
2. Each moderator row now carries a `transcript_match_confidence` field: `confirmed`, `probable`, `unclear`, or `no_transcript_available`.
3. **confirmed** means the moderator name or a close variant appears in the transcript text with an explicit moderator role designation.
4. **probable** means the transcript contains a generic moderator/session-manager role label and the workbook assigns this person, but the transcript does not contain the moderator's name.
5. **unclear** means the transcript has no moderator role label and no name match, even though the workbook assigns this person.
6. **no_transcript_available** means no transcript file exists for that table number, so no transcript-level evidence can confirm or deny the assignment.
7. During the preparation stage, moderator speech must be identified using both the register and transcript context. A `probable` or `unclear` moderator must not be silently promoted to `confirmed` without new evidence.

## Participant logic
1. Extract speaker labels fresh from the refreshed transcript files only after the derived-text layer is rebuilt.
2. Any speaker label not matched to the moderator roster should not automatically become `participant`; it must be judged from transcript context.
3. Named speakers, defensible role labels, and generic speaker labels may be classified as `participant` only when the transcript preserves substantive contribution.
4. Brief acknowledgements, turn-management speech, or organizational instructions must not be treated as participant evidence.
5. Note-only sources can support contextual role awareness but should not create transcript-equivalent participant rows unless later source evidence makes that defensible.

## Note-taker summary logic
- Use `note_taker_summary` only for note-derived summaries or summarized contributions that cannot be tied cleanly to a transcript speaker turn.
- Do not merge note-taker summary rows into participant quotation counts.
- If a note file contains an attributed speaker label that can later be confirmed in a transcript, the transcript remains authoritative.

## Pairing confidence rules
- `confirmed`: exact shared source code prefix with both transcript and note files present in current scan.
- `probable`: likely pairing supported by the source code prefix, but affected by filename irregularity (e.g. HWAD10NTI.docx).
- `ambiguous`: multiple plausible pairings or unresolved evidence conflict.
- `none`: no defensible pairing available (note-only, transcript-only, or temp/lock).

## Day-level participant-availability summary
- **Day 1 (CASE_D1)**: 7 transcripts with mixed speaker-label styles (named, role-labelled, generic Speaker N, moderator-role labels). Participant extraction feasible but requires careful normalization.
- **Day 2 (CASE_D2)**: 7 transcripts with variable speaker-label quality. Two transcripts (HWYO3AR, HWYO7AR) yielded NO extracted speaker labels, which limits participant identification for those tables.
- **Day 3 (CASE_D3)**: 5 transcripts. Several use descriptive inline role labels rather than clean "Name:" format. HWAD1AR has confirmed moderator naming. Others are sparser.
- **Day 4 (CASE_D4)**: 5 transcripts. HWEL1AR and HWEL9AR have confirmed moderator labels. Others use mixed naming conventions.

## Operational rule before case analysis
No case may begin coding or theme work until the refreshed source map, moderator register, and this participant-register logic are treated as the active Gate 1 foundation.
