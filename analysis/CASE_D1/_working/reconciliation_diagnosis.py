"""CASE_D1 Reconciliation Diagnosis — identify exact contradictions before fixing."""
import csv
from pathlib import Path
from collections import Counter, defaultdict

root = Path(r'c:\Users\baram\OneDrive\Desktop\themnatic')
d1_out = root / 'analysis' / 'CASE_D1'

with open(d1_out / 'CASE_D1_coded_segments.csv', 'r', encoding='utf-8') as f:
    segments = list(csv.DictReader(f))

theme_codes = {
    'Theme_1_Balanced_Contentment': [
        'contentment_as_core', 'balance_multidimensional', 'spiritual_moral_anchor',
        'safety_security', 'inner_peace', 'pillar_physical', 'pillar_emotional',
        'pillar_social', 'pillar_intellectual', 'pillar_spiritual'
    ],
    'Theme_2_Care_Ecology': [
        'interdependent_care', 'school_clinical_link', 'family_support_ecology',
        'community_volunteer_bridge', 'professional_identity', 'service_recipient_voice'
    ],
    'Theme_3_Service_Fragmentation': [
        'system_disconnection', 'training_deficit', 'resource_strain',
        'healthcare_system_critique', 'consultation_time_pressure',
        'staffing_shortage_isolation', 'medical_model_dominance',
        'missing_stepdown_services', 'bureaucratic_barrier',
        'child_vulnerability', 'child_mental_health', 'bullying_violence',
        'child_rights_inclusion'
    ],
    'Theme_4_Culturally_Grounded_Solutions': [
        'cultural_local_adaptation', 'transcultural_workforce',
        'awareness_education', 'early_detection_prevention',
        'practical_recommendation', 'top_down_systemic_change',
        'healthcare_worker_wellbeing', 'gradual_implementation',
        'digital_platform_proposal', 'respite_inclusive_resources'
    ],
}

p_segs = [s for s in segments if s['speaker_type'] == 'participant']

# ═══════ ISSUE 2: Q6/Q7 Theme 4 ═══════
print("=" * 60)
print("ISSUE 2: Q6/Q7 Theme 4 support")
print("=" * 60)

for qid in ['Q6', 'Q7']:
    q_p_segs = [s for s in p_segs if s['question_id'] == qid]
    print(f"\n{qid}: {len(q_p_segs)} participant segments")
    t4_codes_set = set(theme_codes['Theme_4_Culturally_Grounded_Solutions'])
    t4_matches = []
    code_dist = Counter()
    for s in q_p_segs:
        seg_codes = set(s['codes'].split(';'))
        for c in seg_codes:
            code_dist[c] += 1
        if seg_codes & t4_codes_set:
            t4_matches.append(s)
    print(f"  Theme 4 code matches: {len(t4_matches)}")
    for code, cnt in code_dist.most_common(15):
        in_themes = [t.split('_', 2)[-1][:20] for t, cs in theme_codes.items() if code in cs]
        print(f"    {code}: {cnt}  -> {in_themes if in_themes else 'NO THEME'}")
    # Show all theme matches for this Q
    for theme in theme_codes:
        t_codes = set(theme_codes[theme])
        matches = sum(1 for s in q_p_segs if set(s['codes'].split(';')) & t_codes)
        print(f"  {theme}: {matches} matches")

# ═══════ ISSUE 3: note_taker_summary ═══════
print("\n" + "=" * 60)
print("ISSUE 3: note_taker_summary traceability")
print("=" * 60)
type_counts = Counter(s['speaker_type'] for s in segments)
for t, c in type_counts.most_common():
    print(f"  {t}: {c}")
print(f"  note_taker_summary present: {'note_taker_summary' in type_counts}")

# ═══════ ISSUE 4: Codebook counts ═══════
print("\n" + "=" * 60)
print("ISSUE 4: Codebook count mismatch")
print("=" * 60)
print(f"  ACTUAL from CSV: participant={type_counts.get('participant',0)}, "
      f"moderator={type_counts.get('moderator',0)}, "
      f"unclear={type_counts.get('unclear',0)}, total={len(segments)}")
print(f"  Codebook claims: 947 participant, 144 moderator, 67 unclear (total 1158)")
print(f"  Cross-check claims: 811 participant, 278 moderator, 69 unclear (total 1158)")

# ═══════ ISSUE 5: Source contribution / HWCH7AR ═══════
print("\n" + "=" * 60)
print("ISSUE 5: Source contribution — per-source theme matches")
print("=" * 60)

source_theme_data = defaultdict(lambda: {'themes': set(), 'p_segs': 0, 'total': 0, 'speakers': set()})
for s in segments:
    src = s['source_file']
    source_theme_data[src]['total'] += 1
    if s['speaker_type'] == 'participant':
        source_theme_data[src]['p_segs'] += 1
        source_theme_data[src]['speakers'].add(s['speaker_label'])
        seg_codes = set(s['codes'].split(';'))
        for theme, codes in theme_codes.items():
            if seg_codes & set(codes):
                source_theme_data[src]['themes'].add(theme)

for src in sorted(source_theme_data):
    d = source_theme_data[src]
    themes_str = ';'.join(sorted(d['themes'])) if d['themes'] else 'NONE'
    print(f"  {src:20s} total={d['total']:4d} p_segs={d['p_segs']:4d} spk={len(d['speakers']):3d} themes={themes_str}")

# Specifically check HWCH7AR codes
print(f"\n  HWCH7AR detailed code breakdown:")
hwch7_p = [s for s in p_segs if 'HWCH7AR' in s['source_file']]
hwch7_codes = Counter()
for s in hwch7_p:
    for c in s['codes'].split(';'):
        hwch7_codes[c] += 1
for code, cnt in hwch7_codes.most_common():
    in_themes = [t.split('_', 2)[-1][:25] for t, cs in theme_codes.items() if code in cs]
    print(f"    {code}: {cnt}  -> {in_themes if in_themes else 'NO THEME'}")

# ═══════ ISSUE 6: Cross-check file count ═══════
print("\n" + "=" * 60)
print("ISSUE 6: Cross-check deliverable count")
print("=" * 60)
actual_files = [f for f in sorted(d1_out.glob('*')) if f.is_file() and not f.name.startswith('_')]
print(f"  Actual files in CASE_D1 dir: {len(actual_files)}")
for f in actual_files:
    print(f"    {f.name}")

# ═══════ ISSUE 1: HWCH10AR content style ═══════
print("\n" + "=" * 60)
print("ISSUE 1: HWCH10AR content style check")
print("=" * 60)
hwch10_p = [s for s in p_segs if 'HWCH10AR' in s['source_file']]
print(f"  HWCH10AR participant segments: {len(hwch10_p)}")
third_person_markers = ['Described ', 'Noted ', 'Called for', 'Argued ', 'Highlighted ',
                        'Identified ', 'Introduced ', 'Proposed ', 'Recommended ', 'Provided ',
                        'Recounted ', 'Suggested ', 'Emphasized ', 'Critiqued ', 'Shared ']
tp_count = 0
for s in hwch10_p:
    text = s['segment_text'][:50]
    if any(text.startswith(m) for m in third_person_markers):
        tp_count += 1
print(f"  Segments starting with third-person markers: {tp_count}/{len(hwch10_p)}")
print(f"  Conclusion: HWCH10AR contains note-style summaries, not verbatim speech")

# ═══════ EXCERPT BANK: check sources ═══════
print("\n" + "=" * 60)
print("EXCERPT BANK: source distribution")
print("=" * 60)
with open(d1_out / 'CASE_D1_excerpt_bank.csv', 'r', encoding='utf-8') as f:
    excerpts = list(csv.DictReader(f))
exc_sources = Counter(e['source_file'] for e in excerpts)
for src, cnt in exc_sources.most_common():
    print(f"  {src}: {cnt}")

# Check if any HWCH10AR excerpts are note-style
hwch10_exc = [e for e in excerpts if 'HWCH10AR' in e['source_file']]
print(f"\n  HWCH10AR excerpts: {len(hwch10_exc)}")
for e in hwch10_exc:
    style = "note_style" if any(e['excerpt_text'][:50].startswith(m) for m in third_person_markers) else "possible_verbatim"
    print(f"    {e['segment_id']} [{style}]: {e['excerpt_text'][:80]}...")
