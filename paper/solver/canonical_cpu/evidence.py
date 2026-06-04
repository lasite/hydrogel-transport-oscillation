"""Evidence helpers for convergence/control-case checks.

These helpers compute audit observables from the final canonical solver output.
They do not validate any model or claim by themselves.
"""

from __future__ import annotations

import csv
import hashlib
import json
import math
import shutil
from dataclasses import replace
from pathlib import Path
from typing import Any, Dict, Iterable

import numpy as np
import scipy
from scipy.signal import correlate, correlation_lags, find_peaks

from .solver import (
    CanonicalParams,
    classify_run,
    conservation_diagnostics,
    dumps_strict_json,
    finalize_params,
    git_metadata,
    model_branch_labels,
    save_run_bundle,
    simulate,
    solver_audit_diagnostics,
    state_fluxes,
)


ROOT = Path(__file__).resolve().parents[3]


def _finite_or_none(value: float) -> float | None:
    value = float(value)
    return value if math.isfinite(value) else None


def _safe_summary(values: Iterable[float]) -> Dict[str, float | None]:
    arr = np.asarray(list(values), dtype=float)
    finite = arr[np.isfinite(arr)]
    if finite.size == 0:
        return {"min": None, "max": None, "mean": None}
    return {
        "min": float(np.min(finite)),
        "max": float(np.max(finite)),
        "mean": float(np.mean(finite)),
    }


def evidence_source_file_hashes(root: Path | None = None) -> Dict[str, str | None]:
    root = root or ROOT
    paths = [
        "paper/solver/canonical_cpu/solver.py",
        "paper/solver/canonical_cpu/evidence.py",
        "paper/solver/canonical_cpu/run_evidence_checks.py",
        "tests/test_evidence_observables.py",
    ]
    hashes: Dict[str, str | None] = {}
    for rel in paths:
        path = root / rel
        hashes[rel] = hashlib.sha256(path.read_bytes()).hexdigest() if path.exists() else None
    return hashes


def evidence_suite_metadata(outdir: str | Path) -> Dict[str, Any]:
    return {
        "command": "python -m paper.solver.canonical_cpu.run_evidence_checks",
        "outdir": str(outdir),
        "runtime": {
            "numpy": np.__version__,
            "scipy": scipy.__version__,
        },
        "git": git_metadata(ROOT),
        "source_file_sha256": evidence_source_file_hashes(ROOT),
    }


def ensure_output_dir(outdir: Path, overwrite: bool = False) -> None:
    if outdir.exists() and any(outdir.iterdir()) and not overwrite:
        raise FileExistsError(
            f"{outdir} already contains evidence outputs; pass --overwrite to replace them."
        )
    if outdir.exists() and overwrite:
        shutil.rmtree(outdir)
    outdir.mkdir(parents=True, exist_ok=True)


def oscillation_summary(
    t: np.ndarray,
    y: np.ndarray,
    tail_fraction: float = 0.60,
    min_amplitude: float = 1.0e-3,
) -> Dict[str, Any]:
    """Estimate tail-period statistics from one scalar observable."""
    t = np.asarray(t, dtype=float)
    y = np.asarray(y, dtype=float)
    start = max(0, int(tail_fraction * len(t)))
    tt = t[start:]
    yy = y[start:]
    if len(tt) < 8:
        return {
            "is_oscillatory": False,
            "period": None,
            "amplitude": 0.0,
            "cycle_cv": None,
            "complete_cycles": 0,
            "peak_count": 0,
        }

    coeff = np.polyfit(tt, yy, 1)
    detrended = yy - np.polyval(coeff, tt)
    amplitude = float(np.max(yy) - np.min(yy))
    if amplitude < min_amplitude:
        return {
            "is_oscillatory": False,
            "period": None,
            "amplitude": amplitude,
            "cycle_cv": None,
            "complete_cycles": 0,
            "peak_count": 0,
        }

    prominence = max(0.15 * amplitude, min_amplitude)
    min_distance = max(3, len(detrended) // 30)
    peaks, _ = find_peaks(detrended, prominence=prominence, distance=min_distance)
    troughs, _ = find_peaks(-detrended, prominence=prominence, distance=min_distance)
    if len(peaks) < 2 or len(troughs) < 2:
        return {
            "is_oscillatory": False,
            "period": None,
            "amplitude": amplitude,
            "cycle_cv": None,
            "complete_cycles": 0,
            "peak_count": int(len(peaks)),
        }

    periods = np.diff(tt[peaks])
    period = float(np.mean(periods))
    cycle_cv = float(np.std(periods) / period) if len(periods) > 1 else 0.0
    complete_cycles = int(min(len(peaks), len(troughs)) - 1)
    return {
        "is_oscillatory": bool(complete_cycles >= 2 and cycle_cv < 0.40),
        "period": period,
        "amplitude": amplitude,
        "cycle_cv": cycle_cv,
        "complete_cycles": complete_cycles,
        "peak_count": int(len(peaks)),
    }


def phase_lag_summary(
    t: np.ndarray,
    reference: np.ndarray,
    response: np.ndarray,
    tail_fraction: float = 0.60,
) -> Dict[str, float | None]:
    """Return the lag where response best correlates with reference."""
    t = np.asarray(t, dtype=float)
    reference = np.asarray(reference, dtype=float)
    response = np.asarray(response, dtype=float)
    start = max(0, int(tail_fraction * len(t)))
    tt = t[start:]
    ref = reference[start:]
    rsp = response[start:]
    if len(tt) < 8 or np.ptp(ref) == 0.0 or np.ptp(rsp) == 0.0:
        return {"lag_time": None, "correlation": None}

    ref = ref - np.mean(ref)
    rsp = rsp - np.mean(rsp)
    corr = correlate(rsp, ref, mode="full")
    denom = np.linalg.norm(ref) * np.linalg.norm(rsp)
    if denom == 0.0:
        return {"lag_time": None, "correlation": None}
    corr = corr / denom
    lags = correlation_lags(len(rsp), len(ref), mode="full")
    dt = float(np.median(np.diff(tt)))
    idx = int(np.argmax(np.abs(corr)))
    return {"lag_time": float(lags[idx] * dt), "correlation": float(corr[idx])}


def _collapsed_skin_from_surface(x: np.ndarray, collapsed: np.ndarray) -> tuple[float, float | None]:
    if not np.any(collapsed):
        return 0.0, None
    dx = float(np.median(np.diff(x))) if len(x) > 1 else 1.0
    count = 0
    for flag in collapsed[::-1]:
        if flag:
            count += 1
        else:
            break
    thickness = count * dx
    front_position = float(1.0 - thickness) if count else None
    return float(thickness), front_position


def _penetration_depth_from_surface(x: np.ndarray, u: np.ndarray, threshold: float = 0.5) -> float:
    dx = float(np.median(np.diff(x))) if len(x) > 1 else 1.0
    above = np.asarray(u) >= threshold
    count = 0
    for flag in above[::-1]:
        if flag:
            count += 1
        else:
            break
    return float(count * dx)


def compute_observables(data: Dict[str, Any], p: CanonicalParams) -> Dict[str, Any]:
    """Compute time-series and summary observables for one solver run."""
    p = finalize_params(p)
    t = np.asarray(data["t"], dtype=float)
    x = np.asarray(data["x"], dtype=float)
    J = np.asarray(data["J"], dtype=float)
    W = np.asarray(data["W"], dtype=float)
    u = np.asarray(data["u"], dtype=float)
    theta = np.asarray(data["theta"], dtype=float)
    dx = 1.0 / p.N
    J_threshold = 0.9 * p.J_init
    phi_threshold = p.phi_p0 / J_threshold

    series: list[Dict[str, Any]] = []
    source_integral = []
    source_mean = []
    heat_localization = []
    skin_thickness = []
    front_position = []
    penetration_depth = []
    min_A = []
    mean_A = []
    min_D = []
    mean_D = []
    min_M = []
    mean_M = []
    surface_q = []
    surface_n = []
    surface_h = []

    for k, tk in enumerate(t):
        aux = state_fluxes(J[:, k], W[:, k], theta[:, k], p, dx)
        source = p.Da * aux["source_density"]
        collapsed = J[:, k] <= J_threshold
        thickness, front = _collapsed_skin_from_surface(x, collapsed)
        penetration = _penetration_depth_from_surface(x, u[:, k])
        source_total = float(np.sum(source) * dx)
        source_abs_total = float(np.sum(np.abs(source)) * dx)
        heat_loc = (
            float(np.max(np.abs(source)) / max(float(np.mean(np.abs(source))), 1.0e-30))
            if source.size
            else 0.0
        )

        row = {
            "t": float(tk),
            "J_mean": float(np.mean(J[:, k])),
            "theta_mean": float(np.mean(theta[:, k])),
            "u_mean": float(np.mean(u[:, k])),
            "W_inventory": float(np.sum(W[:, k]) * dx),
            "source_integral": source_total,
            "source_mean": float(np.mean(source)),
            "collapsed_skin_thickness": thickness,
            "front_position": front,
            "reactant_penetration_depth": penetration,
            "heat_source_localization": heat_loc,
            "min_A": float(np.min(aux["accessibility"])),
            "mean_A": float(np.mean(aux["accessibility"])),
            "min_D": float(np.min(aux["D_ref"])),
            "mean_D": float(np.mean(aux["D_ref"])),
            "min_M": float(np.min(aux["M_ref"])),
            "mean_M": float(np.mean(aux["M_ref"])),
            "surface_q": float(aux["q"][-1]),
            "surface_n": float(aux["nflux"][-1]),
            "surface_h": float(aux["h"][-1]),
        }
        series.append(row)
        source_integral.append(row["source_integral"])
        source_mean.append(row["source_mean"])
        heat_localization.append(row["heat_source_localization"])
        skin_thickness.append(row["collapsed_skin_thickness"])
        front_position.append(float("nan") if front is None else front)
        penetration_depth.append(row["reactant_penetration_depth"])
        min_A.append(row["min_A"])
        mean_A.append(row["mean_A"])
        min_D.append(row["min_D"])
        mean_D.append(row["mean_D"])
        min_M.append(row["min_M"])
        mean_M.append(row["mean_M"])
        surface_q.append(row["surface_q"])
        surface_n.append(row["surface_n"])
        surface_h.append(row["surface_h"])

    J_mean = np.array([row["J_mean"] for row in series])
    theta_mean = np.array([row["theta_mean"] for row in series])
    u_mean = np.array([row["u_mean"] for row in series])
    source_mean_arr = np.asarray(source_mean)

    theta_osc = oscillation_summary(t, theta_mean, min_amplitude=2.0e-3)
    J_osc = oscillation_summary(t, J_mean, min_amplitude=2.0e-4)
    classification = classify_run(data)
    audit = data.get("audit_diagnostics") or solver_audit_diagnostics(data, p)
    conservation = data.get("conservation_diagnostics") or conservation_diagnostics(data, p)
    clipping_total = int(
        audit["logJ_low_clip_count"]
        + audit["logJ_high_clip_count"]
        + audit["u_floor_clip_count"]
        + audit["phi_hard_ceiling_exceed_count"]
        + audit.get("arrh_exp_cap_hit_count", 0)
        + audit["nonfinite_source_count"]
        + audit["nonfinite_flux_count"]
    )

    summary = {
        "classification_label": classification["label"],
        "oscillatory": bool(theta_osc["is_oscillatory"] or J_osc["is_oscillatory"]),
        "theta_period": theta_osc["period"],
        "theta_amplitude": theta_osc["amplitude"],
        "theta_cycle_cv": theta_osc["cycle_cv"],
        "theta_complete_cycles": theta_osc["complete_cycles"],
        "J_period": J_osc["period"],
        "J_amplitude": J_osc["amplitude"],
        "J_cycle_cv": J_osc["cycle_cv"],
        "J_complete_cycles": J_osc["complete_cycles"],
        "max_collapsed_skin_thickness": float(np.max(skin_thickness)),
        "mean_collapsed_skin_thickness": float(np.mean(skin_thickness)),
        "min_front_position": _finite_or_none(np.nanmin(front_position))
        if np.any(np.isfinite(front_position))
        else None,
        "max_reactant_penetration_depth": float(np.max(penetration_depth)),
        "mean_heat_source_localization": float(np.mean(heat_localization)),
        "min_accessibility": float(np.min(min_A)),
        "mean_accessibility": float(np.mean(mean_A)),
        "max_barrier_suppression_A": float(1.0 - np.min(min_A)),
        "min_diffusivity": float(np.min(min_D)),
        "mean_diffusivity": float(np.mean(mean_D)),
        "min_mobility": float(np.min(min_M)),
        "mean_mobility": float(np.mean(mean_M)),
        "phase_lag_source_to_theta": phase_lag_summary(t, source_mean_arr, theta_mean),
        "phase_lag_theta_to_collapse": phase_lag_summary(t, theta_mean, -J_mean),
        "phase_lag_source_to_reactant_depletion": phase_lag_summary(
            t, source_mean_arr, -u_mean
        ),
        "reactant_balance_residual": conservation["reactant_balance_residual"],
        "heat_balance_residual": conservation["heat_balance_residual"],
        "clipping_total": clipping_total,
        "surface_q": _safe_summary(surface_q),
        "surface_n": _safe_summary(surface_n),
        "surface_h": _safe_summary(surface_h),
    }

    return {
        "definitions": {
            "collapse_threshold": {
                "description": "collapsed cells are cells with J <= 0.9 * J_init",
                "J_threshold": float(J_threshold),
                "phi_threshold": float(phi_threshold),
            },
            "skin_thickness": "contiguous collapsed region measured inward from the free surface x=1",
            "front_position": "inner edge of the surface collapsed region; null when no surface skin exists",
            "reactant_penetration_depth": "contiguous surface region where u >= 0.5",
            "heat_source_localization": "max(abs(Da*S_R)) divided by mean(abs(Da*S_R))",
            "phase_lag": "cross-correlation lag on the final 40 percent of the run",
        },
        "summary": summary,
        "series": series,
    }


def case_id_from_params(prefix: str, p: CanonicalParams) -> str:
    bits = [
        prefix,
        f"N{p.N}",
        f"Da{p.Da:g}".replace(".", "p"),
        f"BiT{p.Bi_T:g}".replace(".", "p"),
    ]
    return "_".join(bits)


def build_case_plan() -> Dict[str, Any]:
    base = CanonicalParams(N=51, t_end=120.0, n_save=601, max_step=0.2)
    search_Da = [0.5, 1.0, 2.0, 4.0, 8.0]
    search_Bi_T = [0.1, 0.2, 0.5]
    cases: list[Dict[str, Any]] = [
        {
            "case_id": "baseline_default",
            "group": "baseline",
            "params": base,
            "purpose": "Current final canonical default point.",
        }
    ]
    for Da in search_Da:
        for Bi_T in search_Bi_T:
            p = replace(base, N=31, Da=Da, Bi_T=Bi_T)
            cases.append(
                {
                    "case_id": case_id_from_params("search", p),
                    "group": "local_search",
                    "params": p,
                    "purpose": "Bounded local search over Da x Bi_T because the default point is not assumed oscillatory.",
                }
            )

    reference = replace(base, Da=1.0, Bi_T=0.2)
    for N in (51, 101, 201):
        p = replace(reference, N=N)
        cases.append(
            {
                "case_id": f"convergence_N{N}",
                "group": "convergence",
                "params": p,
                "purpose": "Resolution check at the best clipping-free non-oscillatory reference if no oscillatory point is found.",
            }
        )

    cases.extend(
        [
            {
                "case_id": "time_half_max_step",
                "group": "time_tolerance",
                "params": replace(reference, max_step=0.1),
                "purpose": "Half max-step check.",
            },
            {
                "case_id": "time_tighter_tolerance",
                "group": "time_tolerance",
                "params": replace(reference, rtol=1.0e-7, atol=1.0e-9),
                "purpose": "Tighter tolerance check.",
            },
            {
                "case_id": "control_no_reaction",
                "group": "control",
                "params": replace(reference, Da=0.0),
                "purpose": "No self-heating source.",
            },
            {
                "case_id": "control_no_lcst",
                "group": "control",
                "params": replace(reference, S_chi=0.0),
                "purpose": "No temperature-dependent LCST chi feedback.",
            },
            {
                "case_id": "control_no_barrier",
                "group": "control",
                "params": replace(reference, transport_closure="constant_no_barrier"),
                "purpose": "No accessibility, diffusivity, or mobility barrier.",
            },
            {
                "case_id": "sensitivity_current_volume_source",
                "group": "sensitivity",
                "params": replace(reference, source_scaling="current_volume"),
                "purpose": "Legacy current-volume source scaling sensitivity only.",
            },
            {
                "case_id": "sensitivity_strict_chi",
                "group": "sensitivity",
                "params": replace(reference, chi_closure="strict_chi_derivative"),
                "purpose": "Strict chi derivative sensitivity only.",
            },
            {
                "case_id": "initial_condition_flat",
                "group": "initial_condition",
                "params": replace(reference, eps_J=0.0, eps_u=0.0, eps_theta=0.0),
                "purpose": "Initial-condition robustness with flat initial state.",
            },
            {
                "case_id": "initial_condition_stronger",
                "group": "initial_condition",
                "params": replace(reference, eps_J=0.02, eps_u=0.02, eps_theta=5.0e-4),
                "purpose": "Initial-condition robustness with stronger perturbation.",
            },
        ]
    )
    return {
        "cases": cases,
        "search_grid": {"Da": search_Da, "Bi_T": search_Bi_T},
        "skipped_controls": {
            "control_no_accessibility_barrier": "The final solver exposes all-barrier and no-barrier branches but no branch that sets only A(phi)=1 while retaining D/M suppression.",
            "control_no_diffusivity_mobility_barrier": "The final solver exposes all-barrier and no-barrier branches but no branch that keeps A(phi) while setting D/M constant.",
        },
    }


def select_reference_case(rows: list[Dict[str, Any]]) -> Dict[str, Any]:
    oscillatory = [
        row for row in rows if row["oscillatory"] and row.get("clipping_total", 0) == 0
    ]
    if oscillatory:
        selected = max(oscillatory, key=lambda row: row.get("theta_amplitude", 0.0))
        return {**selected, "selection_reason": "oscillatory_clipping_free"}
    clean = [row for row in rows if row.get("clipping_total", 0) == 0]
    if clean:
        selected = max(clean, key=lambda row: row.get("theta_amplitude", 0.0))
        return {**selected, "selection_reason": "nonoscillatory_clipping_free_largest_theta_amplitude"}
    selected = max(rows, key=lambda row: row.get("theta_amplitude", 0.0))
    return {**selected, "selection_reason": "no_clipping_free_case_found"}


def _write_observables_csv(path: Path, series: list[Dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not series:
        path.write_text("", encoding="utf-8")
        return
    keys = list(series[0].keys())
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=keys)
        writer.writeheader()
        writer.writerows(series)


def _run_one_case(case: Dict[str, Any], outdir: Path, suite_outdir: Path) -> Dict[str, Any]:
    p = finalize_params(case["params"])
    data = simulate(p, include_audit=True)
    run_dir = outdir / "runs" / case["case_id"]
    run_dir.mkdir(parents=True, exist_ok=True)
    save_run_bundle(data, p, run_dir, run_name="run")
    observables = compute_observables(data, p)
    (run_dir / "observables.json").write_text(
        dumps_strict_json(observables), encoding="utf-8"
    )
    _write_observables_csv(run_dir / "observables_timeseries.csv", observables["series"])
    run_summary = {
        "case_id": case["case_id"],
        "group": case["group"],
        "purpose": case["purpose"],
        "model_branches": model_branch_labels(p),
        "suite_metadata": evidence_suite_metadata(suite_outdir),
        "params": {
            "N": p.N,
            "t_end": p.t_end,
            "n_save": p.n_save,
            "max_step": p.max_step,
            "rtol": p.rtol,
            "atol": p.atol,
            "Da": p.Da,
            "Bi_T": p.Bi_T,
            "Bi_c": p.Bi_c,
            "S_chi": p.S_chi,
            "source_scaling": p.source_scaling,
            "chi_closure": p.chi_closure,
            "transport_closure": p.transport_closure,
        },
        "observables": observables["summary"],
        "classification": classify_run(data),
        "audit": data["audit_diagnostics"],
        "conservation": data["conservation_diagnostics"],
        "files": {
            "params": "run_params.json",
            "diagnostics": "run_diagnostics.json",
            "timeseries": "run_timeseries.npz",
            "observables_json": "observables.json",
            "observables_csv": "observables_timeseries.csv",
        },
    }
    (run_dir / "run_summary.json").write_text(
        dumps_strict_json(run_summary), encoding="utf-8"
    )
    return {
        "case_id": case["case_id"],
        "group": case["group"],
        "N": p.N,
        "Da": p.Da,
        "Bi_T": p.Bi_T,
        "source_scaling": p.source_scaling,
        "chi_closure": p.chi_closure,
        "transport_closure": p.transport_closure,
        "oscillatory": bool(observables["summary"]["oscillatory"]),
        "theta_period": observables["summary"]["theta_period"],
        "theta_amplitude": observables["summary"]["theta_amplitude"],
        "theta_complete_cycles": observables["summary"]["theta_complete_cycles"],
        "J_amplitude": observables["summary"]["J_amplitude"],
        "max_collapsed_skin_thickness": observables["summary"][
            "max_collapsed_skin_thickness"
        ],
        "mean_heat_source_localization": observables["summary"][
            "mean_heat_source_localization"
        ],
        "reactant_balance_residual": observables["summary"][
            "reactant_balance_residual"
        ],
        "heat_balance_residual": observables["summary"]["heat_balance_residual"],
        "clipping_total": observables["summary"]["clipping_total"],
        "run_dir": str(run_dir),
    }


def run_evidence_suite(outdir: Path | str, overwrite: bool = False) -> Dict[str, Any]:
    outdir = Path(outdir)
    ensure_output_dir(outdir, overwrite=overwrite)
    plan = build_case_plan()
    rows = [_run_one_case(case, outdir, outdir) for case in plan["cases"]]
    search_rows = [row for row in rows if row["group"] == "local_search"]
    selected = select_reference_case(search_rows)
    evidence_pass = (
        selected["selection_reason"] == "oscillatory_clipping_free"
        and selected.get("theta_complete_cycles", 0) >= 5
    )
    readiness = (
        "convergence/control evidence ready for figure regeneration"
        if evidence_pass
        else "not evidence ready"
    )
    summary = {
        "status": "completed",
        "readiness_label": readiness,
        "suite_metadata": evidence_suite_metadata(outdir),
        "evidence_passed": bool(evidence_pass),
        "reason": "No clipping-free oscillatory attractor with at least five complete post-transient cycles was found in the bounded Da x Bi_T search."
        if not evidence_pass
        else "A clipping-free oscillatory reference was found.",
        "canonical_branch_settings": model_branch_labels(finalize_params(CanonicalParams())),
        "selected_reference": selected,
        "search_grid": plan["search_grid"],
        "skipped_controls": plan["skipped_controls"],
        "rows": rows,
        "claim_boundary": [
            "The final canonical model was tested as implemented.",
            "The bounded local search did not establish the intended oscillatory attractor.",
            "The generated results are not manuscript-ready evidence.",
            "No model or claim was promoted to validated status.",
        ],
    }
    (outdir / "suite_summary.json").write_text(
        dumps_strict_json(summary), encoding="utf-8"
    )
    _write_summary_csv(outdir / "suite_summary.csv", rows)
    return summary


def _write_summary_csv(path: Path, rows: list[Dict[str, Any]]) -> None:
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    keys = list(rows[0].keys())
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=keys)
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--outdir",
        default="results/evidence_convergence_control",
        help="Directory for non-final convergence/control evidence outputs.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Replace an existing non-final evidence output directory.",
    )
    args = parser.parse_args()
    summary = run_evidence_suite(Path(args.outdir), overwrite=args.overwrite)
    print(json.dumps({"summary": str(Path(args.outdir) / "suite_summary.json"), "readiness": summary["readiness_label"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
