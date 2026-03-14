from __future__ import annotations

THEME_ORDER = [
    "Theme_1_Elderly_Wellbeing_as_Dignified_Integrated_Balance",
    "Theme_2_Good_Ageing_as_Relational_Belonging_Non_Burden_and_Continued_Significance",
    "Theme_3_Holistic_Elder_Care_as_Partially_Present_but_Unevenly_Integrated",
    "Theme_4_Institutionally_Embedded_and_Socially_Distributed_Routes_to_Elder_Care_Redesign",
]

THEME_LABELS = {
    "Theme_1_Elderly_Wellbeing_as_Dignified_Integrated_Balance": (
        "Elderly wellbeing as dignified integrated balance, spiritual-moral steadiness, and lived acceptance"
    ),
    "Theme_2_Good_Ageing_as_Relational_Belonging_Non_Burden_and_Continued_Significance": (
        "Good ageing as relational belonging, non-burden, and continued social significance"
    ),
    "Theme_3_Holistic_Elder_Care_as_Partially_Present_but_Unevenly_Integrated": (
        "Holistic elder care as partially present but unevenly integrated across services, training, and coordination"
    ),
    "Theme_4_Institutionally_Embedded_and_Socially_Distributed_Routes_to_Elder_Care_Redesign": (
        "Institutionally embedded and socially distributed routes to elder-care redesign"
    ),
}

THEME_CODES = {
    "Theme_1_Elderly_Wellbeing_as_Dignified_Integrated_Balance": {
        "balance_multidimensional",
        "contentment_acceptance",
        "spiritual_moral_anchor",
        "dignity_autonomy",
        "inner_peace_stability",
        "safety_security",
        "mental_health_elderly",
    },
    "Theme_2_Good_Ageing_as_Relational_Belonging_Non_Burden_and_Continued_Significance": {
        "family_caregiver_ecology",
        "dependence_resistance",
        "dignity_autonomy",
        "community_support_programs",
        "age_dignity_language",
        "post_retirement_gap",
        "intergenerational_shift",
        "containment_emotional_holding",
    },
    "Theme_3_Holistic_Elder_Care_as_Partially_Present_but_Unevenly_Integrated": {
        "service_adequacy_reflection",
        "institutional_example",
        "workforce_constraint",
        "care_fragmentation",
        "training_deficit",
        "cultural_barrier",
        "awareness_deficit",
        "institutional_culture_gap",
        "multidisciplinary_team",
        "home_care_services",
        "person_centered_care",
        "rehabilitation_services",
    },
    "Theme_4_Institutionally_Embedded_and_Socially_Distributed_Routes_to_Elder_Care_Redesign": {
        "practical_suggestion",
        "awareness_education",
        "technology_integration",
        "policy_recommendation",
        "training_development",
        "interdisciplinary_model",
        "community_support_programs",
        "institutional_example",
        "home_care_services",
    },
}

THEME_QUESTION_BOUNDS = {
    "Theme_1_Elderly_Wellbeing_as_Dignified_Integrated_Balance": (1, 4),
    "Theme_2_Good_Ageing_as_Relational_Belonging_Non_Burden_and_Continued_Significance": (1, 5),
    "Theme_3_Holistic_Elder_Care_as_Partially_Present_but_Unevenly_Integrated": (4, 6),
    "Theme_4_Institutionally_Embedded_and_Socially_Distributed_Routes_to_Elder_Care_Redesign": (5, 7),
}

SALIENCE_LABELS = [
    "most_prominent",
    "highly_prominent",
    "moderately_prominent",
    "present_but_less_prominent",
]

EXCERPT_SPECS = {
    "Theme_1_Elderly_Wellbeing_as_Dignified_Integrated_Balance": [
        ("D4_S0002", "theme_evidence"),
        ("D4_S0009", "theme_evidence"),
        ("D4_S0012", "close_reading_theme_support"),
        ("D4_S0034", "theme_evidence"),
        ("D4_S0057", "theme_evidence"),
        ("D4_S0063", "theme_evidence"),
        ("D4_S0106", "theme_evidence"),
        ("D4_S0200", "theme_evidence"),
    ],
    "Theme_2_Good_Ageing_as_Relational_Belonging_Non_Burden_and_Continued_Significance": [
        ("D4_S0007", "theme_evidence"),
        ("D4_S0013", "theme_evidence"),
        ("D4_S0036", "theme_evidence"),
        ("D4_S0062", "theme_evidence"),
        ("D4_S0068", "theme_evidence"),
        ("D4_S0093", "theme_evidence"),
        ("D4_S0097", "close_reading_theme_support"),
        ("D4_S0100", "theme_evidence"),
    ],
    "Theme_3_Holistic_Elder_Care_as_Partially_Present_but_Unevenly_Integrated": [
        ("D4_S0018", "close_reading_theme_support"),
        ("D4_S0019", "theme_evidence"),
        ("D4_S0020", "theme_evidence"),
        ("D4_S0021", "theme_evidence"),
        ("D4_S0168", "theme_evidence"),
        ("D4_S0169", "theme_evidence"),
        ("D4_S0173", "theme_evidence"),
        ("D4_S0177", "theme_evidence"),
        ("D4_S0182", "theme_evidence"),
    ],
    "Theme_4_Institutionally_Embedded_and_Socially_Distributed_Routes_to_Elder_Care_Redesign": [
        ("D4_S0022", "theme_evidence"),
        ("D4_S0024", "theme_evidence"),
        ("D4_S0025", "theme_evidence"),
        ("D4_S0028", "theme_evidence"),
        ("D4_S0030", "close_reading_theme_support"),
        ("D4_S0087", "theme_evidence"),
        ("D4_S0091", "theme_evidence"),
        ("D4_S0179", "theme_evidence"),
        ("D4_S0193", "theme_evidence"),
        ("D4_S0616", "theme_evidence"),
        ("D4_S0625", "theme_evidence"),
    ],
}
