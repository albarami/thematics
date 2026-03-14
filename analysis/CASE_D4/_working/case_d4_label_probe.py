from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(r"c:\Users\baram\OneDrive\Desktop\themnatic")
TRANSCRIPTS_JSON = ROOT / "analysis" / "CASE_D4" / "_working" / "d4_transcripts_extracted.json"

LABEL_PATTERNS = [
    re.compile(r"^(?P<label>[^:]{1,120}):\s*(?P<content>.+)$"),
    re.compile(r"^(?P<label>(?:د\.|أ\.|دكتور|أستاذ|أستاذة)[^\n]{0,120})$"),
]

SKIP_LABELS = {
    "HWEL1AR",
    "HWEL3AR",
    "HWEL7AR",
    "HWEL9AR",
    "HWEL10AR",
    "الجزء الأول",
    "الجزء الثاني",
}


def main() -> None:
    """Print candidate speaker labels and counts from extracted Day 4 transcripts."""
    with TRANSCRIPTS_JSON.open(encoding="utf-8") as handle:
        records = json.load(handle)

    for record in records:
        counter: Counter[str] = Counter()
        for paragraph in record["paragraphs"]:
            matched = False
            for pattern in LABEL_PATTERNS:
                match = pattern.match(paragraph.strip())
                if not match:
                    continue
                label = match.group("label").strip()
                if label in SKIP_LABELS:
                    matched = True
                    break
                if len(label) <= 1:
                    matched = True
                    break
                counter[label] += 1
                matched = True
                break
            if matched:
                continue
        print(f"## {record['filename']}")
        for label, count in counter.most_common(30):
            print(f"{count:>3} | {label}")
        print()


if __name__ == "__main__":
    main()
