# Hydrogel Transport-Induced Relaxation Oscillation

## Central hypothesis

A single exothermic Arrhenius reaction, although non-oscillatory in a well-mixed setting, can generate self-sustained relaxation oscillations when coupled to LCST poroelastic collapse because the collapsed surface layer self-organizes into a transport and reaction-accessibility barrier.

## Current stage

Status: paper-results production repository with candidate-only scientific status

Active stage: Paper Results Production

Internal anchor: `G6_figures`

Research Idea Brief and Literature / Novelty Mapping have been accepted by the user.

No model or claim has been promoted to validated status.

The user has authorized entering paper-results production and continuing to use the imported `paper/figures/` result assets as the initial manuscript figure source set. This production decision does not by itself validate the model, solver, numerical attractor, or mechanism claims.

The official paper-reproduction smoke route uses the migrated `scan_optimized.py` through `paper.solver.official_paper_solver`. These are reduced workflow checks only; final captions and manuscript claims must remain evidence-bounded unless later validation evidence is recorded.

Long derivations belong in `.tex`, not Markdown.

## Workflow design

The Git repository is the source of truth.

ChatGPT is the theory-planning and review interface. Codex is the repository-editing, command-execution, and verification interface.

This workflow is for interaction with a physics expert, not primarily for programmer task management.

Design principles:

* Formality only at state transitions.
* Physics-first everywhere else.
* Concrete task names first; internal stage anchors such as `G6_figures` are secondary labels for ordering and traceability.

Use full TASK files and CODEX reports when a change affects project state, gate status, validation status, executable behavior, numerical evidence, claim evidence, figures, or manuscript text.

Use lightweight physics notes for non-state-changing theory review, derivation sketches, physical intuition, and critique. Physics notes must not promote claims or validated status.

## Repository layers

* `docs/`: idea log, project brief, hypotheses, open questions, literature/novelty mapping, tasks, reports, decisions, and manuscript planning.
* `docs/project_state.md`: centralized project-control snapshot for current stage, blockers, gates, and next tasks.
* `docs/stages/`: human-readable stage gates with internal anchors.
* `docs/manuscript/figure_blueprint.md`: active figure blueprint for paper-results production.
* `docs/manuscript/paper_results_figure_plan.md`: source mapping and missing-image plan for the production figure set.
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
* `paper/`: manuscript placeholders, migrated paper-source audit material, and production result figures.
* `paper/figures/fig01/`: homogeneous stability and parameter-map figure assets.
* `paper/figures/fig02/`: PDE regime-map figure assets.
* `paper/figures/fig03/`: representative spatial/front-diagnostic figure assets.
* `paper/figures/fig09/`: source-draft Fig. 7 spinodal demonstration assets retained as Fig. 9 / supplementary material.
* `paper/solver/official_paper_solver.py`: official paper-reproduction solver entry point routed to the migrated `scan_optimized.py`; smoke only, not validated claim evidence.
* `paper/solver/run_figure_smoke_checks.py`: reduced Fig. 1/2/3/9 workflow smoke checks using the official solver route.
* `paper/solver/canonical_cpu/`: superseded candidate canonical CPU solver path retained for audit, regression tests, and historical diagnostics.

## Minimal checks

```bash
make install
make env-check
make quickcheck
make derivations
make figure-smoke
```

From a fresh checkout, run `make install` before `make quickcheck` unless dependencies are already available in the active Python environment.

`make derivations` may report a warning if `latexmk` is unavailable. During the exploratory or production-planning stage, that warning should not block repository structure checks.

`make figure-smoke` runs reduced Fig. 1/2/3/9 workflow checks through `scan_optimized.py`. It does not perform full figure reproduction and does not validate the numerical model.

## Workflow

1. Read `docs/project_state.md` before starting a new task.
2. Choose the work mode: physics note, Codex task, or gate/state transition.
3. ChatGPT defines or reviews the physics scope.
4. Codex modifies files or runs commands only within the assigned task scope.
5. Run the task's required verification commands.
6. Produce a CODEX report under `docs/reports/` only when Codex changed repository content, ran verification, or prepared a state transition.
7. During Paper Results Production, prioritize source mapping, figure captions, claim boundaries, missing explanatory images, and provenance.
8. Do not write new production solver code unless a later task explicitly scopes it.
9. Do not promote any claim or model into `docs/validated/` before the required gates pass.
