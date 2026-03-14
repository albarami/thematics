"""Extract key quotations for the final report from the excerpt bank and coded segments."""
import csv
from pathlib import Path

root = Path(r'c:\Users\baram\OneDrive\Desktop\themnatic')
d1_out = root / 'analysis' / 'CASE_D1'

with open(d1_out / 'CASE_D1_excerpt_bank.csv', 'r', encoding='utf-8') as f:
    excerpts = list(csv.DictReader(f))

print(f'Total excerpts: {len(excerpts)}')
for e in excerpts:
    theme_short = e['theme'].replace('Theme_', 'T').replace('_Balanced_Contentment', '1')
    theme_short = theme_short.replace('_Care_Ecology', '2').replace('_Service_Fragmentation', '3')
    theme_short = theme_short.replace('_Culturally_Grounded_Solutions', '4')
    lang = e['language']
    print(f"\n[{theme_short}] T{e['table_id']} {e['speaker_label'][:35]} Q={e['question_id']} [{lang}]")
    print(f"  {e['excerpt_text'][:250]}")

# Also get key quotes from coded segments for Q7 (which had 0 theme matches)
with open(d1_out / 'CASE_D1_coded_segments.csv', 'r', encoding='utf-8') as f:
    segments = list(csv.DictReader(f))

q7_segs = [s for s in segments if s['question_id'] == 'Q7' and s['speaker_type'] == 'participant']
print(f"\n\n=== Q7 PARTICIPANT SEGMENTS ({len(q7_segs)}) ===")
for s in q7_segs[:10]:
    print(f"\nT{s['table_id']} {s['speaker_label'][:35]} codes={s['codes']}")
    print(f"  {s['segment_text'][:250]}")

# Q6 segments
q6_segs = [s for s in segments if s['question_id'] == 'Q6' and s['speaker_type'] == 'participant']
print(f"\n\n=== Q6 PARTICIPANT SEGMENTS ({len(q6_segs)}) ===")
for s in q6_segs[:8]:
    print(f"\nT{s['table_id']} {s['speaker_label'][:35]} codes={s['codes']}")
    print(f"  {s['segment_text'][:250]}")
