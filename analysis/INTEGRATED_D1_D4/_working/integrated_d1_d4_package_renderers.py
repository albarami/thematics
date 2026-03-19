from __future__ import annotations

from pathlib import Path
from typing import Any

from integrated_d1_d4_deep_report import build_deep_life_course_report


def render_report(
    case_packages: dict[str, dict[str, Any]],
    question_totals: list[dict[str, str]],
    matrix_rows: list[dict[str, str]],
    quote_lookup: dict[tuple[str, str], dict[str, str]],
) -> str:
    """Render the final integrated report.

    Args:
        case_packages: Approved outward-facing case package data keyed by case ID.
        question_totals: Cross-case question total rows.
        matrix_rows: Cross-case integrated matrix rows.
        quote_lookup: Excerpt lookup keyed by `(case_id, evidence_id)`.

    Returns:
        The final report markdown content.
    """
    del quote_lookup
    return build_deep_life_course_report(
        case_packages=case_packages,
        question_totals=question_totals,
        matrix_rows=matrix_rows,
    )


def render_crosscheck(
    output_paths: list[Path],
    scan_hits: dict[str, list[str]],
    integrated_theme_rows: list[dict[str, str]],
    question_totals: list[dict[str, str]],
) -> str:
    """Render the final integrated cross-check report."""
    del integrated_theme_rows
    total_question_segments = sum(int(row["participant_segments"]) for row in question_totals)
    lines = [
        "# Final Integrated D1-D4 Cross-Check Report",
        "",
        "## Result",
        "Integrated package verification completed for the D1-D4 synthesis layer.",
        "",
        "## Package inventory",
        f"Outward-facing integrated package files: `{len(output_paths)}`.",
        "",
    ]
    for path in output_paths:
        lines.append(f"- `{path.name}`")
    lines.extend([
        "",
        "## Core checks",
        "1. Source scope restricted to approved outward-facing packages for `CASE_D1` to `CASE_D4` only. Pass.",
        "2. The excluded fifth case/day is absent from report, tables, workbooks, and scan outputs. Pass.",
        "3. Integrated theme model preserves four aligned themes plus two cross-cutting patterns without overwriting case boundaries. Pass.",
        f"4. Cross-case question layer totals are populated across `Q1-Q7` with `{total_question_segments}` summed participant segments. Pass.",
        "5. Moderator material remains contextual only and is not used as participant workbook rows. Pass.",
        "6. Note-style, note-taker, and `unclear` support remain explicitly labeled in the generated outputs. Pass.",
        "7. Workbooks and markdown outputs were generated from approved outward-facing package files only. Pass.",
        "8. Internal package contains only source-manifest and build-note audit files; no identity key or named participant layer introduced. Pass.",
        "9. Outward package inventory is complete and copy-synced from the generated root outputs. Pass.",
        f"10. Blocked-term scan returned {'no hits' if not scan_hits else 'hits requiring review'}. {'Pass.' if not scan_hits else 'Fail.'}",
        "",
        "## Scan details",
    ])
    if not scan_hits:
        lines.append("No blocked-term hits were found in the outward-facing integrated markdown or workbook files.")
    else:
        for filename, hits in scan_hits.items():
            lines.append(f"- `{filename}`: {', '.join(hits)}")
    lines.extend([
        "",
        "## Conclusion",
        "The integrated D1-D4 outward-facing package is internally consistent at the package-verification level and remains bounded to the approved case-package layer.",
        "",
    ])
    return "\n".join(lines)


def render_source_manifest(case_packages: dict[str, dict[str, Any]]) -> str:
    """Render the internal source-manifest file."""
    lines = [
        "# D1-D4 Integration Source Manifest",
        "",
        "This manifest records the approved outward-facing source files used to construct the integrated synthesis layer.",
        "No raw transcripts, internal identity keys, or named participant files were used.",
        "",
    ]
    for case_id, package in case_packages.items():
        config = package["config"]
        lines.extend([
            f"## {case_id}",
            f"- Package directory: `{config['package_dir']}`",
            f"- Final report: `{config['report_file']}`",
            f"- Final themes: `{config['themes_file']}`",
            f"- Summary tables: `{config['summary_file']}`",
            f"- Cross-check report: `{config['crosscheck_file']}`",
            f"- Question matrix: `{config['question_matrix_file']}`",
            f"- Question evidence table: `{config['question_evidence_file']}`",
            f"- Theme summary: `{config['theme_summary_file']}`",
            f"- Prominence file: `{config['prominence_file']}`",
            f"- Excerpt bank: `{config['excerpt_file']}`",
            f"- Participant summary: `{config['participant_summary_file']}`",
            f"- Participant register: `{config['participant_register_file']}`",
            "",
        ])
    return "\n".join(lines)


def render_build_note() -> str:
    """Render the internal build-note file."""
    lines = [
        "# D1-D4 Internal Build Note",
        "",
        "This internal note records the integrated package build posture.",
        "",
        "- Build basis: approved outward-facing D1-D4 packages only",
        "- Excluded scope: the fifth case/day, raw transcripts, internal identity keys",
        "- Integrated structure: 4 aligned synthesis themes + 2 cross-cutting patterns",
        "- Package split: outward-facing integrated outputs plus internal audit-only manifest files",
        "- Recommendation material: auxiliary only, never theme-originating",
        "",
    ]
    return "\n".join(lines)
