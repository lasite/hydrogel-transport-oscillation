#!/usr/bin/env python3
"""Run reduced figure-workflow smoke checks through ``scan_optimized.py``.

The checks here are wiring checks only. They verify that the official paper
solver route invokes the migrated ``scan_optimized.py`` module and can produce
the expected class of reduced artifact for manuscript Fig. 1, Fig. 2, Fig. 3,
and Fig. 9 without running full-resolution reproduction.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any, Dict, Iterable, Sequence

import numpy as np

from paper.solver import official_paper_solver as official


FIGURE_SMOKE_CASES: tuple[dict[str, Any], ...] = (
    {
        "figure_id": "fig01",
        "figure_label": "Fig. 1",
        "source_bundle": "paper/figures/fig01",
        "artifact_kind": "reduced_scan_table",
        "parameter_variation": {"Bi_T": [0.08, 0.10]},
        "params": {"N": 6, "t_end": 0.04, "n_save": 5, "max_step": 0.02},
    },
    {
        "figure_id": "fig02",
        "figure_label": "Fig. 2",
        "source_bundle": "paper/figures/fig02",
        "artifact_kind": "working_point_timeseries",
        "params": {
            "N": 6,
            "t_end": 0.04,
            "n_save": 5,
            "max_step": 0.02,
            "alpha": 0.03,
        },
    },
    {
        "figure_id": "fig03",
        "figure_label": "Fig. 3",
        "source_bundle": "paper/figures/fig03",
        "artifact_kind": "derived_profile_npz",
        "params": {
            "N": 6,
            "t_end": 0.04,
            "n_save": 5,
            "max_step": 0.02,
            "alpha": 0.03,
        },
    },
    {
        "figure_id": "fig09",
        "figure_label": "Fig. 9",
        "source_bundle": "paper/figures/fig09",
        "artifact_kind": "spinodal_like_field_npz",
        "params": {
            "N": 6,
            "t_end": 0.03,
            "n_save": 4,
            "max_step": 0.015,
            "Da": 0.0,
            "J_init": 0.34,
            "theta_init": 1.0,
            "eps_J": 1.0e-3,
            "eps_u": 0.0,
        },
    },
)


def _json_default(value: Any) -> Any:
    if isinstance(value, Path):
        return value.as_posix()
    if isinstance(value, np.generic):
        return value.item()
    if isinstance(value, np.ndarray):
        return value.tolist()
    raise TypeError(f"Object of type {type(value).__name__} is not JSON serializable")


def _write_json(path: Path, payload: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, indent=2, sort_keys=True, default=_json_default) + "\n",
        encoding="utf-8",
    )


def _case_lookup() -> dict[str, dict[str, Any]]:
    return {case["figure_id"]: case for case in FIGURE_SMOKE_CASES}


def _params(case: dict[str, Any], overrides: dict[str, Any] | None = None) -> official.Params:
    values = dict(case.get("params", {}))
    if overrides:
        values.update(overrides)
    return official.finalize_params(official.Params(**values))


def _artifact_record(
    case: dict[str, Any],
    artifact: Path,
    p: official.Params,
    data: Dict[str, Any] | None,
) -> Dict[str, Any]:
    provenance = official.solver_provenance()
    row = {
        "figure_id": case["figure_id"],
        "figure_label": case["figure_label"],
        "source_bundle": case["source_bundle"],
        "artifact_kind": case["artifact_kind"],
        "artifact": artifact.as_posix(),
        "status": "completed",
        "invoked_solver_basename": provenance["solver_basename"],
        "invoked_solver_module": provenance["module"],
        "invoked_solver_source": provenance["source_path"],
        "validation_status": "smoke_only_not_validation",
        "params": official.params_to_dict(p, finalized=False),
    }
    if data is not None:
        row.update(
            {
                "n_time": int(len(data["t"])),
                "n_space": int(len(data["x"])),
                "nfev": int(data.get("nfev", -1)),
                "J_shape": list(np.asarray(data["J"]).shape),
                "theta_shape": list(np.asarray(data["theta"]).shape),
            }
        )
    return row


def _run_fig01(case: dict[str, Any], outdir: Path) -> Dict[str, Any]:
    rows: list[dict[str, Any]] = []
    artifact = outdir / "fig01_reduced_scan_table.csv"
    variation = case["parameter_variation"]
    param_name, values = next(iter(variation.items()))
    base_params: official.Params | None = None

    for value in values:
        p = _params(case, {param_name: float(value)})
        base_params = p
        data = official.simulate(p)
        info = official.classify_run(data)
        rows.append(
            {
                param_name: float(value),
                "label": info["label"],
                "is_oscillatory": int(info["is_oscillatory"]),
                "theta_mean_final": float(info["theta_mean_final"]),
                "J_mean_final": float(info["J_mean_final"]),
                "nfev": int(info["nfev"]),
            }
        )

    artifact.parent.mkdir(parents=True, exist_ok=True)
    with artifact.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    record = _artifact_record(case, artifact, base_params or _params(case), data=None)
    record["scan_rows"] = len(rows)
    record["scan_parameter"] = param_name
    return record


def _run_fig02(case: dict[str, Any], outdir: Path) -> Dict[str, Any]:
    p = _params(case)
    data = official.simulate(p)
    artifact = outdir / "fig02_working_point_timeseries.npz"
    np.savez(
        artifact,
        x=data["x"],
        t=data["t"],
        J=data["J"],
        u=data["u"],
        theta=data["theta"],
    )
    return _artifact_record(case, artifact, p, data)


def _run_fig03(case: dict[str, Any], outdir: Path) -> Dict[str, Any]:
    p = _params(case)
    data = official.simulate(p)
    artifact = outdir / "fig03_derived_profile.npz"
    J = np.asarray(data["J"])
    theta = np.asarray(data["theta"])
    phi = p.phi_p0 / J
    access = np.power(np.clip(1.0 - phi, 1.0e-12, 1.0), p.m_act)
    np.savez(
        artifact,
        x=data["x"],
        J_mean=np.mean(J, axis=1),
        theta_mean=np.mean(theta, axis=1),
        access_mean=np.mean(access, axis=1),
        J_min=np.min(J, axis=1),
        J_max=np.max(J, axis=1),
    )
    return _artifact_record(case, artifact, p, data)


def _run_fig09(case: dict[str, Any], outdir: Path) -> Dict[str, Any]:
    p = _params(case)
    data = official.simulate(p)
    artifact = outdir / "fig09_spinodal_like_field.npz"
    np.savez(
        artifact,
        x=data["x"],
        t=data["t"],
        J=data["J"],
        theta=data["theta"],
        Da=np.float64(p.Da),
        note=np.array(
            [
                "Reduced field smoke artifact only; not the full spinodal figure reproduction.",
            ],
            dtype=str,
        ),
    )
    return _artifact_record(case, artifact, p, data)


_RUNNERS = {
    "fig01": _run_fig01,
    "fig02": _run_fig02,
    "fig03": _run_fig03,
    "fig09": _run_fig09,
}


def run_figure_smoke_suite(
    outdir: str | Path,
    figure_ids: Sequence[str] | None = None,
) -> Dict[str, Any]:
    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    by_id = _case_lookup()
    selected = tuple(figure_ids or by_id.keys())
    unknown = sorted(set(selected) - set(by_id))
    if unknown:
        raise ValueError(f"unknown figure smoke case(s): {', '.join(unknown)}")

    runs = []
    for figure_id in selected:
        runs.append(_RUNNERS[figure_id](by_id[figure_id], outdir))

    summary = {
        "status": "completed",
        "validation_status": "smoke_only_not_validation",
        "evidence_status": "not_paper_evidence",
        "official_solver": official.solver_provenance(),
        "figures_requested": list(selected),
        "runs": runs,
        "notes": [
            "Smoke checks use minimal or reduced settings only.",
            "The output artifacts are wiring checks, not publication-grade figures.",
            "No model or claim was promoted to validated status.",
        ],
    }
    _write_json(outdir / "figure_smoke_summary.json", summary)
    return summary


def parse_args(argv: Iterable[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--outdir",
        default="results/figure_smoke_scan_optimized",
        help="Directory for reduced figure smoke outputs.",
    )
    parser.add_argument(
        "--figures",
        nargs="*",
        choices=sorted(_case_lookup()),
        default=None,
        help="Optional subset of figure smoke IDs. Defaults to fig01 fig02 fig03 fig09.",
    )
    return parser.parse_args(argv)


def main(argv: Iterable[str] | None = None) -> int:
    args = parse_args(argv)
    summary = run_figure_smoke_suite(args.outdir, figure_ids=args.figures)
    print(
        json.dumps(
            {
                "summary": str(Path(args.outdir) / "figure_smoke_summary.json"),
                "status": summary["status"],
                "official_solver": summary["official_solver"]["solver_basename"],
                "figures": summary["figures_requested"],
                "validation_status": summary["validation_status"],
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
