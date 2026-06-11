# Gate: 06 Paper Results Production / Figures

## Status

active

## Purpose

Enable paper-results production from the existing `paper/figures/` assets while preventing figures from implying validation that the repository has not recorded.

This gate is active by user decision. It does not supersede the requirement to keep model, solver, and mechanism claims evidence-bounded.

## Required outputs

* Figure blueprint updated for the production figure set.
* Source mapping for each reused result figure.
* Claim boundary for each final or supplementary figure.
* Reproducible or provenance-preserved generation path for each figure.
* Explicit list of missing explanatory, control, or provenance images.
* Caption plan that distinguishes reused source-draft results from repository-validated evidence.

## Accepted initial source set

The initial production figure source set is:

* `paper/figures/fig01/`: homogeneous stability, eigenvalue, dispersion, and stability-map assets.
* `paper/figures/fig02/`: PDE regime-map, period-map, and peak-polymer-fraction assets.
* `paper/figures/fig03/`: representative spatial/front-diagnostic kymograph and derived-quantity assets.
* `paper/figures/fig09/`: source-draft Fig. 7 spinodal demonstration assets, retained as Fig. 9 or supplementary material.

## Acceptance criteria

* Each final figure supports a bounded claim.
* Exploratory or reused source-draft figures are labeled with appropriate status.
* Every reused result figure records source path, script path, data/cache path, and figure-output path when available.
* Figure captions avoid validated-language unless evidence is recorded elsewhere.
* The new missing-image list is resolved or explicitly deferred before result-section drafting.
* No figure is based on unreproduced source appendix numerical notes without an explicit provenance and limitation statement.

## Evidence

* `docs/manuscript/figure_blueprint.md` exists and is active for production.
* `docs/manuscript/paper_results_figure_plan.md` records the source mapping and new-image plan.
* Existing `paper/figures/fig01`, `fig02`, `fig03`, and `fig09` assets are available as the initial result source set.
* No model or claim has been promoted to validated status.

## Blockers and limitations

* Model Specification was not completed as a validation gate.
* The official `scan_optimized.py` route is not a validated numerical implementation.
* Existing smoke checks are wiring checks only.
* Imported figure assets have not been newly reproduced as validated results in this repository.
* Captions and manuscript text must reflect these limitations.

## Next tasks

* Map Existing `paper/figures` Assets to Manuscript Figures.
* Add Missing Mechanism Schematic and Observable-Definition Images.
* Prepare Control and Provenance Supplementary Figures.
* Draft Evidence-Bounded Captions for Fig. 1/2/3 and Supplementary Fig. 9.

## Promotion rule

Figures may move toward paper-production status only when their source path, claim boundary, and evidence/provenance status are recorded. Do not move any claim or model into `docs/validated/` from this gate without a separate validation decision.
