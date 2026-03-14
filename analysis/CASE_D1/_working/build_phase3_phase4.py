"""Build Phase 3 remaining deliverables and Phase 4 theme development artifacts."""
import csv, json
from pathlib import Path
from collections import Counter, defaultdict

root = Path(r'c:\Users\baram\OneDrive\Desktop\themnatic')
d1_out = root / 'analysis' / 'CASE_D1'

# Read corrected coded segments
with open(d1_out / 'CASE_D1_coded_segments.csv', 'r', encoding='utf-8') as f:
    segments = list(csv.DictReader(f))

# ═══════════════════════════════════════════════════════
# PARTICIPANT SUMMARY (corrected)
# ═══════════════════════════════════════════════════════
participant_data = defaultdict(lambda: {
    'source_file': '', 'table_id': '', 'speaker_type': '',
    'segments': 0, 'total_chars': 0,
    'questions': set(), 'codes': Counter(),
    'sample_texts': []
})

for seg in segments:
    key = (seg['speaker_label'], seg['source_file'])
    d = participant_data[key]
    d['source_file'] = seg['source_file']
    d['table_id'] = seg['table_id']
    d['speaker_type'] = seg['speaker_type']
    d['segments'] += 1
    d['total_chars'] += len(seg['segment_text'])
    d['questions'].add(seg['question_id'])
    for c in seg['codes'].split(';'):
        d['codes'][c] += 1
    if len(d['sample_texts']) < 2 and len(seg['segment_text']) > 50:
        d['sample_texts'].append(seg['segment_text'][:200])

rows = []
for (speaker, source), d in sorted(participant_data.items(), key=lambda x: (-x[1]['total_chars'], x[0])):
    top_codes = [c for c, _ in d['codes'].most_common(5) if c != 'general_response']
    rows.append({
        'speaker_label': speaker,
        'source_file': d['source_file'],
        'table_id': d['table_id'],
        'speaker_type': d['speaker_type'],
        'segment_count': d['segments'],
        'total_chars': d['total_chars'],
        'questions_covered': ';'.join(sorted(d['questions'])),
        'top_codes': ';'.join(top_codes[:5]) if top_codes else 'general_response',
    })

with open(d1_out / 'CASE_D1_participant_summary.csv', 'w', encoding='utf-8', newline='') as csvf:
    w = csv.DictWriter(csvf, fieldnames=list(rows[0].keys()))
    w.writeheader()
    w.writerows(rows)

print(f'Participant summary: {len(rows)} speakers')
print(f'  Participants: {sum(1 for r in rows if r["speaker_type"]=="participant")}')
print(f'  Moderators: {sum(1 for r in rows if r["speaker_type"]=="moderator")}')
print(f'  Unclear: {sum(1 for r in rows if r["speaker_type"]=="unclear")}')

# Show top 10 participants by chars
print(f'\nTop 10 participants by contribution volume:')
p_rows = [r for r in rows if r['speaker_type'] == 'participant']
for r in sorted(p_rows, key=lambda x: -x['total_chars'])[:10]:
    print(f"  {r['speaker_label'][:35]:35s} T{r['table_id']:3s} segs={r['segment_count']:4d} chars={r['total_chars']:6d} Qs={r['questions_covered']}")

# ═══════════════════════════════════════════════════════
# QUESTION-LINKED EVIDENCE TABLE (corrected)
# ═══════════════════════════════════════════════════════
q_evidence = defaultdict(lambda: {
    'participant_segments': 0, 'moderator_segments': 0, 'unclear_segments': 0,
    'participant_speakers': set(), 'sources': set(), 'codes': Counter(),
})

for seg in segments:
    q = seg['question_id']
    d = q_evidence[q]
    d[f"{seg['speaker_type']}_segments"] += 1
    d['sources'].add(seg['source_file'])
    if seg['speaker_type'] == 'participant':
        d['participant_speakers'].add(seg['speaker_label'])
        for c in seg['codes'].split(';'):
            if c != 'general_response':
                d['codes'][c] += 1

q_rows = []
for q in sorted(q_evidence.keys()):
    d = q_evidence[q]
    top_codes = [c for c, _ in d['codes'].most_common(5)]
    q_rows.append({
        'question_id': q,
        'participant_segments': d['participant_segments'],
        'moderator_segments': d['moderator_segments'],
        'unclear_segments': d['unclear_segments'],
        'unique_participant_speakers': len(d['participant_speakers']),
        'source_files': len(d['sources']),
        'top_codes': ';'.join(top_codes) if top_codes else 'general_response',
    })

with open(d1_out / 'CASE_D1_question_evidence_table.csv', 'w', encoding='utf-8', newline='') as csvf:
    w = csv.DictWriter(csvf, fieldnames=list(q_rows[0].keys()))
    w.writeheader()
    w.writerows(q_rows)

print(f'\nQuestion evidence table (participant segments only):')
for r in q_rows:
    print(f"  {r['question_id']:6s} p_segs={r['participant_segments']:4d} speakers={r['unique_participant_speakers']:3d} sources={r['source_files']:2d} top_codes={r['top_codes'][:70]}")

# ═══════════════════════════════════════════════════════
# CODE DISTRIBUTION FOR THEME DEVELOPMENT
# ═══════════════════════════════════════════════════════
p_segs = [s for s in segments if s['speaker_type'] == 'participant']
code_by_question = defaultdict(lambda: Counter())
code_by_table = defaultdict(lambda: Counter())
code_total = Counter()

for seg in p_segs:
    for c in seg['codes'].split(';'):
        if c != 'general_response':
            code_total[c] += 1
            code_by_question[seg['question_id']][c] += 1
            code_by_table[seg['table_id']][c] += 1

print(f'\n=== CODE DISTRIBUTION (participant segments, excluding general_response) ===')
print(f'Total coded instances: {sum(code_total.values())}')
print(f'\nAll codes by frequency:')
for code, cnt in code_total.most_common():
    # Show which questions this code appears in
    q_dist = {q: code_by_question[q].get(code, 0) for q in sorted(code_by_question.keys()) if code_by_question[q].get(code, 0) > 0}
    t_dist = {t: code_by_table[t].get(code, 0) for t in sorted(code_by_table.keys()) if code_by_table[t].get(code, 0) > 0}
    print(f'  {code:40s} {cnt:4d}  Qs={dict(q_dist)}  Ts={dict(t_dist)}')
