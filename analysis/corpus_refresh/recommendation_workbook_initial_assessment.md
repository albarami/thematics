# Recommendation Workbook Initial Assessment (D1-D4 Only)

## Scope
This assessment covers the four recommendation workbooks found in the D1-D4 raw folders. The assessed cases are CASE_D1, CASE_D2, CASE_D3, and CASE_D4.

---

## CASE_D1 - Health_Workshop_Suggestions Day 1.xlsx

- **Exact path**: `Day1_Childhood/Recommendations_Data/Health_Workshop_Suggestions Day 1.xlsx`
- **Sheet count**: 1
- **Sheet name**: `First_Day_01_02_2026`
- **Verified max_row**: 41
- **Verified max_column**: 3
- **Verified column headers**: `No` | `User` | `Suggestion`
- **Non-empty cells by column**: Col A (No): 39 | Col B (User): 39 | Col C (Suggestion): 41
- **Structural note**: Rows 1-39 follow a clean No/User/Suggestion pattern. Rows 40-41 have empty No and User columns but contain Suggestion text. Row 40 is a manually collected supplementary note block (begins with "نقاط إضافية من مداخلات الحضور تم جمعها بشكل يدوي" = "Additional points from audience interventions collected manually"). Row 41 is another aggregated recommendation block.
- **Row type assessment**: Rows 2-39 appear to be **grouped/cleaned recommendations** under generic user placeholders (`User 1`, `User 2`, etc.). They are not raw conversational turns. Rows 40-41 are **manually aggregated supplementary notes** without user attribution.
- **Speaker traceability**: Weak. Generic `User X` labels do not map to named transcript speakers.
- **Question traceability**: No explicit question column. Content is action-oriented and most relevant to Q6/Q7 style material.
- **Data row count (substantive)**: 38 user-attributed rows + 2 supplementary note rows = 40 data rows total.

---

## CASE_D2 - Health_Workshop_Suggestions Day 2.xlsx

- **Exact path**: `Day2_Youth/Recommendations_Data/Health_Workshop_Suggestions Day 2.xlsx`
- **Sheet count**: 1
- **Sheet name**: `Second_Day_02_02_2026`
- **Verified max_row**: 58
- **Verified max_column**: 4
- **Verified column headers**: `No` | `User` | `Suggestion` | (empty header, column D)
- **Non-empty cells by column**: Col A (No): 58 | Col B (User): 58 | Col C (Suggestion): 58 | Col D: 0
- **Structural note**: Column D exists in the sheet structure but is entirely empty across all 58 rows (including header). This is a formatting artifact, not a data column. Effective structure is 3 columns.
- **Row type assessment**: All 57 data rows follow the No/User/Suggestion pattern with generic `User X` labels. Content appears **grouped/cleaned** like Day 1. Mixed Arabic/English.
- **Speaker traceability**: Weak. Same generic user pattern as Day 1.
- **Question traceability**: No explicit question column. Content is recommendation-oriented.
- **Data row count (substantive)**: 57 user-attributed rows.

---

## CASE_D3 - Health_Workshop_Suggestions Day 3.xlsx

- **Exact path**: `Day3_Adults/Recommendations_Data/Health_Workshop_Suggestions Day 3.xlsx`
- **Sheet count**: 1
- **Sheet name**: `Third_Day_03_02_2026`
- **Verified max_row**: 65
- **Verified max_column**: 3
- **Verified column headers**: `No` | `User` | `Suggestion`
- **Non-empty cells by column**: Col A (No): 65 | Col B (User): 65 | Col C (Suggestion): 65
- **Structural note**: All 64 data rows are fully populated across all 3 columns. No trailing supplementary blocks or empty-cell rows detected.
- **Row type assessment**: All 64 data rows follow the No/User/Suggestion pattern with generic `User X` labels. Content appears **grouped/cleaned**. Mixed Arabic/English.
- **Speaker traceability**: Weak. Same generic user pattern.
- **Question traceability**: No explicit question column.
- **Data row count (substantive)**: 64 user-attributed rows.

---

## CASE_D4 - Health_Workshop_Suggestions Day 4.xlsx

- **Exact path**: `Day4_Elderly/Recommendations_Data/Health_Workshop_Suggestions Day 4.xlsx`
- **Sheet count**: 1
- **Sheet name**: `Forth_Day_04_02_2026`
- **Verified max_row**: 40
- **Verified max_column**: 3
- **Verified column headers**: `No` | `User` | `Suggestion`
- **Non-empty cells by column**: Col A (No): 40 | Col B (User): 40 | Col C (Suggestion): 40
- **Structural note**: All 39 data rows are fully populated across all 3 columns. No trailing supplementary blocks.
- **Row type assessment**: All 39 data rows follow the No/User/Suggestion pattern with generic `User X` labels. Content appears **grouped/cleaned**. Mixed Arabic/English.
- **Speaker traceability**: Weak. Same generic user pattern.
- **Question traceability**: No explicit question column.
- **Data row count (substantive)**: 39 user-attributed rows.

---

## Cross-workbook summary

| Case | Sheet name | Data rows | Columns | Supplementary rows | Empty col |
|------|-----------|-----------|---------|-------------------|-----------|
| D1 | First_Day_01_02_2026 | 38 | 3 | 2 (rows 40-41) | No |
| D2 | Second_Day_02_02_2026 | 57 | 3 effective (4 physical, col D empty) | 0 | Yes (col D) |
| D3 | Third_Day_03_02_2026 | 64 | 3 | 0 | No |
| D4 | Forth_Day_04_02_2026 | 39 | 3 | 0 | No |

## Provisional treatment decision (all four workbooks)

All four workbooks should be treated as:
- **Auxiliary structured recommendation material**
- **Usable for recommendation / policy / implementation sections** (especially Q7, secondarily Q6)
- **Not primary theme-generation evidence**
- **Not transcript-equivalent participant speech**
- **Not valid for participant quotation counting or quotation diversity reporting**

Where these workbooks are used later, they must be labeled explicitly as auxiliary recommendation data and kept structurally separated from transcript-grounded participant evidence.

## Remaining uncertainties
1. Whether the `User X` labels in any workbook correspond to the same numbered participants across days is unknown and should not be assumed.
2. The Day 1 supplementary rows (40-41) appear to be facilitator/researcher-aggregated notes; their evidentiary status is weaker than the user-attributed rows.
3. The Day 2 empty column D could be a formatting artifact or a deleted column; it has no analytical significance but is documented for completeness.
