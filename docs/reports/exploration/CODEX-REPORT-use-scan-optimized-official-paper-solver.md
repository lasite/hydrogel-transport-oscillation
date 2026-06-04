# CODEX Report: Use scan_optimized.py as Official Paper Solver Route

## Concrete task name

Use `scan_optimized.py` as the official paper-reproduction solver route.

## Task ID or slug

`use-scan-optimized-official-paper-solver`

## Human-readable stage

Model Specification

## Internal stage anchor

`G2`

## Base commit

`0606bc9` (`origin/main`)

## Final commit

Pending until branch commit is created.

## Branch or worktree name

`codex/use-scan-optimized-paper-solver`

## Files changed

Created:

* `docs/tasks/exploration/TASK-use-scan-optimized-official-paper-solver.md`
* `docs/reports/exploration/CODEX-REPORT-use-scan-optimized-official-paper-solver.md`
* `paper/solver/__init__.py`
* `paper/solver/official_paper_solver.py`
* `paper/solver/run_figure_smoke_checks.py`
* `tests/test_official_paper_solver.py`
* `results/figure_smoke_scan_optimized/figure_smoke_summary.json`
* `results/figure_smoke_scan_optimized/fig01_reduced_scan_table.csv`
* `results/figure_smoke_scan_optimized/fig02_working_point_timeseries.npz`
* `results/figure_smoke_scan_optimized/fig03_derived_profile.npz`
* `results/figure_smoke_scan_optimized/fig09_spinodal_like_field.npz`

Modified:

* `README.md`
* `Makefile`
* `docs/project_state.md`
* `paper/README.md`
* `paper/figures/fig01/README.md`
* `paper/figures/fig02/README.md`
* `paper/figures/fig03/README.md`
* `paper/figures/fig09/README.md`
* `paper/solver/canonical_cpu/README.md`
* `paper/solver/canonical_cpu/run_smoke_checks.py`
* `paper/solver/canonical_cpu/solver.py`
* `paper/solver/paper_latest_cpu/README.md`
* `scripts/check_repo_structure.py`
* `tests/test_repo_structure.py`

## Summary of changes

Issue #20 was implemented as a workflow-routing change. The official
paper-reproduction solver route is now `paper.solver.official_paper_solver`,
which directly re-exports and invokes
`paper/solver/paper_latest_cpu/scan_optimized.py`.

A reduced smoke runner was added at `paper/solver/run_figure_smoke_checks.py`.
It covers Fig. 1, Fig. 2, Fig. 3, and Fig. 9 with minimal settings and writes
small artifacts under `results/figure_smoke_scan_optimized/`. The summary file
records the invoked solver basename, module, source path, SHA-256 hash, and
`validation_status: smoke_only_not_validation`.

The previous issue #15 `paper/solver/canonical_cpu/` path remains in the repo
for audit and regression context, but documentation now marks it as superseded
for official paper reproduction.

## Commands run

| Command | Exit code |
| ------- | --------- |
| `. .venv/bin/activate && make quickcheck` | 0 |
| `. .venv/bin/activate && python -m pytest tests/test_official_paper_solver.py -q` before implementation | 2, expected RED import failure |
| `. .venv/bin/activate && python -m pytest tests/test_official_paper_solver.py -q` after adding route, before README update | 1, expected RED documentation failure |
| `. .venv/bin/activate && python -m pytest tests/test_official_paper_solver.py -q` after implementation | 0 |
| `. .venv/bin/activate && python -m paper.solver.run_figure_smoke_checks --outdir results/figure_smoke_scan_optimized` | 0 |
| `. .venv/bin/activate && python -m pytest tests/test_official_paper_solver.py tests/test_repo_structure.py -q` | 0, 16 passed |
| `. .venv/bin/activate && python -m py_compile $(find paper/solver scripts tests -name '*.py' -print \| sort)` | 0 |
| `git diff --check` | 0 |
| `git status --short -- paper/figures` | 0, README-only changes under figure bundles |
| `. .venv/bin/activate && make quickcheck` | 0, 36 passed |
| `. .venv/bin/activate && make derivations` | 0 |
| `. .venv/bin/activate && make figure-smoke` | 0 |

## Environment

OS if known: Linux

Python version: Python 3.12 in `.venv`

Dependency setup command used: existing `.venv`

## Artifacts produced

* `results/figure_smoke_scan_optimized/figure_smoke_summary.json`
* `results/figure_smoke_scan_optimized/fig01_reduced_scan_table.csv`
* `results/figure_smoke_scan_optimized/fig02_working_point_timeseries.npz`
* `results/figure_smoke_scan_optimized/fig03_derived_profile.npz`
* `results/figure_smoke_scan_optimized/fig09_spinodal_like_field.npz`

## Checks passed

* Baseline `make quickcheck` passed before implementation.
* New tests pass and verify that the official route invokes
  `scan_optimized.py`.
* Reduced Fig. 1/2/3/9 smoke checks completed and produced the expected
  artifact classes.
* `make quickcheck`, `make derivations`, and `make figure-smoke` passed.
* No generated `paper/figures/**/Figure/` assets were changed.

## Checks failed

Expected RED checks:

* Missing official route import failed before implementation.
* README status assertion failed before documentation was updated.

No unexpected failure is currently unresolved.

## Known limitations

* The smoke artifacts are deliberately tiny and are not publication-grade
  figure outputs.
* Fig. 9 uses a reduced field smoke artifact through the official route; it is
  not the full spinodal appendix reproduction.
* The migrated `scan_optimized.py` model still needs scientific review against
  the active derivation before future numerical evidence tasks.

## Deviations from task instructions

None.

## Forbidden actions avoided

Forbidden actions were avoided.

No model or claim was promoted to validated status.

## Recommended next task

Request ChatGPT review of the official `scan_optimized.py` paper-route solver
against the active derivation before using it for any formal convergence,
control-case, or figure-evidence task.
