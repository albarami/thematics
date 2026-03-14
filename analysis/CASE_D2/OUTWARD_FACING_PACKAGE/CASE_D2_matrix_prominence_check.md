# CASE_D2 Matrix and Prominence Check

## Case: CASE_D2 — Day 2 (Youth)
## Status: VERIFIED FOR CURRENT GATE 5 STRUCTURED CHECKS

---

## Matrix and prominence summary

The Day 2 question-theme matrix and prominence layer are built directly from participant-coded transcript rows in `CASE_D2_coded_segments.csv`. `note_taker_summary` rows in the excerpt bank remain explicit contextual support only and do not alter the matrix or salience counts. A `0` value in the question-theme matrix is used as the explicit absence marker for that Q × Theme cell.

## Gate 5 checks

| Check | Result |
|-------|--------|
| Question-theme matrix aligned with coded segments | PASS — every matrix count is recomputed from the reviewed participant-coded base |
| Prominence table aligned with salience CSV and theme summary table | PASS — `CASE_D2_prominence_salience.csv` and `CASE_D2_theme_summary_table.csv` are generated from one ranked calculation |
| No unjustified all-high pattern | PASS — salience labels are ranked from most prominent to present but less prominent rather than assigning all themes high status |
| Each prominence label explained | PASS — every theme row includes a count-based salience explanation |
| Q × Theme cells explicit | PASS — 26 cells contain evidence-backed counts and 2 cells are explicitly marked by `0` |

## Prominence order

| Theme | Salience | Participant segments | Questions present |
|-------|----------|----------------------|-------------------|
| Theme_1_Multidimensional_Wellbeing_Framework | most_prominent | 83 | Q1;Q2;Q3;Q4;Q5;Q6;Q7 |
| Theme_3_Pressured_and_Trust_Sensitive_Care | highly_prominent | 44 | Q1;Q2;Q3;Q4;Q5;Q6;Q7 |
| Theme_2_Youth_Social_Ecology_and_Disconnection | moderately_prominent | 32 | Q1;Q2;Q3;Q4;Q5;Q6;Q7 |
| Theme_4_Youth_Sensitive_Implementation | present_but_less_prominent | 40 | Q3;Q4;Q5;Q6;Q7 |

**Errors:** 0
**Warnings:** 0