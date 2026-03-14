"""Fix unmapped Arabic labels by building mapping from actual CSV speaker labels."""
import csv
from pathlib import Path
from collections import Counter

root = Path(r'c:\Users\baram\OneDrive\Desktop\themnatic')
d1_out = root / 'analysis' / 'CASE_D1'

with open(d1_out / 'CASE_D1_coded_segments.csv', 'r', encoding='utf-8') as f:
    segments = list(csv.DictReader(f))

# Get all unique speaker labels per table + type
label_info = {}
for s in segments:
    key = (s['table_id'], s['speaker_label'], s['speaker_type'])
    if key not in label_info:
        label_info[key] = {'count': 0, 'chars': 0}
    label_info[key]['count'] += 1
    label_info[key]['chars'] += len(s['segment_text'])

print("All unique speaker labels in coded_segments.csv:")
print(f"{'Table':>5} {'Type':>15} {'Count':>6} {'Chars':>8}  Label")
print("-" * 100)
for (tid, label, stype), info in sorted(label_info.items(), key=lambda x: (x[0][0], x[0][2], -x[1]['chars'])):
    print(f"{tid:>5} {stype:>15} {info['count']:>6} {info['chars']:>8}  {label[:60]}")
