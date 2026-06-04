# Official Paper Solver Source

Status: official paper-reproduction solver source; smoke only
Validation: not validated
Evidence status: not paper evidence

This directory preserves the CPU model script and homogeneous/stability
diagnostic helper from the sibling draft:

* `scan_optimized.py`
* `linear_stability_1d.py`

Issue #20 makes `scan_optimized.py` the official paper-reproduction solver
source through the wrapper:

* `paper.solver.official_paper_solver`

The wrapper does not change the migrated equations. It provides one auditable
import path for reduced figure workflow smoke checks.

This status does not validate the model, does not promote the repository to a
numerics stage, and does not authorize full-scale paper reproduction during the
current Model Specification stage.

Audit note:

* `SOLVER_MODEL_AUDIT.md`

The audit note records the actual state vector, flux convention, RHS/source
terms, boundary convention, chemical-potential variants, clipping interventions,
and opt-in diagnostic path for this legacy solver. It does not validate the
model or any figure data generated from the migrated scripts.

Reduced figure smoke runner:

* `../run_figure_smoke_checks.py`

The issue #15 candidate canonical CPU solver path is retained under
`../canonical_cpu/` for audit and regression context, but it is no longer the
official paper-reproduction entry point.

No model or claim was promoted to validated status.
