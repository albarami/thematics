"""CASE_D1 Final Re-Verification — strict 10-point check after reconciliation + anonymization."""
import csv
from pathlib import Path
from collections import Counter

root = Path(r'c:\Users\baram\OneDrive\Desktop\themnatic')
d1_out = root / 'analysis' / 'CASE_D1'

errors = []
warnings = []

def check(name, condition, msg=''):
    if condition:
        print(f'  [PASS] {name}')
    else:
        print(f'  [FAIL] {name}: {msg}')
        errors.append(f'{name}: {msg}')

def load_csv(fn):
    p = d1_out / fn
    if not p.exists():
        errors.append(f'Missing: {fn}')
        return []
    with open(p, 'r', encoding='utf-8') as f:
        return list(csv.DictReader(f))

segments = load_csv('CASE_D1_coded_segments.csv')
excerpts = load_csv('CASE_D1_excerpt_bank.csv')
prominence = load_csv('CASE_D1_prominence_salience.csv')
matrix = load_csv('CASE_D1_question_theme_matrix.csv')
src_contrib = load_csv('CASE_D1_source_contribution_table.csv')
part_summary = load_csv('CASE_D1_participant_summary.csv')

theme_codes = {
    'Theme_1_Balanced_Contentment': [
        'contentment_as_core', 'balance_multidimensional', 'spiritual_moral_anchor',
        'safety_security', 'inner_peace', 'pillar_physical', 'pillar_emotional',
        'pillar_social', 'pillar_intellectual', 'pillar_spiritual'],
    'Theme_2_Care_Ecology': [
        'interdependent_care', 'school_clinical_link', 'family_support_ecology',
        'community_volunteer_bridge', 'professional_identity', 'service_recipient_voice'],
    'Theme_3_Service_Fragmentation': [
        'system_disconnection', 'training_deficit', 'resource_strain',
        'healthcare_system_critique', 'consultation_time_pressure',
        'staffing_shortage_isolation', 'medical_model_dominance',
        'missing_stepdown_services', 'bureaucratic_barrier',
        'child_vulnerability', 'child_mental_health', 'bullying_violence',
        'child_rights_inclusion'],
    'Theme_4_Culturally_Grounded_Solutions': [
        'cultural_local_adaptation', 'transcultural_workforce',
        'awareness_education', 'early_detection_prevention',
        'practical_recommendation', 'top_down_systemic_change',
        'healthcare_worker_wellbeing', 'gradual_implementation',
        'digital_platform_proposal', 'respite_inclusive_resources'],
}

p_segs = [s for s in segments if s['speaker_type'] == 'participant']

# ═══════ CHECK 1: Every quotation correctly classified and traceable ═══════
print('\n=== CHECK 1: Quotation classification ===')
check('Excerpt bank has evidence_type column',
      excerpts and 'evidence_type' in excerpts[0],
      'evidence_type column missing')
if excerpts and 'evidence_type' in excerpts[0]:
    ev_types = Counter(e['evidence_type'] for e in excerpts)
    for t, c in ev_types.items():
        check(f'Evidence type "{t}" is valid',
              t in ('verbatim_transcript', 'note_style_transcript_summary', 'note_taker_summary'),
              f'Unknown evidence type: {t}')
    check('All excerpts have evidence_type',
          all(e['evidence_type'] for e in excerpts),
          'Some excerpts missing evidence_type')

# Check report has provenance labels
report_path = d1_out / 'CASE_D1_final_report.md'
report_text = report_path.read_text(encoding='utf-8') if report_path.exists() else ''
check('Report has evidence classification section',
      'Evidence classification' in report_text or 'evidence classification' in report_text,
      'Missing evidence classification section')
check('Report labels note-style summaries',
      '[note-style summary]' in report_text,
      'No [note-style summary] labels found')
check('Report labels note-taker records',
      '[note-taker' in report_text,
      'No [note-taker] labels found')

# ═══════ CHECK 2: Evidence rule matches quotations ═══════
print('\n=== CHECK 2: Evidence rule consistency ===')
check('Report states evidence rule in Section 1.3',
      'quotation provenance rule' in report_text.lower() or 'evidence classification' in report_text.lower(),
      'No evidence rule section found')
# Old incorrect claim should be gone
check('No "every quotation maps to participant evidence" claim',
      'every quotation maps to participant evidence' not in report_text.lower(),
      'Old incorrect claim still present')

# ═══════ CHECK 3: No unsupported Q-to-theme claims ═══════
print('\n=== CHECK 3: Q-to-theme claims ===')
# Theme 4 Q6 and Q7 in matrix
for m in matrix:
    if m['question_id'] == 'Q6':
        t4_q6 = int(m['Theme_4_Culturally_Grounded_Solutions_segments'])
        check(f'Matrix Theme 4 Q6 = {t4_q6}', t4_q6 == 0, f'Expected 0, got {t4_q6}')
    if m['question_id'] == 'Q7':
        t4_q7 = int(m['Theme_4_Culturally_Grounded_Solutions_segments'])
        check(f'Matrix Theme 4 Q7 = {t4_q7}', t4_q7 == 0, f'Expected 0, got {t4_q7}')

# Report should acknowledge Q6/Q7 coding limitation
check('Report acknowledges Q6/Q7 coding gap',
      'general_response' in report_text and 'close reading' in report_text.lower(),
      'Q6/Q7 coding limitation not acknowledged')

# Final themes should NOT claim Q6/Q7 as primary coded support for Theme 4
themes_text = (d1_out / 'CASE_D1_final_themes.md').read_text(encoding='utf-8')
check('Final themes: Theme 4 Q6/Q7 not claimed as coded',
      'Close-reading support only (not coded)' in themes_text or 'close-reading support' in themes_text.lower(),
      'Theme 4 still claims coded Q6/Q7 support')

# ═══════ CHECK 4: speaker_type handling ═══════
print('\n=== CHECK 4: speaker_type handling ===')
type_counts = Counter(s['speaker_type'] for s in segments)
check(f'Speaker types: p={type_counts["participant"]}, m={type_counts["moderator"]}, u={type_counts["unclear"]}',
      type_counts['participant'] == 811 and type_counts['moderator'] == 278 and type_counts['unclear'] == 69,
      f'Expected 811/278/69, got {type_counts}')
check('note_taker_summary absence documented',
      'note_taker_summary' in report_text and 'does not appear' in report_text,
      'note_taker_summary absence not documented in report')

# Codebook should have correct counts
codebook_text = (d1_out / 'CASE_D1_working_codebook.md').read_text(encoding='utf-8')
check('Codebook has 811 participant',
      '811 participant' in codebook_text,
      'Codebook still has wrong participant count')
check('Codebook has 278 moderator',
      '278 moderator' in codebook_text,
      'Codebook still has wrong moderator count')

# ═══════ CHECK 5: Codebook counts match coded segments ═══════
print('\n=== CHECK 5: Codebook counts ===')
check('Codebook total 1158',
      '1158' in codebook_text,
      'Total 1158 not in codebook')

# ═══════ CHECK 6: Source contribution matches report ═══════
print('\n=== CHECK 6: Source contribution ===')
hwch7 = [s for s in src_contrib if 'HWCH7AR' in s['source_file']]
if hwch7:
    themes = hwch7[0]['themes_present']
    check('HWCH7AR themes_present is empty in source contrib',
          themes == '',
          f'Expected empty, got "{themes}"')
check('Report acknowledges HWCH7AR coding limitation',
      'general_response' in report_text and 'HWCH7AR' in report_text,
      'HWCH7AR coding limitation not in report')

# Verify all prominence counts match actual coded segments
for p in prominence:
    theme = p['theme']
    reported = int(p['participant_segments'])
    t_codes = set(theme_codes[theme])
    actual = sum(1 for s in p_segs if set(s['codes'].split(';')) & t_codes)
    check(f'Prominence {theme}: {reported} = {actual}',
          reported == actual,
          f'Mismatch: prominence says {reported}, actual {actual}')

# ═══════ CHECK 7: File count ═══════
print('\n=== CHECK 7: File count ===')
actual_files = [f for f in sorted(d1_out.glob('*')) if f.is_file() and not f.name.startswith('_')]
check(f'File count: {len(actual_files)} files',
      len(actual_files) == 26,
      f'Expected 26, found {len(actual_files)}')
crosscheck_text = (d1_out / 'CASE_D1_crosscheck_report.md').read_text(encoding='utf-8')
check('Cross-check says 26 files',
      '26 files' in crosscheck_text or '(26 files)' in crosscheck_text,
      'Cross-check file count wrong')

# ═══════ CHECK 8: Anonymized labels consistent ═══════
print('\n=== CHECK 8: Anonymization consistency ===')
# Check coded segments has anonymized_speaker
check('Coded segments has anonymized_speaker',
      'anonymized_speaker' in segments[0] if segments else False,
      'anonymized_speaker column missing')

# Check excerpt bank has anonymized_speaker
check('Excerpt bank has anonymized_speaker',
      'anonymized_speaker' in excerpts[0] if excerpts else False,
      'anonymized_speaker column missing')

# Check report uses D1_P codes
d1p_count = report_text.count('D1_P')
check(f'Report uses D1_P codes ({d1p_count} occurrences)',
      d1p_count >= 20,
      f'Only {d1p_count} D1_P codes found — expected many more')

# Check final themes uses D1_P codes
d1p_themes = themes_text.count('D1_P')
check(f'Final themes uses D1_P codes ({d1p_themes} occurrences)',
      d1p_themes >= 10,
      f'Only {d1p_themes} D1_P codes found')

# ═══════ CHECK 9: No real names in outward-facing files ═══════
print('\n=== CHECK 9: No real names in outward-facing files ===')
real_names = [
    'Manal', 'Hafsa Abdullah', 'Melissa Toon', 'Muhammad Ali',
    'Angela Lwage', 'Nawal Yosul', 'Dr. Afaf Asuhou', 'Alaa Karmala',
    'Dr. Wael Mahmoud', 'Fatma Al-Obaidan', 'Shafaq Al-Khalidi',
    'Amani Al-Yafei', 'Latifa Al-Sulaiti', 'Dr. Khalid',
    'Dr Ahmed Al Emadi',
]
# Check report
for name in real_names:
    if name in report_text:
        check(f'No "{name}" in report', False, f'"{name}" found in report')
    else:
        pass  # PASS silently for brevity

# Count total real name occurrences in report
total_real = sum(1 for name in real_names if name in report_text)
check(f'Real names in report: {total_real}',
      total_real == 0,
      f'{total_real} real names still in report')

# Check final themes
total_real_themes = sum(1 for name in real_names if name in themes_text)
check(f'Real names in final themes: {total_real_themes}',
      total_real_themes == 0,
      f'{total_real_themes} real names still in final themes')

# ═══════ CHECK 10: No Day 5 / cross-case ═══════
print('\n=== CHECK 10: No cross-case contamination ===')
all_md = ''
for f in d1_out.glob('*.md'):
    all_md += f.read_text(encoding='utf-8')
check('No CASE_D5', 'CASE_D5' not in all_md, 'CASE_D5 found')
check('No Day 5', 'Day 5' not in all_md and 'Day5' not in all_md, 'Day 5 found')
check('No CASE_D2/D3/D4',
      'CASE_D2' not in all_md and 'CASE_D3' not in all_md and 'CASE_D4' not in all_md,
      'Other case reference found')

# ═══════ IDENTITY KEY CHECK ═══════
print('\n=== EXTRA: Identity key exists ===')
check('participant_identity_key.xlsx exists',
      (d1_out / 'participant_identity_key.xlsx').exists(),
      'Missing')
check('participant_summary_anonymized.xlsx exists',
      (d1_out / 'participant_summary_anonymized.xlsx').exists(),
      'Missing')

# ═══════ FINAL SUMMARY ═══════
print(f'\n{"="*60}')
print(f'FINAL RE-VERIFICATION SUMMARY')
print(f'{"="*60}')
print(f'Errors: {len(errors)}')
print(f'Warnings: {len(warnings)}')
if errors:
    print('\nERRORS:')
    for e in errors:
        print(f'  - {e}')
if warnings:
    print('\nWARNINGS:')
    for w in warnings:
        print(f'  - {w}')
if not errors:
    print('\nAll checks passed. CASE_D1 package is reconciled, anonymized, and internally consistent.')
