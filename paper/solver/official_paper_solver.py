"""Official paper solver entry point routed to migrated ``scan_optimized.py``.

This module intentionally re-exports the migrated paper solver without changing
its equations. It exists so figure-reproduction smoke tests and future paper
workflow code have one auditable import path.
"""

from __future__ import annotations

import hashlib
from pathlib import Path
from typing import Any, Dict

from paper.solver.paper_latest_cpu import scan_optimized as _scan_optimized


OFFICIAL_SOLVER_SOURCE = Path(_scan_optimized.__file__).resolve()
OFFICIAL_SOLVER_MODULE = _scan_optimized.__name__

Params = _scan_optimized.Params
accessibility_factor = _scan_optimized.accessibility_factor
classify_run = _scan_optimized.classify_run
conservation_diagnostics = _scan_optimized.conservation_diagnostics
finalize_params = _scan_optimized.finalize_params
local_chem_pot = _scan_optimized.local_chem_pot
params_to_dict = _scan_optimized.params_to_dict
plot_scan = _scan_optimized.plot_scan
reaction_rate = _scan_optimized.reaction_rate
rhs_mol_logJ = _scan_optimized.rhs_mol_logJ
simulate = _scan_optimized.simulate
solver_audit_diagnostics = _scan_optimized.solver_audit_diagnostics
state_fluxes = _scan_optimized.state_fluxes
sweep_parallel = _scan_optimized.sweep_parallel


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def solver_provenance() -> Dict[str, Any]:
    """Return auditable metadata for the official smoke-test solver path."""
    return {
        "solver_basename": OFFICIAL_SOLVER_SOURCE.name,
        "source_path": OFFICIAL_SOLVER_SOURCE.as_posix(),
        "module": OFFICIAL_SOLVER_MODULE,
        "sha256": _sha256(OFFICIAL_SOLVER_SOURCE),
        "status": "official_paper_reproduction_solver",
        "validation_status": "smoke_only_not_validation",
        "notes": [
            "This route preserves the migrated scan_optimized.py equations.",
            "Smoke checks confirm workflow wiring only, not numerical validity.",
            "No model or claim was promoted to validated status.",
        ],
    }


__all__ = [
    "OFFICIAL_SOLVER_MODULE",
    "OFFICIAL_SOLVER_SOURCE",
    "Params",
    "accessibility_factor",
    "classify_run",
    "conservation_diagnostics",
    "finalize_params",
    "local_chem_pot",
    "params_to_dict",
    "plot_scan",
    "reaction_rate",
    "rhs_mol_logJ",
    "simulate",
    "solver_audit_diagnostics",
    "solver_provenance",
    "state_fluxes",
    "sweep_parallel",
]
