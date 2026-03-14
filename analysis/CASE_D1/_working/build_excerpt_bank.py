"""Build the excerpt bank, Q×Theme matrix, and prominence table from coded segments."""
import csv, json
from pathlib import Path
from collections import Counter, defaultdict

root = Path(r'c:\Users\baram\OneDrive\Desktop\themnatic')
d1_out = root / 'analysis' / 'CASE_D1'

# Read coded segments
with open(d1_out / 'CASE_D1_coded_segments.csv', 'r', encoding='utf-8') as f:
    segments = list(csv.DictReader(f))

# Theme-code mapping
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

# ═══════════════════════════════════════════════════════
# EXCERPT BANK — select best quotations per theme
# ═══════════════════════════════════════════════════════
p_segs = [s for s in segments if s['speaker_type'] == 'participant']

excerpt_bank = []
for theme_name, codes in theme_codes.items():
    # Get all participant segments matching this theme
    theme_segs = [s for s in p_segs if theme_name in s.get('themes', '')]
    
    # Sort by text length (longer = richer) and select diverse speakers
    theme_segs.sort(key=lambda x: -len(x['segment_text']))
    
    selected_speakers = set()
    selected_tables = set()
    
    for seg in theme_segs:
        speaker = seg['speaker_label']
        table = seg['table_id']
        # Prefer diversity: different speakers and tables
        diversity_bonus = (speaker not in selected_speakers) or (table not in selected_tables)
        if diversity_bonus or len([e for e in excerpt_bank if e['theme'] == theme_name]) < 8:
            if len([e for e in excerpt_bank if e['theme'] == theme_name]) >= 12:
                break
            excerpt_bank.append({
                'theme': theme_name,
                'segment_id': seg['segment_id'],
                'source_file': seg['source_file'],
                'table_id': seg['table_id'],
                'speaker_label': seg['speaker_label'],
                'speaker_type': seg['speaker_type'],
                'question_id': seg['question_id'],
                'excerpt_text': seg['segment_text'],
                'codes': seg['codes'],
                'language': seg['language'],
            })
            selected_speakers.add(speaker)
            selected_tables.add(table)

# Write excerpt bank
eb_fields = ['theme','segment_id','source_file','table_id','speaker_label',
             'speaker_type','question_id','excerpt_text','codes','language']
with open(d1_out / 'CASE_D1_excerpt_bank.csv', 'w', encoding='utf-8', newline='') as f:
    w = csv.DictWriter(f, fieldnames=eb_fields)
    w.writeheader()
    w.writerows(excerpt_bank)

print(f'Excerpt bank: {len(excerpt_bank)} excerpts')
for theme in theme_codes:
    count = sum(1 for e in excerpt_bank if e['theme'] == theme)
    speakers = len(set(e['speaker_label'] for e in excerpt_bank if e['theme'] == theme))
    tables = len(set(e['table_id'] for e in excerpt_bank if e['theme'] == theme))
    print(f'  {theme}: {count} excerpts, {speakers} speakers, {tables} tables')

# ═══════════════════════════════════════════════════════
# Q × THEME MATRIX
# ═══════════════════════════════════════════════════════
q_theme = defaultdict(lambda: defaultdict(int))
q_theme_speakers = defaultdict(lambda: defaultdict(set))
q_theme_tables = defaultdict(lambda: defaultdict(set))

for seg in p_segs:
    q = seg['question_id']
    for theme in seg.get('themes', '').split(';'):
        if theme and theme != 'unthemed':
            q_theme[q][theme] += 1
            q_theme_speakers[q][theme].add(seg['speaker_label'])
            q_theme_tables[q][theme].add(seg['table_id'])

# Write Q×Theme matrix CSV
questions = sorted(set(s['question_id'] for s in p_segs))
themes = list(theme_codes.keys())

matrix_rows = []
for q in questions:
    row = {'question_id': q}
    for theme in themes:
        count = q_theme[q].get(theme, 0)
        speakers = len(q_theme_speakers[q].get(theme, set()))
        tables = len(q_theme_tables[q].get(theme, set()))
        row[f'{theme}_segments'] = count
        row[f'{theme}_speakers'] = speakers
        row[f'{theme}_tables'] = tables
    matrix_rows.append(row)

matrix_fields = ['question_id']
for theme in themes:
    matrix_fields.extend([f'{theme}_segments', f'{theme}_speakers', f'{theme}_tables'])

with open(d1_out / 'CASE_D1_question_theme_matrix.csv', 'w', encoding='utf-8', newline='') as f:
    w = csv.DictWriter(f, fieldnames=matrix_fields)
    w.writeheader()
    w.writerows(matrix_rows)

print(f'\nQ×Theme matrix:')
header = f'{"Q":6s}'
for theme in themes:
    short = theme.replace('Theme_', 'T').replace('_Balanced_Contentment', '1').replace('_Care_Ecology', '2').replace('_Service_Fragmentation', '3').replace('_Culturally_Grounded_Solutions', '4')
    header += f' {short:>8s}'
print(header)
for row in matrix_rows:
    line = f'{row["question_id"]:6s}'
    for theme in themes:
        segs = row[f'{theme}_segments']
        spk = row[f'{theme}_speakers']
        line += f' {segs:3d}/{spk:2d}sp'
    print(line)

# ═══════════════════════════════════════════════════════
# PROMINENCE / SALIENCE TABLE
# ═══════════════════════════════════════════════════════
prominence_rows = []
for theme in themes:
    theme_p_segs = [s for s in p_segs if theme in s.get('themes', '')]
    total_segs = len(theme_p_segs)
    unique_speakers = len(set(s['speaker_label'] for s in theme_p_segs))
    unique_tables = len(set(s['table_id'] for s in theme_p_segs))
    total_chars = sum(len(s['segment_text']) for s in theme_p_segs)
    questions_present = sorted(set(s['question_id'] for s in theme_p_segs))
    
    # Salience assessment
    if total_segs >= 50 and unique_speakers >= 10 and unique_tables >= 3:
        salience = 'high'
    elif total_segs >= 20 and unique_speakers >= 5 and unique_tables >= 2:
        salience = 'medium'
    else:
        salience = 'emerging'
    
    prominence_rows.append({
        'theme': theme,
        'participant_segments': total_segs,
        'unique_speakers': unique_speakers,
        'unique_tables': unique_tables,
        'total_chars': total_chars,
        'questions_present': ';'.join(questions_present),
        'salience': salience,
        'salience_basis': f'{total_segs} segments from {unique_speakers} speakers across {unique_tables} tables covering {len(questions_present)} questions'
    })

prom_fields = ['theme','participant_segments','unique_speakers','unique_tables','total_chars','questions_present','salience','salience_basis']
with open(d1_out / 'CASE_D1_prominence_salience.csv', 'w', encoding='utf-8', newline='') as f:
    w = csv.DictWriter(f, fieldnames=prom_fields)
    w.writeheader()
    w.writerows(prominence_rows)

print(f'\nProminence/salience:')
for r in prominence_rows:
    print(f"  {r['theme']:45s} segs={r['participant_segments']:4d} spk={r['unique_speakers']:3d} tbl={r['unique_tables']:2d} sal={r['salience']:10s}")
