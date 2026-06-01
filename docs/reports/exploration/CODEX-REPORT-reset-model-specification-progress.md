# CODEX Report: Reset Model Specification Progress

## Concrete task name

Reset Model Specification Progress for Fresh Model A Review

## Task ID or slug

reset-model-specification-progress

## Human-readable stage

Model Specification workflow maintenance

## Internal stage anchor

`G2_model` context only; this task resets progress inside Model Specification and does not advance the gate.

## Base commit

Main branch after the physics-first workflow restructuring and stages README synchronization.

## Final commit

See the commit containing this report.

## Branch or worktree name

`main`

## Files changed

* `docs/project_state.md`
* `docs/stages/stage_index.md`
* `docs/stages/02_model/gate.md`
* `docs/stages/README.md`
* `docs/reports/exploration/GPT-REVIEW-G2-001.md`
* `docs/tasks/exploration/EXP-002-sanity-check-candidate-model.md`
* `docs/reports/exploration/CODEX-REPORT-reset-model-specification-progress.md`

## Summary of changes

Model Specification progress was reset so candidate Model A can be re-reviewed under the physics-first workflow.

Retained:

* Research Idea Brief completion.
* Literature / Novelty Mapping completion.
* Model A candidate summary.
* Initial derivation source and rendered derivation artifact.
* EXP-001 ingestion history.
* Candidate claim status as unvalidated.

Reset or superseded:

* Prior ChatGPT G2 review progress.
* Prior accepted P0 blocker list.
* Old EXP-002 task as the current active task.

The old GPT review is retained only as a historical artifact and no longer drives current source-of-truth state.

## Commands run

| Command | Exit code |
| ------- | --------- |
| Not run; documentation/state reset only | Not applicable |

## Environment

OS if known: not applicable

Python version: not applicable

Dependency setup command used: not applicable

## Artifacts produced

* Reset project-state snapshot.
* Superseded notice for old GPT G2 review.
* Superseded notice for old EXP-002 task.
* This CODEX report.

## Checks passed

* Source-of-truth files now state that Model Specification is active but reset for fresh review.
* No current Model Specification blocker list is accepted.
* Old GPT review is explicitly marked superseded.
* Old EXP-002 task is explicitly marked superseded.

## Checks failed

No command checks were run for this documentation-only reset.

## Known limitations

This reset does not create the fresh Model A review. It only clears the prior Model Specification progress and prevents stale review carryover.

## Deviations from task instructions

No model content, derivation content, solver code, numerical evidence, figures, or manuscript text was advanced.

## Forbidden actions avoided

No model or claim was promoted to validated status.

## Recommended next task

Re-review Candidate Model A from Scratch.
