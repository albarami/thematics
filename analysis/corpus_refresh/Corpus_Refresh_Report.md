# Corpus Refresh Report (D1-D4 Only)

## Scope
This report documents the refreshed foundation layer for the D1-D4 assessment scope. The assessed cases are CASE_D1, CASE_D2, CASE_D3, and CASE_D4.

## Active foundation outputs
- `analysis/corpus_refresh/file_inventory_refresh.csv` (65 rows, D1-D4 only)
- `analysis/corpus_refresh/case_register_refresh.csv` (4 rows, D1-D4 only)
- `analysis/corpus_refresh/source_map_refresh.csv` (39 rows, D1-D4 only)
- `analysis/corpus_refresh/moderator_register_refresh.csv` (45 rows, D1-D4 only)
- `analysis/corpus_refresh/participant_register_logic_note.md`
- `analysis/corpus_refresh/recommendation_workbook_initial_assessment.md`
- `analysis/corpus_refresh/Corpus_Refresh_Report.md` (this file)
- `analysis/corpus_refresh/Foundation_Verification_Report.md`
- `analysis/corpus_refresh/Foundation_Verification_Appendix.md`
- `analysis/corpus_refresh/Foundation_Check_Script.md`

## Source-role rules
- **Transcript files** (`*AR.docx`): primary verbal data.
- **Note-taker files** (`*NT*.docx`): contextual/triangulation data.
- **Recommendation workbooks** (`Health_Workshop_Suggestions Day X.xlsx`): auxiliary structured recommendation material; not transcript-equivalent; not theme-generating.
- **Temp/lock files** (`_$*`, `~$*`): excluded from analysis.

## Pairing confidence scale
- `confirmed` - exact shared prefix, both transcript and note present
- `probable` - likely pairing but affected by filename irregularity
- `ambiguous` - multiple plausible pairings or unresolved conflict
- `none` - no defensible pairing (note-only, transcript-only, or temp/lock)

---

## CASE_D1 - Day 1 Childhood

### Verified file counts
| Type | Count |
|------|-------|
| Transcripts | 7 |
| Note-taker files | 8 |
| Recommendation workbooks | 1 |
| Temp/lock files | 1 |
| Auxiliary files | 0 |

### Exact filenames
- **Transcripts**: HWCH0AR.docx, HWCH10AR.docx, HWCH2AR.docx, HWCH3AR.docx, HWCH4AR.docx, HWCH6AR.docx, HWCH7AR.docx
- **Note-taker files**: HWCH0NT1.docx, HWCH10NT1.docx, HWCH2NT1.docx, HWCH3NT2.docx, HWCH4NT1.docx, HWCH5NT1.docx, HWCH6NT3.docx, HWCH7NT1.docx
- **Recommendation workbook**: Health_Workshop_Suggestions Day 1.xlsx
- **Temp/lock exclusion**: _$CH0NT1.docx

### Pairing map
| Key | Transcript | Note(s) | Confidence |
|-----|-----------|---------|------------|
| HWCH0 | HWCH0AR.docx | HWCH0NT1.docx | confirmed |
| HWCH2 | HWCH2AR.docx | HWCH2NT1.docx | confirmed |
| HWCH3 | HWCH3AR.docx | HWCH3NT2.docx | confirmed |
| HWCH4 | HWCH4AR.docx | HWCH4NT1.docx | confirmed |
| HWCH5 | - | HWCH5NT1.docx | none (note-only) |
| HWCH6 | HWCH6AR.docx | HWCH6NT3.docx | confirmed |
| HWCH7 | HWCH7AR.docx | HWCH7NT1.docx | confirmed |
| HWCH10 | HWCH10AR.docx | HWCH10NT1.docx | confirmed |

### Moderator roster (from Moderators.xlsx)
11 moderators listed for Day 1 (tables 0-10). Only 7 tables have corresponding transcript files. Transcript-level moderator confirmation: 0 confirmed by name, 6 probable via generic role labels or spelling variants, 1 unclear, 4 no transcript available. See `moderator_register_refresh.csv` for per-row evidence.

### Participant-role availability
Transcript speaker labels are available across all 7 transcripts but use inconsistent formats: named speakers (HWCH10AR), role-labelled speakers (HWCH6AR), generic Speaker N labels (HWCH0AR), and sparse labels (HWCH2AR, HWCH3AR). Two transcripts (HWCH3AR, HWCH2AR) have very few extracted labels. Participant extraction is feasible but requires careful normalization during preparation.

### Filename drift note
The previous analysis referenced `HWCH4AR1.docx`. The current raw folder contains `HWCH4AR.docx`. This is a naming change that must be handled explicitly during the derived-text rebuild.

---

## CASE_D2 - Day 2 Youth

### Verified file counts
| Type | Count |
|------|-------|
| Transcripts | 7 |
| Note-taker files | 10 |
| Recommendation workbooks | 1 |
| Temp/lock files | 0 |
| Auxiliary files | 0 |

### Exact filenames
- **Transcripts**: HWYO0AR.docx, HWYO10AR.docx, HWYO11AR.docx, HWYO3AR.docx, HWYO4AR.docx, HWYO7AR.docx, HWYO9AR.docx
- **Note-taker files**: HWYO0NT1.docx, HWYO10NT1.docx, HWYO11NT2.docx, HWYO1NT.docx, HWYO3NT1.docx, HWYO4NT1.docx, HWYO5NT1.docx, HWYO6NT1.docx, HWYO9NT1[7].docx, HWYO9NT2.docx
- **Recommendation workbook**: Health_Workshop_Suggestions Day 2.xlsx

### Pairing map
| Key | Transcript | Note(s) | Confidence |
|-----|-----------|---------|------------|
| HWYO0 | HWYO0AR.docx | HWYO0NT1.docx | confirmed |
| HWYO1 | - | HWYO1NT.docx | none (note-only) |
| HWYO3 | HWYO3AR.docx | HWYO3NT1.docx | confirmed |
| HWYO4 | HWYO4AR.docx | HWYO4NT1.docx | confirmed |
| HWYO5 | - | HWYO5NT1.docx | none (note-only) |
| HWYO6 | - | HWYO6NT1.docx | none (note-only) |
| HWYO7 | HWYO7AR.docx | - | none (transcript-only) |
| HWYO9 | HWYO9AR.docx | HWYO9NT1[7].docx; HWYO9NT2.docx | confirmed |
| HWYO10 | HWYO10AR.docx | HWYO10NT1.docx | confirmed |
| HWYO11 | HWYO11AR.docx | HWYO11NT2.docx | confirmed |

### Filename irregularities
- `HWYO1NT.docx` uses a non-standard note suffix (no number after NT). Treated as a valid note file.
- `HWYO9NT1[7].docx` contains square brackets. This is unusual and may cause filesystem or tooling issues during preparation.

### Moderator roster
12 moderators listed for Day 2 (tables 0-11). 7 tables have transcript files. Transcript-level moderator confirmation: 0 confirmed by name, 3 probable via generic role labels, 4 unclear (no labels or ambiguous), 5 no transcript available.

### Participant-role availability
7 transcripts available. Two transcripts (HWYO3AR, HWYO7AR) produced NO extracted speaker labels at all, which is a significant limitation for participant identification at those tables. Others have mixed quality: HWYO10AR has clean English labels, HWYO11AR has rich Arabic role-labelled speakers, HWYO4AR has named speakers with role annotations. HWYO0AR has generic descriptions without clean label-colon format. HWYO9AR has clean generic Speaker N labels.

---

## CASE_D3 - Day 3 Adults

### Verified file counts
| Type | Count |
|------|-------|
| Transcripts | 5 |
| Note-taker files | 11 |
| Recommendation workbooks | 1 |
| Temp/lock files | 0 |
| Auxiliary files | 0 |

### Exact filenames
- **Transcripts**: HWAD10AR.docx, HWAD1AR.docx, HWAD3AR.docx, HWAD4AR.docx, HWAD6AR.docx
- **Note-taker files**: HWAD0NT1.docx, HWAD10NT1.docx, HWAD10NTI.docx, HWAD11NT2.docx, HWAD11NT3.docx, HWAD1NT1.docx, HWAD1NT2.docx, HWAD3NT1.docx, HWAD5NT1.docx, HWAD7NT1.docx, HWAD9NT1.docx
- **Recommendation workbook**: Health_Workshop_Suggestions Day 3.xlsx

### Pairing map
| Key | Transcript | Note(s) | Confidence |
|-----|-----------|---------|------------|
| HWAD0 | - | HWAD0NT1.docx | none (note-only) |
| HWAD1 | HWAD1AR.docx | HWAD1NT1.docx; HWAD1NT2.docx | confirmed |
| HWAD3 | HWAD3AR.docx | HWAD3NT1.docx | confirmed |
| HWAD4 | HWAD4AR.docx | - | none (transcript-only) |
| HWAD5 | - | HWAD5NT1.docx | none (note-only) |
| HWAD6 | HWAD6AR.docx | - | none (transcript-only) |
| HWAD7 | - | HWAD7NT1.docx | none (note-only) |
| HWAD9 | - | HWAD9NT1.docx | none (note-only) |
| HWAD10 | HWAD10AR.docx | HWAD10NT1.docx; HWAD10NTI.docx | probable |
| HWAD11 | - | HWAD11NT2.docx; HWAD11NT3.docx | none (note-only) |

### Filename irregularities
- `HWAD10NTI.docx` uses `NTI` instead of `NT` + number. This is an irregular naming pattern. Treated as probably related to the HWAD10 cluster but flagged for preparation-stage verification.

### Moderator roster
12 moderators listed for Day 3 (tables 0-11). 5 tables have transcript files. Transcript-level moderator confirmation: 1 confirmed by name (هنادي أحمد أبو بكر in HWAD1AR), 3 probable via generic role labels, 1 unclear (HWAD6AR has no moderator markers), 7 no transcript available.

### Participant-role availability
5 transcripts with highly variable label quality. HWAD10AR has clean English Speaker N labels. HWAD1AR has inline text with some label-colon patterns and confirmed moderator naming. HWAD3AR, HWAD4AR, and HWAD6AR use descriptive inline role labels (e.g. "طبيب نفسي", "طبيبة اسنان") rather than clean speaker labels, which complicates participant extraction.

### Note-heavy day
Day 3 has 11 note files but only 5 transcripts, giving it the highest note-to-transcript ratio. 6 table numbers (0, 2, 5, 7, 9, 11) are note-only. This limits transcript-based triangulation for nearly half the tables.

---

## CASE_D4 - Day 4 Elderly

### Verified file counts
| Type | Count |
|------|-------|
| Transcripts | 5 |
| Note-taker files | 7 |
| Recommendation workbooks | 1 |
| Temp/lock files | 0 |
| Auxiliary files | 0 |

### Exact filenames
- **Transcripts**: HWEL10AR.docx, HWEL1AR.docx, HWEL3AR.docx, HWEL7AR.docx, HWEL9AR.docx
- **Note-taker files**: HWEL10NT1.docx, HWEL10NT2.docx, HWEL1NT1.docx, HWEL3NT1.docx, HWEL4NT1.docx, HWEL6NT1.docx, HWEL7NT1.docx
- **Recommendation workbook**: Health_Workshop_Suggestions Day 4.xlsx

### Pairing map
| Key | Transcript | Note(s) | Confidence |
|-----|-----------|---------|------------|
| HWEL1 | HWEL1AR.docx | HWEL1NT1.docx | confirmed |
| HWEL3 | HWEL3AR.docx | HWEL3NT1.docx | confirmed |
| HWEL4 | - | HWEL4NT1.docx | none (note-only) |
| HWEL6 | - | HWEL6NT1.docx | none (note-only) |
| HWEL7 | HWEL7AR.docx | HWEL7NT1.docx | confirmed |
| HWEL9 | HWEL9AR.docx | - | none (transcript-only) |
| HWEL10 | HWEL10AR.docx | HWEL10NT1.docx; HWEL10NT2.docx | confirmed |

### Moderator roster
10 moderators listed for Day 4 (tables 1-10; no table 0). 5 tables have transcript files. Transcript-level moderator confirmation: 2 confirmed by name (Diana Hassan in HWEL1AR as "Diana (moderator)"; د. عبد اللطيف سلامي in HWEL9AR as "Dr Abdellatif Moderator"), 3 probable via generic role labels or first-name match, 5 no transcript available.

### Participant-role availability
5 transcripts. HWEL1AR has named speakers with institutional affiliations. HWEL3AR has short Arabic name labels. HWEL7AR has named speakers including institutional figures. HWEL9AR has English speakers with institutional roles. HWEL10AR uses structured Part labels with named speakers. Overall, Day 4 transcripts provide relatively clean speaker identification compared to Days 2-3.

---

## Aggregate verified counts

| | D1 | D2 | D3 | D4 | Total |
|--|----|----|----|----|-------|
| Transcripts | 7 | 7 | 5 | 5 | 24 |
| Note-taker files | 8 | 10 | 11 | 7 | 36 |
| Recommendation workbooks | 1 | 1 | 1 | 1 | 4 |
| Temp/lock files | 1 | 0 | 0 | 0 | 1 |
| Auxiliary files | 0 | 0 | 0 | 0 | 0 |
| **Total files** | **17** | **18** | **17** | **13** | **65** |

## Readiness boundary
The workspace now has a D1-D4 refreshed foundation layer. Case-level analysis may begin only after this foundation is accepted as the active Gate 1 baseline.
