# Hydrogel Transport-Induced Relaxation Oscillation

## Central hypothesis

A single exothermic Arrhenius reaction, although non-oscillatory in a well-mixed setting, can generate self-sustained relaxation oscillations when coupled to LCST poroelastic collapse because the collapsed surface layer self-organizes into a transport and reaction-accessibility barrier.

## Current stage

Status: early exploratory repository

Active stage: Model Specification

Internal anchor: `G2`

Research Idea Brief and Literature / Novelty Mapping have been accepted by the user.

No model has been validated yet.

Model Specification is active. Production PDE implementation, numerical verification, figure generation, and manuscript drafting remain blocked until later gates.

Long derivations belong in `.tex`, not Markdown.

## Workflow design

The Git repository is the source of truth.

ChatGPT is the theory-planning and review interface. Codex is the repository-editing, command-execution, and verification interface.

This workflow is for interaction with a physics expert, not primarily for programmer task management.

Design principles:

* Formality only at state transitions.
* Physics-first everywhere else.
* Concrete task names first; internal stage anchors such as `G2` are secondary labels for ordering and traceability.

Use full TASK files and CODEX reports when a change affects project state, gate status, validation status, executable behavior, numerical evidence, claim evidence, figures, or manuscript text.

Use lightweight physics notes for non-state-changing theory review, derivation sketches, physical intuition, and critique. Physics notes must not promote claims or validated status.

## Repository layers

* `docs/`: idea log, project brief, hypotheses, open questions, literature/novelty mapping, tasks, reports, decisions, and manuscript planning.
* `docs/project_state.md`: centralized project-control snapshot for current stage, blockers, gates, and next tasks.
* `docs/stages/`: human-readable stage gates with internal anchors.
* `docs/notes/`: lightweight physics-first notes that do not change project state.
* `docs/claims/`: candidate claim and evidence registers before validation.
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
2. Choose the work mode: physics note, Codex task, or gate/state transition.
3. ChatGPT defines or reviews the physics scope.
4. Codex modifies files or runs commands only within the assigned task scope.
5. Run the task's required verification commands.
6. Produce a CODEX report under `docs/reports/` only when Codex changed repository content, ran verification, or prepared a state transition.
7. During Model Specification, prioritize model definitions, variable definitions, limiting cases, boundary-condition signs, material-function assumptions, and front/barrier observables.
8. Do not write production solver code until the Model Specification gate passes.
9. Do not promote any claim or model into `docs/validated/` before the required gates pass.
