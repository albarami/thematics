# CASE_D2 Source Sensitivity Memo

## Purpose
This memo documents source-level quality, limitations, and handling decisions that affect how each Day 2 source should be used during familiarisation, coding, and later theme development.

---

## Source-level sensitivity notes

### HWYO0AR (Table 0, Arabic, 50,666 chars)
- **Speaker attribution**: Good. The transcript opens with a participant roster and then preserves repeated named turns for major contributors.
- **Moderator separation**: Strong. `بوزيداني (منسق الجلسة)` is explicitly labeled and can be separated from participant evidence.
- **Participant profile**: Predominantly senior healthcare and policy-oriented professionals. This gives the table high conceptual depth but also strong elite-professional voice dominance.
- **Sensitivity note**: The opening roster includes attendee-style lines that are not always substantive turns. Only later named turns should be treated as participant evidence.
- **Use value**: High for Q1-Q4 conceptual discussion and also useful for the transition into Q5-Q7 implementation talk.

### HWYO3AR (Table 3, Arabic, 41,400 chars)
- **Speaker attribution**: Poor. The extracted transcript contains very little stable speaker labeling.
- **Moderator separation**: Weak. The moderator is assigned in the refreshed moderator register, but transcript extraction does not preserve a robust moderator label.
- **Sensitivity note**: Question prompts are partially visible, especially for Q1 and Q4, but speaker-level attribution is too weak for confident participant mapping.
- **Handling rule**: Use with caution for substantive content; where attribution cannot be secured, mark speaker identity as unclear and avoid over-claiming participant breadth.
- **Use value**: Medium for question-boundary support; lower for participant-level evidence.

### HWYO4AR (Table 4, Arabic, 25,807 chars)
- **Speaker attribution**: Moderate to good. `مدير الجلسة` is clear, and several participant turns preserve role labels.
- **Moderator separation**: Strong. This is a moderator-heavy transcript and the moderator’s facilitation is clearly recoverable.
- **Participant mix**: Valuable because it includes both provider voices and explicitly marked `متلقي خدمة` participants.
- **Sensitivity note**: OCR noise, broken punctuation, and inconsistent role formatting require label consolidation before coding.
- **Use value**: High for Q1-Q4 structure, for moderator-flow clarity, and for the presence of service-recipient perspectives.

### HWYO7AR (Table 7, Arabic, 50,533 chars)
- **Speaker attribution**: Weak to moderate. The opening names the facilitator and several contributors, but the flowing transcript rarely preserves clean turn labels afterward.
- **Moderator separation**: Partial. The facilitator is named in the opening (`يدير الجلسة أ. عبلة خليل`) but later moderator turns are not robustly isolated.
- **Participant mix**: Includes healthcare, student, and psychology-oriented voices, but identity recovery remains incomplete.
- **Sensitivity note**: This source contains useful content on youth wellbeing and implementation, yet attribution uncertainty remains high despite the transcript’s size.
- **Handling rule**: Treat the table as analytically useful but attribution-sensitive. Use note support and question context when coding.
- **Use value**: Medium-high for content, lower for participant-diversity claims.

### HWYO9AR (Table 9, English, 54,577 chars)
- **Speaker attribution**: Excellent. `Speaker 1`-`Speaker 8` are stable and the moderator is clearly labeled throughout.
- **Moderator separation**: Strong. `Moderator` turns are explicit and removable from participant evidence.
- **Participant profile**: Mixed healthcare and academic roles, with one role remaining generic because `Speaker 8` lacks a stable header description in the extracted transcript body.
- **Sensitivity note**: The table is highly productive for Q1-Q7, but one participant role remains only partly recoverable.
- **Use value**: Very high. Best Day 2 source for clean participant-level evidence across the full seven-question structure.

### HWYO10AR (Table 10, English, 9,972 chars)
- **Speaker attribution**: Good. Named English participants and a labeled moderator are preserved.
- **Moderator separation**: Strong for the explicit moderator lines that remain.
- **Compression issue**: This transcript appears partly compressed or note-style rather than fully verbatim. Some paragraphs mix quotation with interpretive summary.
- **Sensitivity note**: It is reliable for question structure and participant-role identification, but should be treated carefully when selecting quotations because some text reads like condensed synthesis rather than clean turn-by-turn speech.
- **Use value**: High for structure, participant roles, and challenge/opportunity content; moderate for verbatim quotation density.

### HWYO11AR (Table 11, Arabic, 30,884 chars)
- **Speaker attribution**: Mixed. `المحاور` is clear, several named/role-labeled participants are recoverable, but many contributions are preserved only as generic `مشارك` or `مشارك آخر`.
- **Moderator separation**: Strong. `المحاور` is explicit and repeated.
- **Participant mix**: Valuable for combining provider, student/service-recipient, and private-sector voices.
- **Sensitivity note**: Some highly substantive turns remain attached to generic labels, so participant-level diversity in this table is partly under-recoverable.
- **Handling rule**: Use named turns as participant evidence; preserve generic but substantive turns as `unclear` where identity cannot be secured.
- **Use value**: High for content and mixed perspective, moderate for attribution precision.

### Note files (contextual triangulation)
- The Day 2 note files follow a standardised Q1-Q7 template and are the strongest source for confirming the canonical seven-question structure across the case.
- `HWYO1NT.docx`, `HWYO5NT1.docx`, and `HWYO6NT1.docx` are note-only sources with no paired transcripts. They are contextually valuable but cannot substitute for primary verbal evidence.
- `HWYO9NT1[7].docx` and `HWYO10NT1.docx` preserve English note structures that are especially useful for participant-role cross-checking and question-boundary confirmation.
- `HWYO9NT2.docx` yielded very little usable structured content in the present extraction and should be treated as low-productivity contextual support unless later review recovers more.
- Note content remains note-taker summary material, not verbatim participant speech.

### Recommendation workbook (auxiliary)
- Usage is governed by `CASE_D2_recommendation_usage_rule.md`.
- The workbook is auxiliary structured recommendation material only.
- It supports recommendation-oriented reporting, especially Q7 and secondarily Q6, but must not be used to generate themes or participant-evidence claims.

---

## Cross-source sensitivity issues

1. **Attribution inequality**: `HWYO9AR` and `HWYO0AR` provide much stronger speaker attribution than `HWYO3AR` and `HWYO7AR`. Participant-level analysis will therefore be uneven across tables.

2. **Moderator contamination risk**: `HWYO3AR` and `HWYO7AR` contain flowing text where facilitator material may be harder to isolate. Coding decisions must preserve this caveat.

3. **Compression vs. verbatim tension**: `HWYO10AR` appears partly compressed/note-style despite being stored as a transcript. Quotations from this source require extra caution.

4. **Professional voice dominance**: Most clearly identifiable Day 2 voices are healthcare, psychology, academic, or service-provider participants. Service-recipient and student voices are present, but not proportionally dominant.

5. **Cross-table evidentiary asymmetry**: Some tables contribute mainly conceptual reflection, while others contribute more implementation, challenge, and suggestion material. This affects how evenly the later coding layer can draw from each source.
