from __future__ import annotations

import re
from collections import Counter
from typing import Any

from integrated_d1_d4_constants import INTEGRATED_THEMES


def build_integrated_theme_rows(case_packages: dict[str, dict[str, Any]]) -> list[dict[str, str]]:
    """Aggregate the four aligned case themes into four integrated theme rows.

    Args:
        case_packages: Loaded outward-facing case package data.

    Returns:
        Aggregated integrated-theme rows for reporting tables.
    """
    rows: list[dict[str, str]] = []
    for theme in INTEGRATED_THEMES:
        totals = {
            "participant_segments": 0,
            "unique_speakers": 0,
            "unique_tables": 0,
            "case_count": 0,
        }
        case_titles: list[str] = []
        question_union: set[str] = set()
        salience_counts: Counter[str] = Counter()
        for case_id, package in case_packages.items():
            match = _theme_summary_by_number(package["theme_summary"], theme["theme_number"])
            if not match:
                continue
            totals["participant_segments"] += _as_int(match.get("participant_segments"))
            totals["unique_speakers"] += _as_int(match.get("unique_speakers"))
            totals["unique_tables"] += _as_int(match.get("unique_tables"))
            totals["case_count"] += 1
            salience_counts[match.get("salience", "")] += 1
            case_titles.append(f"{case_id}: {match.get('theme_name', '')}")
            question_union.update(_split_semicolon(match.get("questions_present", "")))
        rows.append(
            {
                "integrated_theme_id": theme["id"],
                "integrated_theme": theme["title"],
                "cases_present": str(totals["case_count"]),
                "aggregated_participant_segments": str(totals["participant_segments"]),
                "aggregated_unique_speakers": str(totals["unique_speakers"]),
                "aggregated_unique_tables": str(totals["unique_tables"]),
                "questions_present": ";".join(sorted(question_union, key=_question_sort_key)),
                "dominant_salience_pattern": _dominant_salience(salience_counts),
                "case_expressions": " | ".join(case_titles),
                "integrated_summary": theme["summary"],
            }
        )
    return rows


def build_question_totals(case_packages: dict[str, dict[str, Any]]) -> list[dict[str, str]]:
    """Aggregate question-level evidence counts across the approved case packages.

    Args:
        case_packages: Loaded outward-facing case package data.

    Returns:
        Cross-case question summary rows.
    """
    totals: dict[str, dict[str, Any]] = {
        question_id: {
            "participant_segments": 0,
            "moderator_segments": 0,
            "unclear_segments": 0,
            "unique_participant_speakers": 0,
            "case_source_notes": [],
        }
        for question_id in [f"Q{index}" for index in range(1, 8)]
    }
    for case_id, package in case_packages.items():
        for row in package["question_evidence"]:
            question_id = row["question_id"]
            target = totals[question_id]
            target["participant_segments"] += _as_int(row.get("participant_segments"))
            target["moderator_segments"] += _as_int(row.get("moderator_segments"))
            target["unclear_segments"] += _as_int(row.get("unclear_segments"))
            target["unique_participant_speakers"] += _as_int(row.get("unique_participant_speakers"))
            target["case_source_notes"].append(
                f"{case_id}: {_truncate(row.get('top_codes', ''), 80)}"
            )
    return [
        {
            "question_id": question_id,
            "participant_segments": str(values["participant_segments"]),
            "moderator_segments": str(values["moderator_segments"]),
            "unclear_segments": str(values["unclear_segments"]),
            "summed_unique_participant_speakers": str(values["unique_participant_speakers"]),
            "case_signal_notes": " | ".join(values["case_source_notes"]),
        }
        for question_id, values in totals.items()
    ]


def build_integrated_matrix_rows(case_packages: dict[str, dict[str, Any]]) -> list[dict[str, str]]:
    """Aggregate the question-by-theme matrices into aligned integrated theme rows.

    Args:
        case_packages: Loaded outward-facing case package data.

    Returns:
        Cross-case matrix rows keyed by question.
    """
    matrix_rows: list[dict[str, str]] = []
    for question_id in [f"Q{index}" for index in range(1, 8)]:
        row: dict[str, str] = {"question_id": question_id}
        for theme in INTEGRATED_THEMES:
            segments = 0
            speakers = 0
            tables = 0
            case_presence = 0
            for package in case_packages.values():
                match = next(
                    (item for item in package["question_matrix"] if item["question_id"] == question_id),
                    None,
                )
                if match is None:
                    continue
                segments_value = matrix_metric(match, theme["theme_number"], "segments")
                speakers_value = matrix_metric(match, theme["theme_number"], "speakers")
                tables_value = matrix_metric(match, theme["theme_number"], "tables")
                segments += segments_value
                speakers += speakers_value
                tables += tables_value
                if segments_value > 0:
                    case_presence += 1
            key = theme["id"]
            row[f"{key}_segments"] = str(segments)
            row[f"{key}_speakers"] = str(speakers)
            row[f"{key}_tables"] = str(tables)
            row[f"{key}_case_presence"] = str(case_presence)
        matrix_rows.append(row)
    return matrix_rows


def build_evidence_mix_rows(case_packages: dict[str, dict[str, Any]]) -> list[dict[str, str]]:
    """Summarize evidence-type and support-layer mix across cases.

    Args:
        case_packages: Loaded outward-facing case package data.

    Returns:
        Per-case evidence-mix rows.
    """
    rows: list[dict[str, str]] = []
    for case_id, package in case_packages.items():
        excerpt_rows = package["excerpt_bank"]
        evidence_counter = Counter(row.get("evidence_type", "") for row in excerpt_rows)
        speaker_counter = Counter(row.get("speaker_type", "") for row in excerpt_rows)
        report_use_counter = Counter(row.get("report_use", "") for row in excerpt_rows)
        rows.append(
            {
                "case_id": case_id,
                "excerpt_rows": str(len(excerpt_rows)),
                "verbatim_transcript": str(evidence_counter.get("verbatim_transcript", 0)),
                "note_style_transcript_summary": str(evidence_counter.get("note_style_transcript_summary", 0)),
                "note_taker_summary": str(evidence_counter.get("note_taker_summary", 0)),
                "participant_rows": str(speaker_counter.get("participant", 0)),
                "unclear_rows": str(speaker_counter.get("unclear", 0)),
                "theme_evidence_rows": str(report_use_counter.get("theme_evidence", 0)),
                "close_reading_rows": str(report_use_counter.get("close_reading_theme_support", 0)),
                "contextual_rows": str(report_use_counter.get("contextual_theme_support", 0)),
            }
        )
    return rows


def build_case_prominence_rows(case_packages: dict[str, dict[str, Any]]) -> list[dict[str, str]]:
    """Capture case-level salience across the aligned four-theme structure.

    Args:
        case_packages: Loaded outward-facing case package data.

    Returns:
        Case-by-theme salience rows for chart-ready tables.
    """
    rows: list[dict[str, str]] = []
    for case_id, package in case_packages.items():
        for theme in package["prominence"]:
            theme_number = extract_theme_number(theme.get("theme", ""))
            rows.append(
                {
                    "case_id": case_id,
                    "theme_number": theme_number,
                    "integrated_theme_id": f"IT{theme_number}",
                    "participant_segments": str(_as_int(theme.get("participant_segments"))),
                    "unique_speakers": str(_as_int(theme.get("unique_speakers"))),
                    "unique_tables": str(_as_int(theme.get("unique_tables"))),
                    "questions_present": theme.get("questions_present", ""),
                    "salience": theme.get("salience", ""),
                    "salience_explanation": theme.get("salience_explanation", ""),
                }
            )
    return rows


def build_quote_lookup(case_packages: dict[str, dict[str, Any]]) -> dict[tuple[str, str], dict[str, str]]:
    """Build a lookup of excerpt-bank evidence rows keyed by case and evidence ID.

    Args:
        case_packages: Loaded outward-facing case package data.

    Returns:
        Mapping of `(case_id, evidence_id)` to excerpt-bank row.
    """
    lookup: dict[tuple[str, str], dict[str, str]] = {}
    for case_id, package in case_packages.items():
        for row in package["excerpt_bank"]:
            lookup[(case_id, row["evidence_id"])] = row
    return lookup


def as_int(value: str | None) -> int:
    """Convert a string integer to `int` with empty-string tolerance."""
    return _as_int(value)


def extract_theme_number(value: str) -> str:
    """Extract the numeric theme identifier from a theme label."""
    return _extract_theme_number(value)


def matrix_metric(row: dict[str, str], theme_number: str, metric: str) -> int:
    """Read a theme metric from a question-theme matrix row."""
    return _matrix_metric(row, theme_number, metric)


def truncate(text: str, limit: int) -> str:
    """Normalize whitespace and truncate text with an ellipsis when needed."""
    return _truncate(text, limit)


def _as_int(value: str | None) -> int:
    if not value:
        return 0
    return int(value)


def _theme_summary_by_number(rows: list[dict[str, str]], theme_number: str) -> dict[str, str] | None:
    return next((row for row in rows if row.get("theme_number") == theme_number), None)


def _split_semicolon(value: str) -> list[str]:
    return [item for item in value.split(";") if item]


def _question_sort_key(question_id: str) -> int:
    return int(question_id.replace("Q", ""))


def _dominant_salience(counter: Counter[str]) -> str:
    if not counter:
        return ""
    return counter.most_common(1)[0][0]


def _extract_theme_number(value: str) -> str:
    match = re.search(r"Theme[_ ]?(\d)", value)
    return match.group(1) if match else ""


def _matrix_metric(row: dict[str, str], theme_number: str, metric: str) -> int:
    if not theme_number:
        return 0
    suffix = f"_{metric}"
    for key, value in row.items():
        if key.startswith(f"Theme_{theme_number}_") and key.endswith(suffix):
            return _as_int(value)
    return 0


def _truncate(text: str, limit: int) -> str:
    clean = " ".join(text.split())
    return clean if len(clean) <= limit else f"{clean[: limit - 1]}…"
