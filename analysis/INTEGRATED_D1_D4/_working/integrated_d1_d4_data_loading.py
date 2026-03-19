from __future__ import annotations

import csv
from pathlib import Path
from typing import Any

from integrated_d1_d4_constants import CASES


def load_case_packages() -> dict[str, dict[str, Any]]:
    """Load the approved outward-facing D1-D4 case packages.

    Returns:
        A dictionary keyed by case ID containing structured CSV rows and core
        outward-facing markdown text needed for integrated synthesis.
    """
    packages: dict[str, dict[str, Any]] = {}
    for case_id, config in CASES.items():
        package_dir = Path(config["package_dir"])
        coded_segments_path = package_dir / f"{case_id}_coded_segments.csv"
        packages[case_id] = {
            "config": config,
            "package_dir": package_dir,
            "coded_segments": _read_csv(coded_segments_path) if coded_segments_path.exists() else [],
            "theme_summary": _read_csv(package_dir / config["theme_summary_file"]),
            "question_evidence": _read_csv(package_dir / config["question_evidence_file"]),
            "question_matrix": _read_csv(package_dir / config["question_matrix_file"]),
            "prominence": _read_csv(package_dir / config["prominence_file"]),
            "excerpt_bank": _read_csv(package_dir / config["excerpt_file"]),
            "participant_summary": _read_csv(package_dir / config["participant_summary_file"]),
            "participant_register": _read_csv(package_dir / config["participant_register_file"]),
            "report_text": (package_dir / config["report_file"]).read_text(encoding="utf-8"),
            "themes_text": (package_dir / config["themes_file"]).read_text(encoding="utf-8"),
            "crosscheck_text": (package_dir / config["crosscheck_file"]).read_text(encoding="utf-8"),
        }
    return packages


def _read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))
