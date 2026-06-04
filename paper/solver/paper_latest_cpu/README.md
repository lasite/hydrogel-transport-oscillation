# Migrated CPU Solver Source

Status: migrated source material, not production solver for this repository.

This directory preserves the CPU model script and homogeneous/stability
diagnostic helper from the sibling draft:

* `scan_optimized.py`
* `linear_stability_1d.py`

The files are copied for provenance and audit of the existing draft model. Their
presence does not validate the model, does not promote the repository to a
numerics stage, and should not be treated as permission to extend a production
PDE solver during the current Model Specification stage.

Audit note:

* `SOLVER_MODEL_AUDIT.md`

The audit note records the actual state vector, flux convention, RHS/source
terms, boundary convention, chemical-potential variants, clipping interventions,
and opt-in diagnostic path for this legacy solver. It does not validate the
model or any figure data generated from the migrated scripts.

Final canonical solver path:

* `../canonical_cpu/`

The canonical solver preserves this legacy behavior only as a controlled
non-canonical comparison branch. New smoke checks and future paper-evidence
preparation should use the final canonical path rather than extending this
monolithic migrated scan script.
