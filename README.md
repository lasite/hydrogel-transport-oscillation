# Hydrogel Transport-Induced Relaxation Oscillation

## Central hypothesis

A single exothermic Arrhenius reaction, although non-oscillatory in a well-mixed setting, can generate self-sustained relaxation oscillations when coupled to LCST poroelastic collapse because the collapsed surface layer self-organizes into a transport and reaction-accessibility barrier.

## Current stage

Status: early exploratory repository

Active gate: `G2 -- Model Specification`

G0 idea brief and G1 literature / novelty mapping have been accepted by the user.

No model has been validated yet.

G2 model specification is active. Production PDE implementation, numerical verification, figure generation, and manuscript drafting remain blocked until later gates.

Long derivations belong in `.tex`, not Markdown.

## Repository layers

* `docs/`: idea log, project brief, hypotheses, open questions, literature/novelty mapping, tasks, reports, decisions, and manuscript planning.
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
6. During G2, prioritize model specification, variable definitions, limiting cases, boundary-condition signs, material-function assumptions, and front/barrier observables.
7. Do not write production solver code until the G2 model gate passes.
8. Do not promote any claim or model into `docs/validated/` before the required gates pass.
