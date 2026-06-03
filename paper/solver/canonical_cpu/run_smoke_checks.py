#!/usr/bin/env python3
"""Run non-evidence smoke checks for the candidate canonical CPU solver."""

from __future__ import annotations

import argparse
import json
from dataclasses import replace
from pathlib import Path
from typing import Any, Dict

import numpy as np

from .solver import (
    CanonicalParams,
    conservation_diagnostics,
    dumps_strict_json,
    finalize_params,
    save_run_bundle,
    simulate,
    solver_audit_diagnostics,
)


def _run_case(name: str, p: CanonicalParams, outdir: Path) -> Dict[str, Any]:
    p = finalize_params(p)
    data = simulate(p, include_audit=True)
    written = save_run_bundle(data, p, outdir, run_name=name)
    audit = data.get("audit_diagnostics") or solver_audit_diagnostics(data, p)
    conservation = data.get("conservation_diagnostics") or conservation_diagnostics(data, p)

    source = audit["source"]
    return {
        "name": name,
        "model_branches": data["model_branches"],
        "N": p.N,
        "t_end": p.t_end,
        "n_save": p.n_save,
        "max_step": p.max_step,
        "rtol": p.rtol,
        "atol": p.atol,
        "J_mean_final": float(np.mean(data["J"][:, -1])),
        "theta_mean_final": float(np.mean(data["theta"][:, -1])),
        "W_inventory_final": conservation["reactant_inventory_final"],
        "heat_inventory_final": conservation["heat_inventory_final"],
        "source_mean": source["mean"],
        "source_max": source["max"],
        "reactant_balance_residual": conservation["reactant_balance_residual"],
        "heat_balance_residual": conservation["heat_balance_residual"],
        "logJ_low_clip_count": audit["logJ_low_clip_count"],
        "logJ_high_clip_count": audit["logJ_high_clip_count"],
        "u_floor_clip_count": audit["u_floor_clip_count"],
        "phi_hard_ceiling_exceed_count": audit["phi_hard_ceiling_exceed_count"],
        "nonfinite_source_count": audit["nonfinite_source_count"],
        "nonfinite_flux_count": audit["nonfinite_flux_count"],
        "nfev": data["nfev"],
        "files": {key: str(path) for key, path in written.items()},
    }


def _difference(a: Dict[str, Any], b: Dict[str, Any]) -> Dict[str, float]:
    keys = [
        "J_mean_final",
        "theta_mean_final",
        "W_inventory_final",
        "heat_inventory_final",
        "source_mean",
        "source_max",
    ]
    return {key: float(abs(a[key] - b[key])) for key in keys}


def run_smoke_suite(outdir: Path) -> Dict[str, Any]:
    outdir.mkdir(parents=True, exist_ok=True)
    for stale in outdir.glob("*"):
        if stale.is_file() and stale.suffix in {".json", ".npz"}:
            stale.unlink()

    base = CanonicalParams(N=15, t_end=0.6, n_save=13, max_step=0.1)
    cases: list[tuple[str, CanonicalParams]] = []

    for N in (15, 31, 63):
        cases.append((f"grid_N{N}", replace(base, N=N)))

    cases.extend(
        [
            ("time_maxstep_0p10", replace(base, N=31, max_step=0.10)),
            ("time_maxstep_0p05", replace(base, N=31, max_step=0.05)),
            ("source_current_volume", replace(base, source_scaling="current_volume")),
            ("source_reference_volume", replace(base, source_scaling="reference_volume")),
            ("chi_effective_osmotic", replace(base, chi_closure="effective_osmotic_chi")),
            ("chi_strict_derivative", replace(base, chi_closure="strict_chi_derivative")),
            ("control_no_reaction", replace(base, Da=0.0)),
            ("control_no_lcst", replace(base, S_chi=0.0)),
            (
                "control_no_barrier",
                replace(
                    base,
                    transport_closure="constant_no_barrier",
                    floor_scheme="canonical_consistent",
                ),
            ),
        ]
    )

    results = []
    for name, params in cases:
        results.append(_run_case(name, params, outdir))

    by_name = {row["name"]: row for row in results}
    comparisons = {
        "grid_N15_vs_N31": _difference(by_name["grid_N15"], by_name["grid_N31"]),
        "grid_N31_vs_N63": _difference(by_name["grid_N31"], by_name["grid_N63"]),
        "time_maxstep_0p10_vs_0p05": _difference(
            by_name["time_maxstep_0p10"], by_name["time_maxstep_0p05"]
        ),
        "source_current_vs_reference": _difference(
            by_name["source_current_volume"], by_name["source_reference_volume"]
        ),
        "chi_effective_vs_strict": _difference(
            by_name["chi_effective_osmotic"], by_name["chi_strict_derivative"]
        ),
        "baseline_vs_no_reaction": _difference(
            by_name["grid_N15"], by_name["control_no_reaction"]
        ),
        "baseline_vs_no_lcst": _difference(by_name["grid_N15"], by_name["control_no_lcst"]),
        "baseline_vs_no_barrier": _difference(
            by_name["grid_N15"], by_name["control_no_barrier"]
        ),
    }

    warnings = []
    for row in results:
        clip_total = (
            row["logJ_low_clip_count"]
            + row["logJ_high_clip_count"]
            + row["u_floor_clip_count"]
            + row["phi_hard_ceiling_exceed_count"]
        )
        if clip_total:
            warnings.append(
                f"{row['name']}: clipping/floor count is {clip_total}; inspect diagnostics."
            )
        if row["nonfinite_source_count"] or row["nonfinite_flux_count"]:
            warnings.append(f"{row['name']}: non-finite source or flux values were reported.")

    summary = {
        "status": "completed",
        "evidence_status": "not_paper_evidence",
        "validation_status": "candidate_not_validated",
        "runs": results,
        "comparisons": comparisons,
        "warnings": warnings,
        "notes": [
            "These are short smoke checks only, not convergence evidence.",
            "No model or claim was promoted to validated status.",
        ],
    }
    summary_path = outdir / "solver_smoke_summary.json"
    summary_path.write_text(dumps_strict_json(summary), encoding="utf-8")
    return summary


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--outdir",
        default="results/solver_smoke",
        help="Output directory for non-evidence smoke data.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    summary = run_smoke_suite(Path(args.outdir))
    print(json.dumps({"summary": str(Path(args.outdir) / "solver_smoke_summary.json"), "warnings": summary["warnings"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
