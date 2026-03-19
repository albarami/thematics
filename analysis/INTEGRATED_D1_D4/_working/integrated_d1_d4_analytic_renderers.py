from __future__ import annotations

from pathlib import Path
from typing import Any

from integrated_d1_d4_constants import CASES, CROSSCUTTING_PATTERNS, INTEGRATED_THEMES, OUTPUT_FILES


def render_methodology(
    case_packages: dict[str, dict[str, Any]],
    integrated_theme_rows: list[dict[str, str]],
    evidence_mix_rows: list[dict[str, str]],
) -> str:
    """Render the integrated D1-D4 methodology file.

    Args:
        case_packages: Loaded outward-facing case package data.
        integrated_theme_rows: Aggregated integrated-theme rows.
        evidence_mix_rows: Case-level evidence mix rows.

    Returns:
        The methodology markdown content.
    """
    total_excerpt_rows = sum(int(row["excerpt_rows"]) for row in evidence_mix_rows)
    total_note_rows = sum(
        int(row["note_style_transcript_summary"]) + int(row["note_taker_summary"])
        for row in evidence_mix_rows
    )
    lines = [
        "# Integrated D1-D4 Methodology",
        "",
        "## Scope",
        "This methodology governs the final integrated synthesis across `CASE_D1`, `CASE_D2`, `CASE_D3`, and `CASE_D4` only.",
        "The four case packages are treated as frozen outward-facing building blocks unless a real evidence-backed error is identified.",
        "The excluded fifth case/day remains fully out of scope for inventories, matrices, charts, and reporting claims.",
        "",
        "## Source base",
        f"The integrated synthesis draws only from the approved outward-facing package layer of the four assessed cases. Across those packages, the integrated evidence layer includes `{total_excerpt_rows}` excerpt-bank rows and `{total_note_rows}` explicitly labeled note-based support rows.",
        "No internal identity keys, named participant files, or raw transcript layers were reopened during this synthesis build.",
        "",
        "## Source hierarchy and handling rules",
        "The integrated build preserves the same evidence hierarchy used in the approved case packages.",
        "",
        "- `verbatim_transcript` rows remain the strongest outward-facing quotation layer.",
        "- `note_style_transcript_summary` rows remain usable only when explicitly labeled as note-style summary material.",
        "- `note_taker_summary` rows remain auxiliary and are never rewritten as direct participant speech.",
        "- `unclear` attribution rows remain explicitly flagged and do not count as clean participant-diversity evidence.",
        "- Moderator material remains contextual only and is excluded from participant evidence claims.",
        "- Recommendation workbook logic remains auxiliary only: it may support implementation interpretation, but it does not originate themes.",
        "",
        "## Integrated analytic model",
        "The integrated synthesis does not flatten the cases into a single universal narrative. It proceeds in three linked steps:",
        "",
        "1. preserve each case as an already-approved within-case interpretation",
        "2. map the aligned four-theme case structures onto four integrated synthesis themes",
        "3. surface cross-cutting patterns only after life-stage and stakeholder differences have been retained",
        "",
        "The aligned integrated themes are listed below.",
        "",
    ]
    lines.extend(
        _table(
            integrated_theme_rows,
            [
                "integrated_theme_id",
                "integrated_theme",
                "cases_present",
                "aggregated_participant_segments",
                "aggregated_unique_speakers",
                "questions_present",
                "dominant_salience_pattern",
            ],
        )
    )
    lines.extend(
        [
            "",
            "## Cross-cutting synthesis patterns",
            "These patterns are treated as interpretive overlays rather than replacements for the four integrated themes.",
            "",
        ]
    )
    for pattern in CROSSCUTTING_PATTERNS:
        lines.extend([
            f"### {pattern['id']} — {pattern['title']}",
            pattern["summary"],
            "",
        ])
    lines.extend(
        [
            "## Structured outputs",
            f"The integrated build creates the following primary outputs: `{OUTPUT_FILES['report'].name}`, `{OUTPUT_FILES['methodology'].name}`, `{OUTPUT_FILES['synthesis_memo'].name}`, `{OUTPUT_FILES['summary_tables'].name}`, `{OUTPUT_FILES['visuals'].name}`, `{OUTPUT_FILES['question_workbook'].name}`, `{OUTPUT_FILES['theme_workbook'].name}`, `{OUTPUT_FILES['participant_workbook'].name}`, and `{OUTPUT_FILES['crosscheck'].name}`.",
            "",
            "## Quality controls",
            "Integrated quality control is based on the approved case cross-checks plus a final integrated package verification pass.",
            "",
            "- all integrated rows must point back to approved outward-facing files",
            "- D1-D4 case boundaries must remain explicit in every workbook",
            "- no new cross-case claims may override within-case limitations",
            "- no quotes may be silently de-labeled from note-style or note-taker support",
            "- no material from the excluded fifth case/day may appear anywhere in the integrated output layer",
            "",
            "## Case-sensitive limitations carried into integration",
            "The integrated report preserves the main limitations already documented in the approved case packages rather than hiding them behind aggregate counts.",
            "",
        ]
    )
    for case_id, package in case_packages.items():
        lines.append(f"### {case_id}")
        for limitation in package["config"]["limitations"]:
            lines.append(f"- {limitation}")
        lines.append("")
    return "\n".join(lines)


def render_synthesis_memo(
    case_packages: dict[str, dict[str, Any]],
    integrated_theme_rows: list[dict[str, str]],
    question_totals: list[dict[str, str]],
) -> str:
    """Render the cross-case synthesis memo.

    Args:
        case_packages: Loaded outward-facing case package data.
        integrated_theme_rows: Aggregated integrated-theme rows.
        question_totals: Cross-case question total rows.

    Returns:
        The synthesis memo markdown content.
    """
    del case_packages
    strongest_question = max(question_totals, key=lambda row: int(row["participant_segments"]))
    strongest_theme = max(
        integrated_theme_rows,
        key=lambda row: int(row["aggregated_participant_segments"]),
    )
    lines = [
        "# Integrated D1-D4 Cross-Case Synthesis Memo",
        "",
        "## Purpose",
        "This memo captures the interpretive bridge between the frozen case packages and the final integrated report.",
        "It does not reopen the case analyses. It explains how convergence, divergence, and stakeholder-specific emphasis were handled across the four assessed days.",
        "",
        "## Main synthesis judgement",
        f"The strongest cross-case question density sits at `{strongest_question['question_id']}` with `{strongest_question['participant_segments']}` summed participant segments across D1-D4, while the most heavily evidenced aligned integrated theme is `{strongest_theme['integrated_theme_id']}`.",
        "That combination supports a clear overall conclusion: the corpus treats wellbeing as whole-person and value-laden, but it repeatedly shows that current services only partially sustain that ideal in lived practice.",
        "",
        "## Convergence",
        "",
    ]
    for theme in INTEGRATED_THEMES:
        lines.extend([
            f"### {theme['id']} — {theme['title']}",
            theme["summary"],
            "",
        ])
    lines.extend(
        [
            "## Divergence and case-specific weighting",
            "Cross-case comparison does not erase case differences. The main divergences are about which pillar becomes heaviest, who is expected to carry the burden, and where improvement is imagined to start.",
            "",
        ]
    )
    for case_id, config in CASES.items():
        lines.extend([
            f"### {case_id}",
            config["case_variation"],
            "",
        ])
    lines.extend(["## Cross-cutting patterns", ""])
    for pattern in CROSSCUTTING_PATTERNS:
        lines.extend([
            f"### {pattern['id']} — {pattern['title']}",
            pattern["summary"],
            "",
        ])
    lines.extend(
        [
            "## Implication for final reporting",
            "The final integrated report therefore uses a question-and-domain structure rather than a purely case-by-case recap.",
            "That structure allows the report to show the common architecture of the findings while still naming what is specific to childhood, youth, adulthood, and older age.",
            "",
            "## Stop rules",
            "No new integrated claim should be added if it depends on raw files, moderator prompts as participant evidence, or recommendation-workbook rows treated as if they generated themes.",
            "",
        ]
    )
    return "\n".join(lines)


def render_summary_tables(
    integrated_theme_rows: list[dict[str, str]],
    question_totals: list[dict[str, str]],
    matrix_rows: list[dict[str, str]],
    evidence_mix_rows: list[dict[str, str]],
    case_prominence_rows: list[dict[str, str]],
    case_packages: dict[str, dict[str, Any]],
) -> str:
    """Render the integrated summary-tables markdown."""
    lines = [
        "# Integrated D1-D4 Summary Tables",
        "",
        "## Table 1. Integrated theme overview",
        "",
    ]
    lines.extend(
        _table(
            integrated_theme_rows,
            [
                "integrated_theme_id",
                "integrated_theme",
                "cases_present",
                "aggregated_participant_segments",
                "aggregated_unique_speakers",
                "aggregated_unique_tables",
                "questions_present",
                "dominant_salience_pattern",
            ],
        )
    )
    lines.extend(["", "## Table 2. Cross-case question evidence summary", ""])
    lines.extend(
        _table(
            question_totals,
            [
                "question_id",
                "participant_segments",
                "moderator_segments",
                "unclear_segments",
                "summed_unique_participant_speakers",
            ],
        )
    )
    lines.extend(["", "## Table 3. Cross-case question × integrated theme matrix", ""])
    lines.extend(
        _table(
            matrix_rows,
            [
                "question_id",
                "IT1_segments",
                "IT2_segments",
                "IT3_segments",
                "IT4_segments",
                "IT1_case_presence",
                "IT2_case_presence",
                "IT3_case_presence",
                "IT4_case_presence",
            ],
        )
    )
    lines.extend(["", "## Table 4. Evidence-layer mix by case", ""])
    lines.extend(
        _table(
            evidence_mix_rows,
            [
                "case_id",
                "excerpt_rows",
                "verbatim_transcript",
                "note_style_transcript_summary",
                "note_taker_summary",
                "participant_rows",
                "unclear_rows",
                "close_reading_rows",
            ],
        )
    )
    lines.extend(["", "## Table 5. Case salience comparison", ""])
    lines.extend(
        _table(
            case_prominence_rows,
            [
                "case_id",
                "integrated_theme_id",
                "participant_segments",
                "unique_speakers",
                "unique_tables",
                "salience",
            ],
        )
    )
    limitation_rows = []
    for case_id, package in case_packages.items():
        for limitation in package["config"]["limitations"]:
            limitation_rows.append({"case_id": case_id, "limitation": limitation})
    lines.extend(["", "## Table 6. Case-specific limitation carry-through", ""])
    lines.extend(_table(limitation_rows, ["case_id", "limitation"]))
    return "\n".join(lines)


def render_visuals(
    matrix_rows: list[dict[str, str]],
    case_prominence_rows: list[dict[str, str]],
    evidence_mix_rows: list[dict[str, str]],
    question_totals: list[dict[str, str]],
) -> str:
    """Render chart-ready visual and table content."""
    heatmap_rows = []
    for row in matrix_rows:
        heatmap_rows.append(
            {
                "question_id": row["question_id"],
                "IT1_density": _density_label(int(row["IT1_segments"])),
                "IT2_density": _density_label(int(row["IT2_segments"])),
                "IT3_density": _density_label(int(row["IT3_segments"])),
                "IT4_density": _density_label(int(row["IT4_segments"])),
            }
        )
    lines = [
        "# Integrated D1-D4 Visuals and Chart-Ready Tables",
        "",
        "## Visual 1. Theme prominence by case",
        "Use the following table for a grouped bar chart comparing the four aligned integrated themes across D1-D4.",
        "",
    ]
    lines.extend(_table(case_prominence_rows, ["case_id", "integrated_theme_id", "participant_segments", "salience"]))
    lines.extend(["", "## Visual 2. Question burden across the integrated corpus", "Use the following table for a bar chart of participant-segment density by question.", ""])
    lines.extend(_table(question_totals, ["question_id", "participant_segments", "summed_unique_participant_speakers"]))
    lines.extend(["", "## Visual 3. Question × integrated-theme heatmap key", "The density labels below are chart-ready simplifications of the numeric matrix.", ""])
    lines.extend(_table(heatmap_rows, ["question_id", "IT1_density", "IT2_density", "IT3_density", "IT4_density"]))
    lines.extend(["", "## Visual 4. Evidence-layer composition by case", "Use the following table for a stacked bar chart showing how much of each outward-facing evidence layer enters the integrated synthesis.", ""])
    lines.extend(
        _table(
            evidence_mix_rows,
            [
                "case_id",
                "verbatim_transcript",
                "note_style_transcript_summary",
                "note_taker_summary",
                "unclear_rows",
                "close_reading_rows",
            ],
        )
    )
    return "\n".join(lines)


def _table(rows: list[dict[str, str]], columns: list[str]) -> list[str]:
    if not rows:
        return ["No rows."]
    header = "| " + " | ".join(columns) + " |"
    divider = "| " + " | ".join(["---"] * len(columns)) + " |"
    body = ["| " + " | ".join(row.get(column, "") for column in columns) + " |" for row in rows]
    return [header, divider, *body]


def _density_label(value: int) -> str:
    if value >= 60:
        return "very_high"
    if value >= 30:
        return "high"
    if value >= 10:
        return "moderate"
    if value > 0:
        return "low"
    return "none"
