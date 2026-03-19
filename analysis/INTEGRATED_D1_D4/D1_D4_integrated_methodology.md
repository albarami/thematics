# Integrated D1-D4 Methodology

## Scope
This methodology governs the final integrated synthesis across `CASE_D1`, `CASE_D2`, `CASE_D3`, and `CASE_D4` only.
The four case packages are treated as frozen outward-facing building blocks unless a real evidence-backed error is identified.
The excluded fifth case/day remains fully out of scope for inventories, matrices, charts, and reporting claims.

## Source base
The integrated synthesis draws only from the approved outward-facing package layer of the four assessed cases. Across those packages, the integrated evidence layer includes `170` excerpt-bank rows and `22` explicitly labeled note-based support rows.
No internal identity keys, named participant files, or raw transcript layers were reopened during this synthesis build.

## Source hierarchy and handling rules
The integrated build preserves the same evidence hierarchy used in the approved case packages.

- `verbatim_transcript` rows remain the strongest outward-facing quotation layer.
- `note_style_transcript_summary` rows remain usable only when explicitly labeled as note-style summary material.
- `note_taker_summary` rows remain auxiliary and are never rewritten as direct participant speech.
- `unclear` attribution rows remain explicitly flagged and do not count as clean participant-diversity evidence.
- Moderator material remains contextual only and is excluded from participant evidence claims.
- Recommendation workbook logic remains auxiliary only: it may support implementation interpretation, but it does not originate themes.

## Integrated analytic model
The integrated synthesis does not flatten the cases into a single universal narrative. It proceeds in three linked steps:

1. preserve each case as an already-approved within-case interpretation
2. map the aligned four-theme case structures onto four integrated synthesis themes
3. surface cross-cutting patterns only after life-stage and stakeholder differences have been retained

The aligned integrated themes are listed below.

| integrated_theme_id | integrated_theme | cases_present | aggregated_participant_segments | aggregated_unique_speakers | questions_present | dominant_salience_pattern |
| --- | --- | --- | --- | --- | --- | --- |
| IT1 | Wellbeing is a multidimensional, morally grounded balance whose meaning shifts across the life course | 4 | 437 | 85 | Q1;Q2;Q3;Q4;Q5;Q6;Q7 | most_prominent |
| IT2 | Wellbeing is relationally embedded, but the key social ecology changes by case | 4 | 376 | 71 | Q1;Q2;Q3;Q4;Q5;Q6;Q7 | highly_prominent |
| IT3 | The HT pillars are only partially reflected in care because services remain pressured, fragmented, and unevenly relational | 4 | 291 | 71 | Q1;Q2;Q3;Q4;Q5;Q6;Q7 | moderately_prominent |
| IT4 | Sustainable improvement requires institutionally embedded, culturally grounded, and life-stage responsive redesign | 4 | 303 | 66 | Q1;Q2;Q3;Q4;Q5;Q6;Q7 | present_but_less_prominent |

## Cross-cutting synthesis patterns
These patterns are treated as interpretive overlays rather than replacements for the four integrated themes.

### CP1 — Surface functioning is an unreliable guide to inner wellbeing across the life course
From hidden distress in childhood and youth, to concealed strain in adulthood, to non-burden behaviour in older age, the dataset repeatedly warns that visible composure or functionality can mask deeper need.

### CP2 — The pillars are not experienced as flat; different values become heavier in different cases
The five pillars recur across all four cases, but they are not weighted equally. Spiritual-moral grounding is strongest in childhood, social and disclosure-sensitive life is central in youth, role-bearing balance is central in adulthood, and dignity, containment, and relational recognition are especially heavy in older age.

## Structured outputs
The integrated build creates the following primary outputs: `D1_D4_integrated_final_report.md`, `D1_D4_integrated_methodology.md`, `D1_D4_integrated_cross_case_synthesis_memo.md`, `D1_D4_integrated_summary_tables.md`, `D1_D4_integrated_visuals_and_tables.md`, `D1_D4_integrated_question_matrix_workbook.xlsx`, `D1_D4_integrated_theme_evidence_workbook.xlsx`, `D1_D4_integrated_participant_workbook.xlsx`, and `D1_D4_integrated_final_crosscheck_report.md`.

## Quality controls
Integrated quality control is based on the approved case cross-checks plus a final integrated package verification pass.

- all integrated rows must point back to approved outward-facing files
- D1-D4 case boundaries must remain explicit in every workbook
- no new cross-case claims may override within-case limitations
- no quotes may be silently de-labeled from note-style or note-taker support
- no material from the excluded fifth case/day may appear anywhere in the integrated output layer

## Case-sensitive limitations carried into integration
The integrated report preserves the main limitations already documented in the approved case packages rather than hiding them behind aggregate counts.

### CASE_D1
- Three sources (`HWCH3AR`, `HWCH4AR`, `HWCH7AR`) are underrepresented in coded theme mapping because much participant content remained `general_response` in the support layer.
- Q6 and Q7 are analytically important but have little or no coded theme support in the outward-facing matrix; Day 1 late-question interpretation partly relies on close reading and explicitly labeled auxiliary recommendation material.
- Children's own voices remain limited; provider and professional viewpoints dominate the cleanest Day 1 evidence.
- The outward-facing Day 1 package operationalizes 3 `note_taker_summary` excerpt rows and 7 `note_style_transcript_summary` rows, which must remain explicitly labeled rather than merged into verbatim participant speech.

### CASE_D2
- `HWYO10AR` behaves partly like compressed note-style summary material and must remain explicitly labeled whenever quoted.
- The final outward-facing Day 2 evidence layer operationalizes 5 `note_taker_summary` rows and 3 `unclear` rows as contextual or attribution-cautious support, but these do not count as participant-diversity evidence.
- Professional and provider voices still dominate the cleanest evidence even though youth and service-recipient positions are more visible than in Day 1.
- Q6 and Q7 contain meaningful opportunity and suggestion material but should still be read with explicit care around note and `unclear` support layers.

### CASE_D3
- Weak `HWAD1AR` `Q2/Q3` boundaries limit fine-grained question-specific interpretation in part of the early Arabic source.
- `HWAD10AR` does not preserve a clean standalone `Q6` section, so the opportunity layer is real but unevenly distributed across sources.
- Substantial `unclear` material in `HWAD3AR` and `HWAD6AR` remains analytically important and explicitly labeled rather than over-attributed.
- No `note_taker_summary` rows were operationalized in the final outward-facing Day 3 evidence layer; note files remain contextual only.

### CASE_D4
- `HWEL9AR` is highly granular and conversationally over-segmented, so raw counts must not be treated as simple analytic weight by themselves.
- `HWEL9AR` question boundaries remain best-effort and porous in parts of the later discussion.
- `HWEL10AR` preserves a merged late section rather than cleanly separated Q5-Q7 blocks.
- `D4_P25` is unusually dominant in the late evidence base, and no `note_taker_summary` rows were operationalized in the final outward-facing Day 4 evidence layer.
