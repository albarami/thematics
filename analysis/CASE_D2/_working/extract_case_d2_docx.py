from __future__ import annotations

import json
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(r"c:\Users\baram\OneDrive\Desktop\themnatic")
RAW_DIR = ROOT / "Day2_Youth"
TRANSCRIPTS_DIR = RAW_DIR / "Audio Recordings _Transcripts"
NOTES_DIR = RAW_DIR / "NoteTakers_Notes"
OUT_DIR = ROOT / "analysis" / "CASE_D2" / "_working"
TRANSCRIPTS_JSON = OUT_DIR / "d2_transcripts_extracted.json"
NOTES_JSON = OUT_DIR / "d2_notes_extracted.json"
NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}


def extract_docx_text(path: Path) -> dict[str, object]:
    with zipfile.ZipFile(path) as archive:
        xml_bytes = archive.read("word/document.xml")
    root = ET.fromstring(xml_bytes)
    paragraphs: list[str] = []
    for para in root.findall(".//w:p", NS):
        texts: list[str] = []
        for node in para.findall(".//w:t", NS):
            if node.text:
                texts.append(node.text)
        paragraph_text = "".join(texts).strip()
        if paragraph_text:
            paragraphs.append(paragraph_text)
    full_text = "\n".join(paragraphs)
    return {
        "filename": path.name,
        "paragraph_count": len(paragraphs),
        "char_count": len(full_text),
        "paragraphs": paragraphs,
        "full_text": full_text,
    }


def dump_folder(folder: Path, output: Path) -> None:
    records = []
    for path in sorted(folder.glob("*.docx")):
        records.append(extract_docx_text(path))
    output.write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    dump_folder(TRANSCRIPTS_DIR, TRANSCRIPTS_JSON)
    dump_folder(NOTES_DIR, NOTES_JSON)
    print(f"Wrote {TRANSCRIPTS_JSON}")
    print(f"Wrote {NOTES_JSON}")
