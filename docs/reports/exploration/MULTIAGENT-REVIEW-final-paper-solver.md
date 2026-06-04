# Multi-Agent Review: Final Canonical Paper Solver

Status: completed for issue #15

Validation status: candidate model only; not validated

Readiness level: final paper solver; evidence generation pending

No model or claim was promoted to validated status.

## Scope

Reviewed the issue #15 final canonical CPU solver path under:

* `paper/solver/canonical_cpu/`

The review assessed whether the fixed branch decisions are implemented,
documented, tested, and reproducible enough for the next formal
evidence-generation task. It did not validate the hydrogel oscillation
mechanism, convergence, imported figure caches, or manuscript claims.

## Fixed Canonical Choices Reviewed

* `source_scaling = reference_volume`
* `chi_closure = effective_osmotic_chi`
* `transport_closure = normalized_porosity_power`
* `floor_scheme = canonical_consistent`
* `boundary_scheme = cell_center_robin`
* `enthalpy_advection = false`

Legacy and sensitivity controls remain available only as non-canonical
comparisons:

* `source_scaling = current_volume`
* `chi_closure = strict_chi_derivative`
* `transport_closure = legacy_porosity_power`
* `floor_scheme = legacy`

## Reviewer Verdicts

### Physics Model Reviewer

Verdict: pass with limitations

The reviewer found no blocking physics/model inconsistency for the fixed issue
#15 choices. The implementation consistently uses reference-volume source
scaling, effective-osmotic chi, normalized transport floors, outward-positive
cell-center Robin boundary signs, and diagnostic-only heat advection.

Limitations:

* the implementation does not validate the model, oscillation mechanism,
  convergence, or paper claims;
* the retained cell-center Robin scheme remains an approximation;
* the catalyst/reference-volume interpretation is an implemented modeling
  assumption, not a validated physical closure.

### Numerical Analysis Reviewer

Verdict: pass with limitations

The reviewer found no numerical implementation blocker. The finite-volume
residuals use face flux arrays with conservative divergence form, closed-domain
inventory tests cover `J`, `W`, and heat, boundary sign tests cover bath-to-gel
reactant supply, and sparse Jacobian stencil coverage is tested.

Limitations:

* the Jacobian is sparse finite-difference with coloring, not analytic;
* smoke checks are short technical checks, not convergence evidence;
* `theta_clip` remains a parameter but is not an active clipping path.

### Reproducibility/Data Reviewer

Initial verdict: fail

The reviewer found that smoke outputs were stale relative to the current runner
hash, and that deleting expected outputs during a run made saved git status
capture transient deletion state.

Repair applied:

* smoke cleanup now removes only stale `.json`/`.npz` files outside the current
  expected case list;
* smoke summary now records suite command, git metadata, and source-file
  SHA-256 hashes;
* smoke outputs were regenerated after the runner and tests stopped changing;
* provenance checks confirmed all saved params runner hashes match the current
  `run_smoke_checks.py`, strict JSON parsing succeeds, and warnings are empty.

Final verdict: pass with limitations

Remaining limitation: figure READMEs mark figure-local solvers as frozen
provenance, but future figure-generation scripts have not yet been converted to
import the canonical solver. That conversion belongs to a later figure/evidence
task.

### Adversarial Reviewer

Verdict: pass with limitations

The reviewer found no implementation blocker under the issue #15 failure
conditions. Defaults are canonical, non-canonical controls remain available,
boundary/conservation tests pass, and nominal smoke runs are clipping-free and
finite.

Limitations:

* smoke checks are short and do not prove convergence;
* no front/barrier/oscillation evidence is generated;
* final report files were missing at the time of review and are created by this
  task.

## Final Multi-Agent Assessment

Verdict: pass with limitations

No reviewer reported an unresolved implementation blocker after the
reproducibility repair. The solver is acceptable as the final canonical paper
solver path for the next formal evidence-generation task.

This is not paper evidence and does not validate the scientific claims.

