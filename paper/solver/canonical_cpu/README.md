# Final Canonical CPU Solver Path

Status: final paper solver; evidence generation pending
Validation: not validated
Evidence status: not paper evidence

This directory contains the canonical CPU solver path finalized for issue #15.
It refactors the migrated legacy solver into an auditable module while
preserving the legacy `v0` behavior as a controlled non-canonical branch for
short regression and sensitivity comparison.

No model or claim was promoted to validated status.

## Final canonical path

Implementation:

* `paper/solver/canonical_cpu/solver.py`

Smoke runner:

* `paper/solver/canonical_cpu/run_smoke_checks.py`

The old migrated script remains provenance material:

* `paper/solver/paper_latest_cpu/scan_optimized.py`

Figure-local copies under `paper/figures/*/scripts/scan_optimized.py` are frozen
provenance scripts. They are not the active canonical solver definition.
Future paper-evidence figure generation should import this canonical solver
path, after formal convergence and control-case evidence tasks pass.

## State variables

The canonical solver advances:

```text
logJ       numerical positivity variable
J          local swelling / volume ratio
W = J u    conserved reactant content per reference volume
theta      dimensionless temperature excess
```

The laterally constrained 1D slab interpretation is:

```text
J          local swelling / volume ratio
W = J u    conserved reactant content per reference volume
phi = phi0 / J
```

The conservative structure is:

```text
J_t + q_x = optional solvent exchange
W_t + n_x = -Da * R + optional reactant exchange
C theta_t + h_x = +Da * R + optional heat exchange
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

The cell-center Robin boundary scheme is retained as the final finite-volume
boundary approximation for this solver path because closed-domain inventory
tests and outward-positive boundary sign tests pass. A face-value
reconstruction remains a possible later accuracy upgrade, but is not required
before the next evidence-generation task.

## Final default model choices

Every saved run records:

* `source_scaling`: `current_volume` or `reference_volume`
* `chi_closure`: `effective_osmotic_chi` or `strict_chi_derivative`
* `transport_closure`: `legacy_porosity_power`, `normalized_porosity_power`, or
  `constant_no_barrier`
* `floor_scheme`: `legacy` or `canonical_consistent`
* `boundary_scheme`: `cell_center_robin`
* `enthalpy_advection`: currently `false`; `Pe_T` remains diagnostic-only

The final canonical paper-solver defaults are:

```text
source_scaling = reference_volume
chi_closure = effective_osmotic_chi
transport_closure = normalized_porosity_power
floor_scheme = canonical_consistent
boundary_scheme = cell_center_robin
enthalpy_advection = false
```

The reference-volume source scaling implements the immobilized
catalyst/reference-volume interpretation:

```text
S_R = R
W_t     ... - Da R
theta_t ... + Da R / C
```

The effective osmotic chi closure follows the Nature-style osmotic-pressure
convention:

```text
chi_osm = chi_inf + S_chi theta + chi1 phi
m_mix = log(1 - phi) + phi + chi_osm phi^2
```

Here `chi1` is an effective osmotic closure coefficient, not a strict
free-energy derivative coefficient. The strict derivative branch remains only
as a sensitivity control.

The canonical normalized transport/accessibility closure uses:

```text
A(phi) = A_min + (1 - A_min) p(phi)^m_act
D(phi) = D_min + (1 - D_min) p(phi)^m_diff
M(phi) = M_min + (1 - M_min) p(phi)^m_mob
```

with `D` and `M` multiplied by their reference prefactors in the finite-volume
fluxes.

## Legacy and sensitivity controls

These branches remain available for comparison only and are non-canonical:

* `source_scaling = current_volume`, equivalent to legacy `S_R = J R`;
* `chi_closure = strict_chi_derivative`;
* `transport_closure = legacy_porosity_power`;
* `floor_scheme = legacy`;
* the migrated monolithic solver under `paper/solver/paper_latest_cpu/`.

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

The smoke summary records `readiness_level: final paper solver; evidence
generation pending`. It also records whether nominal canonical short runs were
free of active clipping/floor interventions.

Oscillation classifications saved in diagnostics are heuristic run summaries
only. They are labeled `classification_status: heuristic_not_evidence` and must
not be used as evidence for a relaxation-oscillation mechanism without later
front/barrier observables, controls, and convergence checks.

## Remaining blockers before paper evidence

* Minimum front position, collapsed skin thickness, barrier strength, and phase
  lag observables are still undefined for numerical validation.
* Formal grid/timestep convergence and control-case evidence have not yet been
  generated.
* Homogeneous stability and mean-field oscillation labels remain diagnostics
  only; they do not establish the nonlinear spatial attractor.
* The boundary scheme is accepted for this finite-volume paper-solver path, but
  face-value reconstruction remains a possible future accuracy improvement.
* No convergence or control-case evidence has been generated for paper claims.
