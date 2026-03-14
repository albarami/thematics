"""Inspect diverse Day 4 excerpt candidates by code clusters and question spread."""
from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path

CASE_DIR = Path(r"c:\Users\baram\OneDrive\Desktop\themnatic\analysis\CASE_D4")
ROWS = list(csv.DictReader((CASE_DIR / "CASE_D4_coded_segments.csv").open("r", encoding="utf-8-sig")))
P_ROWS = [r for r in ROWS if r["speaker_type"] == "participant"]

print("participant_segments", len(P_ROWS))
print("unique_speakers", len({r['speaker_code'] for r in P_ROWS}))
print()

code_counter: Counter[str] = Counter()
for row in P_ROWS:
    code_counter.update(c for c in row["codes"].split(";") if c)

print("top_codes")
for code, count in code_counter.most_common(30):
    print(f"  {code}: {count}")
print()

CLUSTERS = {
    "T1_conceptual_integrated_good_life": {
        "codes": {
            "balance_multidimensional", "contentment_acceptance",
            "spiritual_moral_anchor", "dignity_autonomy",
            "inner_peace_stability", "age_dignity_language",
            "mental_health_elderly",
        },
        "questions": {"Q1", "Q2", "Q3"},
    },
    "T2_relational_ageing_and_non_burden": {
        "codes": {
            "family_caregiver_ecology", "dependence_resistance",
            "dignity_autonomy", "community_support_programs",
            "age_dignity_language", "post_retirement_gap",
            "intergenerational_shift", "containment_emotional_holding",
        },
        "questions": {"Q1", "Q2", "Q3", "Q4"},
    },
    "T3_partial_holistic_care_and_system_strain": {
        "codes": {
            "service_adequacy_reflection", "institutional_example",
            "workforce_constraint", "care_fragmentation",
            "training_deficit", "cultural_barrier",
            "awareness_deficit", "institutional_culture_gap",
            "multidisciplinary_team", "home_care_services",
            "person_centered_care",
        },
        "questions": {"Q4", "Q5", "Q6"},
    },
    "T4_redesign_and_embedding_routes": {
        "codes": {
            "practical_suggestion", "awareness_education",
            "technology_integration", "policy_recommendation",
            "training_development", "interdisciplinary_model",
            "community_support_programs", "institutional_example",
            "home_care_services",
        },
        "questions": {"Q5", "Q6", "Q7"},
    },
    "cross_cutting_pillars_and_prioritisation": {
        "codes": {
            "pillar_spiritual", "pillar_emotional", "pillar_intellectual",
            "pillar_physical", "pillar_social", "balance_multidimensional",
        },
        "questions": {"Q3", "Q4"},
    },
}


def matches_cluster(row: dict[str, str], spec: dict[str, set[str]]) -> bool:
    codes = {c for c in row["codes"].split(";") if c}
    return row["question_id"] in spec["questions"] and bool(codes & spec["codes"])


for name, spec in CLUSTERS.items():
    rows = [r for r in P_ROWS if matches_cluster(r, spec)]
    rows.sort(key=lambda r: (-len(r["segment_text"]), r["segment_id"]))
    print(f"=== {name} ===")
    print("count", len(rows))
    print("speakers", len({r['speaker_code'] for r in rows}))
    print("questions", sorted({r['question_id'] for r in rows}))
    shown = 0
    seen_speakers: set[str] = set()
    for row in rows:
        if shown >= 15:
            break
        speaker = row["speaker_code"]
        is_new = speaker not in seen_speakers
        if not is_new and len(row["segment_text"]) < 350:
            continue
        seen_speakers.add(speaker)
        snippet = row["segment_text"][:260].replace("\n", " ")
        print(
            f"{row['segment_id']} | {row['speaker_code']} | {row['question_id']} | "
            f"{row['source_file']} | len={len(row['segment_text'])} | {row['codes']}"
        )
        print(f"  {snippet}")
        shown += 1
    print()

print("question_by_source")
source_q = defaultdict(Counter)
for row in P_ROWS:
    source_q[row["source_file"]][row["question_id"]] += 1
for source, ctr in sorted(source_q.items()):
    print(source, dict(sorted(ctr.items())))
