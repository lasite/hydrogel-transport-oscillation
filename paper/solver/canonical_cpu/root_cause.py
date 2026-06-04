"""Root-cause diagnostics for missing oscillations in the canonical model.

This module is diagnostic-only. It adds no validated model claim and does not
change canonical solver defaults.
"""

from __future__ import annotations

import csv
import hashlib
import json
import math
import shutil
from dataclasses import asdict, fields, replace
from pathlib import Path
from typing import Any, Dict, Iterable

import numpy as np
import scipy

from .evidence import compute_observables, oscillation_summary
from .solver import (
    CanonicalParams,
    classify_run,
    conservation_diagnostics,
    dumps_strict_json,
    finalize_params,
    git_metadata,
    model_branch_labels,
    phi_from_J,
    save_run_bundle,
    simulate,
    solver_audit_diagnostics,
    state_fluxes,
)


ROOT = Path(__file__).resolve().parents[3]
EVIDENCE_ROOT = ROOT / "results/evidence_convergence_control"

EXISTING_CASES = [
    "baseline_default",
    "search_N31_Da1_BiT0p2",
    "search_N31_Da4_BiT0p2",
    "search_N31_Da8_BiT0p2",
    "control_no_reaction",
    "control_no_lcst",
    "control_no_barrier",
    "sensitivity_current_volume_source",
    "sensitivity_strict_chi",
]


def _finite_or_none(value: float) -> float | None:
    value = float(value)
    return value if math.isfinite(value) else None


def _mean_or_none(values: Iterable[float]) -> float | None:
    arr = np.asarray(list(values), dtype=float)
    finite = arr[np.isfinite(arr)]
    return float(np.mean(finite)) if finite.size else None


def _safe_div(num: float, den: float) -> float | None:
    if not math.isfinite(num) or not math.isfinite(den) or abs(den) < 1.0e-30:
        return None
    return float(num / den)


def _array_summary(values: np.ndarray) -> Dict[str, float | None]:
    arr = np.asarray(values, dtype=float)
    finite = arr[np.isfinite(arr)]
    if finite.size == 0:
        return {"min": None, "mean": None, "max": None}
    return {
        "min": float(np.min(finite)),
        "mean": float(np.mean(finite)),
        "max": float(np.max(finite)),
    }


def _tail_slice(n: int, fraction: float = 0.60) -> slice:
    return slice(max(0, int(fraction * n)), n)


def _early_slice(n: int, fraction: float = 0.20) -> slice:
    return slice(0, max(1, int(fraction * n)))


def params_from_json(path: str | Path) -> CanonicalParams:
    """Load a CanonicalParams object from a saved run_params.json file."""
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    names = {field.name for field in fields(CanonicalParams)}
    return CanonicalParams(**{key: payload[key] for key in names if key in payload})


def load_run_bundle(run_dir: str | Path) -> tuple[Dict[str, Any], CanonicalParams]:
    """Load arrays and parameters from an evidence/root-cause run directory."""
    run_dir = Path(run_dir)
    p = params_from_json(run_dir / "run_params.json")
    arrays = np.load(run_dir / "run_timeseries.npz")
    data: Dict[str, Any] = {key: arrays[key] for key in arrays.files}
    if "phi" not in data:
        data["phi"] = phi_from_J(data["J"], p)
    data.setdefault("success", True)
    data.setdefault("message", "loaded from saved run bundle")
    data.setdefault("status", 0)
    data.setdefault("nfev", -1)
    data.setdefault("njev", -1)
    data.setdefault("nlu", -1)
    data.setdefault("jac_color_groups", -1)
    data["model_branches"] = model_branch_labels(finalize_params(p))
    return data, p


def surface_skin_thickness(flags: np.ndarray, dx: float) -> float:
    """Return the contiguous flagged skin thickness measured from x=1 inward."""
    flags = np.asarray(flags, dtype=bool)
    count = 0
    for flag in flags[::-1]:
        if flag:
            count += 1
        else:
            break
    return float(count * dx)


def functional_barrier_flags(
    A: np.ndarray,
    D_over_D0: np.ndarray,
    M_over_M0: np.ndarray,
    threshold: float = 0.5,
) -> np.ndarray:
    """Cells where any functional closure is suppressed below threshold."""
    return (
        (np.asarray(A, dtype=float) < threshold)
        | (np.asarray(D_over_D0, dtype=float) < threshold)
        | (np.asarray(M_over_M0, dtype=float) < threshold)
    )


def shutdown_ratio(before: np.ndarray, after: np.ndarray) -> float | None:
    """Return mean(after) / max(before), using finite values only."""
    before = np.asarray(before, dtype=float)
    after = np.asarray(after, dtype=float)
    before = before[np.isfinite(before)]
    after = after[np.isfinite(after)]
    if before.size == 0 or after.size == 0:
        return None
    scale = float(np.max(np.abs(before)))
    if scale < 1.0e-30:
        return None
    return float(np.mean(after) / scale)


def _clipping_total(audit: Dict[str, Any]) -> int:
    keys = [
        "logJ_low_clip_count",
        "logJ_high_clip_count",
        "u_floor_clip_count",
        "phi_hard_ceiling_exceed_count",
        "arrh_exp_cap_hit_count",
        "nonfinite_source_count",
        "nonfinite_flux_count",
    ]
    return int(sum(int(audit.get(key, 0)) for key in keys))


def _time_at(t: np.ndarray, values: np.ndarray, mode: str) -> float | None:
    arr = np.asarray(values, dtype=float)
    finite = np.isfinite(arr)
    if not np.any(finite):
        return None
    idxs = np.where(finite)[0]
    local = arr[finite]
    idx = idxs[int(np.argmax(local) if mode == "max" else np.argmin(local))]
    return float(t[idx])


def _time_scale_from_variation(t: np.ndarray, values: np.ndarray) -> float | None:
    values = np.asarray(values, dtype=float)
    finite = np.isfinite(values)
    if np.count_nonzero(finite) < 3:
        return None
    tt = t[finite]
    yy = values[finite]
    variation = float(np.ptp(yy))
    if variation < 1.0e-12:
        return None
    rate = np.gradient(yy, tt)
    mean_rate = float(np.mean(np.abs(rate)))
    return _safe_div(variation, mean_rate)


def compute_mechanism_diagnostics(
    data: Dict[str, Any],
    p: CanonicalParams,
    functional_threshold: float = 0.5,
) -> Dict[str, Any]:
    """Compute budget, functional-barrier, and timescale diagnostics."""
    p = finalize_params(p)
    t = np.asarray(data["t"], dtype=float)
    x = np.asarray(data["x"], dtype=float)
    J = np.asarray(data["J"], dtype=float)
    W = np.asarray(data["W"], dtype=float)
    u = np.asarray(data["u"], dtype=float)
    theta = np.asarray(data["theta"], dtype=float)
    dx = 1.0 / p.N
    J_threshold = 0.9 * p.J_init

    rows: list[Dict[str, Any]] = []
    scatter_rows: list[Dict[str, Any]] = []

    for k, tk in enumerate(t):
        aux = state_fluxes(J[:, k], W[:, k], theta[:, k], p, dx)
        source = p.Da * aux["source_density"]
        phi = phi_from_J(J[:, k], p)
        A = aux["accessibility"]
        D_over_D0 = aux["D_ref"] / max(float(p.D0), 1.0e-30)
        M_over_M0 = aux["M_ref"] / max(float(p.M0), 1.0e-30)
        geom_flags = J[:, k] <= J_threshold
        func_flags = functional_barrier_flags(A, D_over_D0, M_over_M0, functional_threshold)
        A_flags = A < functional_threshold
        D_flags = D_over_D0 < functional_threshold
        M_flags = M_over_M0 < functional_threshold
        heat_inventory = float(np.sum(theta[:, k]) * dx)
        W_inventory = float(np.sum(W[:, k]) * dx)
        source_integral = float(np.sum(source) * dx)
        heat_loss_surface = float(aux["h"][-1])
        reactant_supply_surface = float(-aux["nflux"][-1])

        row = {
            "t": float(tk),
            "source_integral": source_integral,
            "heat_loss_surface": heat_loss_surface,
            "reactant_supply_surface": reactant_supply_surface,
            "reactant_inventory": W_inventory,
            "heat_inventory": heat_inventory,
            "J_min": float(np.min(J[:, k])),
            "J_mean": float(np.mean(J[:, k])),
            "J_max": float(np.max(J[:, k])),
            "phi_min": float(np.min(phi)),
            "phi_mean": float(np.mean(phi)),
            "phi_max": float(np.max(phi)),
            "theta_min": float(np.min(theta[:, k])),
            "theta_mean": float(np.mean(theta[:, k])),
            "theta_max": float(np.max(theta[:, k])),
            "u_min": float(np.min(u[:, k])),
            "u_mean": float(np.mean(u[:, k])),
            "u_max": float(np.max(u[:, k])),
            "A_min": float(np.min(A)),
            "A_mean": float(np.mean(A)),
            "A_max": float(np.max(A)),
            "D_over_D0_min": float(np.min(D_over_D0)),
            "D_over_D0_mean": float(np.mean(D_over_D0)),
            "D_over_D0_max": float(np.max(D_over_D0)),
            "M_over_M0_min": float(np.min(M_over_M0)),
            "M_over_M0_mean": float(np.mean(M_over_M0)),
            "M_over_M0_max": float(np.max(M_over_M0)),
            "geometric_skin_thickness": surface_skin_thickness(geom_flags, dx),
            "functional_skin_thickness": surface_skin_thickness(func_flags, dx),
            "A_functional_skin_thickness": surface_skin_thickness(A_flags, dx),
            "D_functional_skin_thickness": surface_skin_thickness(D_flags, dx),
            "M_functional_skin_thickness": surface_skin_thickness(M_flags, dx),
            "surface_q": float(aux["q"][-1]),
            "surface_n": float(aux["nflux"][-1]),
            "surface_h": heat_loss_surface,
            "mean_abs_internal_h": float(np.mean(np.abs(aux["h"][1:p.N])))
            if p.N > 1
            else 0.0,
        }
        rows.append(row)

        stride = max(1, p.N // 12)
        for i in range(0, p.N, stride):
            scatter_rows.append(
                {
                    "t": float(tk),
                    "x": float(x[i]),
                    "J": float(J[i, k]),
                    "phi": float(phi[i]),
                    "A": float(A[i]),
                    "D_over_D0": float(D_over_D0[i]),
                    "M_over_M0": float(M_over_M0[i]),
                    "geometric_collapsed": bool(geom_flags[i]),
                    "functional_barrier": bool(func_flags[i]),
                }
            )

    def arr(name: str) -> np.ndarray:
        return np.asarray([row[name] for row in rows], dtype=float)

    early = _early_slice(len(t))
    tail = _tail_slice(len(t))
    audit = data.get("audit_diagnostics") or solver_audit_diagnostics(data, p)
    conservation = data.get("conservation_diagnostics") or conservation_diagnostics(data, p)
    obs = compute_observables(data, p)
    theta_osc = oscillation_summary(t, arr("theta_mean"), min_amplitude=2.0e-3)
    J_osc = oscillation_summary(t, arr("J_mean"), min_amplitude=2.0e-4)

    phase_events = {
        "max_source": _time_at(t, arr("source_integral"), "max"),
        "max_temperature": _time_at(t, arr("theta_mean"), "max"),
        "min_swelling_J": _time_at(t, arr("J_mean"), "min"),
        "min_reactant_inventory": _time_at(t, arr("reactant_inventory"), "min"),
        "min_A": _time_at(t, arr("A_min"), "min"),
        "min_D_over_D0": _time_at(t, arr("D_over_D0_min"), "min"),
        "min_M_over_M0": _time_at(t, arr("M_over_M0_min"), "min"),
        "max_geometric_skin": _time_at(t, arr("geometric_skin_thickness"), "max"),
        "max_functional_skin": _time_at(t, arr("functional_skin_thickness"), "max"),
    }
    ordered_phase_events = [
        {"event": key, "t": val}
        for key, val in sorted(
            phase_events.items(),
            key=lambda item: float("inf") if item[1] is None else item[1],
        )
    ]

    tail_source = _mean_or_none(arr("source_integral")[tail])
    tail_heat_loss = _mean_or_none(arr("heat_loss_surface")[tail])
    tail_supply = _mean_or_none(arr("reactant_supply_surface")[tail])
    tail_heat_inventory = _mean_or_none(np.abs(arr("heat_inventory")[tail]))
    tail_W_inventory = _mean_or_none(arr("reactant_inventory")[tail])
    tail_A = arr("A_min")[tail]
    tail_D = arr("D_over_D0_min")[tail]
    tail_M = arr("M_over_M0_min")[tail]

    summary = {
        "classification_label": classify_run(data)["label"],
        "oscillatory": bool(theta_osc["is_oscillatory"] or J_osc["is_oscillatory"]),
        "theta_complete_cycles": int(theta_osc["complete_cycles"]),
        "theta_amplitude": theta_osc["amplitude"],
        "J_complete_cycles": int(J_osc["complete_cycles"]),
        "J_amplitude": J_osc["amplitude"],
        "clipping_total": _clipping_total(audit),
        "nonfinite_total": int(
            audit.get("nonfinite_J_count", 0)
            + audit.get("nonfinite_W_count", 0)
            + audit.get("nonfinite_u_count", 0)
            + audit.get("nonfinite_theta_count", 0)
            + audit.get("nonfinite_source_count", 0)
            + audit.get("nonfinite_flux_count", 0)
        ),
        "source_shutdown_tail_over_early_peak": shutdown_ratio(
            arr("source_integral")[early],
            arr("source_integral")[tail],
        ),
        "source_shutdown_tail_over_global_peak": _safe_div(
            float(np.mean(arr("source_integral")[tail])),
            float(np.max(arr("source_integral"))),
        ),
        "A_shutdown_tail_over_early_peak": shutdown_ratio(arr("A_min")[early], tail_A),
        "D_shutdown_tail_over_early_peak": shutdown_ratio(
            arr("D_over_D0_min")[early],
            tail_D,
        ),
        "M_shutdown_tail_over_early_peak": shutdown_ratio(
            arr("M_over_M0_min")[early],
            tail_M,
        ),
        "source_heat_loss_balance_tail": _safe_div(tail_source or 0.0, tail_heat_loss or 0.0),
        "reactant_supply_source_balance_tail": _safe_div(tail_supply or 0.0, tail_source or 0.0),
        "source_tail_mean": tail_source,
        "heat_loss_tail_mean": tail_heat_loss,
        "reactant_supply_tail_mean": tail_supply,
        "heat_inventory_tail_mean_abs": tail_heat_inventory,
        "reactant_inventory_tail_mean": tail_W_inventory,
        "heating_time_tail_estimate": _safe_div(tail_heat_inventory or 0.0, tail_source or 0.0),
        "thermal_loss_time_tail_estimate": _safe_div(
            tail_heat_inventory or 0.0,
            tail_heat_loss or 0.0,
        ),
        "reactant_replenishment_time_tail_estimate": _safe_div(
            tail_W_inventory or 0.0,
            tail_supply or 0.0,
        ),
        "reactant_consumption_time_tail_estimate": _safe_div(
            tail_W_inventory or 0.0,
            tail_source or 0.0,
        ),
        "swelling_change_time_estimate": _time_scale_from_variation(t[tail], arr("J_mean")[tail]),
        "barrier_change_time_estimate": _time_scale_from_variation(t[tail], arr("A_min")[tail]),
        "max_geometric_skin_thickness": float(np.max(arr("geometric_skin_thickness"))),
        "max_functional_skin_thickness": float(np.max(arr("functional_skin_thickness"))),
        "max_A_functional_skin_thickness": float(np.max(arr("A_functional_skin_thickness"))),
        "max_D_functional_skin_thickness": float(np.max(arr("D_functional_skin_thickness"))),
        "max_M_functional_skin_thickness": float(np.max(arr("M_functional_skin_thickness"))),
        "min_A": float(np.min(arr("A_min"))),
        "min_D_over_D0": float(np.min(arr("D_over_D0_min"))),
        "min_M_over_M0": float(np.min(arr("M_over_M0_min"))),
        "geometry_overstates_functional_barrier": bool(
            np.max(arr("geometric_skin_thickness"))
            > np.max(arr("functional_skin_thickness")) + dx
        ),
        "reactant_balance_residual": conservation["reactant_balance_residual"],
        "heat_balance_residual": conservation["heat_balance_residual"],
        "phase_events": phase_events,
        "ordered_phase_events": ordered_phase_events,
        "surface_flux_stats": {
            "q": _array_summary(arr("surface_q")),
            "n": _array_summary(arr("surface_n")),
            "h": _array_summary(arr("surface_h")),
            "inward_reactant_supply": _array_summary(arr("reactant_supply_surface")),
        },
        "evidence_observable_summary": obs["summary"],
    }
    return {"series": rows, "scatter": scatter_rows, "summary": summary}


def root_cause_source_file_hashes(root: Path | None = None) -> Dict[str, str | None]:
    root = root or ROOT
    paths = [
        "paper/solver/canonical_cpu/solver.py",
        "paper/solver/canonical_cpu/evidence.py",
        "paper/solver/canonical_cpu/root_cause.py",
        "paper/solver/canonical_cpu/run_root_cause_checks.py",
        "tests/test_canonical_solver.py",
        "tests/test_evidence_observables.py",
        "tests/test_root_cause_diagnostics.py",
    ]
    hashes: Dict[str, str | None] = {}
    for rel in paths:
        path = root / rel
        hashes[rel] = hashlib.sha256(path.read_bytes()).hexdigest() if path.exists() else None
    return hashes


def root_cause_suite_metadata(outdir: str | Path) -> Dict[str, Any]:
    return {
        "command": "python -m paper.solver.canonical_cpu.run_root_cause_checks",
        "outdir": str(outdir),
        "runtime": {
            "numpy": np.__version__,
            "scipy": scipy.__version__,
        },
        "git": git_metadata(ROOT),
        "source_file_sha256": root_cause_source_file_hashes(ROOT),
        "status": "diagnostic_only_not_claim_evidence",
    }


def build_root_cause_case_plan() -> Dict[str, Any]:
    """Return bounded diagnostic cases around the #16 selected reference."""
    base = CanonicalParams(N=31, t_end=120.0, n_save=601, max_step=0.2, Da=1.0, Bi_T=0.2)
    cases = [
        {
            "case_id": "diagnostic_accessibility_constant",
            "group": "mechanism_isolation",
            "params": replace(base, transport_closure="accessibility_constant"),
            "purpose": "Set A(phi)=1 while retaining D/M suppression.",
        },
        {
            "case_id": "diagnostic_transport_constant",
            "group": "mechanism_isolation",
            "params": replace(base, transport_closure="transport_constant"),
            "purpose": "Set D/M constant while retaining A(phi).",
        },
        {
            "case_id": "diagnostic_diffusivity_constant",
            "group": "mechanism_isolation",
            "params": replace(base, transport_closure="diffusivity_constant"),
            "purpose": "Set D constant while retaining A(phi) and M suppression.",
        },
        {
            "case_id": "diagnostic_mobility_constant",
            "group": "mechanism_isolation",
            "params": replace(base, transport_closure="mobility_constant"),
            "purpose": "Set M constant while retaining A(phi) and D suppression.",
        },
        {
            "case_id": "diagnostic_source_beta_0",
            "group": "source_scaling",
            "params": replace(
                base,
                source_scaling="diagnostic_J_beta",
                source_J_exponent=0.0,
            ),
            "purpose": "Diagnostic S_R = J^0 R source scaling.",
        },
        {
            "case_id": "diagnostic_source_beta_0p5",
            "group": "source_scaling",
            "params": replace(
                base,
                source_scaling="diagnostic_J_beta",
                source_J_exponent=0.5,
            ),
            "purpose": "Diagnostic S_R = J^0.5 R source scaling.",
        },
        {
            "case_id": "diagnostic_source_beta_1",
            "group": "source_scaling",
            "params": replace(
                base,
                source_scaling="diagnostic_J_beta",
                source_J_exponent=1.0,
            ),
            "purpose": "Diagnostic S_R = J^1 R source scaling.",
        },
        {
            "case_id": "perturb_m_act_12",
            "group": "local_perturbation",
            "params": replace(base, m_act=12.0),
            "purpose": "Strengthen reaction accessibility suppression.",
        },
        {
            "case_id": "perturb_m_diff_6",
            "group": "local_perturbation",
            "params": replace(base, m_diff=6.0),
            "purpose": "Strengthen solute diffusivity suppression.",
        },
        {
            "case_id": "perturb_m_mob_4",
            "group": "local_perturbation",
            "params": replace(base, m_mob=4.0),
            "purpose": "Strengthen solvent mobility suppression.",
        },
        {
            "case_id": "perturb_A_min_1e_minus_6",
            "group": "local_perturbation",
            "params": replace(base, A_min=1.0e-6),
            "purpose": "Lower accessibility floor.",
        },
        {
            "case_id": "perturb_D_min_1e_minus_6",
            "group": "local_perturbation",
            "params": replace(base, D_min=1.0e-6),
            "purpose": "Lower diffusivity floor.",
        },
        {
            "case_id": "perturb_M_min_1e_minus_6",
            "group": "local_perturbation",
            "params": replace(base, M_min=1.0e-6),
            "purpose": "Lower mobility floor.",
        },
        {
            "case_id": "perturb_Bi_c_0p2",
            "group": "local_perturbation",
            "params": replace(base, Bi_c=0.2),
            "purpose": "Reduce surface reactant supply.",
        },
        {
            "case_id": "perturb_Bi_c_2",
            "group": "local_perturbation",
            "params": replace(base, Bi_c=2.0),
            "purpose": "Increase surface reactant supply.",
        },
        {
            "case_id": "perturb_Gamma_A_2p5",
            "group": "local_perturbation",
            "params": replace(base, Gamma_A=2.5),
            "purpose": "Increase Arrhenius temperature sensitivity.",
        },
        {
            "case_id": "perturb_S_chi_2",
            "group": "local_perturbation",
            "params": replace(base, S_chi=2.0),
            "purpose": "Increase LCST/osmotic temperature sensitivity.",
        },
        {
            "case_id": "perturb_Bi_T_0p05",
            "group": "local_perturbation",
            "params": replace(base, Bi_T=0.05),
            "purpose": "Reduce cooling to test heat-loss-limited reset.",
        },
        {
            "case_id": "perturb_Bi_T_0p5",
            "group": "local_perturbation",
            "params": replace(base, Bi_T=0.5),
            "purpose": "Increase cooling to test reset strength.",
        },
    ]
    return {
        "reference_case": "search_N31_Da1_BiT0p2",
        "base_params": {
            "N": base.N,
            "Da": base.Da,
            "Bi_T": base.Bi_T,
            "t_end": base.t_end,
            "n_save": base.n_save,
            "max_step": base.max_step,
        },
        "existing_cases": EXISTING_CASES,
        "new_cases": cases,
        "scope": "bounded diagnostic perturbations around the selected #16 reference",
    }


def serializable_case_plan(plan: Dict[str, Any]) -> Dict[str, Any]:
    """Return a strict-JSON-safe copy of a root-cause case plan."""
    safe = {key: value for key, value in plan.items() if key != "new_cases"}
    new_cases = []
    for case in plan.get("new_cases", []):
        p = finalize_params(case["params"])
        new_cases.append(
            {
                "case_id": case["case_id"],
                "group": case["group"],
                "purpose": case["purpose"],
                "params": {
                    key: value
                    for key, value in asdict(p).items()
                    if key
                    in {
                        "N",
                        "t_end",
                        "n_save",
                        "max_step",
                        "rtol",
                        "atol",
                        "Da",
                        "Bi_T",
                        "Bi_c",
                        "Gamma_A",
                        "S_chi",
                        "m_act",
                        "m_diff",
                        "m_mob",
                        "A_min",
                        "D_min",
                        "M_min",
                        "source_scaling",
                        "source_J_exponent",
                        "transport_closure",
                        "chi_closure",
                    }
                },
            }
        )
    safe["new_cases"] = new_cases
    return safe


def ensure_output_dir(outdir: Path, overwrite: bool = False) -> None:
    if outdir.exists() and any(outdir.iterdir()) and not overwrite:
        raise FileExistsError(
            f"{outdir} already contains root-cause outputs; pass --overwrite to replace them."
        )
    if outdir.exists() and overwrite:
        shutil.rmtree(outdir)
    outdir.mkdir(parents=True, exist_ok=True)


def write_rows_csv(path: Path, rows: list[Dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    keys: list[str] = []
    for row in rows:
        for key in row:
            if isinstance(row[key], (dict, list)):
                continue
            if key not in keys:
                keys.append(key)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=keys)
        writer.writeheader()
        for row in rows:
            writer.writerow({key: row.get(key) for key in keys})


def _flatten_summary(case_id: str, group: str, purpose: str, summary: Dict[str, Any]) -> Dict[str, Any]:
    row = {
        "case_id": case_id,
        "group": group,
        "purpose": purpose,
    }
    for key, value in summary.items():
        if isinstance(value, (str, int, float, bool)) or value is None:
            row[key] = value
    return row


def _write_case_outputs(
    run_dir: Path,
    case_id: str,
    group: str,
    purpose: str,
    data: Dict[str, Any],
    p: CanonicalParams,
    diagnostics: Dict[str, Any],
) -> Dict[str, Any]:
    run_dir.mkdir(parents=True, exist_ok=True)
    (run_dir / "mechanism_diagnostics.json").write_text(
        dumps_strict_json(diagnostics), encoding="utf-8"
    )
    write_rows_csv(run_dir / "mechanism_timeseries.csv", diagnostics["series"])
    return _flatten_summary(case_id, group, purpose, diagnostics["summary"])


def analyze_existing_case(case_id: str, outdir: Path) -> Dict[str, Any]:
    source_run_dir = EVIDENCE_ROOT / "runs" / case_id
    data, p = load_run_bundle(source_run_dir)
    diagnostics = compute_mechanism_diagnostics(data, p)
    target_dir = outdir / "existing_runs" / case_id
    summary = _write_case_outputs(
        target_dir,
        case_id,
        "existing_evidence_suite",
        f"Reanalyze #16 evidence case {case_id}.",
        data,
        p,
        diagnostics,
    )
    summary["source_run_dir"] = str(source_run_dir)
    return summary


def run_new_case(case: Dict[str, Any], outdir: Path, suite_outdir: Path) -> Dict[str, Any]:
    p = finalize_params(case["params"])
    data = simulate(p, include_audit=True)
    run_dir = outdir / "new_runs" / case["case_id"]
    run_dir.mkdir(parents=True, exist_ok=True)
    save_run_bundle(data, p, run_dir, run_name="run")
    diagnostics = compute_mechanism_diagnostics(data, p)
    summary = _write_case_outputs(
        run_dir,
        case["case_id"],
        case["group"],
        case["purpose"],
        data,
        p,
        diagnostics,
    )
    run_summary = {
        "case_id": case["case_id"],
        "group": case["group"],
        "purpose": case["purpose"],
        "model_branches": model_branch_labels(p),
        "suite_metadata": root_cause_suite_metadata(suite_outdir),
        "params": {
            "N": p.N,
            "t_end": p.t_end,
            "n_save": p.n_save,
            "max_step": p.max_step,
            "Da": p.Da,
            "Bi_T": p.Bi_T,
            "Bi_c": p.Bi_c,
            "Gamma_A": p.Gamma_A,
            "S_chi": p.S_chi,
            "m_act": p.m_act,
            "m_diff": p.m_diff,
            "m_mob": p.m_mob,
            "A_min": p.A_min,
            "D_min": p.D_min,
            "M_min": p.M_min,
            "source_scaling": p.source_scaling,
            "source_J_exponent": p.source_J_exponent,
            "transport_closure": p.transport_closure,
        },
        "classification": classify_run(data),
        "audit": data["audit_diagnostics"],
        "conservation": data["conservation_diagnostics"],
        "mechanism_summary": diagnostics["summary"],
        "validation_status": "candidate_not_validated",
        "paper_evidence_status": "diagnostic_only_not_claim_evidence",
    }
    (run_dir / "run_summary.json").write_text(
        dumps_strict_json(run_summary), encoding="utf-8"
    )
    return summary


def _collect_barrier_samples(outdir: Path, max_rows_per_case: int = 2000) -> list[Dict[str, Any]]:
    samples: list[Dict[str, Any]] = []
    for diag_path in sorted(outdir.glob("*_runs/*/mechanism_diagnostics.json")):
        case_id = diag_path.parent.name
        diagnostics = json.loads(diag_path.read_text(encoding="utf-8"))
        scatter = diagnostics.get("scatter", [])
        if len(scatter) > max_rows_per_case:
            stride = max(1, len(scatter) // max_rows_per_case)
            scatter = scatter[::stride]
        for row in scatter:
            samples.append({"case_id": case_id, **row})
    return samples


def write_barrier_relationship_outputs(outdir: Path) -> Dict[str, Any]:
    samples = _collect_barrier_samples(outdir)
    write_rows_csv(outdir / "barrier_relationship_samples.csv", samples)
    if not samples:
        return {"sample_count": 0, "plot": None}

    try:
        import matplotlib

        matplotlib.use("Agg")
        import matplotlib.pyplot as plt

        J = np.asarray([row["J"] for row in samples], dtype=float)
        A = np.asarray([row["A"] for row in samples], dtype=float)
        D = np.asarray([row["D_over_D0"] for row in samples], dtype=float)
        M = np.asarray([row["M_over_M0"] for row in samples], dtype=float)
        plot_path = outdir / "barrier_relationship.png"
        fig, ax = plt.subplots(figsize=(6.5, 4.2))
        ax.scatter(J, A, s=5, alpha=0.20, label="A")
        ax.scatter(J, D, s=5, alpha=0.20, label="D/D0")
        ax.scatter(J, M, s=5, alpha=0.20, label="M/M0")
        ax.axhline(0.5, color="black", linewidth=0.8, linestyle="--")
        ax.set_xlabel("J")
        ax.set_ylabel("functional factor")
        ax.set_title("Functional closure strength versus swelling")
        ax.legend(loc="best", frameon=False)
        fig.tight_layout()
        fig.savefig(plot_path, dpi=180)
        plt.close(fig)
        return {"sample_count": len(samples), "plot": str(plot_path)}
    except Exception as exc:  # pragma: no cover - plotting is a convenience output
        return {"sample_count": len(samples), "plot": None, "plot_error": str(exc)}


def _classify_root_causes(rows: list[Dict[str, Any]]) -> tuple[str, list[Dict[str, Any]]]:
    by_id = {row["case_id"]: row for row in rows}
    reference = by_id.get("search_N31_Da1_BiT0p2") or by_id.get("diagnostic_source_beta_0")
    high_amp = by_id.get("search_N31_Da4_BiT0p2") or by_id.get("search_N31_Da8_BiT0p2")

    ranked: list[Dict[str, Any]] = []
    if reference:
        geom = float(reference.get("max_geometric_skin_thickness") or 0.0)
        func = float(reference.get("max_functional_skin_thickness") or 0.0)
        source_ratio = reference.get("source_shutdown_tail_over_global_peak")
        balance = reference.get("source_heat_loss_balance_tail")
        supply_balance = reference.get("reactant_supply_source_balance_tail")
        ranked.append(
            {
                "rank": 1,
                "cause": "functional barrier is weak or too late at the clipping-free reference",
                "evidence": {
                    "reference_case": reference["case_id"],
                    "max_geometric_skin_thickness": geom,
                    "max_functional_skin_thickness": func,
                    "min_A": reference.get("min_A"),
                    "min_D_over_D0": reference.get("min_D_over_D0"),
                    "min_M_over_M0": reference.get("min_M_over_M0"),
                    "source_shutdown_tail_over_global_peak": source_ratio,
                },
                "interpretation": "The geometric skin metric is not enough unless A/D/M also suppress the source or transport before a steady balance forms.",
            }
        )
        ranked.append(
            {
                "rank": 2,
                "cause": "late-time dynamics collapse to a steady source/loss and supply/consumption balance",
                "evidence": {
                    "source_heat_loss_balance_tail": balance,
                    "reactant_supply_source_balance_tail": supply_balance,
                    "classification_label": reference.get("classification_label"),
                },
                "interpretation": "A relaxation loop needs delayed negative feedback and reset; the selected reference instead approaches a non-oscillatory balance.",
            }
        )

    source_cases = [
        row
        for row in rows
        if row.get("group") == "source_scaling"
        or row.get("case_id") == "sensitivity_current_volume_source"
    ]
    if source_cases:
        ranked.append(
            {
                "rank": 3,
                "cause": "legacy J-dependent source scaling is not by itself a clean oscillation mechanism in this local test set",
                "evidence": [
                    {
                        "case_id": row["case_id"],
                        "oscillatory": row.get("oscillatory"),
                        "clipping_total": row.get("clipping_total"),
                        "theta_amplitude": row.get("theta_amplitude"),
                    }
                    for row in source_cases
                ],
                "interpretation": "If beta changes do not create clipping-free cycles, J R is at most a sensitivity or artifact candidate, not decisive positive evidence.",
            }
        )

    isolation_cases = [
        by_id.get("diagnostic_accessibility_constant"),
        by_id.get("diagnostic_transport_constant"),
        by_id.get("diagnostic_diffusivity_constant"),
        by_id.get("diagnostic_mobility_constant"),
    ]
    isolation_cases = [row for row in isolation_cases if row]
    if isolation_cases:
        ranked.append(
            {
                "rank": 4,
                "cause": "accessibility, solute transport, and solvent mobility suppressions do not individually reveal a hidden clean oscillator near the reference",
                "evidence": [
                    {
                        "case_id": row["case_id"],
                        "classification_label": row.get("classification_label"),
                        "oscillatory": row.get("oscillatory"),
                        "clipping_total": row.get("clipping_total"),
                        "source_shutdown_tail_over_global_peak": row.get(
                            "source_shutdown_tail_over_global_peak"
                        ),
                    }
                    for row in isolation_cases
                ],
                "interpretation": "The missing loop is not recovered by simply removing one suppression channel around the selected reference.",
            }
        )

    contaminated_near_loop = [
        row
        for row in rows
        if row.get("clipping_total", 0)
        and (
            row.get("oscillatory")
            or row.get("theta_complete_cycles", 0)
            or float(row.get("theta_amplitude") or 0.0) > 0.5
        )
    ]
    if contaminated_near_loop:
        ranked.append(
            {
                "rank": 5,
                "cause": "high-amplitude or near-loop behavior is contaminated by clipping/projection",
                "evidence": [
                    {
                        "case_id": row["case_id"],
                        "classification_label": row.get("classification_label"),
                        "oscillatory": row.get("oscillatory"),
                        "theta_complete_cycles": row.get("theta_complete_cycles"),
                        "theta_amplitude": row.get("theta_amplitude"),
                        "clipping_total": row.get("clipping_total"),
                        "nonfinite_total": row.get("nonfinite_total"),
                        "source_shutdown_tail_over_global_peak": row.get(
                            "source_shutdown_tail_over_global_peak"
                        ),
                        "max_functional_skin_thickness": row.get(
                            "max_functional_skin_thickness"
                        ),
                    }
                    for row in contaminated_near_loop
                ],
                "interpretation": "The high-supply and high-forcing cases are useful clues that a delayed loop may be nearby, but they are numerical artifacts until a zero-clipping case shows sustained complete cycles.",
            }
        )

    conclusion = "root cause partially identified" if ranked else "root cause not identified"
    return conclusion, ranked


def run_root_cause_suite(outdir: str | Path, overwrite: bool = False) -> Dict[str, Any]:
    outdir = Path(outdir)
    ensure_output_dir(outdir, overwrite=overwrite)
    plan = build_root_cause_case_plan()

    rows: list[Dict[str, Any]] = []
    for case_id in plan["existing_cases"]:
        rows.append(analyze_existing_case(case_id, outdir))
    for case in plan["new_cases"]:
        rows.append(run_new_case(case, outdir, outdir))

    write_rows_csv(outdir / "diagnostic_summary.csv", rows)
    relationship = write_barrier_relationship_outputs(outdir)
    conclusion, ranked = _classify_root_causes(rows)
    summary = {
        "status": "completed",
        "conclusion_label": conclusion,
        "paper_evidence_status": "diagnostic_only_not_claim_evidence",
        "validation_status": "candidate_not_validated",
        "suite_metadata": root_cause_suite_metadata(outdir),
        "case_plan": serializable_case_plan(plan),
        "ranked_root_causes": ranked,
        "barrier_relationship": relationship,
        "rows": rows,
        "claim_boundary": [
            "This is a mechanism diagnosis after a failed evidence attempt.",
            "No root-cause diagnostic output is manuscript-ready evidence.",
            "No diagnostic branch is promoted to canonical.",
            "No model or claim was promoted to validated status.",
        ],
    }
    (outdir / "suite_summary.json").write_text(
        dumps_strict_json(summary), encoding="utf-8"
    )
    return summary
