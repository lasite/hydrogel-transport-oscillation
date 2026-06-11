# CODEX Report: Enter Paper Results Production

## Task

`docs/tasks/production/TASK-enter-paper-results-production.md`

## Objective

Update the repository state so paper-results production is active and the existing `paper/figures/` assets are treated as the initial manuscript figure source set by user decision.

## Summary

The repository state was updated from Model Specification to Paper Results Production (`G6_figures`). The transition records that the user authorized reuse of the existing `paper/figures/` result assets for manuscript result production. The transition does not validate the model, solver, numerical outputs, or mechanism claims.

The updated workflow now allows figure-source mapping, evidence-bounded captions, missing explanatory images, figure assembly, and result-section preparation. It continues to block promotion of any model or claim into `docs/validated/` without a separate validation gate.

## Files created

* `docs/manuscript/paper_results_figure_plan.md`
* `docs/tasks/production/TASK-enter-paper-results-production.md`
* `docs/reports/production/CODEX-REPORT-enter-paper-results-production.md`

## Files modified

* `docs/project_state.md`
* `README.md`
* `AGENTS.md`
* `docs/stages/stage_index.md`
* `docs/stages/06_figures/gate.md`
* `docs/manuscript/figure_blueprint.md`
* `scripts/check_repo_structure.py`
* `tests/test_repo_structure.py`

## State changes

* Active stage changed to `Paper Results Production`.
* Internal anchor changed to `G6_figures`.
* `paper/figures/fig01`, `fig02`, `fig03`, and `fig09` were recorded as the initial production figure source set.
* Figure gate 06 was marked active for paper-results production.
* Model Specification was marked as superseded for production by user decision, not completed as a validation gate.
* Manuscript writing was partially unblocked after figure-source mapping, caption boundaries, and the figure blueprint are prepared.

## Existing figure-source mapping

The initial production source set is:

1. `paper/figures/fig01/`: homogeneous stability and linear diagnostics.
2. `paper/figures/fig02/`: PDE regime maps, period map, and maximum polymer-fraction map.
3. `paper/figures/fig03/`: representative spatial dynamics and front/barrier-style diagnostics.
4. `paper/figures/fig09/`: source-draft Fig. 7 spinodal diagnostic, retained as Fig. 9 or supplementary material.

The detailed mapping is recorded in:

* `docs/manuscript/figure_blueprint.md`
* `docs/manuscript/paper_results_figure_plan.md`

## New images recommended

The production plan records the following required or recommended new images:

1. Mechanism schematic.
2. Cycle snapshot montage.
3. Front and barrier observable-definition figure.
4. Control comparison figure.
5. Provenance and numerical-status support figure or table.
6. Optional model architecture graphic.

## Verification

Commands run in this editing session:

* Not run: `make quickcheck`.

Reason:

* Repository edits were performed through the GitHub connector rather than a checked-out local working tree with command execution.

Static verification performed:

* Updated `scripts/check_repo_structure.py` to require the new active stage, figure plan, production task, and production report.
* Updated `tests/test_repo_structure.py` to require `Paper Results Production`, `G6_figures`, source-mapped `paper/figures/` assets, and the required new-image plan.
* Confirmed all updated files keep explicit validation-boundary language.

Recommended next verification command from a checkout:

```bash
make quickcheck
```

## Known TODOs

* Run `make quickcheck` from a local checkout.
* Create the mechanism schematic and front/barrier observable-definition figure first.
* Draft source-bounded captions for the existing Fig. 1/2/3/9 assets.
* Decide whether the cycle snapshot montage should become a new main Fig. 4 or be merged with existing Fig. 3.
* Decide whether the spinodal diagnostic remains supplementary or becomes an appendix figure.
* If stronger claims are desired, add a separate reproduction/verification task for controls and convergence.

## Recommended next task

`Add Missing Mechanism Schematic and Observable-Definition Images`

## Validation statement

No model or claim was promoted to validated status.
