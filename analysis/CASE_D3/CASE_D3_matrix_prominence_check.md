# CASE_D3 Matrix and Prominence Check

## Case: CASE_D3 — Day 3 (Adults)
## Status: VERIFIED FOR CURRENT THEME-LAYER MATRIX/PROMINENCE CHECKS — structured alignment complete for the current Day 3 theme layer; later report-layer work still pending

---

## Matrix and prominence summary

The Day 3 question-theme matrix and prominence layer are built directly from participant-coded transcript rows in `CASE_D3_coded_segments.csv` using explicit Day 3 theme-code clusters plus question bounds. `unclear` rows in the excerpt bank remain explicit supporting context only and do not alter matrix or salience counts. A `0` value in the question-theme matrix is used as the explicit absence marker for that Q × Theme cell.

## Structured checks

| Check | Result |
|-------|--------|
| Question-theme matrix aligned with coded segments | PASS — every matrix count is recomputed from the participant-coded Day 3 base using the locked Day 3 theme rules |
| Prominence table aligned with salience CSV and theme summary table | PASS — `CASE_D3_prominence_salience.csv` and `CASE_D3_theme_summary_table.csv` are generated from one ranked calculation |
| No unjustified all-high pattern | PASS — salience labels are ranked from most prominent to present but less prominent rather than assigning all themes high status |
| Each prominence label explained | PASS — every theme row includes a count-based salience explanation |
| Q × Theme cells explicit | PASS — 19 cells contain evidence-backed counts and 9 cells are explicitly marked by `0` |

## Prominence order

| Theme | Salience | Participant segments | Questions present |
|-------|----------|----------------------|-------------------|
| Theme_1_Adult_Wellbeing_as_Integrated_Balance | most_prominent | 143 | Q1;Q2;Q3;Q4;Q5 |
| Theme_2_Adult_Life_as_Relational_and_Role_Bearing_Strain | highly_prominent | 121 | Q1;Q2;Q3;Q4;Q5 |
| Theme_3_Holistic_Care_Undermined_by_Time_Hierarchy_and_Navigation_Barriers | moderately_prominent | 103 | Q3;Q4;Q5;Q6;Q7 |
| Theme_4_Coordinated_and_Institutionally_Embedded_Adult_Care_Redesign | present_but_less_prominent | 95 | Q4;Q5;Q6;Q7 |

**Errors:** 0
**Warnings:** 1 — matrix/prominence alignment is verified for the current theme layer, but this does not mean CASE_D3 is final-report ready.