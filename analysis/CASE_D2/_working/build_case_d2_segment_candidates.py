from __future__ import annotations

import csv
import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(r"c:\Users\baram\OneDrive\Desktop\themnatic")
CASE_DIR = ROOT / "analysis" / "CASE_D2"
WORKING_DIR = CASE_DIR / "_working"
TRANSCRIPTS_JSON = WORKING_DIR / "d2_transcripts_extracted.json"
PARTICIPANT_REGISTER = CASE_DIR / "CASE_D2_participant_register.csv"
OUTPUT_CSV = WORKING_DIR / "CASE_D2_segment_candidates.csv"
OUTPUT_MD = WORKING_DIR / "CASE_D2_segment_candidate_notes.md"

ARABIC_INLINE_PATTERN = re.compile(
    r"^(?P<label>(?:د\.|أ\.|أ\.د\.)[^:]{0,80}|[^:]{1,80}\([^)]{1,80}\)|المحاور|مدير الجلسة|المشارك(?:\s+الأول|\s+الثاني|\s+الآخر)?|مشارك(?:\s+آخر)?(?:\s+\([^)]*\))?)\s*:\s*(?P<content>.+)$"
)
ENGLISH_INLINE_PATTERN = re.compile(
    r"^(?P<label>(?:(?:Speaker\s+\d+)|Moderator|(?:[A-Za-z][A-Za-z .'-]{0,60}\([^)]{1,60}\))))\s*:\s*(?P<content>.+)$"
)
STANDALONE_LABEL_PATTERN = re.compile(
    r"^(?:بوزيداني \(منسق الجلسة\)|د\. إبراهيم بوزيداني / منسق الجلسة|مدير الجلسة:?|المحاور:?|د\.[^\n]{1,80}|أ\.[^\n]{1,80}|أ\.د\.[^\n]{1,80}|Speaker\s+\d+|Moderator|[A-Za-z][A-Za-z .'-]{0,60}\([^)]{1,60}\))$"
)

QUESTION_RULES = [
    ("Q1", ["السؤال الأول", "ما معنى الحياة الطيبة", "what is wellbeing for you", "what does well-being mean to you"]),
    ("Q2", ["السؤال الثاني", "كيف تعرّف العافية", "كيف تعرف العافية", "مفهوم العافية", "فرق بين الرفاه والعافية", "when we describe someone as", "when we describe someone as \"well\"", "what do we mean", "هذا الشخص بعافية"]),
    ("Q3", ["السؤال الثالث", "سؤال الثالث", "ركائزها الخمسة", "الركائز الخمسة", "كيف يمكن لهذه الركائز الخمسة", "كيف يمكن لهذه الركائز أن تسهم", "these pillars contribute", "how can these pillars contribute", "تحسين عافيتك"]),
    ("Q4", ["السؤال الرابع", "سؤال الرابع", "هل تنعكس ركائز الحياة الطيبة", "هل تطبق في القطاع الصحي", "موجودة في واقعنا الصحي", "are the ht pillars reflected", "are the five pillars reflected", "خدمات الرعاية الصحية المقدمة حاليا"]),
    ("Q5", ["السؤال الخامس", "سؤال الخامس", "ما التحديات الرئيسية", "ما هي التحديات", "التحديات التي ترونها", "ما الذي يسهل أو يعيق", "what are the challenges", "main challenges", "associated with integrating", "تواجه دمج ركائز الحياة الطيبة"]),
    ("Q6", ["السؤال السادس", "سؤال السادس", "ما الفرص المتاحة حاليا", "ما هي الفرص المتاحة", "الفرص المتاحة لتعزيز", "what opportunities are currently available", "what are the opportunities", "دعونا نتكلم عن الفرص", "enhance the integration"]),
    ("Q7", ["السؤال السابع", "سؤال السابع", "ما هي اقتراحاتكم العملية", "اقتراحاتكم العملية", "ما هي التوصيات", "what practical suggestions", "practical suggestions do you have", "other suggestions", "أقترح", "اقتراح"]),
]


def normalize_label(raw: str) -> str:
    label = raw.strip().rstrip(":")
    replacements = {
        "د. سلمى": "د. سلوى",
        "د.هاجر": "د. هاجر",
        "د.هاجر)clinical psychologist": "د. هاجر",
        "د.هاجرclinical psychologist": "د. هاجر",
        "د.هاجر(clinical psychologist)": "د. هاجر",
        "د.ريم": "د. ريم الحاج",
        "د. ريم.": "د. ريم الحاج",
        "أ.د. أحمد العمادي / الرئيس التنفيذي / مركز الحياة الطيبة": "د. أحمد العمادي",
        "د. أحمد الفرجابي / المستشار التربوي والأسري بالشبكة الإسلامية ووزارة الأوقاف.": "د. أحمد الفرجابي",
        "د.ريم :( (Learning Support Specialist)": "د. ريم الحاج",
        "د. ريم الحاج:( (Learning Support Specialist": "د. ريم الحاج",
        "د.ريم:( (Learning Support Specialist": "د. ريم الحاج",
        "د.أمير(GP pediatrics": "د. أمير",
        "د.أمير( GP pediatrics": "د. أمير",
        "د.وائل(أخصائي تأهيل اجتماعي)": "د. وائل",
        "د.وائل)أخصائي تأهيل اجتماعي)": "د. وائل",
        "د.وائل(أخصائي تأهيل اجتماعي": "د. وائل",
        "دكتور وائل(أخصائي تأهيل اجتماعي)": "د. وائل",
        "دكتور وائل (أخصائي تأهيل اجتماعي)": "د. وائل",
        "دكتور وائل(أخصائي تأهيل اجتماعي": "د. وائل",
        "دكتور وائل(أخصائي تأهيل اجتماعي-مركز أمان)": "د. وائل",
        "دكتور وائل(أخصائي تأهيل اجتماعي-مركز أمان": "د. وائل",
        "د.وائل:أخصائي تأهيل اجتماعي": "د. وائل",
        "د.مصطفى(أستاذ جامعي)": "د. مصطفى",
        "د. مصطفى(أستاذ جامعي)": "د. مصطفى",
        "دانا(متلقي خدمة)": "دانا",
        "العافية من منظوري الشخصي والرضى بأن الحياة ، ups and downsدانا (متلقي خدمة)": "دانا",
        "مريم(متلقي خدمة)": "مريم",
        "د. داليا مركز أمان": "د. داليا",
        "د. داليا اخصائية نفسية": "د. داليا",
        "د. داليا اخصائية نفسية مركز أمان": "د. داليا",
        "المشارك الآخر (محمد أبو هاشم - مستفيد)": "محمد أبو هاشم",
        "مشارك آخر (محمد أبو هاشم – مستفيد)": "محمد أبو هاشم",
        "مشارك آخر (محمد أبو هاشم)": "محمد أبو هاشم",
        "المشارك الأول (د سارة طبيب أسنان بالقطاع الخاص)": "د. سارة",
        "مشارك آخر (سارة غازي – طبيب أسنان بالقطاع الخاص)": "سارة غازي",
        "المشارك الثاني (د. أسماء طبيب نفسي)": "د. أسماء",
        "المشارك الآخر (د. أسماء طبيبة نفسية بمركز الشفلح)": "د. أسماء",
        "مشارك آخر (د. أسماء طبيب نفسي)": "د. أسماء",
        "مشارك آخر (د. أسماء)": "د. أسماء",
        "المشارك الأول (د. أسماء)": "د. أسماء",
        "المشارك الآخر (نيلي خليل – ممرضة في أسبيتار)": "نيلي خليل",
        "مشارك (نيلي خليل – ممرضة بمستشفى أسبيتار)": "نيلي خليل",
        "المشارك (نيلي خليل – ممرّضة بمستشفى أسبيتار)": "نيلي خليل",
        "مشارك آخر (عبدالرحمن القديمي – مستفيد)": "عبدالرحمن القديمي",
        "المشارك الآخر (عبدالرحمن - مراجع)": "عبدالرحمن القديمي",
        "مشارك آخر (عبدالرحمن القديمي)": "عبدالرحمن القديمي",
        "مشارك آخر (رشا علام – دكتورة أسنان)": "رشا علام",
        "المشارك الآخر (رشا علّام – دكتورة أسنان بالقطاع الخاص)": "رشا علام",
        "مشارك آخر (نور غازي – طبيب أسنان بالقطاع الخاص)": "د. نور غازي",
        "مشارك (د نور غازي – طبيب أسنان)": "د. نور غازي",
        "المشارك (د نور غازي -طبيب أسنان بالقطاع الخاص)": "د. نور غازي",
        "مشارك آخر (د. نور غازي – طبيب أسنان بالقطاع الخاص)": "د. نور غازي",
        "مشارك آخر (د نور غازي طبيب أسنان)": "د. نور غازي",
        "المشارك الآخر ( د نور غازي – طبيب أسنان)": "د. نور غازي",
        "مشارك آخر (د. أسماء طبيب نفسي بمركز الشفلح)": "د. أسماء",
        "مشارك آخر (دكتورة أسماء)": "د. أسماء",
        "مشارك آخر (دكتورة سارة -طبيب أسنان)": "د. سارة",
        "مشارك آخر (عبدالرحمن القديمي– مستفيد)": "عبدالرحمن القديمي",
        "د.وائل": "د. وائل",
        "المشارك": "مشارك غير مسمى",
        "مشارك آخر": "مشارك غير مسمى",
        "المشارك الأول": "مشارك أول غير مسمى",
        "مشارك": "مشارك غير مسمى",
        "مدير الجلسة": "مدير الجلسة",
        "المحاور (التلخيص)": "المحاور",
    }
    if "وائل" in label and "أخصائي تأهيل اجتماعي" in label:
        return "د. وائل"
    return replacements.get(label, re.sub(r"\s+", " ", label))


def detect_question(paragraph: str, current_question: str | None) -> str | None:
    lowered = paragraph.lower()
    matched_question = current_question
    for qid, markers in QUESTION_RULES:
        for marker in markers:
            if marker.lower() in lowered:
                matched_question = qid
                break
    return matched_question


def is_role_descriptor_fragment(text: str) -> bool:
    lowered = text.lower().strip()
    fragment_markers = [
        "learning support specialist",
        "laboratory psychologist",
        "gp pediatrics",
        "clinical psychologist",
        "clinical psychologist, phcc",
        "occupational therapist",
        "staff nurse",
        "sports podiatry",
        "specialist family medicine",
        "student qu",
        "student, qatar university",
        "academic, college of health science",
        "researcher",
        "أخصائي تأهيل اجتماعي",
        "أستاذ جامعي",
        "متلقي خدمة",
        "health center",
        "women hospital",
        "college of health science",
    ]
    return any(marker in lowered for marker in fragment_markers)


def is_header_descriptor_line(text: str) -> bool:
    stripped = text.strip()
    lowered = stripped.lower()
    if stripped.count("/") >= 2 and len(stripped) <= 180:
        return True
    header_markers = [
        "/",
        "الرئيس التنفيذي",
        "استشاري",
        "جامعة",
        "طالبة",
        "مدونة",
        "المستشار",
        "health center",
        "women hospital",
        "college of health science",
        "student qu",
        "specialist family medicine",
        "laboratory psychologist",
    ]
    if any(marker in lowered for marker in header_markers):
        if len(stripped) <= 120 and "،" not in stripped and "." not in stripped:
            return True
    return False


def is_substantive_content(text: str) -> bool:
    stripped = text.strip()
    if not stripped:
        return False
    if len(stripped) < 8:
        return False
    if is_header_descriptor_line(stripped):
        return False
    if is_role_descriptor_fragment(stripped) and len(stripped.split()) <= 6:
        return False
    return True


def is_label_only_paragraph(text: str) -> bool:
    stripped = text.strip().rstrip(":")
    return bool(STANDALONE_LABEL_PATTERN.match(stripped))


def register_key(row: dict[str, str]) -> tuple[str, str]:
    return (row["source_file"], row["role_label"])


with PARTICIPANT_REGISTER.open(encoding="utf-8-sig") as handle:
    register_rows = list(csv.DictReader(handle))

register_lookup: dict[tuple[str, str], dict[str, str]] = {}
for row in register_rows:
    register_lookup[register_key(row)] = row

label_to_role_labels: dict[tuple[str, str], list[str]] = defaultdict(list)
manual_role_map = {
    ("HWYO0AR.docx", "د. أحمد العمادي"): "Senior healthcare leader, Table 0",
    ("HWYO0AR.docx", "د. سلوى"): "Consultant obstetrician-gynaecologist, Table 0",
    ("HWYO0AR.docx", "د. زينة"): "Consultant obstetrician-gynaecologist and executive leader, Table 0",
    ("HWYO0AR.docx", "د. رائد عمرو"): "Mental-health executive, Table 0",
    ("HWYO0AR.docx", "د. محمد عبد العليم"): "Senior psychiatrist and policy adviser, Table 0",
    ("HWYO0AR.docx", "د. أحمد الفرجابي"): "Family and religious adviser, Table 0",
    ("HWYO0AR.docx", "بوزيداني (منسق الجلسة)"): "Moderator, Table 0",
    ("HWYO0AR.docx", "د. إبراهيم بوزيداني / منسق الجلسة"): "Moderator, Table 0",
    ("HWYO4AR.docx", "د. ريم الحاج"): "Learning support specialist, Table 4",
    ("HWYO4AR.docx", "مريم"): "Service recipient, Table 4",
    ("HWYO4AR.docx", "دانا"): "Service recipient, Table 4",
    ("HWYO4AR.docx", "د. هاجر"): "Clinical psychologist, Table 4",
    ("HWYO4AR.docx", "د. وائل"): "Social rehabilitation specialist, Table 4",
    ("HWYO4AR.docx", "د. أمير"): "General paediatrics clinician, Table 4",
    ("HWYO4AR.docx", "د. مصطفى"): "University academic, Table 4",
    ("HWYO4AR.docx", "مدير الجلسة"): "Moderator, Table 4",
    ("HWYO7AR.docx", "د. داليا"): "Clinical psychologist, Aman Centre, Table 7",
    ("HWYO9AR.docx", "Speaker 1"): "Clinical psychologist, PHCC, Table 9",
    ("HWYO9AR.docx", "Speaker 2"): "Laboratory psychologist, Table 9",
    ("HWYO9AR.docx", "Speaker 3"): "Occupational therapist, mental health services, Table 9",
    ("HWYO9AR.docx", "Speaker 4"): "Midwife, women’s hospital, Table 9",
    ("HWYO9AR.docx", "Speaker 5"): "Student, Qatar University, Table 9",
    ("HWYO9AR.docx", "Speaker 6"): "Academic, college of health science, Table 9",
    ("HWYO9AR.docx", "Speaker 7"): "Specialist family medicine, PHCC, Table 9",
    ("HWYO9AR.docx", "Speaker 8"): "Healthcare participant, Table 9",
    ("HWYO9AR.docx", "Moderator"): "Moderator, Table 9",
    ("HWYO10AR.docx", "Miguel (Sports Podiatry)"): "Sports podiatry professional, Table 10",
    ("HWYO10AR.docx", "Elena (Psychologist)"): "Psychologist, Table 10",
    ("HWYO10AR.docx", "Liam (Sports Podiatry)"): "Sports podiatry professional, Table 10",
    ("HWYO10AR.docx", "Carmona (Staff Nurse)"): "Staff nurse, Table 10",
    ("HWYO10AR.docx", "Safrina (Researcher)"): "Researcher, Table 10",
    ("HWYO10AR.docx", "Herald (HR)"): "Human resources professional, Table 10",
    ("HWYO10AR.docx", "Rehana (Clinical Psychologist)"): "Clinical psychologist, Table 10",
    ("HWYO10AR.docx", "Aziza (Nurse)"): "Nurse, Table 10",
    ("HWYO10AR.docx", "Moderator"): "Moderator, Table 10",
    ("HWYO11AR.docx", "المحاور"): "Moderator, Table 11",
    ("HWYO11AR.docx", "د. سارة"): "Dental clinician, private sector, Table 11",
    ("HWYO11AR.docx", "د. أسماء"): "Psychiatrist, Table 11",
    ("HWYO11AR.docx", "محمد أبو هاشم"): "Service recipient, Table 11",
    ("HWYO11AR.docx", "نيلي خليل"): "Nurse, Aspetar, Table 11",
    ("HWYO11AR.docx", "عبدالرحمن القديمي"): "Service recipient, Table 11",
    ("HWYO11AR.docx", "رشا علام"): "Dental clinician, private sector, Table 11",
    ("HWYO11AR.docx", "د. نور غازي"): "Dental clinician, private sector, Table 11",
    ("HWYO11AR.docx", "سارة غازي"): "Dental clinician, private sector, Table 11",
    ("HWYO11AR.docx", "مشارك غير مسمى"): "Unclear speaker identity, Table 11",
    ("HWYO11AR.docx", "مشارك أول غير مسمى"): "Unclear speaker identity, Table 11",
}

for (source_file, label), role_label in manual_role_map.items():
    label_to_role_labels[(source_file, label)].append(role_label)

speaker_codes: dict[tuple[str, str], str] = {}
speaker_types: dict[tuple[str, str], str] = {}
for row in register_rows:
    key = (row["source_file"], row["role_label"])
    speaker_codes[key] = row["anonymized_code"]
    speaker_types[key] = row["speaker_type"]

with TRANSCRIPTS_JSON.open(encoding="utf-8") as handle:
    transcripts = json.load(handle)

rows: list[dict[str, str]] = []
notes: list[str] = ["# CASE_D2 Segment Candidate Notes", ""]
segment_counter = 1

for record in transcripts:
    source_file = record["filename"]
    table_match = re.search(r"HWYO(\d+)", source_file)
    table_id = table_match.group(1) if table_match else ""
    current_question = None
    extracted_count = 0
    unresolved_labels: set[str] = set()
    paragraphs = record["paragraphs"]

    for index, paragraph in enumerate(paragraphs):
        current_question = detect_question(paragraph, current_question)
        match = ARABIC_INLINE_PATTERN.match(paragraph) or ENGLISH_INLINE_PATTERN.match(paragraph)
        raw_label = ""
        content = ""
        if match:
            raw_label = match.group("label")
            content = match.group("content").strip()
        elif is_label_only_paragraph(paragraph) and index + 1 < len(paragraphs):
            if current_question is None:
                continue
            raw_label = paragraph.strip().rstrip(":")
            content = paragraphs[index + 1].strip()
            if is_label_only_paragraph(content):
                continue
            if is_header_descriptor_line(content):
                continue
            current_question = detect_question(content, current_question)
        else:
            continue
        if not is_substantive_content(content):
            continue
        label = normalize_label(raw_label)
        if source_file == "HWYO9AR.docx" and is_role_descriptor_fragment(content):
            continue
        role_candidates = label_to_role_labels.get((source_file, label), [])
        if not role_candidates:
            unresolved_labels.add(label)
            continue
        role_label = role_candidates[0]
        reg_key = (source_file, role_label)
        speaker_code = speaker_codes.get(reg_key, "")
        speaker_type = speaker_types.get(reg_key, "unclear")
        attribution_status = "identified" if speaker_type != "unclear" and speaker_code else "indeterminate"
        if speaker_type == "moderator":
            codes = "moderator_context"
        else:
            codes = "general_response"
        if not current_question:
            current_question = "Q1"
        rows.append({
            "segment_id": f"D2_S{segment_counter:04d}",
            "source_file": source_file,
            "table_id": table_id,
            "speaker_code": speaker_code,
            "speaker_type": speaker_type,
            "role_label": role_label if speaker_type != "unclear" else "Attribution indeterminate",
            "attribution_status": attribution_status,
            "question_id": current_question,
            "segment_text": content,
            "codes": codes,
            "language": "en" if source_file in {"HWYO9AR.docx", "HWYO10AR.docx"} else "ar",
        })
        segment_counter += 1
        extracted_count += 1

    notes.append(f"## {source_file}")
    notes.append(f"- Extracted candidate segments: {extracted_count}")
    notes.append(f"- Unresolved labels skipped: {len(unresolved_labels)}")
    if unresolved_labels:
        for label in sorted(unresolved_labels):
            notes.append(f"  - {label}")
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
