"""Find best excerpt candidates for each theme."""
import csv
from pathlib import Path

CSV = Path(r"c:\Users\baram\OneDrive\Desktop\themnatic\analysis\CASE_D4\CASE_D4_coded_segments.csv")
rows = list(csv.DictReader(CSV.open("r", encoding="utf-8-sig")))
p = [r for r in rows if r["speaker_type"] == "participant" and len(r["segment_text"]) > 150]

THEMES = {
    "T1": {
        "codes": {"contentment_acceptance", "spiritual_moral_anchor", "dignity_autonomy",
                  "inner_peace_stability", "balance_multidimensional", "age_dignity_language"},
        "questions": {"Q1", "Q2", "Q3"},
    },
    "T2": {
        "codes": {"family_caregiver_ecology", "containment_emotional_holding",
                  "intergenerational_shift", "dependence_resistance", "post_retirement_gap"},
        "questions": None,
    },
    "T3": {
        "codes": {"care_fragmentation", "workforce_constraint", "training_deficit",
                  "cultural_barrier", "institutional_culture_gap", "awareness_deficit",
                  "service_adequacy_reflection"},
        "questions": {"Q4", "Q5", "Q6"},
    },
    "T4": {
        "codes": {"practical_suggestion", "technology_integration", "awareness_education",
                  "policy_recommendation", "training_development", "interdisciplinary_model",
                  "community_support_programs"},
        "questions": {"Q5", "Q6", "Q7"},
    },
}

for tid, spec in THEMES.items():
    cands = []
    for r in p:
        seg_codes = set(r["codes"].split(";"))
        if not spec["codes"].intersection(seg_codes):
            continue
        if spec["questions"] and r["question_id"] not in spec["questions"]:
            continue
        cands.append(r)
    cands.sort(key=lambda x: -len(x["segment_text"]))
    print(f"\n=== {tid} candidates: {len(cands)} ===")
    seen_speakers = set()
    shown = 0
    for r in cands:
        if shown >= 12:
            break
        sp = r["speaker_code"]
        marker = " *NEW*" if sp not in seen_speakers else ""
        seen_speakers.add(sp)
        codes_short = r["codes"][:90]
        print(f"  {r['segment_id']} {sp} {r['question_id']} {r['source_file'][:10]} "
              f"len={len(r['segment_text']):>4} {codes_short}{marker}")
        shown += 1
