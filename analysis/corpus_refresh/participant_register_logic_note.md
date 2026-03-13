# Participant Register Logic Note

## Purpose
This note defines the refreshed participant-register logic, moderator-register logic, and source-role rules for the rebuilt analysis workspace.

## Foundation rule
No old participant assumptions, speaker counts, or prior case outputs are reused automatically. Every participant and role decision must be rebuilt from the refreshed raw corpus, the restored method baseline, and transcript context.

## Source-role rules
- **Transcript files** are the primary verbal data source for participant and moderator extraction.
- **Note-taker files** are contextual and triangulation data. They may preserve role clues, but they do not override transcript speaker attribution.
- **Recommendation workbooks** are auxiliary structured recommendation material. They may support Q6/Q7 and policy-facing reporting, but they are not transcript-equivalent participant evidence.
- **Presentation artifacts** are auxiliary contextual material only.
- **Temp/lock files** are excluded from analysis entirely.

## Allowed `speaker_type` values
The refreshed workspace uses only these values:
- `participant`
- `moderator`
- `note_taker_summary`
- `unclear`

## Moderator logic
1. Use `analysis/corpus_refresh/moderator_register_refresh.csv` as the first-pass moderator roster for Days 1-4.
2. Match moderator names to transcript labels using spelling normalization only when the transcript context supports the match.
3. If a transcript speaker clearly performs moderation but is absent from `Moderators.xlsx`, record that row as `moderator` with an explicit note explaining the evidence.
4. Day 5 currently has no workbook-based moderator roster, so moderator identification for Day 5 must remain transcript/context dependent if later evidence appears.

## Participant logic
1. Extract speaker labels fresh from the refreshed transcript files only after the derived-text layer is rebuilt.
2. Any speaker label not matched to the moderator roster should not automatically become `participant`; it must be judged from transcript context.
3. Named speakers, defensible role labels, and generic speaker labels may be classified as `participant` only when the transcript preserves substantive contribution.
4. Brief acknowledgements, turn-management speech, or organizational instructions must not be treated as participant evidence.
5. Note-only sources can support contextual role awareness, but they should not create transcript-equivalent participant rows unless later source evidence makes that defensible.
6. Day 5 should be treated as especially constrained because there is no transcript-based speaker layer in the current raw corpus.

## Note-taker summary logic
- Use `note_taker_summary` only for note-derived summaries or summarized contributions that cannot be tied cleanly to a transcript speaker turn.
- Do not merge note-taker summary rows into participant quotation counts.
- If a note file contains an attributed speaker label that can later be confirmed in a transcript, the transcript remains authoritative.

## Pairing confidence rules
Use only these values in the refreshed source map:
- `confirmed`: exact current-scan pairing supported by a shared source code prefix.
- `probable`: likely pairing supported by the source code prefix, but affected by filename irregularity or another refresh risk.
- `ambiguous`: multiple plausible pairings or unresolved evidence conflict.
- `none`: no defensible pairing available.

## Day-level implications
- **Days 1-4**: transcript-based participant and moderator extraction appears feasible after preparation.
- **Day 5**: participant extraction is limited because the current day folder contains note-taker material plus an auxiliary presentation, not a transcript set.

## Operational rule before case analysis
No case may begin coding or theme work until the refreshed source map, moderator register, and participant-register logic above are treated as the active Gate 1 foundation.
