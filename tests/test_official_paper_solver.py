from pathlib import Path

import numpy as np

from paper.solver import official_paper_solver as official
from paper.solver.run_figure_smoke_checks import (
    FIGURE_SMOKE_CASES,
    run_figure_smoke_suite,
)


ROOT = Path(__file__).resolve().parents[1]


def test_official_paper_solver_routes_to_migrated_scan_optimized_module():
    assert official.OFFICIAL_SOLVER_SOURCE.name == "scan_optimized.py"
    assert official.OFFICIAL_SOLVER_SOURCE.as_posix().endswith(
        "paper/solver/paper_latest_cpu/scan_optimized.py"
    )
    assert official.Params.__module__ == "paper.solver.paper_latest_cpu.scan_optimized"
    assert official.simulate.__module__ == "paper.solver.paper_latest_cpu.scan_optimized"


def test_official_solver_provenance_records_scan_optimized_source_hash():
    provenance = official.solver_provenance()

    assert provenance["solver_basename"] == "scan_optimized.py"
    assert provenance["module"] == "paper.solver.paper_latest_cpu.scan_optimized"
    assert len(provenance["sha256"]) == 64
    assert provenance["validation_status"] == "smoke_only_not_validation"


def test_default_figure_smoke_cases_cover_issue_targets():
    by_id = {case["figure_id"]: case for case in FIGURE_SMOKE_CASES}

    assert set(by_id) == {"fig01", "fig02", "fig03", "fig09"}
    assert by_id["fig01"]["artifact_kind"] == "reduced_scan_table"
    assert by_id["fig02"]["artifact_kind"] == "working_point_timeseries"
    assert by_id["fig03"]["artifact_kind"] == "derived_profile_npz"
    assert by_id["fig09"]["artifact_kind"] == "spinodal_like_field_npz"


def test_figure_smoke_suite_writes_artifact_using_scan_optimized(tmp_path):
    summary = run_figure_smoke_suite(tmp_path, figure_ids=("fig02",))

    assert summary["status"] == "completed"
    assert summary["validation_status"] == "smoke_only_not_validation"
    assert summary["official_solver"]["solver_basename"] == "scan_optimized.py"
    assert len(summary["runs"]) == 1
    row = summary["runs"][0]
    assert row["figure_id"] == "fig02"
    assert row["invoked_solver_basename"] == "scan_optimized.py"
    assert row["artifact_kind"] == "working_point_timeseries"
    artifact = Path(row["artifact"])
    assert artifact.exists()
    with np.load(artifact) as data:
        assert {"x", "t", "J", "u", "theta"}.issubset(set(data.files))


def test_canonical_cpu_readme_no_longer_claims_to_be_official_final_path():
    readme = (ROOT / "paper/solver/canonical_cpu/README.md").read_text(encoding="utf-8")

    assert "Status: superseded by scan_optimized.py for official paper reproduction" in readme
    assert "paper.solver.official_paper_solver" in readme
