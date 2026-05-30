# Hydrogel Transport-Induced Relaxation Oscillation

## Central hypothesis

A single exothermic Arrhenius reaction, although non-oscillatory in a well-mixed setting, can generate self-sustained relaxation oscillations when coupled to LCST poroelastic collapse because the collapsed surface layer self-organizes into a transport and reaction-accessibility barrier.

## Current stage

Status: early exploratory repository

Active gate: `G0 -- Idea Brief`

No model has been validated yet.

The initial model derivation should be inserted into `docs/derivations/initial_model_derivation.tex` and summarized in `docs/model_candidates/model_A_initial_lcst_transport_barrier.md`.

Long derivations belong in `.tex`, not Markdown.

Model review is paused until G0 exits or the user explicitly opens G2 model work.

## Repository layers

* `docs/`: idea log, project brief, hypotheses, open questions, tasks, reports, decisions, and manuscript planning.
* `docs/project_state.md`: centralized project-control snapshot for current stage, blockers, gates, and next tasks.
* `docs/stages/`: explicit project-stage gates from idea to submission.
* `docs/model_candidates/`: candidate models before validation.
* `docs/derivations/`: long mathematical derivations in LaTeX.
* `docs/validated/`: only models, derivations, and claims that pass sanity checks and verification gates.
* `src/`: reusable Python package code, intentionally minimal at this stage.
* `scripts/`: scaffold checks and derivation build helpers.
* `configs/`: placeholder configuration files.
* `data/`: raw and processed data placeholders.
* `results/`: reproducible output placeholders.
* `paper/`: manuscript placeholders.

## Minimal checks

```bash
make install
make env-check
make quickcheck
make derivations
```

From a fresh checkout, run `make install` before `make quickcheck` unless dependencies are already available in the active Python environment.

`make derivations` may report a warning if `latexmk` is unavailable. During the exploratory scaffold stage, that warning should not block repository structure checks.

## Workflow

1. Read `docs/project_state.md` before starting a new task.
2. ChatGPT defines or reviews the task scope.
3. Codex implements only within the assigned TASK scope.
4. Run the task's required verification commands.
5. Produce a CODEX report under `docs/reports/` for handoff back to ChatGPT.
6. Do not run model review tasks until G0 exits or the user explicitly opens G2 model work.
7. Do not promote any claim or model into `docs/validated/` before the required gates pass.
