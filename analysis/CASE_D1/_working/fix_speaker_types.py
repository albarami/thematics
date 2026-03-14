"""Fix speaker_type misclassifications in CASE_D1_coded_segments.csv"""
import csv
from pathlib import Path
from collections import Counter

root = Path(r'c:\Users\baram\OneDrive\Desktop\themnatic')
d1_out = root / 'analysis' / 'CASE_D1'

with open(d1_out / 'CASE_D1_coded_segments.csv', 'r', encoding='utf-8') as f:
    segments = list(csv.DictReader(f))

fixes = 0
for seg in segments:
    label = seg['speaker_label']
    tid = seg['table_id']
    old_type = seg['speaker_type']

    # T4 session manager = moderator
    if tid == '4' and 'مدير الجلسة' in label:
        seg['speaker_type'] = 'moderator'
        if old_type != 'moderator':
            fixes += 1

    # T7 session manager = moderator
    if tid == '7' and 'مدير الجلسه' in label:
        seg['speaker_type'] = 'moderator'
        if old_type != 'moderator':
            fixes += 1

    # T6 نور الوتاري = moderator
    if tid == '6' and 'نور الوتاري' in label:
        seg['speaker_type'] = 'moderator'
        if old_type != 'moderator':
            fixes += 1

    # T3 moderator prompt captured as speaker label
    if tid == '3' and 'دعنا ننتقل' in label:
        seg['speaker_type'] = 'moderator'
        if old_type != 'moderator':
            fixes += 1

    # T4 sentence fragments caught as speaker labels — classify as unclear
    if tid == '4' and ('مرّ علي موضوعين' in label or 'الشخص يكون عارف' in label):
        seg['speaker_type'] = 'unclear'
        if old_type != 'unclear':
            fixes += 1

print(f'Fixed {fixes} speaker_type misclassifications')

# Write back
fieldnames = list(segments[0].keys())
with open(d1_out / 'CASE_D1_coded_segments.csv', 'w', encoding='utf-8', newline='') as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    w.writerows(segments)

# Revised counts
type_counts = Counter(s['speaker_type'] for s in segments)
print(f'\nRevised speaker_type distribution:')
for t, c in type_counts.most_common():
    print(f'  {t}: {c}')

# Verify moderator labels
mod_segs = [s for s in segments if s['speaker_type'] == 'moderator']
mod_labels = Counter(s['speaker_label'][:40] for s in mod_segs)
print(f'\nModerator labels ({len(mod_segs)} total):')
for l, c in mod_labels.most_common():
    print(f'  {l}: {c}')

# Participant-only count
p_segs = [s for s in segments if s['speaker_type'] == 'participant']
print(f'\nParticipant segments: {len(p_segs)}')
