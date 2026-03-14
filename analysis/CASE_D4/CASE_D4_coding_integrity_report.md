# CASE_D4 Coding Integrity Report (Gate 3)

## 1. Segment extraction summary

| Metric | Value |
|--------|-------|
| Total segments | 701 |
| Participant segments | 619 |
| Moderator segments | 82 |
| Unclear segments | 0 |
| Unique participant speakers | 29 |
| Source transcripts | 5 (HWEL1AR, HWEL3AR, HWEL7AR, HWEL9AR, HWEL10AR) |
| Questions covered | Q1–Q7 |

## 2. Per-source extraction

| Source | Paragraphs | Segments | Unmatched lines | Language |
|--------|-----------|----------|-----------------|----------|
| HWEL10AR.docx | 41 | 31 | 0 | en |
| HWEL1AR.docx | 63 | 25 | 1 | ar |
| HWEL3AR.docx | 78 | 35 | 0 | ar |
| HWEL7AR.docx | 113 | 107 | 0 | ar |
| HWEL9AR.docx | 711 | 503 | 0 | ar |

### Notes
- HWEL1AR: 1 unmatched line is a moderator continuation ("فما معنى حياتك الطيبة...") without a label prefix. Analytically insignificant.
- HWEL9AR dominates segment count (503/701 = 71.8%) due to its highly conversational, rapid-exchange format with many short turns.
- HWEL10AR is an English-language transcript; all other sources are Arabic.
- HWEL10AR required a late correction to source-specific paragraph breakpoints because the English transcript uses part headers plus a combined Q5–Q7 section; early Gate 3 drift was corrected rather than smoothed over.

## 3. Question distribution

| Question | Participant | Moderator | Total | Sources | Unique speakers |
|----------|-----------|-----------|-------|---------|----------------|
| Q1 | 40 | 11 | 51 | 5 | 22 |
| Q2 | 32 | 13 | 45 | 5 | 18 |
| Q3 | 124 | 11 | 135 | 5 | 20 |
| Q4 | 115 | 18 | 133 | 5 | 16 |
| Q5 | 108 | 11 | 119 | 5 | 18 |
| Q6 | 83 | 8 | 91 | 4 | 11 |
| Q7 | 117 | 10 | 127 | 4 | 13 |

### Question-boundary method
- Source-specific paragraph breakpoints were set manually after close reading of each transcript.
- Forward-only content-based detection supplements breakpoints using keyword markers (e.g., "العافية", "ركائز", "التحديات", "الفرص", "اقتراحات").
- HWEL10AR uses explicit "Part N" headers as primary boundaries.
- HWEL9AR required the most granular breakpoint calibration due to its organic, non-linear discussion flow.

### Distribution notes
- Q1 and Q2 are lighter because the opening rounds involve structured introductions and shorter individual responses.
- Q3–Q7 are heavier because HWEL9AR's extended conversational exchanges produce many short segments.
- Q4 now has 5 contributing sources after correcting the HWEL10AR part breakpoints; HWEL1AR still has relatively weak Q4 preservation.
- Q6 has 4 sources because HWEL10AR's combined Part 5 contains explicit opportunity content, while HWEL1AR still does not reach a distinct Q6 section.

## 4. Coding layer integrity checks

### 4.1 Every segment maps to source + type + question + code
- **PASS**: All 701 segments have non-empty values for `source_file`, `speaker_type`, `question_id`, and `codes`.

### 4.2 No moderator prompts in participant evidence
- **PASS**: All 82 moderator segments are coded exclusively as `moderator_context`. No moderator segment carries participant-evidence codes.
- Verification: moderator segments are identified by speaker_code matching D4_M01–D4_M07 and are coded with `moderator_context` only.

### 4.3 Mixed-language authority preserved
- **PASS**: HWEL10AR segments are tagged `language=en`; all other segments are tagged `language=ar`.
- Arabic segments preserve original Arabic text including mixed Arabic-English professional terminology (e.g., "I-COPE", "MDT", "home care", "PCCC").

### 4.4 Speaker attribution
- **PASS**: All 701 segments have `attribution_status=identified`. No `indeterminate` or `unclear` segments.
- Speaker matching uses longest-first greedy alias matching with 51 alias strings across 36 speaker codes.
- Current Gate 3 `speaker_type` values are only `participant` and `moderator`. `note_taker_summary` and `unclear` remain schema-valid but were not instantiated in this transcript-derived Gate 3 base.

### 4.5 Code coverage
- 619 participant segments coded with codebook-derived codes.
- `general_response` is applied only when no semantic code matches — serves as a residual category, not a default.
- Pillar-specific codes (pillar_spiritual, pillar_emotional, etc.) are applied alongside substantive codes when explicit pillar references appear.
- Overbroad English marker drift in the first pass (especially HWEL10AR question assignment and short technology markers) was corrected in the final Gate 3 rebuild rather than hidden.

### 4.6 Recommendation workbook remains auxiliary only
- **PASS**: `Health_Workshop_Suggestions Day 4.xlsx` was not used to generate coded segments, participant summary counts, question evidence counts, or quotation-support evidence.
- If used later, it remains restricted to clearly labeled Q6/Q7 recommendation-support functions only.

## 5. Schema compliance

The `CASE_D4_coded_segments.csv` schema matches the locked schema:

```
segment_id, source_file, table_id, speaker_code, speaker_type,
role_label, attribution_status, question_id, segment_text,
codes, language
```

All fields present. No extra or missing columns.
The current coded base parses cleanly and uses only valid locked `speaker_type` values.

## 6. Participant summary validation

- 29 participant rows in `CASE_D4_participant_summary.csv`, matching the 29 participant codes in the register (D4_P01–D4_P29).
- All participants have `segment_count > 0` except D4_P18 (1 segment, 45 chars) and D4_P19 (2 segments, 83 chars) — both are brief contributors from Table 7.
- `questions_covered` field correctly reflects the question IDs present in each participant's segments.

## 7. Known limitations

1. **HWEL9AR segment granularity**: The rapid-exchange conversational format produces many very short segments (some < 20 chars). These are retained for completeness but carry limited analytic weight individually. Theme development will rely on aggregated patterns rather than individual micro-segments.

2. **Question boundary precision in HWEL9AR**: The discussion flow in Table 9 is organic and non-linear. Participants sometimes revisit earlier questions or blend question topics. Breakpoints represent the best-effort forward-only assignment based on moderator transitions and content markers.

3. **HWEL10AR combined Part 5**: Table 10 combines challenges, opportunities, and suggestions into one late section. The corrected Gate 3 build now uses source-specific breakpoints plus narrow content markers (`Challenge:`, `Opportunity:`, `Suggestion:`-style lines) instead of broad English keywords, but this section still remains structurally less clean than a fully separated Q5/Q6/Q7 transcript.

4. **D4_P25 dominance**: Patient voice D4_P25 accounts for 238/619 participant segments (38.4%). This reflects the transcript structure (D4_P25 is the most active speaker in the conversational HWEL9AR format) rather than an extraction error. Theme development must account for this single-speaker concentration.

5. **Transcript-derived Gate 3 only**: No `note_taker_summary` or `unclear` rows were promoted into the coded base. This keeps moderator and note material out of participant evidence, but it also means note files remain contextual rather than operationalized at this gate.

## 8. Gate 3 verdict

**STOP-CLEAN** — All Gate 3 coding integrity checks satisfied after correcting the HWEL10AR boundary drift and overbroad English retrieval markers. Gate 3 is now documented cleanly enough to proceed to Gate 4, but Gate 4 has not been started here.
