from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(r"c:\Users\baram\OneDrive\Desktop\themnatic")
WORKING_DIR = ROOT / "analysis" / "CASE_D2" / "_working"
TRANSCRIPTS_JSON = WORKING_DIR / "d2_transcripts_extracted.json"
NOTES_JSON = WORKING_DIR / "d2_notes_extracted.json"
REPORT_PATH = WORKING_DIR / "case_d2_gate1_diagnostics.md"

label_patterns = [
    re.compile(r"^Speaker\s+\d+:"),
    re.compile(r"^Moderator:"),
    re.compile(r"^Question\s+\d+:"),
    re.compile(r"^Part\s+\d+:"),
    re.compile(r"^بوزيداني \(منسق الجلسة\)$"),
    re.compile(r"^مدير الجلسة:?$"),
    re.compile(r"^المحاور:?$"),
    re.compile(r"^مشارك(?:\s+آخر)?(?:\s+\([^)]*\))?:"),
    re.compile(r"^المشارك(?:\s+الأول|\s+الثاني|\s+الآخر)?:"),
    re.compile(r"^(?:د\.|أ\.|أ\.د\.)[^\n]{0,100}$"),
    re.compile(r"^[^\n]{1,100}\([^\n]{1,80}\):$"),
]

question_patterns = [
    re.compile(r"^Question\s+\d+:", re.IGNORECASE),
    re.compile(r"^\d-\s"),
    re.compile(r"السؤال"),
    re.compile(r"question", re.IGNORECASE),
]

with TRANSCRIPTS_JSON.open(encoding="utf-8") as handle:
    transcripts = json.load(handle)

with NOTES_JSON.open(encoding="utf-8") as handle:
    notes = json.load(handle)

lines: list[str] = ["# CASE_D2 Gate 1 Diagnostics", ""]

for record in transcripts:
    filename = record["filename"]
    paragraphs = record["paragraphs"]
    candidate_labels: list[str] = []
    question_cues: list[str] = []
    for paragraph in paragraphs:
        if any(pattern.search(paragraph) for pattern in label_patterns):
            if paragraph not in candidate_labels:
                candidate_labels.append(paragraph)
        if any(pattern.search(paragraph) for pattern in question_patterns):
            if paragraph not in question_cues:
                question_cues.append(paragraph)
    lines.append(f"## Transcript: {filename}")
    lines.append(f"- Paragraphs: {record['paragraph_count']}")
    lines.append(f"- Characters: {record['char_count']}")
    lines.append("- Candidate labels:")
    if candidate_labels:
        for item in candidate_labels[:40]:
            lines.append(f"  - {item}")
    else:
        lines.append("  - none detected")
    lines.append("- Question cues:")
    if question_cues:
        for item in question_cues[:20]:
            lines.append(f"  - {item}")
    else:
        lines.append("  - none detected")
    lines.append("")

lines.append("# Note question cues")
lines.append("")
for record in notes:
    filename = record["filename"]
    paragraphs = record["paragraphs"]
    question_cues = [p for p in paragraphs if any(pattern.search(p) for pattern in question_patterns)]
    lines.append(f"## Note: {filename}")
    if question_cues:
        for item in question_cues[:20]:
            lines.append(f"- {item}")
    else:
        lines.append("- none detected")
    lines.append("")

REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")
print(f"Wrote {REPORT_PATH}")
