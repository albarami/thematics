from __future__ import annotations

import csv
import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(r"c:\Users\baram\OneDrive\Desktop\themnatic")
WORKING_DIR = ROOT / "analysis" / "CASE_D2" / "_working"
TRANSCRIPTS_JSON = WORKING_DIR / "d2_transcripts_extracted.json"
PARTICIPANT_REGISTER = ROOT / "analysis" / "CASE_D2" / "CASE_D2_participant_register.csv"
QUESTION_MAP = ROOT / "analysis" / "CASE_D2" / "CASE_D2_question_map.md"

ARABIC_INLINE_PATTERN = re.compile(r"^(?P<label>(?:د\.|أ\.|أ\.د\.)[^:]{0,80}|[^:]{1,80}\([^)]{1,80}\)|المحاور|مدير الجلسة|المشارك(?:\s+الأول|\s+الثاني|\s+الآخر)?|مشارك(?:\s+آخر)?(?:\s+\([^)]*\))?)\s*:\s*(?P<content>.+)$")
ENGLISH_INLINE_PATTERN = re.compile(r"^(?P<label>(?:(?:Speaker\s+\d+)|Moderator|(?:[A-Za-z][A-Za-z .'-]{0,60}\([^)]{1,60}\))))\s*:\s*(?P<content>.+)$")
QUESTION_PATTERN = re.compile(r"(?:^Question\s+\d+:|^\d-\s|السؤال)", re.IGNORECASE)


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
        "د.ريم :( (Learning Support Specialist)": "د. ريم الحاج",
        "د. ريم الحاج:( (Learning Support Specialist": "د. ريم الحاج",
        "د.ريم:( (Learning Support Specialist": "د. ريم الحاج",
        "د.أمير(GP pediatrics": "د. أمير",
        "د.أمير( GP pediatrics": "د. أمير",
        "د.وائل(أخصائي تأهيل اجتماعي)": "د. وائل",
        "د.وائل)أخصائي تأهيل اجتماعي)": "د. وائل",
        "دكتور وائل(أخصائي تأهيل اجتماعي)": "د. وائل",
        "دكتور وائل (أخصائي تأهيل اجتماعي)": "د. وائل",
        "د.مصطفى(أستاذ جامعي)": "د. مصطفى",
        "د. مصطفى(أستاذ جامعي)": "د. مصطفى",
        "دانا(متلقي خدمة)": "دانا",
        "العافية من منظوري الشخصي والرضى بأن الحياة ، ups and downsدانا (متلقي خدمة)": "دانا",
        "مريم(متلقي خدمة)": "مريم",
        "المحاور (التلخيص)": "المحاور",
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
        "المشارك": "مشارك غير مسمى",
        "مشارك آخر": "مشارك غير مسمى",
        "المشارك الأول": "مشارك أول غير مسمى",
        "مشارك": "مشارك غير مسمى",
        "المحاور": "المحاور",
    }
    return replacements.get(label, re.sub(r"\s+", " ", label))


def table_id_from_filename(filename: str) -> str:
    match = re.search(r"HWYO(\d+)", filename)
    return match.group(1) if match else ""


with TRANSCRIPTS_JSON.open(encoding="utf-8") as handle:
    transcripts = json.load(handle)

stats: dict[tuple[str, str], dict[str, int]] = defaultdict(lambda: {"turns": 0, "chars": 0})
for record in transcripts:
    filename = record["filename"]
    paragraphs: list[str] = record["paragraphs"]
    for paragraph in paragraphs:
        if QUESTION_PATTERN.search(paragraph):
            continue
        match = ARABIC_INLINE_PATTERN.match(paragraph) or ENGLISH_INLINE_PATTERN.match(paragraph)
        if not match:
            continue
        label = normalize_label(match.group("label"))
        content = match.group("content").strip()
        if not content:
            continue
        key = (filename, label)
        stats[key]["turns"] += 1
        stats[key]["chars"] += len(content)

rows: list[list[str | int]] = []
moderator_counter = 1
participant_counter = 1
unclear_counter = 1


def add_row(code: str, source_file: str, table_id: str, speaker_type: str, role_label: str, turns: int, chars: int, basis: str) -> None:
    rows.append([code, source_file, table_id, speaker_type, role_label, turns, chars, basis])


# Moderators, including zero-turn cases where source foundation is authoritative.
moderators = [
    ("HWYO0AR.docx", "0", "Moderator, Table 0", 14, 517, "Classified as moderator from explicit `منسق الجلسة` labels in the transcript."),
    ("HWYO1NT.docx", "1", "Moderator, Table 1", 0, 0, "Classified as moderator from moderator-register review only because no transcript file is available for table 1."),
    ("HWYO3AR.docx", "3", "Moderator, Table 3", 0, 0, "Retained as moderator from moderator-register review; transcript exists but speaker labels remain too weak for confirmed moderator turn extraction."),
    ("HWYO4AR.docx", "4", "Moderator, Table 4", 35, 1015, "Classified as moderator from repeated `مدير الجلسة` facilitation turns in the transcript."),
    ("HWYO5NT1.docx", "5", "Moderator, Table 5", 0, 0, "Classified as moderator from moderator-register review only because no transcript file is available for table 5."),
    ("HWYO6NT1.docx", "6", "Moderator, Table 6", 0, 0, "Classified as moderator from moderator-register review only because no transcript file is available for table 6."),
    ("HWYO7AR.docx", "7", "Moderator, Table 7", 0, 0, "Classified as moderator from transcript opening (`يدير الجلسة أ. عبلة خليل`) and moderator-register review; facilitation turns could not be robustly separated from flowing text."),
    ("HWYO9AR.docx", "9", "Moderator, Table 9", 24, 5408, "Classified as moderator from explicit `Moderator` speaker labels in the transcript and moderator-register review."),
    ("HWYO10AR.docx", "10", "Moderator, Table 10", 3, 456, "Classified as moderator from explicit `Moderator` speaker labels in the transcript and moderator-register review."),
    ("HWYO11AR.docx", "11", "Moderator, Table 11", 12, 742, "Classified as moderator from repeated `المحاور` facilitation labels in the transcript and moderator-register review."),
]
for source_file, table_id, role_label, turns, chars, basis in moderators:
    add_row(f"D2_M{moderator_counter:02d}", source_file, table_id, "moderator", role_label, turns, chars, basis)
    moderator_counter += 1

# Participants with sufficiently defensible transcript evidence.
participants = [
    ("HWYO0AR.docx", "0", "Senior healthcare leader, Table 0", 3, 1704, "Classified as participant from named substantive turns (`د. أحمد العمادي`) in the transcript."),
    ("HWYO0AR.docx", "0", "Consultant obstetrician-gynaecologist, Table 0", 10, 8524, "Classified as participant from repeated named substantive turns (`د. سلوى`) in the transcript."),
    ("HWYO0AR.docx", "0", "Consultant obstetrician-gynaecologist and executive leader, Table 0", 10, 9262, "Classified as participant from repeated named substantive turns (`د. زينة`) in the transcript."),
    ("HWYO0AR.docx", "0", "Mental-health executive, Table 0", 11, 7713, "Classified as participant from repeated named substantive turns (`د. رائد عمرو`) in the transcript."),
    ("HWYO0AR.docx", "0", "Senior psychiatrist and policy adviser, Table 0", 8, 5719, "Classified as participant from repeated named substantive turns (`د. محمد عبد العليم`) in the transcript."),
    ("HWYO0AR.docx", "0", "Family and religious adviser, Table 0", 2, 3373, "Classified as participant from named substantive turns (`د. أحمد الفرجابي`) in the transcript."),
    ("HWYO4AR.docx", "4", "Learning support specialist, Table 4", 4, 1221, "Classified as participant from role-labelled turns (`د. ريم الحاج`) in the transcript."),
    ("HWYO4AR.docx", "4", "Service recipient, Table 4", 1, 143, "Classified as participant because the transcript explicitly labels `مريم` as `متلقي خدمة`."),
    ("HWYO4AR.docx", "4", "Service recipient, Table 4", 1, 195, "Classified as participant because the transcript explicitly labels `دانا` as `متلقي خدمة`."),
    ("HWYO4AR.docx", "4", "Clinical psychologist, Table 4", 5, 1550, "Classified as participant from repeated role-labelled turns (`د. هاجر`) in the transcript."),
    ("HWYO4AR.docx", "4", "Social rehabilitation specialist, Table 4", 6, 2155, "Classified as participant from repeated role-labelled turns (`د. وائل`) in the transcript."),
    ("HWYO4AR.docx", "4", "General paediatrics clinician, Table 4", 7, 3557, "Classified as participant from repeated role-labelled turns (`د. أمير`) in the transcript."),
    ("HWYO4AR.docx", "4", "University academic, Table 4", 2, 1606, "Classified as participant from role-labelled turns (`د. مصطفى`) in the transcript."),
    ("HWYO7AR.docx", "7", "Clinical psychologist, Aman Centre, Table 7", 5, 1877, "Classified as participant from repeated named turns (`د. داليا`) in the transcript."),
    ("HWYO9AR.docx", "9", "Clinical psychologist, PHCC, Table 9", 12, 3367, "Classified as participant from explicit `Speaker 1` header and substantive turns in the transcript."),
    ("HWYO9AR.docx", "9", "Laboratory psychologist, Table 9", 6, 1956, "Classified as participant from explicit `Speaker 2` header and substantive turns in the transcript."),
    ("HWYO9AR.docx", "9", "Occupational therapist, mental health services, Table 9", 14, 5661, "Classified as participant from explicit `Speaker 3` header and substantive turns in the transcript."),
    ("HWYO9AR.docx", "9", "Midwife, women’s hospital, Table 9", 3, 747, "Classified as participant from explicit `Speaker 4` header and substantive turns in the transcript."),
    ("HWYO9AR.docx", "9", "Student, Qatar University, Table 9", 4, 1246, "Classified as participant from explicit `Speaker 5` header and substantive turns in the transcript."),
    ("HWYO9AR.docx", "9", "Academic, college of health science, Table 9", 10, 5560, "Classified as participant from explicit `Speaker 6` header and substantive turns in the transcript."),
    ("HWYO9AR.docx", "9", "Specialist family medicine, PHCC, Table 9", 6, 2734, "Classified as participant from explicit `Speaker 7` header and substantive turns in the transcript."),
    ("HWYO9AR.docx", "9", "Healthcare participant, Table 9", 14, 5216, "Classified as participant from explicit `Speaker 8` turns, but role label remains generic because the transcript does not provide a stable header for Speaker 8."),
    ("HWYO10AR.docx", "10", "Sports podiatry professional, Table 10", 5, 2074, "Classified as participant from named English Q&A turns (`Miguel`)."),
    ("HWYO10AR.docx", "10", "Psychologist, Table 10", 6, 1949, "Classified as participant from named English Q&A turns (`Elena`)."),
    ("HWYO10AR.docx", "10", "Sports podiatry professional, Table 10", 8, 2240, "Classified as participant from named English Q&A turns (`Liam`)."),
    ("HWYO10AR.docx", "10", "Staff nurse, Table 10", 4, 1039, "Classified as participant from named English Q&A turns (`Carmona`)."),
    ("HWYO10AR.docx", "10", "Researcher, Table 10", 6, 1878, "Classified as participant from named English Q&A turns (`Safrina`)."),
    ("HWYO10AR.docx", "10", "Human resources professional, Table 10", 8, 2305, "Classified as participant from named English Q&A turns (`Herald`)."),
    ("HWYO10AR.docx", "10", "Clinical psychologist, Table 10", 5, 1743, "Classified as participant from named English Q&A turns (`Rehana`)."),
    ("HWYO10AR.docx", "10", "Nurse, Table 10", 6, 2020, "Classified as participant from named English Q&A turns (`Aziza`)."),
    ("HWYO11AR.docx", "11", "Dental clinician, private sector, Table 11", 1, 154, "Classified as participant from explicitly role-labelled turn (`د. سارة`)."),
    ("HWYO11AR.docx", "11", "Psychiatrist, Table 11", 5, 2957, "Classified as participant from repeated role-labelled turns (`د. أسماء`) in the transcript."),
    ("HWYO11AR.docx", "11", "Service recipient, Table 11", 3, 1828, "Classified as participant from repeated role-labelled turns (`محمد أبو هاشم – مستفيد`) in the transcript."),
    ("HWYO11AR.docx", "11", "Nurse, Aspetar, Table 11", 2, 2244, "Classified as participant from role-labelled turns (`نيلي خليل`) in the transcript."),
    ("HWYO11AR.docx", "11", "Service recipient, Table 11", 3, 2380, "Classified as participant from repeated role-labelled turns (`عبدالرحمن القديمي – مستفيد/مراجع`) in the transcript."),
    ("HWYO11AR.docx", "11", "Dental clinician, private sector, Table 11", 2, 1325, "Classified as participant from repeated role-labelled turns (`رشا علام`) in the transcript."),
    ("HWYO11AR.docx", "11", "Dental clinician, private sector, Table 11", 4, 3478, "Classified as participant from repeated role-labelled turns (`د. نور غازي`) in the transcript."),
    ("HWYO11AR.docx", "11", "Dental clinician, private sector, Table 11", 1, 1123, "Classified as participant from explicitly role-labelled turn (`سارة غازي`) in the transcript."),
]
for source_file, table_id, role_label, turns, chars, basis in participants:
    add_row(f"D2_P{participant_counter:02d}", source_file, table_id, "participant", role_label, turns, chars, basis)
    participant_counter += 1

# Unclear rows where the transcript clearly preserves speech but identity/role remains indeterminate.
unclear_rows = [
    ("HWYO11AR.docx", "11", "Unclear speaker identity, Table 11", 11, 3737, "Attribution remained indeterminate after review because multiple substantive turns are preserved only as `مشارك آخر` without stable role recovery."),
    ("HWYO11AR.docx", "11", "Unclear speaker identity, Table 11", 4, 133, "Attribution remained indeterminate after review because the transcript retains a recurrent generic `المشارك` label without stable role recovery."),
]
for source_file, table_id, role_label, turns, chars, basis in unclear_rows:
    add_row(f"D2_U{unclear_counter:02d}", source_file, table_id, "unclear", role_label, turns, chars, basis)
    unclear_counter += 1

with PARTICIPANT_REGISTER.open("w", encoding="utf-8-sig", newline="") as handle:
    writer = csv.writer(handle)
    writer.writerow(["anonymized_code", "source_file", "table_id", "speaker_type", "role_label", "turns", "chars", "classification_basis"])
    writer.writerows(rows)

question_map_text = """# CASE_D2 Question Map

## Scope
CASE_D2 (Day 2 — Youth). Seven discussion questions structured in two parts.

## Question structure

### Part 1 — Wellbeing concept and pillars

| Q# | Question text (Arabic) | Question text (English) | Focus |
|----|----------------------|------------------------|-------|
| Q1 | ما معنى الحياة الطيبة بالنسبة لك؟ | What is wellbeing for you? | Open conceptualisation of wellbeing in the youth-health context |
| Q2 | كيف تعرّف العافية من منظورك الشخصي؟ عندما نقول هذا الشخص \"بعافية\" ماذا نقصد؟ | How do you define wellness from your perspective? When we say someone is \"well\", what do we mean? | Wellness definition, dimensions, visible and hidden aspects |
| Q3 | بناء على منظور الحياة الطيبة وركائزها الخمسة (الروحية، العاطفية، الفكرية، البدنية، والاجتماعية)، كيف يمكن لهذه الركائز أن تسهم في تحسين عافيتك؟ | Based on the five HT pillars (spiritual, emotional, intellectual, physical, and social), how can these pillars contribute to improving your wellbeing? | Pillar-based improvement of youth wellbeing |
| Q4 | من واقع تجربتك، هل تنعكس ركائز الحياة الطيبة في خدمات الرعاية الصحية المقدمة حاليا؟ | Based on your experience, are the HT pillars reflected in current healthcare services? | Current service reflection of the pillars |

### Part 2 — Challenges, opportunities, and action

| Q# | Question text (Arabic) | Question text (English) | Focus |
|----|----------------------|------------------------|-------|
| Q5 | ما التحديات الرئيسية التي تواجه دمج ركائز الحياة الطيبة ضمن خدمات الرعاية الصحية؟ | What are the main challenges in integrating the HT pillars into healthcare services? | Barriers, stigma, time, culture, institutional constraints |
| Q6 | ما الفرص المتاحة حاليا لتعزيز دمج ركائز الحياة الطيبة في ممارسات الرعاية الصحية؟ | What opportunities are currently available to enhance the integration of the HT pillars into healthcare practices? | Existing openings, collaboration routes, service-development opportunities |
| Q7 | ما هي اقتراحاتكم العملية لطرق دمج ركائز الحياة الطيبة لتحسين خدمات الرعاية الصحية؟ | What practical suggestions do you have for integrating the HT pillars to improve healthcare services? | Concrete implementation suggestions and recommendations |

## Question coverage by source

| Source | Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | Q7 | Evidence |
|--------|----|----|----|----|----|----|----|----|
| HWYO0AR | Y | Y | Y | Y | Y | Y | Y | Moderator explicitly separates the first session (Q1–Q4) from the second session (challenges, opportunities, recommendations). |
| HWYO3AR | Y | Y | Y | Y | ? | ? | ? | Transcript has explicit Q1 and Q4 cues. Part 2 content likely present but labels are too weak for full boundary confirmation without coding review. |
| HWYO4AR | Y | Y | Y | Y | ? | ? | ? | `مدير الجلسة` explicitly moves through Q1–Q4. Part 2 is referenced in notes, but transcript boundaries after Q4 are less clean than the note template. |
| HWYO7AR | Y | Y | Y | Y | Y | Y | ? | Transcript opening covers Q1–Q4 and later explicitly shifts to challenges and opportunities; Q7 practical-suggestion boundary is likely present but not cleanly marked in the flowing transcript. |
| HWYO9AR | Y | Y | Y | Y | Y | Y | Y | Explicit moderator prompts for Q1–Q7 in English. |
| HWYO10AR | Y | Y | Y | Y | partial | partial | partial | Explicit `Question 1` through `Question 4`, followed by a compressed interactive discussion that blends Q5–Q7 material rather than cleanly separating them. |
| HWYO11AR | Y | Y | Y | Y | Y | Y | Y | `المحاور` explicitly moves through Q1–Q4, and paired note `HWYO11NT2` preserves the full Q1–Q7 template. |
| Note files | Y | Y | Y | Y | Y | Y | Y | All reviewed note files use the standard Day 2 seven-question template. |
| Rec. workbook | — | — | — | — | — | partial | Y | Auxiliary recommendation material. Supports Q6 opportunities and Q7 practical suggestions only. |

## Notes
- Y = question explicitly covered in source
- ? = content likely present but question boundaries are not explicit enough to lock before coding
- partial = source contributes relevant material but does not preserve a clean question boundary in its current extracted form
- — = question not covered in this source
- The Day 2 note templates are the most reliable Gate 1 evidence for confirming the canonical seven-question structure across the case.
"""
QUESTION_MAP.write_text(question_map_text, encoding="utf-8")
print(f"Wrote {PARTICIPANT_REGISTER}")
print(f"Wrote {QUESTION_MAP}")
