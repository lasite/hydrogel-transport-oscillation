import json

import numpy as np

from paper.solver.canonical_cpu.root_cause import (
    _classify_root_causes,
    build_root_cause_case_plan,
    functional_barrier_flags,
    params_from_json,
    serializable_case_plan,
    shutdown_ratio,
    surface_skin_thickness,
)
from paper.solver.canonical_cpu.solver import dumps_strict_json
from paper.solver.canonical_cpu.solver import CanonicalParams


def test_functional_barrier_flags_do_not_treat_geometric_collapse_as_barrier():
    J = np.array([1.25, 1.20, 1.05, 0.95])
    A = np.array([0.95, 0.94, 0.93, 0.92])
    D_over_D0 = np.array([0.91, 0.90, 0.89, 0.88])
    M_over_M0 = np.array([0.96, 0.95, 0.94, 0.93])

    flags = functional_barrier_flags(A, D_over_D0, M_over_M0, threshold=0.5)

    assert not np.any(flags)
    assert surface_skin_thickness(flags, dx=0.25) == 0.0


def test_functional_barrier_skin_is_contiguous_from_free_surface():
    flags = np.array([True, False, True, True])

    assert surface_skin_thickness(flags, dx=0.25) == 0.5


def test_shutdown_ratio_compares_tail_or_postcollapse_level_to_initial_level():
    ratio = shutdown_ratio(np.array([10.0, 8.0]), np.array([2.0, 1.0]))

    assert ratio == 0.15


def test_params_from_json_filters_metadata_and_keeps_diagnostic_source_exponent(tmp_path):
    payload = {
        "N": 7,
        "Da": 1.5,
        "source_scaling": "diagnostic_J_beta",
        "source_J_exponent": 0.5,
        "model_branches": {"validation_status": "candidate_not_validated"},
        "solver": {"name": "canonical_cpu"},
    }
    path = tmp_path / "run_params.json"
    path.write_text(json.dumps(payload), encoding="utf-8")

    params = params_from_json(path)

    assert isinstance(params, CanonicalParams)
    assert params.N == 7
    assert params.Da == 1.5
    assert params.source_scaling == "diagnostic_J_beta"
    assert params.source_J_exponent == 0.5


def test_serializable_case_plan_removes_dataclass_params_from_json_summary():
    plan = serializable_case_plan(build_root_cause_case_plan())

    encoded = dumps_strict_json(plan)

    assert "diagnostic_accessibility_constant" in encoded
    assert "CanonicalParams" not in encoded


def test_root_cause_ranking_includes_contaminated_high_supply_near_loop_clue():
    rows = [
        {
            "case_id": "search_N31_Da1_BiT0p2",
            "classification_label": "steady_hot_nonuniform",
            "max_geometric_skin_thickness": 1.0,
            "max_functional_skin_thickness": 0.0,
            "min_A": 0.7,
            "min_D_over_D0": 0.9,
            "min_M_over_M0": 0.95,
            "source_shutdown_tail_over_global_peak": 0.99,
            "source_heat_loss_balance_tail": 1.0,
            "reactant_supply_source_balance_tail": 1.0,
        },
        {
            "case_id": "perturb_Bi_c_2",
            "oscillatory": True,
            "theta_complete_cycles": 3,
            "theta_amplitude": 2.0,
            "clipping_total": 299,
            "source_shutdown_tail_over_global_peak": 0.2,
            "max_functional_skin_thickness": 0.13,
        },
    ]

    _, ranked = _classify_root_causes(rows)
    encoded = dumps_strict_json(ranked)

    assert "perturb_Bi_c_2" in encoded
    assert "contaminated" in encoded
