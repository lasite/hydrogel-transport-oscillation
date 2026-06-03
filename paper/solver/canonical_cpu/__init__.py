"""Candidate canonical CPU solver for the hydrogel transport model."""

from .solver import (
    CanonicalParams,
    conservation_diagnostics,
    finalize_params,
    save_run_bundle,
    simulate,
    solver_audit_diagnostics,
)

__all__ = [
    "CanonicalParams",
    "conservation_diagnostics",
    "finalize_params",
    "save_run_bundle",
    "simulate",
    "solver_audit_diagnostics",
]
