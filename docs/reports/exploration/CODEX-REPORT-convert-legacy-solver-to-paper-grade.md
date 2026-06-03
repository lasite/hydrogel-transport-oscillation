# CODEX Report: Convert Legacy CPU Solver into Candidate Canonical Solver

## Concrete task name

Convert Legacy CPU Solver into Paper-Grade Canonical Solver with Multi-Agent
Review

## Task ID or slug

issue-13-convert-legacy-solver-to-paper-grade

## Human-readable stage

Model Specification -> Minimal Numerical Verification bridge

## Internal stage anchor

`G2`

## Base commit

`b1d9e6e`

## Final commit

Pending at report creation; see PR branch history.

## Branch or worktree name

`codex/convert-legacy-solver-to-canonical`

## Final canonical solver path

* `paper/solver/canonical_cpu/solver.py`
* `paper/solver/canonical_cpu/run_smoke_checks.py`

Legacy provenance path preserved:

* `paper/solver/paper_latest_cpu/scan_optimized.py`

## Files changed

Created:

* `paper/solver/canonical_cpu/__init__.py`
* `paper/solver/canonical_cpu/README.md`
* `paper/solver/canonical_cpu/solver.py`
* `paper/solver/canonical_cpu/run_smoke_checks.py`
* `tests/test_canonical_solver.py`
* `results/solver_smoke/*.json`
* `results/solver_smoke/*.npz`
* `docs/reports/exploration/MULTIAGENT-REVIEW-paper-solver.md`
* `docs/reports/exploration/CODEX-REPORT-convert-legacy-solver-to-paper-grade.md`

Modified:

* `README.md`
* `docs/project_state.md`
* `paper/solver/paper_latest_cpu/README.md`
* `paper/figures/fig01/README.md`
* `paper/figures/fig02/README.md`
* `paper/figures/fig03/README.md`
* `paper/figures/fig09/README.md`
* `scripts/check_repo_structure.py`
* `tests/test_repo_structure.py`

## Exact model equations implemented

The candidate canonical solver advances the same finite-volume structure as the
migrated legacy default when branch labels select the legacy-equivalent path.
Physical state variables are:

```text
J          local swelling / volume ratio
W = J u    conserved reactant content per reference volume
theta      dimensionless temperature excess
```

The numerical state uses `logJ` for positivity:

```text
y = [logJ_0 ... logJ_{N-1}, W_0 ... W_{N-1}, theta_0 ... theta_{N-1}]
```

Fluxes:

```text
q = -M(phi, theta) m_x
n = u q - delta D(phi, theta) u_x
h = -alpha K(phi, theta) theta_x
```

Surface boundary convention is outward-positive:

```text
q_N = Bi_mu (m_N - m_b)
n_N = Bi_c (u_N - 1)
h_N = Bi_T theta_N
```

Semidiscrete equations:

```text
logJ_t = -(q_{i+1/2} - q_{i-1/2}) / (dx J_i)
         - Bi_J_vol (m_i - m_b) / J_i

W_t = -(n_{i+1/2} - n_{i-1/2}) / dx
      - Da S_R
      + B_vol (J_i - W_i)
      + Bi_c_vol (J_i - W_i)

theta_t = (-(h_{i+1/2} - h_{i-1/2}) / dx + Da S_R) / C_i
          - B_Tvol theta_i
```

Source branch:

```text
current_volume:   S_R = J R
reference_volume: S_R = R
```

Reaction rate:

```text
R = u^reaction_order A(phi) thermal_factor(theta)
```

Chi closure branch:

```text
effective_osmotic_chi:
  m_mix = log(1 - phi) + phi + chi phi^2

strict_chi_derivative:
  m_mix = log(1 - phi) + phi + chi phi^2
          - phi^2 (1 - phi) chi1
```

## Branch/default decisions

Defaults preserve the migrated legacy v0 short trajectory:

* `source_scaling = current_volume`
* `chi_closure = effective_osmotic_chi`
* `transport_closure = legacy_porosity_power`
* `floor_scheme = legacy`
* `boundary_scheme = cell_center_robin`
* `enthalpy_advection = false`

Exposed controlled branches:

* `source_scaling`: `current_volume`, `reference_volume`
* `chi_closure`: `effective_osmotic_chi`, `strict_chi_derivative`
* `transport_closure`: `legacy_porosity_power`, `normalized_porosity_power`,
  `constant_no_barrier`
* `floor_scheme`: `legacy`, `canonical_consistent`
* `boundary_scheme`: `cell_center_robin`

`Pe_T` remains diagnostic-only; enthalpy advection is not implemented in this
candidate branch.

## Whether legacy default trajectory is preserved

Yes for a short regression run. `tests/test_canonical_solver.py` compares
`J`, `W`, `u`, and `theta` from `CanonicalParams` against the migrated
`LegacyParams` path for `N=8`, `t_end=0.2`, `n_save=5`, and matching tolerances.

This preserves legacy behavior for comparison only. It does not validate the
legacy model.

## Summary of changes

* Created a canonical candidate solver module rather than extending the
  monolithic scan script.
* Made unresolved source scaling, chi closure, transport closure, floor scheme,
  boundary scheme, and heat-advection status explicit and machine-readable.
* Added clipping/floor/source/flux/inventory diagnostics.
* Added strict JSON provenance with finalized params, branch labels, git state,
  runtime metadata, and source-file SHA-256 hashes.
* Added small invariant/unit tests and short smoke outputs under
  `results/solver_smoke/`.
* Marked figure-local solver copies as frozen provenance.
* Updated project state and README guardrails.

## Commands run

| Command | Exit code |
| ------- | --------- |
| `python3 -m pytest tests/test_canonical_solver.py -q` | 0 |
| `python3 -m paper.solver.canonical_cpu.run_smoke_checks --outdir results/solver_smoke` | 0 |
| `python3` JSON literal scan for `NaN`/`Infinity` in `results/solver_smoke/*.json` | 0 |
| `. .venv/bin/activate && python -m py_compile $(find src paper/solver scripts tests -name '*.py' -print \| sort)` | 0 |
| `make quickcheck` | 0 |
| `python -m pytest tests/test_canonical_solver.py -q` | 0 |
| `make derivations` | 0 |
| `git diff --check` | 0 |

## Environment

OS if known: Linux

Python version: project venv / `python3`

Dependency setup command used: existing `uv`/venv environment from prior repo
setup.

## Artifacts produced

* `results/solver_smoke/solver_smoke_summary.json`
* Per-case params, diagnostics, and time-series files in `results/solver_smoke/`
* `docs/reports/exploration/MULTIAGENT-REVIEW-paper-solver.md`

Smoke suite summary:

* runs: 12
* warnings: none reported
* JSON files contain no bare `NaN`/`Infinity` tokens after sanitization
* current-volume versus reference-volume source scaling changes short-run
  diagnostics and remains a blocker
* effective-osmotic versus strict-derivative chi closure is now covered by smoke
  output

## Multi-agent review summary

Initial reviewers covered:

* physics model consistency;
* numerical analysis;
* reproducibility/data;
* adversarial scientific risks.

Post-implementation reviewers requested revisions for active numerical bounds,
strict chi coverage, classification labeling, strict JSON, stale smoke outputs,
and README blocker scope. Those revisions were applied.

See:

* `docs/reports/exploration/MULTIAGENT-REVIEW-paper-solver.md`

## Checks passed

* Candidate canonical solver path exists and is documented.
* Legacy v0 short trajectory is preserved for regression comparison.
* Source scaling branches are implemented and tested for flux isolation.
* Chemical potential closure labels are explicit and tested.
* Free-surface reactant supply sign is tested.
* Invariant tests cover reaction-off uniform/nonuniform conservation and
  reaction-source reactant-to-heat transfer in a closed domain.
* Clipping/floor diagnostics and active numerical bounds are automatically
  saved.
* Smoke outputs are written outside paper figure caches.

## Checks failed

No required local command failed after the implemented revisions.

Known non-failure limitation: source scaling changes short-run diagnostics, so
this branch is not ready for paper evidence generation.

## Known limitations

* Current-volume versus reference-volume source scaling is unresolved.
* Effective-osmotic versus strict-derivative chi closure is unresolved.
* Boundary exchange remains a cell-center Robin approximation.
* Floors and clipping remain numerical/model regularizations to be reported.
* Front/barrier observables remain undefined.
* Smoke checks are not convergence evidence.
* No imported figure cache was regenerated from the canonical solver.

## Deviations from task instructions

The task asks for iterative multi-agent repair/review cycles until no blocking
issue remains or unresolved blockers are isolated. Remaining physical blockers
were isolated rather than solved, because source scaling and closure choices
require human/ChatGPT scientific decision.

## Forbidden actions avoided

* Did not overwrite migrated paper figure data or caches.
* Did not move anything into `docs/validated/`.
* Did not run long production parameter scans.
* Did not claim scientific validation.
* Did not silently change the legacy branch.

No model or claim was promoted to validated status.

## Readiness level

`candidate paper solver`

This is not `paper evidence ready after convergence runs`.

## Recommended next task

Ask ChatGPT/human to decide the canonical source-scaling and chi-closure path,
then run a follow-up task for formal convergence/control-case evidence
generation design.
