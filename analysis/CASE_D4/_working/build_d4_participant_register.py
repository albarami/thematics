"""Build CASE_D4_participant_register.csv from extracted Day 4 transcripts.

Reads d4_transcripts_extracted.json, matches speaker labels to the
locked participant/moderator roster, counts turns and characters per
speaker, and writes the register CSV.
"""
from __future__ import annotations

import csv
import json
import re
from pathlib import Path
from typing import Final

ROOT: Final = Path(r"c:\Users\baram\OneDrive\Desktop\themnatic")
CASE_DIR: Final = ROOT / "analysis" / "CASE_D4"
WORKING_DIR: Final = CASE_DIR / "_working"
TRANSCRIPTS_JSON: Final = WORKING_DIR / "d4_transcripts_extracted.json"
OUTPUT_PATH: Final = CASE_DIR / "CASE_D4_participant_register.csv"

HEADER: Final = [
    "anonymized_code", "source_file", "table_id", "speaker_type",
    "role_label", "turns", "chars", "classification_basis",
]

SPEAKERS: Final = (
    # (code, source_file, table_id, speaker_type, role_label, aliases, basis)
    ("D4_M01", "HWEL1AR.docx", 1, "moderator", "Moderator, Table 1",
     ("Diana (moderator)",),
     "Explicit `Diana (moderator)` labels and moderator_register_refresh.csv."),
    ("D4_M02", "HWEL3AR.docx", 3, "moderator", "Moderator, Table 3",
     ("\u0623.\u0647\u0627\u0644\u0629", "\u0623\u0633\u062a\u0627\u0630\u0629 \u0647\u0627\u0644\u0629", "\u0627.\u0647\u0627\u0644\u0629"),
     "Facilitation turns and moderator-register review; probable not fully confirmed."),
    ("D4_M03", "HWEL4NT1.docx", 4, "moderator", "Moderator, Table 4",
     (),
     "Moderators.xlsx only; table 4 is note-only."),
    ("D4_M04", "HWEL6NT1.docx", 6, "moderator", "Moderator, Table 6",
     (),
     "Moderators.xlsx only; table 6 is note-only."),
    ("D4_M05", "HWEL7AR.docx", 7, "moderator", "Moderator, Table 7",
     ("\u0645\u062f\u064a\u0631 \u0627\u0644\u062c\u0644\u0633\u0629", "\u0645\u062f\u064a\u0631 \u0627\u0644\u062c\u0644\u0633\u0647"),
     "Repeated facilitation turns and moderator-register review; probable."),
    ("D4_M06", "HWEL9AR.docx", 9, "moderator", "Moderator, Table 9",
     ("Dr Abdellatif Moderator",),
     "Explicit `Dr Abdellatif Moderator` labeling and moderator-register review."),
    ("D4_M07", "HWEL10AR.docx", 10, "moderator", "Moderator, Table 10",
     ("Moderator",),
     "Explicit `Moderator` labels in English transcript and moderator-register review."),
    ("D4_P01", "HWEL1AR.docx", 1, "participant",
     "Participant, role not stated, Table 1",
     ("\u062f. \u062f\u0631\u0648\u064a\u0634 \u0627\u0644\u0639\u0645\u0627\u062f\u064a",),
     "Repeated named substantive turns in HWEL1AR."),
    ("D4_P02", "HWEL1AR.docx", 1, "participant",
     "Director of Pharmacy, Table 1",
     ("\u0623\u0646\u0627 \u062f. \u0623\u0645\u064a\u0646\u0629 \u0627\u0644\u064a\u0632\u064a\u062f\u064a \u062f\u064a\u0631\u064a\u0643\u062a\u0648\u0631 \u0627\u0644\u0641\u0627\u0631\u0645\u0633\u064a(Director of Pharmacy)",
      "\u062f. \u0623\u0645\u064a\u0646\u0629 \u0627\u0644\u064a\u0632\u064a\u062f\u064a \u062f\u064a\u0631\u064a\u0643\u062a\u0648\u0631 \u0627\u0644\u0641\u0627\u0631\u0645\u0633\u064a(Director of Pharmacy)"),
     "Named turns with explicit Director of Pharmacy role wording."),
    ("D4_P03", "HWEL1AR.docx", 1, "participant",
     "Home care participant, Hamad Medical Corporation, Table 1",
     ("\u0645\u0631\u064a\u0645 \u0627\u0644\u062a\u0645\u064a\u0645\u064a \u0645\u0646 \u0627\u0644\u0631\u0639\u0627\u064a\u0629 \u0627\u0644\u0645\u0646\u0632\u0644\u064a\u0629 \u0645\u0624\u0633\u0633\u0629 \u062d\u0645\u062f \u0627\u0644\u0637\u0628\u064a\u0629",
      "\u0645\u0631\u064a\u0645 \u0627\u0644\u062a\u0645\u064a\u0645\u064a \u0645\u0646 \u0627\u0644\u0631\u0639\u0627\u064a\u0629 \u0627\u0644\u0645\u0646\u0632\u0644\u064a\u0629"),
     "Named turns with explicit home-care role wording."),
    ("D4_P04", "HWEL1AR.docx", 1, "participant",
     "Service recipient, Table 1",
     ("\u0647\u0646\u062f \u0627\u0644\u062c\u0627\u0628\u0631  :(\u0070\u0061\u0074\u0069\u0065\u006e\u0074)",
      "\u0647\u0646\u062f \u0627\u0644\u062c\u0627\u0628\u0631"),
     "Transcript labels speaker as (patient) with substantive turns."),
    ("D4_P05", "HWEL1AR.docx", 1, "participant",
     "Participant, Hamad Medical Corporation, Table 1",
     ("\u0628\u0634\u0627\u064a\u0631 \u0627\u0644\u0631\u0627\u0634\u062f \u0645\u0646 \u0645\u0624\u0633\u0633\u0629 \u062d\u0645\u062f \u0627\u0644\u0637\u0628\u064a\u0629",),
     "Named turns with institutional affiliation."),
    ("D4_P06", "HWEL1AR.docx", 1, "participant",
     "Participant, role not stated, Table 1",
     ("\u0627\u0644\u062f\u0643\u062a\u0648\u0631 \u0643\u0627\u0643\u0644 \u0631\u0633\u0648\u0644",
      "\u062f. \u0643\u0627\u0643\u0644 \u0631\u0633\u0648\u0644"),
     "Named substantive turns in HWEL1AR."),
    ("D4_P07", "HWEL1AR.docx", 1, "participant",
     "Participant, role not stated, Table 1",
     ("\u062f. \u0627\u062d\u0645\u062f \u0647\u0627\u0646\u064a",),
     "Named substantive turns in HWEL1AR."),
    ("D4_P08", "HWEL3AR.docx", 3, "participant",
     "Participant, Hamad Medical Corporation, Table 3",
     ("\u062f.\u0633\u0648\u0633\u0648 (Hamad Medical Corporate)",
      "\u062f.\u0633\u0648\u0633\u0648"),
     "Repeated short-label turns and one fuller role-labelled line."),
    ("D4_P09", "HWEL3AR.docx", 3, "participant",
     "Psychologist, Ihsan Center, Table 3",
     ("\u0623.\u0645\u0631\u064a\u0645", "\u0623\u0633\u062a\u0627\u0630\u0629 \u0645\u0631\u064a\u0645"),
     "Repeated short-label turns and embedded PSYCHOLOGIST - Ihsan Center role."),
    ("D4_P10", "HWEL3AR.docx", 3, "participant",
     "Social-welfare / social-work participant, Table 3",
     ("\u062f\u0643\u062a\u0648\u0631\u0629 \u0641\u064a\u0631\u0648\u0632 ( clinical social worker - HMC-Mental Health)",
      "\u062f\u0643\u062a\u0648\u0631\u0629 \u0641\u064a\u0631\u0648\u0632 (Head of Social Welfare Section - Ihsan Center)",
      "\u062f.\u0641\u064a\u0631\u0648\u0632"),
     "Named turns with social-work / welfare role labels."),
    ("D4_P11", "HWEL3AR.docx", 3, "participant",
     "Participant, role not stated, Table 3",
     ("\u0623.\u0631\u064a\u0645\u0627 \u062e\u0644\u064a\u0641\u0629",
      "\u0623.\u0631\u064a\u0645"),
     "Named roster in HWEL3NT1 and corresponding transcript turns."),
    ("D4_P12", "HWEL3AR.docx", 3, "participant",
     "Occupational therapy, elderly care, Hamad Medical Corporation, Table 3",
     ("\u0623\u0633\u062a\u0627\u0630 \u0645\u062d\u0645\u0648\u062f (OCCUPATIONAL THERAPY-ELDERLY - Hamad Medical Corporate)",
      "\u0623\u0633\u062a\u0627\u0630 \u0645\u062d\u0645\u0648\u062f",
      "\u0623.\u0645\u062d\u0645\u0648\u062f"),
     "Named turns with occupational-therapy role label."),
    ("D4_P13", "HWEL7AR.docx", 7, "participant",
     "Rehabilitation-hospital participant, Table 7",
     ("\u0636\u062d\u0649 \u0645\u062d\u0645\u0648\u062f",),
     "Repeated named substantive turns including rehabilitation-hospital experience."),
    ("D4_P14", "HWEL7AR.docx", 7, "participant",
     "Home care physician, Table 7",
     ("\u062f. \u062d\u0646\u0627\u0646 \u0627\u0644\u064a\u0627\u0641\u0639\u0649",
      "\u062f.\u062d\u0646\u0627\u0646 \u0627\u0644\u064a\u0627\u0641\u0639\u064a",
      "\u062f. \u062d\u0646\u0627\u0646 \u0627\u0644\u064a\u0627\u0641\u0639\u064a"),
     "Repeated named turns with home-care physician positioning."),
    ("D4_P15", "HWEL7AR.docx", 7, "participant",
     "Participant, role not stated, Table 7",
     ("\u062f.\u0639\u0644\u0627\u0621 \u0627\u0644\u062f\u064a\u0646 \u0627\u0644\u0643\u064a\u0644\u0627\u0646\u064a",),
     "Repeated named substantive turns in HWEL7AR."),
    ("D4_P16", "HWEL7AR.docx", 7, "participant",
     "Participant, role not stated, Table 7",
     ("\u062f. \u0634\u0627\u0643\u064a\u0646\u0627\u0632",),
     "Repeated named substantive turns in HWEL7AR."),
    ("D4_P17", "HWEL7AR.docx", 7, "participant",
     "Elderly-center participant, Table 7",
     ("\u0639\u0627\u062f\u0644 \u0627\u0644\u0633\u0644\u064a\u0637\u064a",),
     "Repeated named turns with elderly-center service-experience examples."),
    ("D4_P18", "HWEL7AR.docx", 7, "participant",
     "Service recipient, Table 7",
     ("\u062f. \u0645\u0635\u0637\u0641\u0649",),
     "Named turn and moderator clarification of service-user voice."),
    ("D4_P19", "HWEL7AR.docx", 7, "participant",
     "Participant, role not stated, Table 7",
     ("\u0627\u0645\u0644 \u0627\u0644\u0639\u0628\u064a\u062f\u0644\u0649",),
     "Named turns late in transcript; brief contribution."),
    ("D4_P20", "HWEL7AR.docx", 7, "participant",
     "Senior public-sector leader, Table 7",
     ("\u0627\u0644\u0648\u0632\u064a\u0631",),
     "Repeated substantive turns labeled al-wazir with late role-description line."),
    ("D4_P21", "HWEL7AR.docx", 7, "participant",
     "Participant, role not stated, Table 7",
     ("\u062f.\u0645\u062d\u0645\u062f",),
     "Named substantive turn late in HWEL7AR; role not preserved."),
    ("D4_P22", "HWEL9AR.docx", 9, "participant",
     "Social worker, Ihsan Center, Table 9",
     ("Noor Ali Albadr Social Worker - ishan",
      "Noor Ali Albadr Social Worker \u2013 ishan"),
     "Repeated role-labelled turns in HWEL9AR."),
    ("D4_P23", "HWEL9AR.docx", 9, "participant",
     "Acute geriatric and elderly care, Hamad Medical Corporation, Table 9",
     ("Esmat Swallmeh Acute Geriatric and Elderly care - Hamad Medical Corporate",),
     "Repeated role-labelled turns in HWEL9AR."),
    ("D4_P24", "HWEL9AR.docx", 9, "participant",
     "Senior pharmacist, Naufar, Table 9",
     ("Randa Al Okka Sr. Pharmacist - Naufar",),
     "Repeated role-labelled turns in HWEL9AR."),
    ("D4_P25", "HWEL9AR.docx", 9, "participant",
     "Service recipient / patient voice, Table 9",
     ("patient \u062f. \u0645\u062d\u0645\u062f \u0639\u0628\u062f \u0627\u0644\u0639\u0644\u064a\u0645",),
     "Repeated substantive turns labeled patient in HWEL9AR."),
    ("D4_P26", "HWEL10AR.docx", 10, "participant",
     "Consultant in family medicine, PHCC, Table 10",
     ("Dr. Amit",),
     "Stable named turns in English transcript corroborated by HWEL10NT2."),
    ("D4_P27", "HWEL10AR.docx", 10, "participant",
     "Student, HBKU, Table 10",
     ("Manal Sherif",),
     "Stable named turns in English transcript corroborated by HWEL10NT2."),
    ("D4_P28", "HWEL10AR.docx", 10, "participant",
     "Rumailah Hospital participant, Table 10",
     ("Al anood",),
     "Stable named turns in English transcript corroborated by HWEL10NT2."),
    ("D4_P29", "HWEL10AR.docx", 10, "participant",
     "Qatar University participant, Table 10",
     ("Dr. Khalood",),
     "Stable named turns in English transcript corroborated by HWEL10NT2."),
)


def _normalize(text: str) -> str:
    """Collapse whitespace and normalize dashes."""
    return re.sub(r"\s+", " ", text.replace("\u2013", "-").replace("\u2014", "-")).strip()


def _build_alias_lookup() -> list[tuple[str, str]]:
    """Return (normalized_alias, code) sorted longest-first."""
    pairs: list[tuple[str, str]] = []
    for code, _sf, _tid, _st, _rl, aliases, _cb in SPEAKERS:
        for alias in aliases:
            pairs.append((_normalize(alias), code))
    return sorted(pairs, key=lambda p: len(p[0]), reverse=True)


def _match_label(text: str, lookup: list[tuple[str, str]]) -> tuple[str | None, str]:
    """Return (matched_code, remaining_content) or (None, '') if no match."""
    for alias, code in lookup:
        if text == alias or text == f"{alias}:" or text == f"{alias} :":
            return code, ""
        for sep in (":", " :"):
            prefix = f"{alias}{sep}"
            if text.startswith(prefix):
                return code, text[len(prefix):].strip()
    return None, ""


SKIP_PREFIXES: Final = ("HWEL", "Part ", "Top of Form", "Bottom of Form")
SKIP_EXACT: Final = frozenset({"-" * 80})


def _is_skip(text: str) -> bool:
    if not text:
        return True
    if text in SKIP_EXACT:
        return True
    return any(text.startswith(p) for p in SKIP_PREFIXES)


def main() -> None:
    """Compute per-speaker turn/char counts and write the register CSV."""
    with TRANSCRIPTS_JSON.open(encoding="utf-8") as fh:
        records = json.load(fh)

    lookup = _build_alias_lookup()
    metrics: dict[str, list[int]] = {s[0]: [0, 0] for s in SPEAKERS}

    for record in records:
        active_code: str | None = None
        active_parts: list[str] = []
        for raw_para in record["paragraphs"]:
            text = _normalize(raw_para)
            if _is_skip(text):
                continue
            matched, inline = _match_label(text, lookup)
            if matched is not None:
                if active_code and active_parts:
                    metrics[active_code][0] += 1
                    metrics[active_code][1] += len(" ".join(active_parts))
                active_code = matched
                active_parts = [inline] if inline else []
                continue
            if active_code is not None:
                active_parts.append(text)
        if active_code and active_parts:
            metrics[active_code][0] += 1
            metrics[active_code][1] += len(" ".join(active_parts))

    rows: list[list[str]] = []
    for code, src, tid, stype, rlabel, _aliases, basis in SPEAKERS:
        turns, chars = metrics[code]
        rows.append([code, src, str(tid), stype, rlabel, str(turns), str(chars), basis])

    with OUTPUT_PATH.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(HEADER)
        writer.writerows(rows)

    print(f"Wrote {len(rows)} rows to {OUTPUT_PATH}")
    total_p = sum(1 for s in SPEAKERS if s[3] == "participant")
    total_m = sum(1 for s in SPEAKERS if s[3] == "moderator")
    print(f"  participants: {total_p}  moderators: {total_m}")
    zero_turn = [code for code, src, *_ in rows if int(_[3]) == 0 and SPEAKERS[[s[0] for s in SPEAKERS].index(code)][3] != "moderator"]
    if zero_turn:
        print(f"  WARNING zero-turn participants: {zero_turn}")


if __name__ == "__main__":
    main()
