import math

import numpy as np
import pytest

from paper.solver.canonical_cpu.evidence import (
    build_case_plan,
    compute_observables,
    evidence_suite_metadata,
    ensure_output_dir,
    oscillation_summary,
    select_reference_case,
)
from paper.solver.canonical_cpu.solver import CanonicalParams


def test_oscillation_summary_recovers_period_and_cycle_count_for_sine_wave():
    t = np.linspace(0.0, 20.0, 2001)
    y = 2.0 + 0.4 * np.sin(2.0 * np.pi * t / 2.5)

    summary = oscillation_summary(t, y, tail_fraction=0.5, min_amplitude=0.05)

    assert summary["is_oscillatory"] is True
    assert summary["complete_cycles"] >= 3
    assert math.isclose(summary["period"], 2.5, rel_tol=0.03)
    assert math.isclose(summary["amplitude"], 0.8, rel_tol=0.05)


def test_compute_observables_reports_skin_thickness_and_barrier_suppression():
    p = CanonicalParams(N=5, J_init=1.3)
    x = np.linspace(0.1, 0.9, 5)
    J = np.array(
        [
            [1.30, 1.30],
            [1.24, 1.24],
            [1.18, 1.18],
            [1.05, 1.05],
            [0.90, 0.90],
        ]
    )
    theta = np.zeros_like(J)
    u = np.ones_like(J) * 0.5
    data = {
        "x": x,
        "t": np.array([0.0, 1.0]),
        "J": J,
        "W": J * u,
        "u": u,
        "theta": theta,
        "success": True,
        "message": "synthetic",
        "status": 0,
        "nfev": 0,
        "njev": 0,
        "nlu": 0,
        "jac_color_groups": 0,
        "model_branches": {},
    }

    obs = compute_observables(data, p)

    assert obs["definitions"]["collapse_threshold"]["J_threshold"] == 0.9 * p.J_init
    assert obs["summary"]["max_collapsed_skin_thickness"] > 0.0
    assert obs["summary"]["min_accessibility"] <= obs["summary"]["mean_accessibility"]
    assert obs["summary"]["max_barrier_suppression_A"] >= 0.0


def test_select_reference_case_prefers_oscillatory_clipping_free_candidate():
    rows = [
        {"case_id": "steady", "oscillatory": False, "clipping_total": 0, "theta_amplitude": 0.1},
        {"case_id": "clipped_osc", "oscillatory": True, "clipping_total": 4, "theta_amplitude": 2.0},
        {"case_id": "clean_osc", "oscillatory": True, "clipping_total": 0, "theta_amplitude": 0.5},
    ]

    selected = select_reference_case(rows)

    assert selected["case_id"] == "clean_osc"
    assert selected["selection_reason"] == "oscillatory_clipping_free"


def test_build_case_plan_contains_required_controls_and_skipped_unavailable_controls():
    plan = build_case_plan()
    case_ids = {case["case_id"] for case in plan["cases"]}

    assert "baseline_default" in case_ids
    assert "control_no_reaction" in case_ids
    assert "control_no_lcst" in case_ids
    assert "control_no_barrier" in case_ids
    assert "sensitivity_current_volume_source" in case_ids
    assert "sensitivity_strict_chi" in case_ids
    assert "control_no_accessibility_barrier" in plan["skipped_controls"]
    assert "control_no_diffusivity_mobility_barrier" in plan["skipped_controls"]


def test_evidence_suite_metadata_records_driver_hashes_and_outdir():
    metadata = evidence_suite_metadata("results/evidence_convergence_control")

    assert metadata["command"] == "python -m paper.solver.canonical_cpu.run_evidence_checks"
    assert metadata["outdir"] == "results/evidence_convergence_control"
    assert metadata["runtime"]["scipy"]
    assert metadata["source_file_sha256"]["paper/solver/canonical_cpu/evidence.py"]
    assert metadata["source_file_sha256"][
        "paper/solver/canonical_cpu/run_evidence_checks.py"
    ]


def test_ensure_output_dir_requires_overwrite_for_existing_outputs(tmp_path):
    outdir = tmp_path / "evidence"
    outdir.mkdir()
    (outdir / "suite_summary.json").write_text("{}", encoding="utf-8")

    with pytest.raises(FileExistsError):
        ensure_output_dir(outdir, overwrite=False)

    ensure_output_dir(outdir, overwrite=True)

    assert outdir.exists()
    assert not (outdir / "suite_summary.json").exists()
