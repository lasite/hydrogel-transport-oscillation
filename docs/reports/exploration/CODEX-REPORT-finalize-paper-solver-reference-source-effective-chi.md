# CODEX Report: Finalize Paper Solver with Reference Source and Effective Chi

## Concrete task name

Finalize the Paper Solver with Reference-Volume Source Scaling and
Nature-Style Effective-Osmotic Chi

## Task ID or slug

issue-15-finalize-paper-solver-reference-source-effective-chi

## Human-readable stage

Model Specification -> Paper Solver Finalization

## Internal stage anchor

`G2`

## Final solver path

* `paper/solver/canonical_cpu/solver.py`
* `paper/solver/canonical_cpu/run_smoke_checks.py`

## Final default model branch choices

```text
source_scaling = reference_volume
chi_closure = effective_osmotic_chi
transport_closure = normalized_porosity_power
floor_scheme = canonical_consistent
boundary_scheme = cell_center_robin
enthalpy_advection = false
```

## Exact equations implemented

Physical state:

```text
J          local swelling / volume ratio
W = J u    conserved reactant content per reference volume
theta      dimensionless temperature excess
phi = phi0 / J
```

Fluxes:

```text
q = -M(phi, theta) m_x
n = u q - delta D(phi, theta) u_x
h = -alpha K(phi, theta) theta_x
```

Outward-positive free-surface boundary laws:

```text
q_N = Bi_mu (m_N - m_b)
n_N = Bi_c (u_N - 1)
h_N = Bi_T theta_N
```

Semidiscrete source terms use reference-volume scaling:

```text
S_R = R
W_t     ... - Da R
theta_t ... + Da R / C
```

Reaction closure:

```text
R = u^reaction_order A(phi) thermal_factor(theta)
```

Effective osmotic chi closure:

```text
chi_osm = chi_inf + S_chi theta + chi1 phi
m_mix = log(1 - phi) + phi + chi_osm phi^2
```

The strict derivative sensitivity branch subtracts
`phi^2 (1 - phi) chi1`, but it is not canonical.

Canonical normalized transport/accessibility closure:

```text
A(phi) = A_min + (1 - A_min) p(phi)^m_act
D(phi) = D_min + (1 - D_min) p(phi)^m_diff
M(phi) = M_min + (1 - M_min) p(phi)^m_mob
```

with `D` and `M` multiplied by their reference prefactors in flux evaluation.

## Physical justification

Reference-volume source scaling is used because the selected paper-solver
interpretation treats the catalytic/reactive capacity as tied to the reference
gel/catalyst volume. Therefore the canonical source density is `S_R = R`, not
legacy `S_R = J R`.

The canonical chi closure follows the Nature-style effective osmotic pressure
convention. In this branch `chi1` is an effective osmotic closure coefficient,
not a strict free-energy derivative coefficient.

## Boundary scheme decision

The final solver retains `boundary_scheme = cell_center_robin`.

Rationale:

* the sign convention is outward-positive and tested;
* bath-to-gel reactant supply is tested when `u_N < 1`;
* closed-domain inventory tests pass when boundary Biot numbers are zero;
* short smoke runs show no clipping or finite-value warnings.

A reconstructed face-value Robin treatment remains a possible later accuracy
upgrade, but no implementation blocker remains for the next evidence-generation
task.

## Files changed

Created:

* `docs/reports/exploration/MULTIAGENT-REVIEW-final-paper-solver.md`
* `docs/reports/exploration/CODEX-REPORT-finalize-paper-solver-reference-source-effective-chi.md`

Modified:

* `README.md`
* `docs/project_state.md`
* `paper/solver/canonical_cpu/README.md`
* `paper/solver/canonical_cpu/solver.py`
* `paper/solver/canonical_cpu/run_smoke_checks.py`
* `paper/solver/paper_latest_cpu/README.md`
* `paper/figures/fig01/README.md`
* `paper/figures/fig02/README.md`
* `paper/figures/fig03/README.md`
* `paper/figures/fig09/README.md`
* `tests/test_canonical_solver.py`
* `results/solver_smoke/*.json`
* `results/solver_smoke/*.npz`

## Verification commands

| Command | Exit code |
| ------- | --------- |
| `. .venv/bin/activate && python -m pytest tests/test_canonical_solver.py -q` before implementation | 1, expected red phase |
| `. .venv/bin/activate && python -m pytest tests/test_canonical_solver.py -q` after implementation | 0 |
| `. .venv/bin/activate && python -m paper.solver.canonical_cpu.run_smoke_checks --outdir results/solver_smoke` | 0 |
| `. .venv/bin/activate && python` strict JSON / provenance hash check for `results/solver_smoke/*.json` | 0 |
| `. .venv/bin/activate && python -m py_compile $(find src paper/solver scripts tests -name '*.py' -print \| sort)` | 0 |
| `. .venv/bin/activate && python -m pytest tests/test_canonical_solver.py -q` final | 0, 20 passed |
| `. .venv/bin/activate && make quickcheck` | 0, 31 passed |
| `git diff --check` | 0 |

`make derivations` was not run because this task did not modify `.tex`
derivation files.

## Results

* Canonical defaults are fixed to reference-volume source scaling and
  effective-osmotic chi.
* Legacy current-volume source scaling remains available only as a
  non-canonical control.
* Strict chi derivative remains available only as a sensitivity branch.
* The canonical `A`, `D`, and `M` normalized floor treatment is consistent.
* Smoke outputs were regenerated under `results/solver_smoke/`.
* Smoke summary reports no warnings and nominal canonical runs are
  clipping-free.
* Smoke JSON files parse as strict JSON and saved runner hashes match the
  current runner source.

## Readiness level

final paper solver; evidence generation pending

## Known limitations

* This task does not validate the self-oscillation mechanism.
* This task does not generate formal convergence evidence.
* This task does not regenerate paper figures.
* Front position, collapsed skin thickness, barrier strength, and phase-lag
  observables remain to be defined before formal evidence generation.

## Next recommended task

Generate formal convergence and control-case evidence from the final canonical
solver, then regenerate paper figures from that solver only after evidence
criteria pass.

No model or claim was promoted to validated status.
