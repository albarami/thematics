# CASE_D3 Schema Check

## Gate 2 purpose
This file locks the structured-artifact schema for `CASE_D3` before coding begins, using the current `CASE_D1` artifact set as the operational baseline.

## Gate 2 status
- **Status**: Locked for the active Day 3 build
- **Baseline case used for schema lock**: `CASE_D1`
- **Rule applied**: Match the current Day 1 artifact schema exactly where the Day 1 artifact already exists, and preserve the `speaker_type` rule everywhere relevant

---

## 1. Structured CSV headers locked from CASE_D1

### CASE_D3 coded segments CSV
Authoritative Day 1 header:
```csv
segment_id,source_file,table_id,speaker_code,speaker_type,role_label,attribution_status,question_id,segment_text,codes,language
```

### CASE_D3 excerpt bank CSV
Authoritative Day 1 header:
```csv
evidence_id,theme,segment_id,source_file,table_id,speaker_code,speaker_type,role_label,attribution_status,evidence_type,question_id,excerpt_text,codes,language,report_use
```

### CASE_D3 question-by-theme matrix CSV
Authoritative Day 1 pattern:
- first column: `question_id`
- then, for each locked theme name, three columns:
  - `{THEME}_segments`
  - `{THEME}_speakers`
  - `{THEME}_tables`

Current Day 1 example header:
```csv
question_id,Theme_1_Balanced_Contentment_segments,Theme_1_Balanced_Contentment_speakers,Theme_1_Balanced_Contentment_tables,Theme_2_Care_Ecology_segments,Theme_2_Care_Ecology_speakers,Theme_2_Care_Ecology_tables,Theme_3_Service_Fragmentation_segments,Theme_3_Service_Fragmentation_speakers,Theme_3_Service_Fragmentation_tables,Theme_4_Culturally_Grounded_Solutions_segments,Theme_4_Culturally_Grounded_Solutions_speakers,Theme_4_Culturally_Grounded_Solutions_tables
```

### CASE_D3 prominence / salience CSV
Authoritative Day 1 header:
```csv
theme,participant_segments,unique_speakers,unique_tables,total_chars,questions_present,composite_score,salience,salience_explanation
```

### CASE_D3 participant summary CSV
Authoritative Day 1 header:
```csv
anonymized_code,source_file,table_id,speaker_type,segment_count,total_chars,questions_covered,top_codes
```

### CASE_D3 question evidence table CSV
Authoritative Day 1 header:
```csv
question_id,participant_segments,moderator_segments,unclear_segments,unique_participant_speakers,source_files,top_codes
```

---

## 2. Working codebook baseline

## Operational reality
The current Day 1 baseline does **not** provide a `CASE_D1_working_codebook.csv` file. The operative artifact in the workspace is:
- `analysis/CASE_D1/CASE_D1_working_codebook.md`

## Gate 2 decision
Until a CSV mirror is explicitly created for Day 1 and adopted as the baseline, the Day 3 working codebook will follow the current operational Day 1 structure:
- markdown file format
- grouped by code families
- table columns inside each family:
  - `Code`
  - `Definition`
  - `Example indicators`

This is an explicit documented exception to the QA spec wording that mentions a codebook CSV. The live workspace baseline is markdown, and Day 3 will not invent a different codebook format mid-case.

---

## 3. `speaker_type` rule locked

Wherever speaker-role distinction is relevant, `speaker_type` must be present and may use only these values:
- `participant`
- `moderator`
- `note_taker_summary`
- `unclear`

## Mandatory implications
- Moderator rows must be retained as moderator rows and never counted as participant evidence
- Note-derived summary material must not be relabeled as participant speech without transcript confirmation
- Unclear speaker material may be retained with caution but must not inflate participant diversity metrics

---

## 4. Existing CASE_D3 Gate 1 schema checks already satisfied

The following Day 3 Gate 1 artifacts already match the active baseline structure:
- `CASE_D3_source_register.csv`
- `CASE_D3_participant_register.csv`
- `CASE_D3_question_map.md`
- `CASE_D3_preparation_checklist.md`

`CASE_D3_participant_register.csv` already includes the locked `speaker_type` field and uses only the allowed values.

---

## 5. Pre-coding requirements for the remaining CASE_D3 artifacts

Before the Day 3 coding layer is treated as valid:
1. Each new CSV must use the locked header exactly
2. CSV quoting must parse cleanly
3. `speaker_type` must remain consistent with the participant register
4. Moderator-coded segments must remain available for context counts but excluded from participant-evidence use
5. Any source compressed enough to blur verbatim vs summary status must preserve that distinction in `evidence_type` and memo notes
6. Warm-up material in `HWAD10AR` must not be miscoded as though it belonged to the seven-question Day 3 guide

---

## 6. Gate 2 conclusion

`CASE_D3` may proceed to the coding/evidence layer under the schema lock above.

The only documented schema exception is the working codebook format: the current workspace baseline is markdown rather than CSV, and the Day 3 build will preserve that baseline unless the project explicitly migrates both cases to a new canonical codebook format.
