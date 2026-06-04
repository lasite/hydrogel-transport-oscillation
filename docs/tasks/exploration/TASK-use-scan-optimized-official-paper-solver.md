# TASK: Use scan_optimized.py as Official Paper Solver Route

## Concrete task name

Use `scan_optimized.py` as the official paper-reproduction solver route.

## Task ID or slug

`use-scan-optimized-official-paper-solver`

## Human-readable stage

Model Specification

## Internal stage anchor

`G2`

## Objective

Switch the official paper-reproduction smoke workflow to invoke the previously
migrated `paper/solver/paper_latest_cpu/scan_optimized.py` script and verify
reduced Fig. 1/2/3/9 workflows without running full-scale validation.

## Scientific or workflow context

GitHub issue #20 requests that `scan_optimized.py` become the formal/canonical
solver used by paper reproduction workflows. This task is a workflow routing
change, not a model-validation task. It must not change model equations or
promote any numerical result to evidence.

## Inputs

* GitHub issue #20.
* `docs/project_state.md`
* `paper/solver/paper_latest_cpu/scan_optimized.py`
* `paper/solver/canonical_cpu/README.md`
* `paper/figures/fig01/README.md`
* `paper/figures/fig02/README.md`
* `paper/figures/fig03/README.md`
* `paper/figures/fig09/README.md`

## Allowed files to read

* `docs/**`
* `paper/**`
* `scripts/**`
* `tests/**`
* `results/solver_smoke/**`

## Allowed files to modify

* `README.md`
* `Makefile`
* `docs/project_state.md`
* `docs/tasks/exploration/TASK-use-scan-optimized-official-paper-solver.md`
* `docs/reports/exploration/CODEX-REPORT-use-scan-optimized-official-paper-solver.md`
* `paper/README.md`
* `paper/solver/**`
* `paper/figures/fig01/README.md`
* `paper/figures/fig02/README.md`
* `paper/figures/fig03/README.md`
* `paper/figures/fig09/README.md`
* `scripts/check_repo_structure.py`
* `tests/**`
* `results/figure_smoke_scan_optimized/**`

## Forbidden actions

* Do not change model equations in `scan_optimized.py`.
* Do not write a new PDE solver.
* Do not run full-resolution figure reproduction.
* Do not tune numerical parameters for publication-grade output.
* Do not move any model, claim, or result into `docs/validated/`.
* Do not regenerate paper figure assets under `paper/figures/**/Figure/`.
* Do not claim that any smoke output validates the mechanism.

## Deliverables

1. Official solver wrapper routed to `scan_optimized.py`.
2. Reduced Fig. 1/2/3/9 smoke runner and artifacts.
3. Test coverage proving the official route invokes `scan_optimized.py`.
4. Documentation updates marking the checks as smoke-only.
5. CODEX report.

## Verification commands

```bash
make quickcheck
make derivations
make figure-smoke
```

## Acceptance criteria

* `scan_optimized.py` is the official paper-reproduction solver route.
* Legacy or superseded solver paths are documented as non-official or historical.
* Reduced smoke coverage exists for Fig. 1, Fig. 2, Fig. 3, and Fig. 9.
* Smoke logs record that `scan_optimized.py` was invoked.
* Smoke outputs are labeled as not validation and not paper evidence.
* No candidate model or claim is promoted to validated status.

## Failure conditions

* Any equation in `scan_optimized.py` is changed.
* A full-resolution reproduction or broad parameter scan is run.
* Smoke outputs overwrite manuscript figure assets.
* Documentation implies the numerical model or figure data are validated.
* `make quickcheck` fails for reasons caused by this task.
* `make figure-smoke` fails to produce all four reduced target artifacts.

## Required CODEX-REPORT path

`docs/reports/exploration/CODEX-REPORT-use-scan-optimized-official-paper-solver.md`

## User approval required before merge

Yes

## ChatGPT review required before merge

Recommended before treating any future numerical output as evidence.
