# CASE_D1 Source Sensitivity Memo

## Purpose
This memo documents source-level quality, limitations, and handling decisions that affect how each Day 1 source can be used during coding and theme development.

---

## Source-level sensitivity notes

### HWCH0AR (Table 0, Arabic, 90721 chars)
- **Speaker attribution**: Good. Named speakers (Kulood, Dr Ahmed Al Emadi) and pseudonymized speakers (Speaker 2-7) are colon-delimited.
- **Moderator separation**: Kulood identified as moderator (Dr. Kholoud). Her turns must be excluded from participant evidence.
- **Speaker 2 concern**: 23 turns but only 299 chars (avg ~13 chars/turn). Likely brief acknowledgments or interjections rather than substantive contributions. Treat as marginal/unclear unless content review shows otherwise.
- **Coding note**: Richest source for Q1-Q3 conceptual discussion. Speaker 4 and Speaker 5 are the dominant participant voices.

### HWCH2AR (Table 2, Arabic, 53225 chars)
- **Speaker attribution**: Poor. Mostly continuous flowing text with only 3 "مداخلة" (intervention) labels and 1 "د. حصة" label. ~21000 chars are unlabeled.
- **Moderator separation**: Assigned moderator (هنادي أحمد أبو بكر) not explicitly labeled. Moderator prompts are likely embedded in the flowing text but cannot be systematically separated without manual reading.
- **Coding decision**: Code the substantive content but flag attribution uncertainty. Where speaker identity cannot be determined, mark speaker_type as "unclear" and note the limitation. Do not attribute unlabeled text to specific participants.
- **Risk**: Some content coded from this transcript may inadvertently include moderator prompts. This risk is acknowledged and documented.

### HWCH3AR (Table 3, Arabic, 33087 chars)
- **Speaker attribution**: Very poor. One identified turn is actually a moderator prompt sentence ("طيب، دعنا ننتقل للسؤال اللي بعده، السؤال الرابع" = "OK, let's move to the next question, the fourth question"). Remainder is unlabeled.
- **Moderator separation**: Same limitation as HWCH2AR. Assigned moderator (هالة فايد حسن فتحي) not explicitly labeled.
- **Coding decision**: Same as HWCH2AR — code substantive content, flag attribution uncertainty, exclude identifiable moderator prompts.

### HWCH4AR (Table 4, Arabic, 19588 chars)
- **Speaker attribution**: Moderate. Clear moderator label (مدير الجلسة) but limited participant labels. Two sentence fragments were captured as false speaker labels.
- **Moderator separation**: Clean. مدير الجلسة (session manager) = عبد الكريم شعبان. 19 turns, 15774 chars — this is a moderator-heavy transcript. A large proportion of the text is moderator-led.
- **Participant voices**: Limited. Dr. Yaseen (2 turns) and Ali-service recipient (3 turns, variant labels) are the identifiable participants.
- **Coding note**: Valuable for the service-recipient perspective (Ali) but thin on participant evidence overall. Moderator summaries within the text should be coded as moderator context, not participant evidence.

### HWCH6AR (Table 6, Arabic, 45376 chars)
- **Speaker attribution**: Good for participants (professional role labels in parentheses). Multiple label variants for the same speaker must be consolidated.
- **Moderator separation**: نور الوتاري (= Nour Al-Watadi from Moderators.xlsx). 4 turns, 960 chars — clearly facilitation.
- **Dominant speaker**: Manal (psychologist, Sidra Hospital) contributes ~27000 chars across variant labels — over half the transcript. This is analytically rich but means the transcript is heavily shaped by one clinical perspective.
- **Coding note**: Code Manal's contributions as participant evidence but note the dominance when assessing theme support breadth. Jumana (1 turn, 1081 chars) classified as unclear — include if content is substantive.

### HWCH7AR (Table 7, Arabic, 51018 chars)
- **Speaker attribution**: Good. Named participants with consistent labels.
- **Moderator separation**: مدير الجلسه (session manager) = عبلة أحمد خليل. 45 turns but only 6199 chars — short facilitation prompts.
- **Participant diversity**: Best in corpus. 7 named participants with substantive contributions ranging from 2732 to 13280 chars.
- **Coding note**: Most balanced source for multi-participant evidence. All 7 participants are clearly distinguished.

### HWCH10AR (Table 10, English, 8436 chars)
- **Speaker attribution**: Excellent. Named participants with professional roles, explicit question markers, and topic-specific labels (e.g., "Melissa Toon (Challenge)").
- **Moderator separation**: Moderator 1 and Moderator 2 clearly labeled. Small contribution (764 chars total).
- **Language**: English. Quotations can be used directly without translation. Cross-language comparison with Arabic transcripts requires care.
- **Coding note**: Most structured source. Best for system-level critique (Q4-Q5) and implementation proposals (Q6-Q7). Smallest transcript — good density but limited volume.

### Note files (contextual triangulation)
- All notes use standardised table templates covering Q1-Q7.
- HWCH0NT1 is in English (for Arabic transcript HWCH0AR) — cross-language triangulation.
- HWCH10NT1 has named participants with professional roles — useful for participant identification.
- HWCH5NT1 has no paired transcript. Content is contextual only; cannot be used as primary evidence.
- Note content represents note-taker summaries, not verbatim participant speech. Must be coded as speaker_type = note_taker_summary.

### Recommendation workbook (auxiliary)
- Usage governed by CASE_D1_recommendation_usage_rule.md.
- 40 suggestion rows with generic "User" labels.
- Not used in coding or theme development. Used only for Q6-Q7 supplementary tables.

---

## Cross-source sensitivity issues

1. **Attribution inequality**: HWCH7AR and HWCH10AR have excellent speaker attribution; HWCH2AR and HWCH3AR have poor attribution. This means participant-level analysis will be stronger for some tables than others.

2. **Professional voice dominance**: Nearly all identifiable participants are healthcare/social work professionals. Service-recipient voices (only Ali in HWCH4AR, and possibly some unlabeled speakers) are rare. This shapes the entire analysis toward a provider perspective on childhood wellbeing.

3. **Single-speaker dominance**: HWCH6AR is dominated by Manal. Her views are analytically important but should not be treated as representative of the table's full discussion.

4. **Moderator contamination risk**: In HWCH2AR and HWCH3AR, moderator prompts cannot be reliably separated from participant content. Any evidence from these transcripts carries this risk.
