from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANALYSIS_ROOT = ROOT.parent
OUTWARD_DIR = ROOT / "OUTWARD_FACING_PACKAGE"
INTERNAL_DIR = ROOT / "INTERNAL_CONFIDENTIAL"

OUTPUT_FILES = {
    "report": ROOT / "D1_D4_integrated_final_report.md",
    "methodology": ROOT / "D1_D4_integrated_methodology.md",
    "synthesis_memo": ROOT / "D1_D4_integrated_cross_case_synthesis_memo.md",
    "summary_tables": ROOT / "D1_D4_integrated_summary_tables.md",
    "visuals": ROOT / "D1_D4_integrated_visuals_and_tables.md",
    "question_workbook": ROOT / "D1_D4_integrated_question_matrix_workbook.xlsx",
    "theme_workbook": ROOT / "D1_D4_integrated_theme_evidence_workbook.xlsx",
    "participant_workbook": ROOT / "D1_D4_integrated_participant_workbook.xlsx",
    "crosscheck": ROOT / "D1_D4_integrated_final_crosscheck_report.md",
}

INTERNAL_FILES = {
    "source_manifest": INTERNAL_DIR / "D1_D4_integration_source_manifest.md",
    "build_note": INTERNAL_DIR / "D1_D4_internal_build_note.md",
}

CASES = {
    "CASE_D1": {
        "label": "Day 1 — Childhood",
        "day_label": "Childhood",
        "package_dir": ANALYSIS_ROOT / "CASE_D1" / "OUTWARD_FACING_PACKAGE",
        "report_file": "CASE_D1_final_report.md",
        "themes_file": "CASE_D1_final_themes.md",
        "summary_file": "CASE_D1_summary_tables.md",
        "crosscheck_file": "CASE_D1_crosscheck_report.md",
        "question_matrix_file": "CASE_D1_question_theme_matrix.csv",
        "question_evidence_file": "CASE_D1_question_evidence_table.csv",
        "theme_summary_file": "CASE_D1_theme_summary_table.csv",
        "prominence_file": "CASE_D1_prominence_salience.csv",
        "excerpt_file": "CASE_D1_excerpt_bank.csv",
        "participant_summary_file": "CASE_D1_participant_summary.csv",
        "participant_register_file": "CASE_D1_participant_register.csv",
        "theme_number_titles": {
            "1": "Balanced contentment, safety, and moral steadiness as the grounding of wellbeing",
            "2": "The interdependent professional support ecology around children",
            "3": "Fragmented, strained, and uneven childhood service conditions",
            "4": "Culturally grounded coordination, early awareness, and formal implementation as routes to change",
        },
        "case_variation": "Childhood is interpreted largely through provider-described support ecologies, moral-spiritual grounding, and the absence of strong direct child voice.",
        "limitations": [
            "Three sources (`HWCH3AR`, `HWCH4AR`, `HWCH7AR`) are underrepresented in coded theme mapping because much participant content remained `general_response` in the support layer.",
            "Q6 and Q7 are analytically important but have little or no coded theme support in the outward-facing matrix; Day 1 late-question interpretation partly relies on close reading and explicitly labeled auxiliary recommendation material.",
            "Children's own voices remain limited; provider and professional viewpoints dominate the cleanest Day 1 evidence.",
            "The outward-facing Day 1 package operationalizes 3 `note_taker_summary` excerpt rows and 7 `note_style_transcript_summary` rows, which must remain explicitly labeled rather than merged into verbatim participant speech.",
        ],
    },
    "CASE_D2": {
        "label": "Day 2 — Youth",
        "day_label": "Youth",
        "package_dir": ANALYSIS_ROOT / "CASE_D2" / "OUTWARD_FACING_PACKAGE",
        "report_file": "CASE_D2_final_report.md",
        "themes_file": "CASE_D2_final_themes.md",
        "summary_file": "CASE_D2_summary_tables.md",
        "crosscheck_file": "CASE_D2_final_crosscheck_report.md",
        "question_matrix_file": "CASE_D2_question_theme_matrix.csv",
        "question_evidence_file": "CASE_D2_question_evidence_table.csv",
        "theme_summary_file": "CASE_D2_theme_summary_table.csv",
        "prominence_file": "CASE_D2_prominence_salience.csv",
        "excerpt_file": "CASE_D2_excerpt_bank.csv",
        "participant_summary_file": "CASE_D2_participant_summary.csv",
        "participant_register_file": "CASE_D2_participant_register.csv",
        "theme_number_titles": {
            "1": "Multidimensional wellbeing as balanced stability, moral-spiritual grounding, and daily functioning",
            "2": "Youth wellbeing as relational ecology, peer worlds, and social disconnection",
            "3": "Holistic care constrained by rushed, fragmented, and trust-sensitive encounters",
            "4": "Coordinated, youth-sensitive, and institutionally backed routes to change",
        },
        "case_variation": "Youth wellbeing is strongly shaped by peer worlds, family visibility, digital exposure, and the risk that distress hides behind outward functioning.",
        "limitations": [
            "`HWYO10AR` behaves partly like compressed note-style summary material and must remain explicitly labeled whenever quoted.",
            "The final outward-facing Day 2 evidence layer operationalizes 5 `note_taker_summary` rows and 3 `unclear` rows as contextual or attribution-cautious support, but these do not count as participant-diversity evidence.",
            "Professional and provider voices still dominate the cleanest evidence even though youth and service-recipient positions are more visible than in Day 1.",
            "Q6 and Q7 contain meaningful opportunity and suggestion material but should still be read with explicit care around note and `unclear` support layers.",
        ],
    },
    "CASE_D3": {
        "label": "Day 3 — Adults",
        "day_label": "Adults",
        "package_dir": ANALYSIS_ROOT / "CASE_D3" / "OUTWARD_FACING_PACKAGE",
        "report_file": "CASE_D3_final_report.md",
        "themes_file": "CASE_D3_final_themes.md",
        "summary_file": "CASE_D3_summary_tables.md",
        "crosscheck_file": "CASE_D3_final_crosscheck_report.md",
        "question_matrix_file": "CASE_D3_question_theme_matrix.csv",
        "question_evidence_file": "CASE_D3_question_evidence_table.csv",
        "theme_summary_file": "CASE_D3_theme_summary_table.csv",
        "prominence_file": "CASE_D3_prominence_salience.csv",
        "excerpt_file": "CASE_D3_excerpt_bank.csv",
        "participant_summary_file": "CASE_D3_participant_summary.csv",
        "participant_register_file": "CASE_D3_participant_register.csv",
        "theme_number_titles": {
            "1": "Adult wellbeing as integrated balance, moral-spiritual grounding, and workable coping",
            "2": "Adult wellbeing as negotiated through family, work, caregiving, and role-bearing strain",
            "3": "Holistic adult care undermined by time pressure, hierarchy, navigation gaps, and uneven communication",
            "4": "Coordinated, access-aware, and institutionally embedded routes to adult-care redesign",
        },
        "case_variation": "Adult wellbeing is repeatedly interpreted through role-bearing strain, self-versus-system responsibility, and the burden hidden behind apparently competent functioning.",
        "limitations": [
            "Weak `HWAD1AR` `Q2/Q3` boundaries limit fine-grained question-specific interpretation in part of the early Arabic source.",
            "`HWAD10AR` does not preserve a clean standalone `Q6` section, so the opportunity layer is real but unevenly distributed across sources.",
            "Substantial `unclear` material in `HWAD3AR` and `HWAD6AR` remains analytically important and explicitly labeled rather than over-attributed.",
            "No `note_taker_summary` rows were operationalized in the final outward-facing Day 3 evidence layer; note files remain contextual only.",
        ],
    },
    "CASE_D4": {
        "label": "Day 4 — Elderly",
        "day_label": "Elderly",
        "package_dir": ANALYSIS_ROOT / "CASE_D4" / "OUTWARD_FACING_PACKAGE",
        "report_file": "CASE_D4_final_report.md",
        "themes_file": "CASE_D4_final_themes.md",
        "summary_file": "CASE_D4_summary_tables.md",
        "crosscheck_file": "CASE_D4_final_crosscheck_report.md",
        "question_matrix_file": "CASE_D4_question_theme_matrix.csv",
        "question_evidence_file": "CASE_D4_question_evidence_table.csv",
        "theme_summary_file": "CASE_D4_theme_summary_table.csv",
        "prominence_file": "CASE_D4_prominence_salience.csv",
        "excerpt_file": "CASE_D4_excerpt_bank.csv",
        "participant_summary_file": "CASE_D4_participant_summary.csv",
        "participant_register_file": "CASE_D4_participant_register.csv",
        "theme_number_titles": {
            "1": "Elderly wellbeing as dignified integrated balance, spiritual-moral steadiness, and lived acceptance",
            "2": "Good ageing as relational belonging, non-burden, and continued social significance",
            "3": "Holistic elder care as partially present but unevenly integrated across services, training, and coordination",
            "4": "Institutionally embedded and socially distributed routes to elder-care redesign",
        },
        "case_variation": "Older-age wellbeing is strongly shaped by dignity, non-burden status, social recognition, and the weighting of pillars rather than a flat five-part model.",
        "limitations": [
            "`HWEL9AR` is highly granular and conversationally over-segmented, so raw counts must not be treated as simple analytic weight by themselves.",
            "`HWEL9AR` question boundaries remain best-effort and porous in parts of the later discussion.",
            "`HWEL10AR` preserves a merged late section rather than cleanly separated Q5-Q7 blocks.",
            "`D4_P25` is unusually dominant in the late evidence base, and no `note_taker_summary` rows were operationalized in the final outward-facing Day 4 evidence layer.",
        ],
    },
}

INTEGRATED_THEMES = [
    {
        "id": "IT1",
        "theme_number": "1",
        "title": "Wellbeing is a multidimensional, morally grounded balance whose meaning shifts across the life course",
        "summary": "Across D1-D4, participants reject narrow biomedical definitions of wellbeing. They describe it as balance across multiple domains, but the meaning of that balance changes by age and stakeholder position: childhood is framed through moral-spiritual grounding and safety, youth through functionality and livable balance, adulthood through coping under pressure, and older age through dignity, acceptance, and peace.",
    },
    {
        "id": "IT2",
        "theme_number": "2",
        "title": "Wellbeing is relationally embedded, but the key social ecology changes by case",
        "summary": "The cases agree that wellbeing is never purely individual. What changes is the social field that matters most: children are discussed through professional-family support ecologies, youth through peer worlds and disconnection, adults through family-work-caregiving burden, and older people through belonging, non-burden, and social significance.",
    },
    {
        "id": "IT3",
        "theme_number": "3",
        "title": "The HT pillars are only partially reflected in care because services remain pressured, fragmented, and unevenly relational",
        "summary": "All four cases describe a gap between whole-person wellbeing ideals and actual healthcare experience. Time pressure, fragmentation, hierarchical communication, language mismatch, weak navigation, and uneven disclosure safety repeatedly prevent the pillars from becoming reliable lived practice.",
    },
    {
        "id": "IT4",
        "theme_number": "4",
        "title": "Sustainable improvement requires institutionally embedded, culturally grounded, and life-stage responsive redesign",
        "summary": "Across D1-D4, participants do not ask only for nicer attitudes. They call for system design: training, communication standards, public awareness, school-linked and community-linked entry points, differentiated services, workforce support, and formal embedding of wellbeing values into institutions rather than leaving them to goodwill alone.",
    },
]

CROSSCUTTING_PATTERNS = [
    {
        "id": "CP1",
        "title": "Surface functioning is an unreliable guide to inner wellbeing across the life course",
        "summary": "From hidden distress in childhood and youth, to concealed strain in adulthood, to non-burden behaviour in older age, the dataset repeatedly warns that visible composure or functionality can mask deeper need.",
    },
    {
        "id": "CP2",
        "title": "The pillars are not experienced as flat; different values become heavier in different cases",
        "summary": "The five pillars recur across all four cases, but they are not weighted equally. Spiritual-moral grounding is strongest in childhood, social and disclosure-sensitive life is central in youth, role-bearing balance is central in adulthood, and dignity, containment, and relational recognition are especially heavy in older age.",
    },
]

QUOTE_PLAN = {
    "definition": [("CASE_D1", "D1_E001"), ("CASE_D4", "D4_S0009")],
    "wellness": [("CASE_D2", "D2_S0255"), ("CASE_D3", "D3_S0067"), ("CASE_D4", "D4_S0013")],
    "pillars": [("CASE_D1", "D1_E002"), ("CASE_D3", "D3_S0562"), ("CASE_D4", "D4_S0068")],
    "service_reflection": [("CASE_D2", "D2_S0089"), ("CASE_D3", "D3_S0225"), ("CASE_D4", "D4_S0173")],
    "challenges": [("CASE_D1", "D1_S0274"), ("CASE_D2", "D2_S0046"), ("CASE_D3", "D3_S0338"), ("CASE_D4", "D4_S0021")],
    "opportunities": [("CASE_D1", "D1_S0756"), ("CASE_D2", "D2_S0304"), ("CASE_D3", "D3_S0868"), ("CASE_D4", "D4_S0024")],
    "practical": [("CASE_D2", "D2_S0313"), ("CASE_D3", "D3_S1153"), ("CASE_D4", "D4_S0028"), ("CASE_D4", "D4_S0625")],
}

KNOWN_NAME_SCAN_TERMS = [
    "Diana",
    "Abdellatif",
    "علاء",
    "عبلة",
    "فيروز",
    "مريم",
    "participant_identity_key.xlsx",
    "CASE_D5",
    "Day5_PolicyMakers",
]

OUTWARD_PACKAGE_FILENAMES = [
    OUTPUT_FILES["report"].name,
    OUTPUT_FILES["methodology"].name,
    OUTPUT_FILES["synthesis_memo"].name,
    OUTPUT_FILES["summary_tables"].name,
    OUTPUT_FILES["visuals"].name,
    OUTPUT_FILES["question_workbook"].name,
    OUTPUT_FILES["theme_workbook"].name,
    OUTPUT_FILES["participant_workbook"].name,
    OUTPUT_FILES["crosscheck"].name,
]
