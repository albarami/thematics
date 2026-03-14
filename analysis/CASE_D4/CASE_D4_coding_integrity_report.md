# CASE_D4 Coding Integrity Report (Gate 3)

## 1. Segment extraction summary

| Metric | Value |
|--------|-------|
| Total segments | 690 |
| Participant segments | 610 |
| Moderator segments | 80 |
| Unclear segments | 0 |
| Unique participant speakers | 29 |
| Source transcripts | 5 (HWEL1AR, HWEL3AR, HWEL7AR, HWEL9AR, HWEL10AR) |
| Questions covered | Q1–Q7 |

## 2. Per-source extraction

| Source | Paragraphs | Segments | Unmatched lines | Language |
|--------|-----------|----------|-----------------|----------|
| HWEL10AR.docx | 41 | 23 | 0 | en |
| HWEL1AR.docx | 63 | 23 | 1 | ar |
| HWEL3AR.docx | 78 | 35 | 0 | ar |
| HWEL7AR.docx | 113 | 106 | 0 | ar |
| HWEL9AR.docx | 711 | 503 | 0 | ar |

### Notes
- HWEL1AR: 1 unmatched line is a moderator continuation ("فما معنى حياتك الطيبة...") without a label prefix. Analytically insignificant.
- HWEL9AR dominates segment count (503/690 = 72.9%) due to its highly conversational, rapid-exchange format with many short turns.
- HWEL10AR is an English-language transcript; all other sources are Arabic.

## 3. Question distribution

| Question | Participant | Moderator | Total | Sources | Unique speakers |
|----------|-----------|-----------|-------|---------|----------------|
| Q1 | 39 | 10 | 49 | 5 | 20 |
| Q2 | 33 | 12 | 45 | 5 | 20 |
| Q3 | 122 | 12 | 134 | 5 | 19 |
| Q4 | 112 | 17 | 129 | 4 | 13 |
| Q5 | 109 | 11 | 120 | 5 | 15 |
| Q6 | 79 | 7 | 86 | 3 | 9 |
| Q7 | 116 | 11 | 127 | 4 | 11 |

### Question-boundary method
- Source-specific paragraph breakpoints were set manually after close reading of each transcript.
- Forward-only content-based detection supplements breakpoints using keyword markers (e.g., "العافية", "ركائز", "التحديات", "الفرص", "اقتراحات").
- HWEL10AR uses explicit "Part N" headers as primary boundaries.
- HWEL9AR required the most granular breakpoint calibration due to its organic, non-linear discussion flow.

### Distribution notes
- Q1 and Q2 are lighter because the opening rounds involve structured introductions and shorter individual responses.
- Q3–Q7 are heavier because HWEL9AR's extended conversational exchanges produce many short segments.
- Q4 has 4 sources (HWEL1AR does not have a distinct Q4 boundary — its Q4-like content is absorbed into Q3/Q5).
- Q6 has 3 sources because HWEL10AR combines Q5–Q7 into "Part 5: Challenges and Suggestions" and HWEL1AR's discussion does not reach a distinct Q6.

## 4. Coding layer integrity checks

### 4.1 Every segment maps to source + type + question + code
- **PASS**: All 690 segments have non-empty values for `source_file`, `speaker_type`, `question_id`, and `codes`.

### 4.2 No moderator prompts in participant evidence
- **PASS**: All 80 moderator segments are coded exclusively as `moderator_context`. No moderator segment carries participant-evidence codes.
- Verification: moderator segments are identified by speaker_code matching D4_M01–D4_M07 and are coded with `moderator_context` only.

### 4.3 Mixed-language authority preserved
- **PASS**: HWEL10AR segments are tagged `language=en`; all other segments are tagged `language=ar`.
- Arabic segments preserve original Arabic text including mixed Arabic-English professional terminology (e.g., "I-COPE", "MDT", "home care", "PCCC").

### 4.4 Speaker attribution
- **PASS**: All 690 segments have `attribution_status=identified`. No `indeterminate` or `unclear` segments.
- Speaker matching uses longest-first greedy alias matching with 51 alias strings across 36 speaker codes.

### 4.5 Code coverage
- 610 participant segments coded with codebook-derived codes.
- `general_response` is applied only when no semantic code matches — serves as a residual category, not a default.
- Pillar-specific codes (pillar_spiritual, pillar_emotional, etc.) are applied alongside substantive codes when explicit pillar references appear.

## 5. Schema compliance

The `CASE_D4_coded_segments.csv` schema matches the locked schema:

```
segment_id, source_file, table_id, speaker_code, speaker_type,
role_label, attribution_status, question_id, segment_text,
codes, language
```

All fields present. No extra or missing columns.

## 6. Participant summary validation

- 29 participant rows in `CASE_D4_participant_summary.csv`, matching the 29 participant codes in the register (D4_P01–D4_P29).
- All participants have `segment_count > 0` except D4_P18 (1 segment, 45 chars) and D4_P19 (2 segments, 83 chars) — both are brief contributors from Table 7.
- `questions_covered` field correctly reflects the question IDs present in each participant's segments.

## 7. Known limitations

1. **HWEL9AR segment granularity**: The rapid-exchange conversational format produces many very short segments (some < 20 chars). These are retained for completeness but carry limited analytic weight individually. Theme development will rely on aggregated patterns rather than individual micro-segments.

2. **Question boundary precision in HWEL9AR**: The discussion flow in Table 9 is organic and non-linear. Participants sometimes revisit earlier questions or blend question topics. Breakpoints represent the best-effort forward-only assignment based on moderator transitions and content markers.

3. **HWEL10AR Q5–Q7 merge**: Table 10's transcript combines challenges, opportunities, and suggestions into a single "Part 5". Segments in this section are assigned Q5 by default; content-based detection promotes some to Q6/Q7 based on keyword markers.

4. **D4_P25 dominance**: Patient voice D4_P25 accounts for 238/610 participant segments (39.0%). This reflects the transcript structure (D4_P25 is the most active speaker in the conversational HWEL9AR format) rather than an extraction error. Theme development must account for this single-speaker concentration.

## 8. Gate 3 verdict

**PASS** — All coding integrity checks satisfied. The coded segments are ready for theme development (Gate 4).
