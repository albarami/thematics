from __future__ import annotations

import csv
import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(r"c:\Users\baram\OneDrive\Desktop\themnatic")
CASE_DIR = ROOT / "analysis" / "CASE_D3"
WORKING_DIR = CASE_DIR / "_working"
TRANSCRIPTS_JSON = WORKING_DIR / "d3_transcripts_extracted.json"
PARTICIPANT_REGISTER = CASE_DIR / "CASE_D3_participant_register.csv"
OUTPUT_CSV = WORKING_DIR / "CASE_D3_segment_candidates.csv"
OUTPUT_MD = WORKING_DIR / "CASE_D3_segment_candidate_notes.md"

QUESTION_ORDER = ["Q1", "Q2", "Q3", "Q4", "Q5", "Q6", "Q7"]

SOURCE_QUESTION_BREAKPOINTS: dict[str, list[tuple[int, str]]] = {
    "HWAD1AR.docx": [(3, "Q1"), (242, "Q4"), (258, "Q5"), (343, "Q6"), (365, "Q7")],
    "HWAD3AR.docx": [(2, "Q1"), (79, "Q3"), (134, "Q4"), (219, "Q5"), (273, "Q6"), (309, "Q7")],
    "HWAD4AR.docx": [(1, "Q1"), (121, "Q2"), (202, "Q3"), (266, "Q4"), (385, "Q5"), (514, "Q6"), (598, "Q7")],
    "HWAD6AR.docx": [(22, "Q1"), (30, "Q2"), (45, "Q3"), (68, "Q4"), (114, "Q5"), (159, "Q6"), (177, "Q7")],
    "HWAD10AR.docx": [(29, "Q1"), (61, "Q2"), (140, "Q3"), (226, "Q4"), (349, "Q5"), (425, "Q7")],
}

QUESTION_RULES = [
    ("Q1", ["ما معنى الحياة الطيبة", "ما هي الحياة الطيبة بالنسبة لك", "what is wellbeing for you", "what is well-being for you", "as adults, from your perception"]),
    ("Q2", ["كيف تعرّف العافية", "كيف تعرف العافية", "when we describe someone as well", "what do we mean", "هذا الشخص بعافية"]),
    ("Q3", ["كيف يمكن لهذه الركائز أن تسهم", "كيف يمكن لهذا الركائز أن تسهم", "how can these pillars contribute", "how can the pillars enhance your well-being"]),
    ("Q4", ["هل تنعكس ركائز الحياة الطيبة", "هل هذه القيم تنعكس", "هل تعتقدون هذه الركائز موجودة", "هل تعتقد ان هذه الركائز تؤخذ بعين الاعتبار", "هل هي متوفرة حاليا", "are the ht pillars reflected", "healthcare services currently provided", "based on your experience"]),
    ("Q5", ["ما التحديات الرئيسية", "التحديات الأساسية", "ما هي الصعوبات", "المشكلات", "يتعلق بالتحديات", "what are the main challenges", "what are the challenges preventing us from implementing", "main challenges in integrating", "تواجه دمج ركائز الحياة الطيبة"]),
    ("Q6", ["ما الفرص المتاحة حاليا", "ما هي الفرص الموجودة", "ما هي الفرص", "what opportunities are currently available", "دعونا نقول انه حاليا هنالك فرص", "نعطيكم أمثلة", "enhance the integration"]),
    ("Q7", ["ما هي اقتراحاتكم العملية", "نحن محتاجين اقتراحاتكم العملية", "الانتقال للحلول", "ننتقل الى الحلول", "ننتقل للمقترحات", "الحلول المبتكرة", "what practical suggestions", "practical suggestions"]),
]

HWAD3_SHORT_LABEL = re.compile(r"^(د/\s*(?:مها|حنان|داليا)|أ/\s*(?:وضحى|امنة|أمنة|اميرة|أميرة)|المحاور)\s*:?(.*)$")
HWAD10_INLINE_LABEL = re.compile(r"^(Speaker\s+[1-8]|Moderator|Translator):\s*(.+)$")

SOURCE_LANGUAGE = {
    "HWAD10AR.docx": "en",
}

LABEL_ROLE_MAP = {
    ("HWAD1AR.docx", "Moderator"): "Moderator, Table 1",
    ("HWAD1AR.docx", "د. أحمد الفرجابي"): "Islamic affairs expert and family-education consultant, Table 1",
    ("HWAD1AR.docx", "د. وائل"): "Social rehabilitation specialist, Aman Centre, Table 1",
    ("HWAD3AR.docx", "المحاور"): "Moderator, Table 3",
    ("HWAD3AR.docx", "د. مها"): "Psychiatrist, HMC Mental Health, Table 3",
    ("HWAD3AR.docx", "د. حنان"): "College of health sciences leader, Table 3",
    ("HWAD3AR.docx", "د. داليا"): "Psychologist, Aman Centre, Table 3",
    ("HWAD3AR.docx", "أ. وضحى"): "Student, Table 3",
    ("HWAD3AR.docx", "أ. آمنة"): "Midwife, Al Wakra Hospital, Table 3",
    ("HWAD3AR.docx", "أ. أميرة"): "Midwife, Al Wakra Hospital, Table 3",
    ("HWAD4AR.docx", "مدير الجلسة"): "Moderator, Table 4",
    ("HWAD4AR.docx", "د. خالد"): "University academic in psychology, Table 4",
    ("HWAD4AR.docx", "د. ساسجار"): "Senior consultant, Table 4",
    ("HWAD4AR.docx", "د. أروى حسين"): "Psychologist, Table 4",
    ("HWAD4AR.docx", "د. سحر السيد"): "Midwife, Table 4",
    ("HWAD4AR.docx", "أ. عائشة المعصومي"): "Dietitian, Table 4",
    ("HWAD4AR.docx", "هند الجابر"): "Senior research assistant, medical research centre, Table 4",
    ("HWAD4AR.docx", "منى سالم"): "Nurse, HMC psychiatric hospital, Table 4",
    ("HWAD4AR.docx", "مشاعل الأنصاري"): "Head of central laboratories, Hamad Hospital, Table 4",
    ("HWAD6AR.docx", "د. وليد"): "Role not stated, Table 6",
    ("HWAD10AR.docx", "Moderator"): "Moderator, Table 10",
    ("HWAD10AR.docx", "Speaker 1"): "Participant, role not stated, Table 10",
    ("HWAD10AR.docx", "Speaker 2"): "Admin, HMC Mental Health, Table 10",
    ("HWAD10AR.docx", "Speaker 3"): "Manager, social work, Sidra, Table 10",
    ("HWAD10AR.docx", "Speaker 4"): "Manager, occupational therapy, Sidra, Table 10",
    ("HWAD10AR.docx", "Speaker 5"): "Participant, role not stated, Table 10",
    ("HWAD10AR.docx", "Speaker 6"): "Medical student, Table 10",
    ("HWAD10AR.docx", "Speaker 7"): "Occupational therapist, private sector, Table 10",
    ("HWAD10AR.docx", "Speaker 8"): "GP, private healthcare center, Table 10",
}

HWAD4_PREFIXES = {
    "مدير الجلسة": "مدير الجلسة",
    "د.خالد": "د. خالد",
    "د.ساسجار": "د. ساسجار",
    "د.أروى حسين": "د. أروى حسين",
    "د.اروى حسين": "د. أروى حسين",
    "أ.عائشة المعصومي": "أ. عائشة المعصومي",
    "أ.سحر سيد": "د. سحر السيد",
    "د.سحر السيد": "د. سحر السيد",
    "هند الجابر": "هند الجابر",
    "منى سالم": "منى سالم",
    "مشاعل الأنصاري": "مشاعل الأنصاري",
}


def detect_question(text: str, current_question: str | None) -> str | None:
    lowered = text.lower()
    current_index = QUESTION_ORDER.index(current_question) if current_question in QUESTION_ORDER else -1
    detected = current_question
    detected_position: int | None = None
    for question_id, markers in QUESTION_RULES:
        question_index = QUESTION_ORDER.index(question_id)
        if question_index < current_index:
            continue
        for marker in markers:
            position = lowered.find(marker.lower())
            if position == -1:
                continue
            if detected_position is None or position < detected_position:
                detected = question_id
                detected_position = position
                break
    return detected


def apply_source_question_breakpoints(source_file: str, paragraph_number: int, current_question: str | None) -> str | None:
    breakpoints = SOURCE_QUESTION_BREAKPOINTS.get(source_file, [])
    detected = current_question
    for start_paragraph, question_id in breakpoints:
        if paragraph_number >= start_paragraph:
            detected = question_id
        else:
            break
    return detected


def normalise_hw3_label(raw: str) -> str:
    cleaned = re.sub(r"\s+", " ", raw).strip()
    mapping = {
        "د/ مها": "د. مها",
        "د/مها": "د. مها",
        "د/ حنان": "د. حنان",
        "د/حنان": "د. حنان",
        "د/ داليا": "د. داليا",
        "د/داليا": "د. داليا",
        "أ/ وضحى": "أ. وضحى",
        "أ/وضحى": "أ. وضحى",
        "أ/ امنة": "أ. آمنة",
        "أ/امنة": "أ. آمنة",
        "أ/ أمنة": "أ. آمنة",
        "أ/أمنة": "أ. آمنة",
        "أ/ اميرة": "أ. أميرة",
        "أ/اميرة": "أ. أميرة",
        "أ/ أميرة": "أ. أميرة",
        "أ/أميرة": "أ. أميرة",
        "المحاور": "المحاور",
    }
    return mapping.get(cleaned, cleaned)


def is_header_fragment(text: str) -> bool:
    stripped = text.strip()
    lowered = stripped.lower()
    if not stripped:
        return True
    header_starts = ["date:", "table #", "part 1", "part 2", "transcript", "التاريخ", "طاولة رقم", "الجزء الأول", "الجزء الثاني", "م1", "م2", "م3", "م4", "م5", "p1", "p2", "p3", "p4", "p5"]
    if any(lowered.startswith(item) for item in header_starts):
        return True
    if stripped in {"HWAD10AR", "Moderator", "P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8"}:
        return True
    return False


def is_substantive_content(text: str) -> bool:
    stripped = text.strip()
    if not stripped:
        return False
    if is_header_fragment(stripped):
        return False
    if stripped.endswith(":") and len(stripped.split()) <= 4:
        return False
    if len(stripped) < 12:
        return False
    if stripped.startswith(("1-", "2-", "3-", "4-")):
        return False
    return True


def is_probable_moderator_prompt(text: str) -> bool:
    lowered = text.lower().strip()
    prompt_markers = [
        "السؤال",
        "ننتقل",
        "دعنا",
        "دعونا",
        "دعني أعلق",
        "هل السؤال مفهوم",
        "نعيد السؤال",
        "شكرا لكم",
        "شكرا لك",
        "نبدأ",
        "واضح",
        "من يريد أن يبدأ",
        "هل هناك أي إضافة",
        "قبل الانتقال",
        "الجزء الثاني",
        "التحديات",
        "الفرص",
        "الاقتراحات",
        "الحلول",
        "let us move",
        "our second question",
        "move to the",
        "what is wellbeing for you",
        "when we describe someone as well",
        "how can these pillars contribute",
        "are the ht pillars reflected",
        "what are the main challenges",
        "what opportunities are currently available",
        "what practical suggestions",
        "based on your experience",
        "any other comments",
        "please introduce yourself",
        "we will move to another question",
        "i want to translate",
        "from your point of view",
        "amazing",
    ]
    return any(marker in lowered for marker in prompt_markers)


def parse_hw4_label(paragraph: str) -> tuple[str, str, bool] | None:
    text = paragraph.strip()
    for prefix, normalised in HWAD4_PREFIXES.items():
        if not text.startswith(prefix):
            continue
        remainder = text[len(prefix):].strip()
        if normalised == "مدير الجلسة" and remainder.startswith(":") and len(remainder) > 4 and not remainder[1:].strip().startswith("("):
            return normalised, remainder.lstrip(":").strip(), False
        if remainder and not remainder.startswith((":", "(", " :(", ":(")) and len(remainder.split()) > 3:
            return normalised, remainder, False
        return normalised, "", True
    return None


def build_register_lookup() -> tuple[dict[tuple[str, str], dict[str, str]], dict[tuple[str, str], dict[str, str]]]:
    with PARTICIPANT_REGISTER.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    by_source_role: dict[tuple[str, str], dict[str, str]] = {}
    by_code: dict[tuple[str, str], dict[str, str]] = {}
    for row in rows:
        by_source_role[(row["source_file"], row["role_label"])] = row
        by_code[(row["source_file"], row["anonymized_code"])] = row
    return by_source_role, by_code


def build_row(
    segment_id: str,
    source_file: str,
    table_id: str,
    register_row: dict[str, str],
    question_id: str,
    segment_text: str,
    attribution_status: str,
) -> dict[str, str]:
    speaker_type = register_row["speaker_type"]
    return {
        "segment_id": segment_id,
        "source_file": source_file,
        "table_id": table_id,
        "speaker_code": register_row["anonymized_code"],
        "speaker_type": speaker_type,
        "role_label": register_row["role_label"],
        "attribution_status": attribution_status,
        "question_id": question_id,
        "segment_text": segment_text.strip(),
        "codes": "moderator_context" if speaker_type == "moderator" else "general_response",
        "language": SOURCE_LANGUAGE.get(source_file, "ar"),
    }


def main() -> None:
    """Build the initial Day 3 candidate segment layer from the extracted transcripts."""
    register_lookup, _ = build_register_lookup()
    with TRANSCRIPTS_JSON.open(encoding="utf-8") as handle:
        transcripts = json.load(handle)

    rows: list[dict[str, str]] = []
    notes: list[str] = ["# CASE_D3 Segment Candidate Notes", ""]
    segment_counter = 1

    for record in transcripts:
        source_file = record["filename"]
        table_match = re.search(r"HWAD(\d+)", source_file)
        table_id = table_match.group(1) if table_match else ""
        current_question: str | None = None
        active_register_row: dict[str, str] | None = None
        active_attribution_status = "identified"
        guide_started = source_file != "HWAD10AR.docx"
        extracted_count = 0
        unlabeled_unclear = 0
        unlabeled_moderator = 0
        unresolved: set[str] = set()
        paragraphs = record["paragraphs"]
        index = 0

        while index < len(paragraphs):
            paragraph = paragraphs[index].strip()
            if not paragraph:
                index += 1
                continue

            if source_file == "HWAD10AR.docx" and not guide_started:
                lowered = paragraph.lower()
                if "what is well-being for you" in lowered or "what is wellbeing for you" in lowered:
                    guide_started = True
                    current_question = "Q1"
                else:
                    index += 1
                    continue

            paragraph_number = index + 1
            current_question = apply_source_question_breakpoints(source_file, paragraph_number, current_question)
            current_question = detect_question(paragraph, current_question)
            next_paragraph = paragraphs[index + 1].strip() if index + 1 < len(paragraphs) else ""
            label = ""
            content = ""
            consume_next = False
            explicit = False

            if source_file == "HWAD10AR.docx":
                match = HWAD10_INLINE_LABEL.match(paragraph)
                if match:
                    candidate_label = match.group(1)
                    if candidate_label != "Translator":
                        label = candidate_label
                        content = match.group(2).strip()
                        explicit = True
            elif source_file == "HWAD1AR.docx":
                if paragraph in {"Moderator", "Moderator:"}:
                    label = "Moderator"
                    content = next_paragraph
                    consume_next = True
                    explicit = True
                elif paragraph.startswith("د. أحمد الفرجابي"):
                    label = "د. أحمد الفرجابي"
                    content = next_paragraph
                    consume_next = True
                    explicit = True
                elif paragraph.startswith("د. وائل"):
                    label = "د. وائل"
                    content = next_paragraph
                    consume_next = True
                    explicit = True
            elif source_file == "HWAD3AR.docx":
                match = HWAD3_SHORT_LABEL.match(paragraph)
                if match:
                    label = normalise_hw3_label(match.group(1))
                    remainder = match.group(2).strip(" :")
                    if remainder:
                        content = remainder
                    else:
                        content = next_paragraph
                        consume_next = True
                    explicit = True
            elif source_file == "HWAD4AR.docx":
                parsed = parse_hw4_label(paragraph)
                if parsed:
                    label, content, consume_next = parsed
                    if consume_next:
                        content = next_paragraph
                    explicit = True
            elif source_file == "HWAD6AR.docx":
                if paragraph == "د. وليد" or paragraph.startswith("د. وليد"):
                    label = "د. وليد"
                    remainder = paragraph[len("د. وليد"):].strip(" :")
                    if remainder:
                        content = remainder
                    else:
                        content = next_paragraph
                        consume_next = True
                    explicit = True

            if explicit:
                content_paragraph_number = index + 2 if consume_next else paragraph_number
                current_question = apply_source_question_breakpoints(source_file, content_paragraph_number, current_question)
                current_question = detect_question(content, current_question)
                if current_question and is_substantive_content(content):
                    role_label = LABEL_ROLE_MAP.get((source_file, label), "")
                    register_row = register_lookup.get((source_file, role_label)) if role_label else None
                    if register_row:
                        active_register_row = register_row
                        active_attribution_status = "identified" if register_row["speaker_type"] != "unclear" else "indeterminate"
                        rows.append(
                            build_row(
                                f"D3_S{segment_counter:04d}",
                                source_file,
                                table_id,
                                register_row,
                                current_question,
                                content,
                                active_attribution_status,
                            )
                        )
                        segment_counter += 1
                        extracted_count += 1
                    else:
                        unresolved.add(label)
                        active_register_row = None
                elif source_file == "HWAD10AR.docx":
                    active_register_row = None
                if consume_next:
                    index += 2
                else:
                    index += 1
                continue

            if source_file == "HWAD10AR.docx" and current_question and is_substantive_content(paragraph):
                if is_probable_moderator_prompt(paragraph):
                    moderator_role = f"Moderator, Table {table_id}"
                    register_row = register_lookup.get((source_file, moderator_role))
                    if register_row:
                        active_register_row = register_row
                        active_attribution_status = "indeterminate"
                        rows.append(
                            build_row(
                                f"D3_S{segment_counter:04d}",
                                source_file,
                                table_id,
                                register_row,
                                current_question,
                                paragraph,
                                active_attribution_status,
                            )
                        )
                        segment_counter += 1
                        extracted_count += 1
                        unlabeled_moderator += 1
                        index += 1
                        continue
                if active_register_row:
                    rows.append(
                        build_row(
                            f"D3_S{segment_counter:04d}",
                            source_file,
                            table_id,
                            active_register_row,
                            current_question,
                            paragraph,
                            active_attribution_status,
                        )
                    )
                    segment_counter += 1
                    extracted_count += 1
                    index += 1
                    continue
 
            if current_question and source_file in {"HWAD3AR.docx", "HWAD6AR.docx"} and is_substantive_content(paragraph):
                if is_probable_moderator_prompt(paragraph):
                    moderator_role = f"Moderator, Table {table_id}"
                    register_row = register_lookup.get((source_file, moderator_role))
                    if register_row:
                        rows.append(
                            build_row(
                                f"D3_S{segment_counter:04d}",
                                source_file,
                                table_id,
                                register_row,
                                current_question,
                                paragraph,
                                "indeterminate",
                            )
                        )
                        segment_counter += 1
                        extracted_count += 1
                        unlabeled_moderator += 1
                else:
                    unclear_role = f"Unclear speaker identity cluster, Table {table_id}"
                    register_row = register_lookup.get((source_file, unclear_role))
                    if register_row:
                        rows.append(
                            build_row(
                                f"D3_S{segment_counter:04d}",
                                source_file,
                                table_id,
                                register_row,
                                current_question,
                                paragraph,
                                "indeterminate",
                            )
                        )
                        segment_counter += 1
                        extracted_count += 1
                        unlabeled_unclear += 1
            index += 1

        notes.append(f"## {source_file}")
        notes.append(f"- Extracted candidate segments: {extracted_count}")
        notes.append(f"- Unlabeled unclear segments retained: {unlabeled_unclear}")
        notes.append(f"- Unlabeled moderator prompts retained: {unlabeled_moderator}")
        notes.append(f"- Unresolved labels skipped: {len(unresolved)}")
        if unresolved:
            for item in sorted(unresolved):
                notes.append(f"  - {item}")
        notes.append("")

    with OUTPUT_CSV.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "segment_id",
                "source_file",
                "table_id",
                "speaker_code",
                "speaker_type",
                "role_label",
                "attribution_status",
                "question_id",
                "segment_text",
                "codes",
                "language",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)

    OUTPUT_MD.write_text("\n".join(notes), encoding="utf-8")
    print(f"Wrote {OUTPUT_CSV}")
    print(f"Rows: {len(rows)}")
    print(f"Wrote {OUTPUT_MD}")


if __name__ == "__main__":
    main()
