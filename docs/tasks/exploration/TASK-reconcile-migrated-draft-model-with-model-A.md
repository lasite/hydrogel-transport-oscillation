# TASK: Reconcile Migrated Draft Model with Model A

## Concrete task name

Reconcile Migrated Draft Model with Model A

## Task ID or slug

`reconcile-migrated-draft-model-with-model-A`

## Human-readable stage

Model Specification

## Internal stage anchor

`G2_model`

## Objective

Produce a single auditable candidate model specification by reconciling the existing Model A candidate notes with the imported `paper_latest` model section, homogeneous/stability diagnostic section, and appendix.

The output should be a candidate model-specification review, not a validated model and not a numerical implementation task.

## Scientific or workflow context

The repository now contains two overlapping sources for the candidate hydrogel oscillator model:

1. the original Model A candidate summary and initial derivation under `docs/model_candidates/` and `docs/derivations/`;
2. migrated prior-draft source material under `paper/sections/`, `paper/appendix/`, and `paper/solver/paper_latest_cpu/`.

These sources differ in notation and in some modeling details. Before any Model Specification gate can pass, the project needs one explicit candidate specification and a rebuilt blocker list.

No model or claim was promoted to validated status.

## Inputs

* `docs/project_state.md`.
* `docs/reports/exploration/GPT-REVIEW-paper-latest-migration.md`.
* `docs/model_candidates/model_A_initial_lcst_transport_barrier.md`.
* `docs/derivations/initial_model_derivation.tex`.
* `paper/sections/model.tex`.
* `paper/sections/linear_stability.tex`.
* `paper/appendix/appendix.tex`.
* `paper/solver/paper_latest_cpu/scan_optimized.py`.
* `paper/solver/paper_latest_cpu/linear_stability_1d.py`.

## Allowed files to read

* `README.md`.
* `AGENTS.md`.
* `docs/project_state.md`.
* `docs/stages/02_model/gate.md`.
* `docs/stages/stage_index.md`.
* `docs/model_candidates/model_A_initial_lcst_transport_barrier.md`.
* `docs/derivations/initial_model_derivation.tex`.
* `docs/claims/candidate_claim_evidence.md`.
* `docs/reports/exploration/GPT-REVIEW-paper-latest-migration.md`.
* `docs/reports/exploration/CODEX-REPORT-paper-latest-migration.md`.
* `paper/sections/model.tex`.
* `paper/sections/linear_stability.tex`.
* `paper/appendix/appendix.tex`.
* `paper/solver/paper_latest_cpu/scan_optimized.py`.
* `paper/solver/paper_latest_cpu/linear_stability_1d.py`.

## Allowed files to modify

* `docs/model_candidates/model_A_initial_lcst_transport_barrier.md`.
* A new model-specification review note or report under `docs/reports/exploration/`.
* A new or updated blocker-list note under `docs/notes/` or `docs/reports/exploration/`, depending on whether the task only reviews or changes state.
* `docs/project_state.md` only if the blocker list or next task changes.
* `docs/stages/stage_index.md` only if the stage status or next task changes.
* A CODEX report at `docs/reports/exploration/CODEX-REPORT-reconcile-migrated-draft-model-with-model-A.md`.

## Forbidden actions

* Do not move any file into `docs/validated/`.
* Do not claim that the model is validated.
* Do not write or refactor a production PDE solver.
* Do not run large simulations, parameter scans, or figure-generation jobs.
* Do not treat migrated figure data or CPU solver outputs as reproduced evidence.
* Do not begin manuscript drafting.
* Do not change model equations silently. Proposed equation changes must be marked as candidate, unresolved, or requiring human review.

## Deliverables

1. A reconciled candidate-model review that explicitly compares Model A and migrated `paper_latest` model material.
2. A decision table for notation and state variables, including `J`, `u`, `W=Ju`, `theta`, `mu/m`, `phi`, `q`, `n`, and `h`.
3. A boundary-condition audit, especially the free-surface reactant total-flux sign convention.
4. A material-function audit covering accessibility, diffusivity, mobility, thermal conductivity, heat capacity, floors, clipping, and reference-coordinate versus current-coordinate coefficients.
5. A nondimensional-parameter audit that identifies which parameter definitions are accepted, which are candidate-only, and which are ambiguous.
6. A limiting-case checklist for well-mixed, no-reaction, no-collapse/fixed-`J`, no-transport-degradation, no-accessibility-feedback, passive spinodal, and strong/weak surface exchange limits.
7. A minimum-observable list for future verification, including front position, collapsed-skin thickness, barrier strength, period, amplitude, heat-source localization, and reactant penetration metrics.
8. An updated Model Specification blocker list in `docs/project_state.md` or a linked report.
9. A CODEX report with changed files and verification commands.

## Verification commands

At minimum:

```bash
make quickcheck
```

If any `.tex` derivation is edited:

```bash
make derivations
```

No numerical simulation verification is expected in this task.

## Acceptance criteria

* The project has one explicit candidate model specification path or a clear list of unresolved alternatives.
* Notation conflicts between Model A and migrated material are either resolved or listed as blockers.
* Free-surface reactant flux sign convention is audited from the conservation law, not inferred from code style.
* Material closures and coordinate conventions are explicitly marked as accepted candidate, unresolved, or rejected.
* The blocker list is rebuilt from this reconciliation rather than inherited from historical notes.
* No model, numerical result, figure, or claim is promoted to validated status.
* `make quickcheck` passes.

## Failure conditions

* The task cannot reconcile flux signs or material closures without changing equations; in that case, stop and request human review.
* The task discovers that Model A and migrated `paper_latest` equations are materially inconsistent in a way that changes the central hypothesis; in that case, record the conflict and stop before updating later-stage plans.
* Any production solver or parameter scan is introduced.
* Any claim is moved into `docs/validated/`.

## Required CODEX-REPORT path

`docs/reports/exploration/CODEX-REPORT-reconcile-migrated-draft-model-with-model-A.md`

## User approval required before merge

Yes

## ChatGPT review required before merge

Yes
