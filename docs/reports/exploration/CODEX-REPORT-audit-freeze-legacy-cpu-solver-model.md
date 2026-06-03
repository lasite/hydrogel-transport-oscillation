# CODEX Report: Audit and Freeze the Legacy CPU Solver Model

## Concrete task name

Audit and Freeze the Legacy CPU Solver Model

## Task ID or slug

GitHub issue #10 / `audit-freeze-legacy-cpu-solver-model`

## Human-readable stage

Model Specification

## Internal stage anchor

`G2_model`

## Base commit

`53fcfde`

## Final commit

Pending at report creation.

## Branch or worktree name

`codex/audit-freeze-legacy-cpu-solver`

## Files changed

* `paper/solver/paper_latest_cpu/SOLVER_MODEL_AUDIT.md`
* `paper/solver/paper_latest_cpu/README.md`
* `paper/solver/paper_latest_cpu/scan_optimized.py`
* `docs/project_state.md`
* `docs/reports/exploration/CODEX-REPORT-audit-freeze-legacy-cpu-solver-model.md`

## Summary of changes

* Added a solver audit document that records the actual migrated CPU solver
  model, state vector, flux convention, RHS/source terms, boundary signs,
  chemical-potential variants, source scaling, clipping interventions, and
  current limitations.
* Added opt-in, read-only audit diagnostics to `scan_optimized.py`.
* Added full `Params` serialization helpers.
* Linked the audit document from the solver README.
* Updated project state to record that the legacy CPU solver is more auditable
  but remains unvalidated source/provenance material.

## Actual solver PDE, concise statement

The BDF state is:

```text
y = [logJ, W, theta],  W = J u
```

The finite-volume flux convention is positive in increasing `xi`, outward at the
free surface:

```text
q = -M m_x
n = u q - delta D u_x
h = -alpha K theta_x
```

The implemented semidiscrete RHS is:

```text
logJ_t = -(q_{i+1/2} - q_{i-1/2}) / (dx J_i)
         - Bi_J_vol (m_local_i - m_b) / J_i

W_t = -(n_{i+1/2} - n_{i-1/2}) / dx
      - Da J_i R_i
      + B_vol (J_i - W_i)
      + Bi_c_vol (J_i - W_i)

theta_t = (-(h_{i+1/2} - h_{i-1/2}) / dx + Da J_i R_i) / C_i
          - B_Tvol theta_i
```

The default volumetric exchange terms are zero. The reaction source is scaled as
`Da * J * R`, which remains a model blocker for an immobilized-catalyst or
reference-volume interpretation.

At the free surface:

```text
q_N = Bi_mu (m_N - m_b)
n_N = Bi_c (u_N - 1)
h_N = Bi_T theta_N
```

Thus when `u_N < 1`, `n_N < 0`, representing bath-to-gel reactant supply under
the outward-positive convention.

## Diagnostics added or documented

Added:

* `params_to_dict(p)`
* `save_params_json(p, path)`
* `simulate(p, include_raw_state=False, include_audit=False)`
* `solver_audit_diagnostics(data, p)`

The default `simulate(p)` call path keeps the legacy returned fields and does
not include raw-state or audit output. The optional audit path reports:

* `min_raw_logJ`, `max_raw_logJ`;
* low/high `logJ` clipping counts and fractions;
* `min_W`;
* `min_raw_u = min(W / J_raw)`;
* `u_floor` clipping count and fraction;
* `max_phi_before_clip` and hard-ceiling exceedance statistics;
* non-finite counts for `J`, `W`, `u`, `theta`, source, and flux values;
* surface statistics for `q`, `nflux`, and `h`;
* full serialized `Params`.

Documented:

* default `v0` effective-osmotic-chi closure lacks the strict
  `-phi^2 (1 - phi) chi1` derivative term;
* strict derivative variants exist under `v1_first_principles` and
  `v1_metric_corrected_optional`;
* the current `v1_first_principles` name is not fully first-principles until
  source scaling, geometry, and boundary assumptions are also resolved;
* `Pe_T` is present in parameters/diagnostics but inactive in the RHS;
* surface exchange is implemented as cell-center Robin approximations;
* figure-script copies of `scan_optimized.py` are byte-identical to the
  primary migrated CPU solver source at this audit point.

## Whether default solver dynamics were changed

Default solver dynamics were not changed.

No RHS term, default parameter, boundary condition, integration method, solver
tolerance, or default trajectory was altered. The new diagnostics are opt-in and
read from generated trajectories.

## Commands run

| Command | Exit code |
| ------- | --------- |
| `git fetch origin && git checkout main && git pull --ff-only origin main && git checkout -b codex/audit-freeze-legacy-cpu-solver` | 0 |
| `sha256sum paper/solver/paper_latest_cpu/scan_optimized.py paper/figures/fig01/scripts/scan_optimized.py paper/figures/fig02/scripts/scan_optimized.py paper/figures/fig03/scripts/scan_optimized.py paper/figures/fig09/scripts/scan_optimized.py paper/solver/paper_latest_cpu/linear_stability_1d.py paper/figures/fig01/scripts/linear_stability_1d.py` | 0 |
| `. .venv/bin/activate && python - <<'PY' ... tiny audit smoke test ... PY` | 0 |
| `. .venv/bin/activate && python -m py_compile paper/solver/paper_latest_cpu/scan_optimized.py paper/solver/paper_latest_cpu/linear_stability_1d.py && make quickcheck && make derivations && git diff --check` | 0 |

## Tiny-run smoke-test result

Tiny run:

```text
Params(N=15, t_end=1.0, n_save=20, max_step=0.1)
```

Result:

```text
default_keys_has_audit False False
success True
J shape (15, 20)
theta shape (15, 20)
```

Conservation diagnostics:

```text
reactant_balance_residual = 0.0016349087936855548
heat_balance_residual = 8.13461048447263e-05
reactant_balance_residual_late = 4.608217830125417e-05
heat_balance_residual_late = 1.5787598321847504e-05
max_enthalpy_advection_to_conduction_ratio = 0.0
```

Audit subset:

```text
raw_logJ_available = True
min_raw_logJ = 0.24800688835000995
max_raw_logJ = 0.2673036322941065
logJ_low_clip_count = 0
logJ_high_clip_count = 0
min_W = 0.009321723984379847
min_raw_u = 0.0071352262204255725
u_floor_clip_fraction = 0.0
max_phi_before_clip = 0.11705318518561873
nonfinite_source_count = 0
surface_nflux_min = -0.689480826633789
surface_nflux_max = -0.37529602112976346
```

This smoke test checks only importability and diagnostic plumbing. It is not a
scientific validation of the PDE, parameters, or oscillation mechanism.

## Environment

OS if known: Linux

Python version: Python 3.12.3 from `.venv`

Dependency setup command used: none

## Artifacts produced

* Solver audit document:
  `paper/solver/paper_latest_cpu/SOLVER_MODEL_AUDIT.md`
* Opt-in audit diagnostics in:
  `paper/solver/paper_latest_cpu/scan_optimized.py`
* Handoff report:
  `docs/reports/exploration/CODEX-REPORT-audit-freeze-legacy-cpu-solver-model.md`

## Checks passed

* The primary migrated CPU solver and copied figure-script solver files share
  the same SHA-256 checksum for `scan_optimized.py` at this audit point.
* `scan_optimized.py` and `linear_stability_1d.py` compile.
* Tiny audit smoke test passed.
* `make quickcheck` passed: 10 tests passed.
* `make derivations` passed; derivation PDF was already up to date.
* `git diff --check` passed.

## Checks failed

None.

## Known limitations

* The audit does not prove that the legacy CPU model is physically correct.
* The audit does not reproduce or validate any migrated figure data.
* The figure directories still contain migrated solver copies for provenance;
  the new diagnostics were added to the canonical migrated CPU solver under
  `paper/solver/paper_latest_cpu/`.
* `Pe_T` remains inactive in the RHS.
* `Da * J * R` source scaling remains unresolved for the intended physical
  catalyst interpretation.
* The `v0` effective-chi closure and strict derivative closures remain candidate
  alternatives.
* Boundary exchange remains a cell-center Robin approximation until audited.

## Deviations from task instructions

None.

## Forbidden actions avoided

* No default PDE dynamics were changed.
* No data or figure caches were regenerated or replaced.
* No large parameter scan was run.
* No manuscript claims were changed.
* No production PDE solver was introduced.
* Nothing was moved into `docs/validated/`.

No model or claim was promoted to validated status.

## Recommended next task

After ChatGPT review of this audit task, run a separate Model Specification task
to decide whether the canonical paper model should remain the legacy `v0`
effective-osmotic-chi/current-volume-source model or branch to a corrected
source-scaling / strict-closure comparison model.
