# Corpus Refresh Report

## Scope
This report documents the refreshed foundation layer rebuilt from the current raw corpus after the intentional reset. It establishes the new active inventory, case register, source map, moderator roster, participant/source-role logic, and initial recommendation-workbook assessment before any case-level analysis begins.

## Active foundation outputs
- `analysis/corpus_refresh/file_inventory_refresh.csv`
- `analysis/corpus_refresh/case_register_refresh.csv`
- `analysis/corpus_refresh/source_map_refresh.csv`
- `analysis/corpus_refresh/moderator_register_refresh.csv`
- `analysis/corpus_refresh/participant_register_logic_note.md`
- `analysis/corpus_refresh/recommendation_workbook_initial_assessment.md`
- `analysis/corpus_refresh/Corpus_Refresh_Report.md`

## Source-role rules established in the refresh
- Transcript files are primary verbal data.
- Note-taker files are contextual/triangulation data and may also require `note_taker_summary` handling later.
- Recommendation workbooks are auxiliary structured recommendation material, not transcript-equivalent evidence.
- Presentation artifacts are auxiliary contextual material only.
- Temp/lock files are excluded from analysis.

## Pairing confidence scale used
- `confirmed`
- `probable`
- `ambiguous`
- `none`

## Day-by-day refresh summary

### CASE_D1 - Day 1 Childhood

- **Transcript count**: 7
- **Note-taker file count**: 8
- **Auxiliary file count**: 1
- **Temp/lock file count**: 1

- **Exact filenames by type**
  - Transcripts: HWCH0AR.docx, HWCH10AR.docx, HWCH2AR.docx, HWCH3AR.docx, HWCH4AR.docx, HWCH6AR.docx, HWCH7AR.docx
  - Note-taker files: HWCH0NT1.docx, HWCH10NT1.docx, HWCH2NT1.docx, HWCH3NT2.docx, HWCH4NT1.docx, HWCH5NT1.docx, HWCH6NT3.docx, HWCH7NT1.docx
  - Auxiliary files: Health_Workshop_Suggestions Day 1.xlsx
  - Temp/lock files: _$CH0NT1.docx

- **Probable pairings**
  - HWCH0: HWCH0AR.docx <-> HWCH0NT1.docx (confirmed)
  - HWCH2: HWCH2AR.docx <-> HWCH2NT1.docx (confirmed)
  - HWCH3: HWCH3AR.docx <-> HWCH3NT2.docx (confirmed)
  - HWCH4: HWCH4AR.docx <-> HWCH4NT1.docx (confirmed)
  - HWCH5: No transcript <-> HWCH5NT1.docx (none)
  - HWCH6: HWCH6AR.docx <-> HWCH6NT3.docx (confirmed)
  - HWCH7: HWCH7AR.docx <-> HWCH7NT1.docx (confirmed)
  - HWCH10: HWCH10AR.docx <-> HWCH10NT1.docx (confirmed)

- **Participant/role availability**: Transcript speaker labels appear available across seven files; expect a mix of named, role-labelled, and generic speaker labels that must be re-extracted fresh.
- **Moderator presence**: Moderator roster available in Moderators.xlsx for Day 1; transcript spelling and role-context reconciliation still required.
- **New or changed files relative to the prior baseline**: Current scan confirms seven transcripts, eight substantive note files, one recommendation workbook, and one temp/lock file. Fresh provenance rebuilding is required because earlier active analysis traces referenced HWCH4AR1 while the current raw folder contains HWCH4AR.docx. HWCH5NT1 remains a note-only file.
- **Important implications for later analysis**: Day 1 can support a full Gate 1 rebuild, but moderator mapping, filename drift, note-only material, and temp-lock exclusion must be resolved explicitly before derived text and registers are recreated.

### CASE_D2 - Day 2 Youth

- **Transcript count**: 7
- **Note-taker file count**: 10
- **Auxiliary file count**: 1
- **Temp/lock file count**: 0

- **Exact filenames by type**
  - Transcripts: HWYO0AR.docx, HWYO10AR.docx, HWYO11AR.docx, HWYO3AR.docx, HWYO4AR.docx, HWYO7AR.docx, HWYO9AR.docx
  - Note-taker files: HWYO0NT1.docx, HWYO10NT1.docx, HWYO11NT2.docx, HWYO1NT.docx, HWYO3NT1.docx, HWYO4NT1.docx, HWYO5NT1.docx, HWYO6NT1.docx, HWYO9NT1[7].docx, HWYO9NT2.docx
  - Auxiliary files: Health_Workshop_Suggestions Day 2.xlsx
  - Temp/lock files: None

- **Probable pairings**
  - HWYO0: HWYO0AR.docx <-> HWYO0NT1.docx (confirmed)
  - HWYO1: No transcript <-> HWYO1NT.docx (none)
  - HWYO3: HWYO3AR.docx <-> HWYO3NT1.docx (confirmed)
  - HWYO4: HWYO4AR.docx <-> HWYO4NT1.docx (confirmed)
  - HWYO5: No transcript <-> HWYO5NT1.docx (none)
  - HWYO6: No transcript <-> HWYO6NT1.docx (none)
  - HWYO7: HWYO7AR.docx <-> No note file (none)
  - HWYO9: HWYO9AR.docx <-> HWYO9NT1[7].docx; HWYO9NT2.docx (confirmed)
  - HWYO10: HWYO10AR.docx <-> HWYO10NT1.docx (confirmed)
  - HWYO11: HWYO11AR.docx <-> HWYO11NT2.docx (confirmed)

- **Participant/role availability**: Transcript speaker labels appear available across seven files; participant and role extraction should be feasible but must be rebuilt from zero.
- **Moderator presence**: Moderator roster available in Moderators.xlsx for Day 2; transcript spelling and role-context reconciliation still required.
- **New or changed files relative to the prior baseline**: The pre-reset inventory was deleted, so the refreshed scan becomes the new active baseline. Material signals requiring fresh handling include the Day 2 recommendation workbook, note-only files HWYO1NT.docx/HWYO5NT1.docx/HWYO6NT1.docx, and irregular filename HWYO9NT1[7].docx.
- **Important implications for later analysis**: Day 2 has enough transcript coverage for a full rerun, but note-only files and irregular note naming mean the refreshed source map must become the single source of truth.

### CASE_D3 - Day 3 Adults

- **Transcript count**: 5
- **Note-taker file count**: 11
- **Auxiliary file count**: 1
- **Temp/lock file count**: 0

- **Exact filenames by type**
  - Transcripts: HWAD10AR.docx, HWAD1AR.docx, HWAD3AR.docx, HWAD4AR.docx, HWAD6AR.docx
  - Note-taker files: HWAD0NT1.docx, HWAD10NT1.docx, HWAD10NTI.docx, HWAD11NT2.docx, HWAD11NT3.docx, HWAD1NT1.docx, HWAD1NT2.docx, HWAD3NT1.docx, HWAD5NT1.docx, HWAD7NT1.docx, HWAD9NT1.docx
  - Auxiliary files: Health_Workshop_Suggestions Day 3.xlsx
  - Temp/lock files: None

- **Probable pairings**
  - HWAD0: No transcript <-> HWAD0NT1.docx (none)
  - HWAD1: HWAD1AR.docx <-> HWAD1NT1.docx; HWAD1NT2.docx (confirmed)
  - HWAD3: HWAD3AR.docx <-> HWAD3NT1.docx (confirmed)
  - HWAD4: HWAD4AR.docx <-> No note file (none)
  - HWAD5: No transcript <-> HWAD5NT1.docx (none)
  - HWAD6: HWAD6AR.docx <-> No note file (none)
  - HWAD7: No transcript <-> HWAD7NT1.docx (none)
  - HWAD9: No transcript <-> HWAD9NT1.docx (none)
  - HWAD10: HWAD10AR.docx <-> HWAD10NT1.docx; HWAD10NTI.docx (probable)
  - HWAD11: No transcript <-> HWAD11NT2.docx; HWAD11NT3.docx (none)

- **Participant/role availability**: Transcript speaker labels appear available across five files, but extra note-only sources and irregular note filenames increase provenance complexity.
- **Moderator presence**: Moderator roster available in Moderators.xlsx for Day 3; transcript spelling and role-context reconciliation still required.
- **New or changed files relative to the prior baseline**: The pre-reset inventory was deleted, so the refreshed scan becomes the new active baseline. Material signals requiring fresh handling include the Day 3 recommendation workbook, irregular filename HWAD10NTI.docx, and several note-only keys (HWAD0, HWAD5, HWAD7, HWAD9, HWAD11).
- **Important implications for later analysis**: Day 3 can proceed to a full rerun after the source map is locked; note-only clusters and the irregular HWAD10NTI filename should be treated as provenance risks until confirmed.

### CASE_D4 - Day 4 Elderly

- **Transcript count**: 5
- **Note-taker file count**: 7
- **Auxiliary file count**: 1
- **Temp/lock file count**: 0

- **Exact filenames by type**
  - Transcripts: HWEL10AR.docx, HWEL1AR.docx, HWEL3AR.docx, HWEL7AR.docx, HWEL9AR.docx
  - Note-taker files: HWEL10NT1.docx, HWEL10NT2.docx, HWEL1NT1.docx, HWEL3NT1.docx, HWEL4NT1.docx, HWEL6NT1.docx, HWEL7NT1.docx
  - Auxiliary files: Health_Workshop_Suggestions Day 4.xlsx
  - Temp/lock files: None

- **Probable pairings**
  - HWEL1: HWEL1AR.docx <-> HWEL1NT1.docx (confirmed)
  - HWEL3: HWEL3AR.docx <-> HWEL3NT1.docx (confirmed)
  - HWEL4: No transcript <-> HWEL4NT1.docx (none)
  - HWEL6: No transcript <-> HWEL6NT1.docx (none)
  - HWEL7: HWEL7AR.docx <-> HWEL7NT1.docx (confirmed)
  - HWEL9: HWEL9AR.docx <-> No note file (none)
  - HWEL10: HWEL10AR.docx <-> HWEL10NT1.docx; HWEL10NT2.docx (confirmed)

- **Participant/role availability**: Transcript speaker labels appear available across five files; participant and role extraction should be feasible with explicit handling of transcript-only and note-only items.
- **Moderator presence**: Moderator roster available in Moderators.xlsx for Day 4; transcript spelling and role-context reconciliation still required.
- **New or changed files relative to the prior baseline**: The pre-reset inventory was deleted, so the refreshed scan becomes the new active baseline. Material signals requiring fresh handling include the Day 4 recommendation workbook, transcript-only HWEL9AR.docx, and note-only files HWEL4NT1.docx and HWEL6NT1.docx.
- **Important implications for later analysis**: Day 4 has workable transcript coverage, but transcript-only and note-only items mean triangulation cannot be assumed uniformly across all tables.

### CASE_D5 - Day 5 Policy Makers

- **Transcript count**: 0
- **Note-taker file count**: 1
- **Auxiliary file count**: 1
- **Temp/lock file count**: 0

- **Exact filenames by type**
  - Transcripts: None
  - Note-taker files: اليوم الخامس - صناع القرار.docx
  - Auxiliary files: العافية والحياة الطيبة - الجلسة الختامية  02.05.26 7AM (1).pptx
  - Temp/lock files: None

- **Probable pairings**
  - None

- **Participant/role availability**: No transcript file is currently present; participant and role availability is limited because the day is represented by a note file plus an auxiliary presentation only.
- **Moderator presence**: No Day 5 moderator roster is present in Moderators.xlsx; any moderator identification will require note/presentation context only.
- **New or changed files relative to the prior baseline**: Current scan matches the preserved method baseline description of Day 5 as note-taker material plus an auxiliary presentation artifact; there is still no transcript file in the raw folder.
- **Important implications for later analysis**: Day 5 cannot be treated like the earlier transcript-based cases; any later case analysis must explicitly account for the absence of transcript-level participant speech and the auxiliary status of the presentation.

## Moderator register implication
Days 1-4 now have an explicit workbook-based moderator register in `analysis/corpus_refresh/moderator_register_refresh.csv`. Day 5 does not appear in `Moderators.xlsx`, so later Day 5 source-role decisions must document that limitation explicitly.

## Recommendation workbook implication
The initial Day 1 recommendation-workbook assessment indicates a grouped/cleaned auxiliary workbook with generic user labels and action-oriented recommendation rows. It should support recommendation and policy synthesis only, not transcript-equivalent participant evidence or theme generation.

## Readiness boundary
The workspace is now equipped with a refreshed foundation layer. Case-level analysis may begin only after this foundation is accepted as the active Gate 1 baseline.
