# Multi-Agent Review: Candidate Canonical Paper Solver

Status: completed for issue #13

Validation status: candidate only; not validated

No model or claim was promoted to validated status.

## Scope

Reviewed the conversion of the migrated legacy CPU solver into a candidate
canonical solver scaffold under:

* `paper/solver/canonical_cpu/`

The review explicitly does not validate the hydrogel self-oscillation mechanism,
the imported figure caches, or any paper claim.

## Reviewer Sections

### Physics Model Reviewer Findings

Initial review found that the canonical solver must:

* treat `J`, `W = J u`, and `theta` as the physical state variables, with
  `logJ` only as a numerical positivity variable;
* expose current-volume source scaling `S_R = J R` and reference-volume source
  scaling `S_R = R` as unresolved branches;
* label chi closures scientifically as `effective_osmotic_chi` and
  `strict_chi_derivative`;
* keep the immobilized-catalyst interpretation unresolved until source scaling
  is physically decided;
* retain outward-positive boundary signs and test that `u_N < 1` gives
  bath-to-gel reactant supply;
* keep limiting cases and front/barrier observables as blockers.

Post-implementation review assessed the result as revised but acceptable as a
candidate scaffold. Requested revisions were applied:

* active clipping/projection bounds are now recorded through
  `active_numerical_bounds`;
* strict-chi branch has tests and smoke output;
* diagnostic classification is marked `heuristic_not_evidence`;
* solver README mirrors front/barrier and homogeneous-diagnostic cautions.

### Numerical Analysis Reviewer Findings

Initial review found no numerical tests protecting the solver and requested:

* reaction-off inventory tests;
* heat inventory checks;
* free-surface bath-supply sign test;
* source-scaling branch isolation;
* clipping diagnostics;
* sparse Jacobian structural coverage;
* short legacy-v0 regression.

Implemented tests now cover:

* uniform and nonuniform closed-domain conservation with reaction off;
* closed-domain reactant-to-heat inventory transfer with reaction on;
* free-surface reactant supply sign;
* no-LCST local-potential control;
* no-barrier transport branch;
* source-scaling branch isolation;
* strict chi branch;
* sparse finite-difference pattern coverage;
* short trajectory regression against the migrated legacy default branch.

### Reproducibility/Data Reviewer Findings

Initial review found that the migrated CLI did not save complete metadata and
that figure-local solver copies bypassed any canonical solver. The canonical
scaffold now:

* saves finalized params JSON, diagnostics JSON, and time-series NPZ bundles;
* records branch labels, solver status, numerical settings, git state, runtime,
  and source-file SHA-256 hashes;
* writes smoke outputs to `results/solver_smoke/`, not paper figure caches;
* marks migrated figure-local `scan_optimized.py` copies as frozen provenance in
  figure README files.

Post-implementation review requested strict JSON without bare `NaN` and less
stale-output risk. Revisions applied:

* JSON payloads are sanitized and written with `allow_nan=False`;
* smoke runner removes its prior `.json`/`.npz` outputs before regenerating;
* smoke output now includes strict-chi branch comparison.

### Adversarial Scientific Reviewer Findings

The adversarial review agreed that issue #13 can proceed only as a bridge task,
not as paper evidence. It highlighted blockers:

* source scaling can qualitatively affect results;
* boundary signs must be tested through integral inventory checks;
* clipping can hide or create mechanisms;
* closure labels must not imply first-principles status;
* controls and grid/time smoke checks remain non-evidence;
* a canonical scaffold must not bypass Model Specification gates.

The final implementation records source-scaling sensitivity in smoke summaries.
Because current-volume versus reference-volume source scaling changes short-run
diagnostics, this remains a human/ChatGPT decision blocker.

## Repair Cycles Performed

1. Created failing tests for canonical solver imports and core invariants.
2. Implemented `paper/solver/canonical_cpu/solver.py` with explicit branch
   labels and legacy-v0 trajectory preservation.
3. Added smoke runner and non-evidence output bundle saving.
4. Updated documentation to freeze figure-local solver copies as provenance.
5. Ran first smoke suite and found source-scaling sensitivity.
6. Per post-review findings, revised active numerical bounds, strict JSON,
   strict-chi branch coverage, classification status, README blocker language,
   and nonuniform conservation tests.
7. Regenerated `results/solver_smoke/` outputs.

## Remaining Unresolved Blockers

* Current-volume versus reference-volume source scaling requires physical
  decision.
* Effective-osmotic chi versus strict-derivative chi remains an unresolved
  closure branch.
* The boundary scheme remains the legacy cell-center Robin approximation; sign
  is tested, but face-value accuracy is not upgraded.
* Transport/accessibility floors remain candidate regularizations.
* Front position, collapsed skin thickness, barrier strength, and phase lag
  observables remain undefined for validation.
* Smoke checks are short technical checks only and are not convergence evidence.

## Final Readiness Assessment

Readiness level: candidate paper solver.

The candidate canonical solver is technically ready for a follow-up task that
asks ChatGPT/human to decide unresolved model branches and then design formal
convergence/control-case evidence generation. It is not paper evidence ready.
