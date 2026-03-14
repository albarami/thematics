from __future__ import annotations

THEME_ORDER = [
    "Theme_1_Adult_Wellbeing_as_Integrated_Balance",
    "Theme_2_Adult_Life_as_Relational_and_Role_Bearing_Strain",
    "Theme_3_Holistic_Care_Undermined_by_Time_Hierarchy_and_Navigation_Barriers",
    "Theme_4_Coordinated_and_Institutionally_Embedded_Adult_Care_Redesign",
]

THEME_LABELS = {
    "Theme_1_Adult_Wellbeing_as_Integrated_Balance": (
        "Adult wellbeing as integrated balance, moral-spiritual grounding, and workable coping"
    ),
    "Theme_2_Adult_Life_as_Relational_and_Role_Bearing_Strain": (
        "Adult wellbeing as negotiated through family, work, caregiving, and role-bearing strain"
    ),
    "Theme_3_Holistic_Care_Undermined_by_Time_Hierarchy_and_Navigation_Barriers": (
        "Holistic adult care undermined by time pressure, hierarchy, navigation gaps, and uneven communication"
    ),
    "Theme_4_Coordinated_and_Institutionally_Embedded_Adult_Care_Redesign": (
        "Coordinated, access-aware, and institutionally embedded routes to adult-care redesign"
    ),
}

THEME_CODES = {
    "Theme_1_Adult_Wellbeing_as_Integrated_Balance": {
        "balance_multidimensional",
        "contentment_acceptance",
        "inner_peace_stability",
        "functionality_coping_capacity",
        "spiritual_moral_anchor",
        "values_action_alignment",
        "relational_connectedness",
    },
    "Theme_2_Adult_Life_as_Relational_and_Role_Bearing_Strain": {
        "adult_role_responsibility",
        "family_caregiving_ecology",
        "work_life_strain",
        "self_responsibility_orientation",
        "system_responsibility_orientation",
        "provider_self_as_adult",
    },
    "Theme_3_Holistic_Care_Undermined_by_Time_Hierarchy_and_Navigation_Barriers": {
        "trust_questioning_barrier",
        "health_literacy_navigation",
        "patient_provider_relationship",
        "empathy_reassurance",
        "consultation_time_pressure",
        "authority_defensiveness",
        "stigma_help_seeking_barrier",
        "language_cultural_mismatch",
        "fragmented_service_pathway",
    },
    "Theme_4_Coordinated_and_Institutionally_Embedded_Adult_Care_Redesign": {
        "interdisciplinary_integration",
        "awareness_outreach",
        "differentiated_service_design",
        "digital_admin_relief",
        "top_down_system_change",
        "healthcare_worker_wellbeing",
        "practical_recommendation",
    },
}

THEME_QUESTION_BOUNDS = {
    "Theme_1_Adult_Wellbeing_as_Integrated_Balance": (1, 5),
    "Theme_2_Adult_Life_as_Relational_and_Role_Bearing_Strain": (1, 5),
    "Theme_3_Holistic_Care_Undermined_by_Time_Hierarchy_and_Navigation_Barriers": (3, 7),
    "Theme_4_Coordinated_and_Institutionally_Embedded_Adult_Care_Redesign": (4, 7),
}

SALIENCE_LABELS = [
    "most_prominent",
    "highly_prominent",
    "moderately_prominent",
    "present_but_less_prominent",
]

EXCERPT_SPECS = {
    "Theme_1_Adult_Wellbeing_as_Integrated_Balance": [
        ("D3_S0004", "theme_evidence"),
        ("D3_S0008", "theme_evidence"),
        ("D3_S0030", "theme_evidence"),
        ("D3_S0405", "theme_evidence"),
        ("D3_S0406", "theme_evidence"),
        ("D3_S0488", "theme_evidence"),
        ("D3_S0496", "theme_evidence"),
        ("D3_S0775", "theme_evidence"),
    ],
    "Theme_2_Adult_Life_as_Relational_and_Role_Bearing_Strain": [
        ("D3_S0016", "theme_evidence"),
        ("D3_S0067", "theme_evidence"),
        ("D3_S0173", "theme_evidence"),
        ("D3_S0311", "theme_evidence"),
        ("D3_S0466", "theme_evidence"),
        ("D3_S0504", "theme_evidence"),
        ("D3_S0562", "theme_evidence"),
        ("D3_S0793", "theme_evidence"),
    ],
    "Theme_3_Holistic_Care_Undermined_by_Time_Hierarchy_and_Navigation_Barriers": [
        ("D3_S0202", "theme_evidence"),
        ("D3_S0218", "theme_evidence"),
        ("D3_S0241", "theme_evidence"),
        ("D3_S0307", "theme_evidence"),
        ("D3_S0338", "theme_evidence"),
        ("D3_S0342", "theme_evidence"),
        ("D3_S0464", "theme_evidence"),
        ("D3_S0851", "theme_evidence"),
        ("D3_S1139", "theme_evidence"),
    ],
    "Theme_4_Coordinated_and_Institutionally_Embedded_Adult_Care_Redesign": [
        ("D3_S0225", "theme_evidence"),
        ("D3_S0324", "theme_evidence"),
        ("D3_S0331", "theme_evidence"),
        ("D3_S0333", "theme_evidence"),
        ("D3_S0568", "theme_evidence"),
        ("D3_S0868", "theme_evidence"),
        ("D3_S1140", "theme_evidence"),
        ("D3_S1149", "theme_evidence"),
        ("D3_S0873", "close_reading_theme_support"),
        ("D3_S1153", "close_reading_theme_support"),
    ],
}
