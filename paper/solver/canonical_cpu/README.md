# Candidate Canonical CPU Solver

Status: candidate paper solver scaffold
Validation: not validated
Evidence status: not paper evidence

This directory contains the candidate canonical CPU solver created for issue
#13. It refactors the migrated legacy solver into an auditable module while
preserving the legacy `v0` behavior as a controlled branch for short regression
comparison.

No model or claim was promoted to validated status.

## Canonical path

Implementation:

* `paper/solver/canonical_cpu/solver.py`

Smoke runner:

* `paper/solver/canonical_cpu/run_smoke_checks.py`

The old migrated script remains provenance material:

* `paper/solver/paper_latest_cpu/scan_optimized.py`

Figure-local copies under `paper/figures/*/scripts/scan_optimized.py` are frozen
provenance scripts. They are not the active canonical solver definition.

## State variables

The candidate canonical solver advances:

```text
logJ       numerical positivity variable
J          local swelling / volume ratio
W = J u    conserved reactant content per reference volume
theta      dimensionless temperature excess
```

The conservative structure is:

```text
J_t + q_x = optional solvent exchange
W_t + n_x = -Da * S_R + optional reactant exchange
C theta_t + h_x = +Da * S_R + optional heat exchange
```

with outward-positive free-surface fluxes:

```text
q = -M(phi, theta) m_x
n = u q - delta D(phi, theta) u_x
h = -alpha K(phi, theta) theta_x
```

The free-surface boundary scheme is currently the legacy cell-center Robin
approximation:

```text
q_N = Bi_mu (m_N - m_b)
n_N = Bi_c (u_N - 1)
h_N = Bi_T theta_N
```

When `u_N < 1`, `n_N < 0`, so bath-to-gel supply increases total `W`.

## Explicit model branches

Every saved run records:

* `source_scaling`: `current_volume` or `reference_volume`
* `chi_closure`: `effective_osmotic_chi` or `strict_chi_derivative`
* `transport_closure`: `legacy_porosity_power`, `normalized_porosity_power`, or
  `constant_no_barrier`
* `floor_scheme`: `legacy` or `canonical_consistent`
* `boundary_scheme`: `cell_center_robin`
* `enthalpy_advection`: currently `false`; `Pe_T` remains diagnostic-only

The default source scaling is `current_volume` because it preserves the migrated
legacy trajectory. This is not a resolved physical decision for immobilized
catalyst interpretation.

## Non-evidence smoke checks

Run:

```bash
python3 -m paper.solver.canonical_cpu.run_smoke_checks --outdir results/solver_smoke
```

The smoke suite runs short cases only:

* `N = 15, 31, 63` grid sensitivity smoke runs;
* two `max_step` values;
* current-volume versus reference-volume source scaling;
* effective-osmotic versus strict-derivative chi closure;
* no-reaction, no-LCST, and no-barrier controls.

The generated files under `results/solver_smoke/` are not paper evidence.
They are technical smoke outputs for audit and future task planning.

Oscillation classifications saved in diagnostics are heuristic run summaries
only. They are labeled `classification_status: heuristic_not_evidence` and must
not be used as evidence for a relaxation-oscillation mechanism without later
front/barrier observables, controls, and convergence checks.

## Current blockers

* Current-volume versus reference-volume source scaling changes short-run
  diagnostics and requires human/ChatGPT physical decision.
* The cell-center Robin boundary scheme is tested for sign convention but has
  not been upgraded to a reconstructed face-value treatment.
* `effective_osmotic_chi` versus `strict_chi_derivative` remains a model branch,
  not a settled closure.
* Transport/accessibility floor values remain candidate regularizations.
* Minimum front position, collapsed skin thickness, barrier strength, and phase
  lag observables are still undefined for numerical validation.
* Homogeneous stability and mean-field oscillation labels remain diagnostics
  only; they do not establish the nonlinear spatial attractor.
* No convergence or control-case evidence has been generated for paper claims.
