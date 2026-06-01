# CODEX Report: Physics-First Workflow Structure Update

## Concrete task name

Structure Workflow for Physics-First AI Research Collaboration

## Task ID or slug

structure-physics-first-workflow

## Human-readable stage

Model Specification workflow maintenance

## Internal stage anchor

`G2_model` context only; this task does not advance the Model Specification gate.

## Base commit

`252d4720d436f0a208a5ef410c939c4003202d90`

## Final repository state

The structural workflow update was merged into `main` through PR #5. The PR squash merge commit was:

`8d7e8feb5ab88769888817a13b74e24aba42f3a4`

This report was refreshed after merge to remove stale PR-review wording.

## Branch or worktree name

`workflow-physics-first-structure`, merged to `main`

## Files changed

Structural and workflow files only:

* `README.md`
* `AGENTS.md`
* `docs/project_state.md`
* `docs/stages/stage_index.md`
* `docs/stages/02_model/gate.md`
* `docs/tasks/README.md`
* `docs/tasks/TASK-TEMPLATE.md`
* `docs/reports/README.md`
* `docs/reports/CODEX-REPORT-TEMPLATE.md`
* `docs/notes/README.md`
* `docs/notes/PHYSICS-NOTE-TEMPLATE.md`
* `docs/workflow_eval.md`
* `docs/decisions/ADR-001-physics-first-workflow.md`
* `docs/claims/README.md`
* `docs/claims/candidate_claim_evidence.md`
* `docs/validated/README.md`
* `docs/validated/claim_evidence.md`
* `scripts/check_repo_structure.py`
* `tests/test_repo_structure.py`

## Summary of changes

The workflow was restructured around three principles:

* formality only at state transitions;
* physics-first reasoning elsewhere;
* concrete task names before abstract internal anchors.

The active stage is now written as `Model Specification` with `G2` retained as an internal anchor. Lightweight physics notes were added for non-state-changing theoretical reasoning. Candidate claim-evidence tracking was moved out of the validated area into `docs/claims/`. Structural checks and tests were updated to guard these workflow invariants.

## Commands run

| Command | Exit code |
| ------- | --------- |
| `make quickcheck` on a local mirror of the updated structural files | 0 |

## Environment

OS if known: local container environment

Python version: Python 3.13 in local verification environment

Dependency setup command used: not required; `pytest` was available in the verification environment

## Artifacts produced

* PR #5: `Structure workflow for physics-first AI research collaboration`, merged to `main`
* New physics-note template under `docs/notes/`
* New candidate-claims directory under `docs/claims/`
* New workflow-evaluation rubric under `docs/workflow_eval.md`
* New ADR under `docs/decisions/ADR-001-physics-first-workflow.md`

## Checks passed

* Structural file presence check passed in the local mirror.
* Updated pytest structure tests passed in the local mirror.
* PR #5 was mergeable and was merged to `main`.

## Checks failed

None for the structural quickcheck in the local mirror.

## Known limitations

The branch was not cloned directly in the local container because external GitHub network access was unavailable there. Files were modified through the GitHub connector and the structural verification was run on a local mirror of the intended file state.

`make derivations` was not run for this workflow task because no `.tex` derivation source was edited.

## Deviations from task instructions

No scientific project work was advanced. No model blocker was resolved. No solver, simulation, figure, or manuscript text was created.

## Forbidden actions avoided

No model or claim was promoted to validated status.

## Recommended next task

From a fresh checkout, run `make quickcheck` once in the normal development environment. Then continue with the first concrete physics task only if the user chooses to proceed.
