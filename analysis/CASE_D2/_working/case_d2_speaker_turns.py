from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(r"c:\Users\baram\OneDrive\Desktop\themnatic")
WORKING_DIR = ROOT / "analysis" / "CASE_D2" / "_working"
TRANSCRIPTS_JSON = WORKING_DIR / "d2_transcripts_extracted.json"
REPORT_PATH = WORKING_DIR / "case_d2_speaker_turns.md"

ARABIC_INLINE_PATTERN = re.compile(r"^(?P<label>(?:د\.|أ\.|أ\.د\.)[^:]{0,80}|[^:]{1,80}\([^)]{1,80}\)|المحاور|مدير الجلسة|المشارك(?:\s+الأول|\s+الثاني|\s+الآخر)?|مشارك(?:\s+آخر)?(?:\s+\([^)]*\))?)\s*:\s*(?P<content>.+)$")
ENGLISH_INLINE_PATTERN = re.compile(r"^(?P<label>(?:Speaker\s+\d+|Moderator|[A-Za-z][A-Za-z .'-]{0,60}\([^)]{1,60}\)))\s*:\s*(?P<content>.+)$")
STANDALONE_LABEL_PATTERN = re.compile(r"^(?:بوزيداني \(منسق الجلسة\)|مدير الجلسة:?|المحاور:?|د\.[^\n]{1,60}|أ\.[^\n]{1,60}|أ\.د\.[^\n]{1,60}|Speaker\s+\d+:.*|Moderator:.*|[A-Z][a-z]+ \([^)]{1,60}\):.*)$")
QUESTION_PATTERN = re.compile(r"(?:^Question\s+\d+:|^\d-\s|السؤال)", re.IGNORECASE)


def normalize_label(raw: str) -> str:
    label = raw.strip().rstrip(":")
    replacements = {
        "د. سلمى": "د. سلوى",
        "دكتورة ريم.": "د. ريم الحاج",
        "د.ريم": "د. ريم الحاج",
        "د.ريم ": "د. ريم الحاج",
        "د.هاجر": "د. هاجر",
        "د.وائل": "د. وائل",
        "د.أمير": "د. أمير",
        "محاور": "المحاور",
    }
    if label in replacements:
        return replacements[label]
    label = re.sub(r"\s+", " ", label)
    return label


with TRANSCRIPTS_JSON.open(encoding="utf-8") as handle:
    transcripts = json.load(handle)

lines: list[str] = ["# CASE_D2 Speaker Turn Diagnostics", ""]

for record in transcripts:
    filename = record["filename"]
    paragraphs: list[str] = record["paragraphs"]
    counts: Counter[str] = Counter()
    examples: dict[str, str] = {}
    speaker_types: defaultdict[str, str] = defaultdict(str)

    for idx, paragraph in enumerate(paragraphs):
        if QUESTION_PATTERN.search(paragraph):
            continue

        match = ARABIC_INLINE_PATTERN.match(paragraph) or ENGLISH_INLINE_PATTERN.match(paragraph)
        if match:
            label = normalize_label(match.group("label"))
            content = match.group("content").strip()
            if not content:
                continue
            counts[label] += 1
            examples.setdefault(label, content[:180])
            if "منسق الجلسة" in label or label in {"المحاور", "مدير الجلسة", "Moderator"}:
                speaker_types[label] = "moderator"
            elif label.startswith("Speaker "):
                speaker_types[label] = "participant"
            else:
                speaker_types.setdefault(label, "participant")
            continue

        if STANDALONE_LABEL_PATTERN.match(paragraph):
            normalized = normalize_label(paragraph.replace(":", ""))
            next_content = ""
            if idx + 1 < len(paragraphs):
                next_content = paragraphs[idx + 1].strip()
            if next_content and not QUESTION_PATTERN.search(next_content):
                counts[normalized] += 1
                examples.setdefault(normalized, next_content[:180])
                if "منسق الجلسة" in normalized or normalized in {"المحاور", "مدير الجلسة", "Moderator"}:
                    speaker_types[normalized] = "moderator"
                elif normalized.startswith("Speaker "):
                    speaker_types[normalized] = "participant"
                else:
                    speaker_types.setdefault(normalized, "participant")

    lines.append(f"## {filename}")
    if not counts:
        lines.append("- No robust speaker-turn labels detected")
        lines.append("")
        continue
    for label, count in counts.most_common():
        role = speaker_types.get(label, "participant")
        example = examples.get(label, "")
        lines.append(f"- {label} | type={role} | turns={count} | example={example}")
    lines.append("")

REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")
print(f"Wrote {REPORT_PATH}")
