from __future__ import annotations

from pathlib import Path

from integrated_d1_d4_build_helpers import (
    build_case_prominence_rows,
    build_evidence_mix_rows,
    build_integrated_matrix_rows,
    build_integrated_theme_rows,
    build_participant_master_rows,
    build_question_totals,
    build_question_workbook_sheets,
    build_quote_lookup,
    build_theme_workbook_sheets,
    copy_to_outward,
    load_case_packages,
    prepare_output_dirs,
    scan_output_paths,
    write_internal_markdown,
    write_workbook,
)
from integrated_d1_d4_constants import INTERNAL_FILES, OUTPUT_FILES, OUTWARD_PACKAGE_FILENAMES
from integrated_d1_d4_renderers import (
    render_build_note,
    render_crosscheck,
    render_methodology,
    render_report,
    render_source_manifest,
    render_summary_tables,
    render_synthesis_memo,
    render_visuals,
)


def write_markdown(path: Path, content: str) -> None:
    """Write markdown content to disk.

    Args:
        path: Destination file path.
        content: Markdown content.

    Returns:
        None. Writes the markdown file to disk.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")



def build_participant_workbook_rows(case_packages: dict[str, dict[str, object]]) -> dict[str, list[dict[str, str]]]:
    """Build the participant workbook sheet mapping.

    Args:
        case_packages: Loaded outward-facing case package data.

    Returns:
        Sheet mapping for the integrated participant workbook.
    """
    quote_lookup = build_quote_lookup(case_packages)
    participant_rows = build_participant_master_rows(case_packages, quote_lookup)
    participant_rows = sorted(
        participant_rows,
        key=lambda row: (row["case_id"], row["participant_id"]),
    )
    sheets: dict[str, list[dict[str, str]]] = {"Participants_Master": participant_rows}
    for case_id in sorted(case_packages):
        sheets[f"{case_id}_Participants"] = [
            row for row in participant_rows if row["case_id"] == case_id
        ]
    return sheets



def sort_sheet_rows(sheets: dict[str, list[dict[str, str]]], sort_keys: list[str]) -> dict[str, list[dict[str, str]]]:
    """Sort workbook sheet rows by common keys where present.

    Args:
        sheets: Workbook sheet mapping.
        sort_keys: Candidate row keys used for sorting.

    Returns:
        A new workbook sheet mapping with sorted rows.
    """
    sorted_sheets: dict[str, list[dict[str, str]]] = {}
    for sheet_name, rows in sheets.items():
        if not rows:
            sorted_sheets[sheet_name] = rows
            continue
        applicable_keys = [key for key in sort_keys if key in rows[0]]
        sorted_sheets[sheet_name] = sorted(
            rows,
            key=lambda row: tuple(row[key] for key in applicable_keys),
        )
    return sorted_sheets



def build_outputs() -> list[Path]:
    """Build the full integrated D1-D4 output layer.

    Returns:
        The list of outward-facing integrated output paths.
    """
    case_packages = load_case_packages()
    integrated_theme_rows = build_integrated_theme_rows(case_packages)
    question_totals = build_question_totals(case_packages)
    matrix_rows = build_integrated_matrix_rows(case_packages)
    evidence_mix_rows = build_evidence_mix_rows(case_packages)
    case_prominence_rows = build_case_prominence_rows(case_packages)
    quote_lookup = build_quote_lookup(case_packages)

    methodology = render_methodology(
        case_packages=case_packages,
        integrated_theme_rows=integrated_theme_rows,
        evidence_mix_rows=evidence_mix_rows,
    )
    synthesis_memo = render_synthesis_memo(
        case_packages=case_packages,
        integrated_theme_rows=integrated_theme_rows,
        question_totals=question_totals,
    )
    summary_tables = render_summary_tables(
        integrated_theme_rows=integrated_theme_rows,
        question_totals=question_totals,
        matrix_rows=matrix_rows,
        evidence_mix_rows=evidence_mix_rows,
        case_prominence_rows=case_prominence_rows,
        case_packages=case_packages,
    )
    visuals = render_visuals(
        matrix_rows=matrix_rows,
        case_prominence_rows=case_prominence_rows,
        evidence_mix_rows=evidence_mix_rows,
        question_totals=question_totals,
    )
    report = render_report(
        case_packages=case_packages,
        question_totals=question_totals,
        matrix_rows=matrix_rows,
        quote_lookup=quote_lookup,
    )

    write_markdown(OUTPUT_FILES["methodology"], methodology)
    write_markdown(OUTPUT_FILES["synthesis_memo"], synthesis_memo)
    write_markdown(OUTPUT_FILES["summary_tables"], summary_tables)
    write_markdown(OUTPUT_FILES["visuals"], visuals)
    write_markdown(OUTPUT_FILES["report"], report)

    question_sheets = sort_sheet_rows(
        build_question_workbook_sheets(case_packages),
        ["question_id", "case_id", "quotation_reference"],
    )
    theme_sheets = sort_sheet_rows(
        build_theme_workbook_sheets(case_packages),
        ["theme_name", "case_id", "excerpt_reference"],
    )
    participant_sheets = build_participant_workbook_rows(case_packages)

    write_workbook(OUTPUT_FILES["question_workbook"], question_sheets)
    write_workbook(OUTPUT_FILES["theme_workbook"], theme_sheets)
    write_workbook(OUTPUT_FILES["participant_workbook"], participant_sheets)

    outward_output_paths = [OUTPUT_FILES[key] for key in [
        "report",
        "methodology",
        "synthesis_memo",
        "summary_tables",
        "visuals",
        "question_workbook",
        "theme_workbook",
        "participant_workbook",
    ]]
    preliminary_scan_hits = scan_output_paths(outward_output_paths)
    crosscheck = render_crosscheck(
        output_paths=outward_output_paths + [OUTPUT_FILES["crosscheck"]],
        scan_hits=preliminary_scan_hits,
        integrated_theme_rows=integrated_theme_rows,
        question_totals=question_totals,
    )
    write_markdown(OUTPUT_FILES["crosscheck"], crosscheck)

    write_internal_markdown(
        INTERNAL_FILES["source_manifest"],
        render_source_manifest(case_packages),
    )
    write_internal_markdown(
        INTERNAL_FILES["build_note"],
        render_build_note(),
    )

    return [OUTPUT_FILES[name] for name in [
        "report",
        "methodology",
        "synthesis_memo",
        "summary_tables",
        "visuals",
        "question_workbook",
        "theme_workbook",
        "participant_workbook",
        "crosscheck",
    ]]



def validate_output_inventory(output_paths: list[Path]) -> None:
    """Validate the final outward-facing output inventory.

    Args:
        output_paths: Built outward-facing integrated output paths.

    Returns:
        None. Raises `ValueError` if the inventory is incomplete.
    """
    actual_names = {path.name for path in output_paths}
    expected_names = set(OUTWARD_PACKAGE_FILENAMES)
    if actual_names != expected_names:
        missing = sorted(expected_names - actual_names)
        extra = sorted(actual_names - expected_names)
        raise ValueError(f"Integrated outward inventory mismatch. missing={missing} extra={extra}")



def main() -> None:
    """Build and package the integrated D1-D4 synthesis outputs.

    Returns:
        None. Writes the integrated outputs, workbooks, and package folders.
    """
    prepare_output_dirs()
    output_paths = build_outputs()
    validate_output_inventory(output_paths)
    copy_to_outward(output_paths)



if __name__ == "__main__":
    main()
