"""Fix prominence salience (avoid uniformly high), build summary tables and Excel workbooks."""
import csv, json
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

# Assign themes to segments
for seg in segments:
    seg_codes = set(seg['codes'].split(';'))
    themes = []
    for theme, codes in theme_codes.items():
        if seg_codes & set(codes):
            themes.append(theme)
    seg['themes'] = ';'.join(themes) if themes else 'unthemed'

p_segs = [s for s in segments if s['speaker_type'] == 'participant']

# ═══════════════════════════════════════════════════════
# RECALIBRATED PROMINENCE / SALIENCE TABLE
# ═══════════════════════════════════════════════════════
prominence_data = {}
for theme in theme_codes:
    theme_p_segs = [s for s in p_segs if theme in s.get('themes', '')]
    total_segs = len(theme_p_segs)
    unique_speakers = len(set(s['speaker_label'] for s in theme_p_segs))
    unique_tables = len(set(s['table_id'] for s in theme_p_segs))
    total_chars = sum(len(s['segment_text']) for s in theme_p_segs)
    questions_present = sorted(set(s['question_id'] for s in theme_p_segs))
    prominence_data[theme] = {
        'segments': total_segs, 'speakers': unique_speakers,
        'tables': unique_tables, 'chars': total_chars,
        'questions': questions_present
    }

# Rank themes by a composite score: segments + (speakers * 3) + (tables * 5) + (questions * 2)
for theme, d in prominence_data.items():
    d['composite'] = d['segments'] + (d['speakers'] * 3) + (d['tables'] * 5) + (len(d['questions']) * 2)

ranked = sorted(prominence_data.items(), key=lambda x: -x[1]['composite'])

# Assign differentiated salience based on ranking and evidence characteristics
salience_map = {}
for i, (theme, d) in enumerate(ranked):
    if i == 0:
        salience_map[theme] = 'most_prominent'
    elif i == 1:
        salience_map[theme] = 'highly_prominent'
    elif i == 2:
        salience_map[theme] = 'moderately_prominent'
    else:
        salience_map[theme] = 'present_but_less_prominent'

prominence_rows = []
for theme in theme_codes:
    d = prominence_data[theme]
    sal = salience_map[theme]
    
    # Detailed salience explanation
    if sal == 'most_prominent':
        explanation = f'Highest composite evidence: {d["segments"]} segments from {d["speakers"]} speakers across {d["tables"]} tables in {len(d["questions"])} questions. Sustained presence across the widest range of discussion.'
    elif sal == 'highly_prominent':
        explanation = f'Strong evidence base: {d["segments"]} segments from {d["speakers"]} speakers across {d["tables"]} tables. Frequently spoken about but with slightly narrower scope than the most prominent theme.'
    elif sal == 'moderately_prominent':
        explanation = f'Solid evidence with broad speaker base: {d["segments"]} segments from {d["speakers"]} speakers across {d["tables"]} tables. Well-supported but with fewer coded segments than the top two themes.'
    else:
        explanation = f'Present with meaningful evidence: {d["segments"]} segments from {d["speakers"]} speakers across {d["tables"]} tables. Important analytically but with more limited coded evidence volume.'
    
    prominence_rows.append({
        'theme': theme,
        'participant_segments': d['segments'],
        'unique_speakers': d['speakers'],
        'unique_tables': d['tables'],
        'total_chars': d['chars'],
        'questions_present': ';'.join(d['questions']),
        'composite_score': d['composite'],
        'salience': sal,
        'salience_explanation': explanation,
    })

prom_fields = list(prominence_rows[0].keys())
with open(d1_out / 'CASE_D1_prominence_salience.csv', 'w', encoding='utf-8', newline='') as f:
    w = csv.DictWriter(f, fieldnames=prom_fields)
    w.writeheader()
    w.writerows(prominence_rows)

print('Recalibrated prominence/salience:')
for r in prominence_rows:
    print(f"  {r['theme']:45s} segs={r['participant_segments']:4d} spk={r['unique_speakers']:3d} tbl={r['unique_tables']:2d} composite={r['composite_score']:4d} → {r['salience']}")

# ═══════════════════════════════════════════════════════
# SUMMARY TABLES
# ═══════════════════════════════════════════════════════
# Table 1: Theme summary
theme_summary = []
theme_short_names = {
    'Theme_1_Balanced_Contentment': 'Balanced contentment, safety, and moral steadiness',
    'Theme_2_Care_Ecology': 'Interdependent professional support ecology',
    'Theme_3_Service_Fragmentation': 'Fragmented, strained childhood service conditions',
    'Theme_4_Culturally_Grounded_Solutions': 'Culturally grounded coordination and implementation',
}
for theme in theme_codes:
    d = prominence_data[theme]
    theme_summary.append({
        'theme_number': theme.split('_')[1],
        'theme_name': theme_short_names[theme],
        'participant_segments': d['segments'],
        'unique_speakers': d['speakers'],
        'unique_tables': d['tables'],
        'questions_present': ';'.join(d['questions']),
        'salience': salience_map[theme],
    })

with open(d1_out / 'CASE_D1_theme_summary_table.csv', 'w', encoding='utf-8', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(theme_summary[0].keys()))
    w.writeheader()
    w.writerows(theme_summary)

# Table 2: Source contribution summary
source_summary = defaultdict(lambda: {'segments': 0, 'participant_segs': 0, 'speakers': set(), 'themes': set(), 'questions': set()})
for seg in segments:
    src = seg['source_file']
    source_summary[src]['segments'] += 1
    if seg['speaker_type'] == 'participant':
        source_summary[src]['participant_segs'] += 1
        source_summary[src]['speakers'].add(seg['speaker_label'])
    source_summary[src]['questions'].add(seg['question_id'])
    for t in seg.get('themes', '').split(';'):
        if t and t != 'unthemed':
            source_summary[src]['themes'].add(t)

src_rows = []
for src in sorted(source_summary.keys()):
    d = source_summary[src]
    src_rows.append({
        'source_file': src,
        'total_segments': d['segments'],
        'participant_segments': d['participant_segs'],
        'unique_speakers': len(d['speakers']),
        'questions_covered': ';'.join(sorted(d['questions'])),
        'themes_present': ';'.join(sorted(d['themes'])),
    })

with open(d1_out / 'CASE_D1_source_contribution_table.csv', 'w', encoding='utf-8', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(src_rows[0].keys()))
    w.writeheader()
    w.writerows(src_rows)

print(f'\nSource contribution:')
for r in src_rows:
    print(f"  {r['source_file']:25s} segs={r['total_segments']:4d} p_segs={r['participant_segments']:4d} spk={r['unique_speakers']:3d}")

print('\nAll summary CSVs written.')
