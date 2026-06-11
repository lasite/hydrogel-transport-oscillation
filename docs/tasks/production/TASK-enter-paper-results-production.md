# TASK: Enter Paper Results Production

Internal stage anchor: `G6_figures`

## Objective

Update the repository state so paper-results production is active and the existing `paper/figures/` assets are treated as the initial manuscript figure source set by user decision.

## Scientific / workflow context

The user requested entering the paper-results production phase and continuing to use the imported `paper/figures/` result assets. This transition changes workflow state and figure-production permissions, but it does not validate the candidate model, solver, numerical results, or mechanism claims.

## Inputs

* `docs/project_state.md`
* `README.md`
* `AGENTS.md`
* `docs/stages/stage_index.md`
* `docs/stages/06_figures/gate.md`
* `docs/manuscript/figure_blueprint.md`
* `paper/paper_latest_migration_manifest.tsv`
* existing `paper/figures/fig01`, `fig02`, `fig03`, and `fig09` assets

## Allowed files to read

* all source-of-truth workflow and manuscript planning files
* figure-local scripts and migration manifest needed for source mapping

## Allowed files to modify

* `docs/project_state.md`
* `README.md`
* `AGENTS.md`
* `docs/stages/stage_index.md`
* `docs/stages/06_figures/gate.md`
* `docs/manuscript/figure_blueprint.md`
* `docs/manuscript/paper_results_figure_plan.md`
* `docs/tasks/production/TASK-enter-paper-results-production.md`
* `docs/reports/production/CODEX-REPORT-enter-paper-results-production.md`
* `scripts/check_repo_structure.py`
* `tests/test_repo_structure.py`

## Forbidden actions

* Do not move any model, result, or claim into `docs/validated/`.
* Do not relabel reused `paper/figures/` assets as repository-validated evidence.
* Do not run or create large simulations.
* Do not edit generated PDFs directly.
* Do not make manuscript novelty claims stronger than the recorded evidence boundary.

## Deliverables

* Project state updated to Paper Results Production.
* Figure gate activated for source-mapped paper production.
* Figure blueprint updated for the existing Fig. 1/2/3/9 assets.
* New paper-results figure plan listing required new images.
* Repository structure checks updated for the new active stage.
* CODEX report recording files changed and validation status.

## Verification commands

```bash
make quickcheck
```

If full command execution is unavailable in the editing environment, perform static consistency checks against the updated stage strings and record that command execution was not run.

## Acceptance criteria

* `docs/project_state.md` records `Stage: Paper Results Production` and `Internal anchor: G6_figures`.
* `README.md` and `AGENTS.md` match the new active stage.
* `docs/stages/stage_index.md` marks `G6_figures` active.
* `docs/stages/06_figures/gate.md` is active and records figure-source mapping requirements.
* `docs/manuscript/figure_blueprint.md` and `docs/manuscript/paper_results_figure_plan.md` identify existing figures and missing images.
* `scripts/check_repo_structure.py` and `tests/test_repo_structure.py` no longer enforce the old G2 active stage.
* No validated model or claim is created.

## Failure conditions

* Any file states or implies that the model is validated.
* Any file states or implies that reused `paper/figures/` assets are newly reproduced repository evidence.
* Stage strings are inconsistent across project state, README, AGENTS, and tests.
* `make quickcheck` fails because the repository still expects Model Specification as the active stage.

## Required CODEX report path

* `docs/reports/production/CODEX-REPORT-enter-paper-results-production.md`

## User approval before merge

User approval is the originating instruction for this state transition.

## ChatGPT review before merge

Required for figure claim boundaries and missing-image recommendations.

## Validation statement

No model or claim was promoted to validated status.
