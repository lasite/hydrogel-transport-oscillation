# Project State

## Current Stage

Stage: Paper Results Production

Internal anchor: `G6_figures`

Stage entry decision: on 2026-06-11, the user authorized a transition into paper-results production and requested continued use of the existing `paper/figures/` result assets.

Previous stages:

* Research Idea Brief (`G0_idea_brief`) completed after user accepted the project brief, central hypothesis, candidate claims, and uncertainty list.
* Literature / Novelty Mapping (`G1_literature`) completed after user accepted the novelty framing and prior-art risk matrix; the frozen literature corpus was created for Model Specification.
* Model Specification (`G2_model`) is superseded for production by user decision, not completed as a validation gate. Its unresolved model, solver, and observable issues remain manuscript limitations and figure-caption constraints.

Substage: paper figure-source consolidation, figure blueprint update, and planning of missing production images.

Model status: candidate only. No model or claim has been promoted to `docs/validated/`. The active derivation source remains `docs/derivations/initial_model_derivation.tex`, which mechanically copies migrated Appendix A--B material from `paper/appendix/appendix.tex`; it remains candidate model material.

Numerics status: the official paper-reproduction route uses `paper.solver.official_paper_solver`, which invokes `paper/solver/paper_latest_cpu/scan_optimized.py`. The issue #15 candidate canonical CPU solver scaffold under `paper/solver/canonical_cpu/` remains available for audit and regression context, but it is not the active paper-reproduction route. The repository is now allowed to use the imported `paper/figures/` numerical assets for manuscript-result production by user decision; this does not retroactively validate the solver or the mechanism.

Figure status: selected generated figures, data, and plotting scripts under `paper/figures/fig01`, `paper/figures/fig02`, `paper/figures/fig03`, and `paper/figures/fig09` are accepted as the initial paper-result source set. Reduced Fig. 1/2/3/9 workflow smoke checks through `scan_optimized.py` remain wiring checks only. New figure work should focus on source mapping, caption-bounded claims, explanatory schematics, observable definitions, controls, and provenance rather than unconstrained new simulations.

Manuscript status: paper-results production is active. The manuscript draft is still skeletal; final writing remains evidence-bounded and must not imply that candidate models or imported results are newly validated in this repository.

This document is a project-control snapshot for GPT and Codex workflows. It summarizes the current factual state of the repository without promoting candidate claims.

Stage details are tracked in `docs/stages/stage_index.md`.

## Workflow Structure

Current workflow policy:

* Formality only at state transitions.
* Physics-first everywhere else.
* Use concrete task names first; internal anchors such as `G6_figures` are secondary labels.
* Use full TASK files and CODEX reports for repository edits, verification runs, and state transitions.
* Use lightweight physics notes for non-state-changing theoretical reasoning.

## Production Figure Policy

The paper-results production state is authorized to reuse existing `paper/figures/` assets, with the following boundaries:

1. Reused figures are paper-production assets, not newly validated evidence.
2. Every manuscript figure must have a source path, script path, data path or provenance note, and claim boundary.
3. Captions must use bounded language when a figure depends on migrated numerical results or unreproduced source data.
4. New figures should first fill presentation and evidentiary gaps: mechanism schematic, cycle phase montage, front/barrier observable definition, control comparison, and convergence/provenance support.
5. No result should be moved into `docs/validated/` unless a later explicit validation gate records evidence and user approval.

## Active Paper Figure Source Set

The initial production figure set is:

1. `paper/figures/fig01/`: homogeneous bifurcation, leading eigenvalues, dispersion relation, stability maps, and period/eigenvalue diagnostics.
2. `paper/figures/fig02/`: PDE regime maps on `(Bi_T, S_chi)` and `(Bi_T, Da)`, period map, and peak polymer-fraction map.
3. `paper/figures/fig03/`: regime-resolved kymographs and derived spatial/front diagnostics at representative regimes.
4. `paper/figures/fig09/`: source-draft Fig. 7 spinodal demonstration, retained as a supplementary or appendix-style figure unless the manuscript needs it in the main text.

Detailed figure-production planning is tracked in `docs/manuscript/paper_results_figure_plan.md` and the updated `docs/manuscript/figure_blueprint.md`.

## Required New Images

The current `paper/figures/` assets do not fully cover the manuscript's explanatory and evidence-boundary needs. The production phase should add:

1. Mechanism schematic: reaction, heat release, LCST collapse, transport/accessibility barrier, reactant starvation, cooling, and reopening in one cycle.
2. Representative cycle montage: 4--6 time snapshots from one oscillation showing `J`, `theta`, `u`, accessibility or reaction rate, and the moving collapsed skin/front.
3. Front/barrier observable definition panel: annotated profile defining front position, collapsed-skin thickness, barrier strength, reactant penetration depth, and phase lag.
4. Control comparison figure: baseline versus no reaction, no LCST coupling, no barrier, and possibly strict-chi/current-volume-source sensitivity.
5. Convergence/provenance support figure or supplementary panel: grid/timestep/source-cache lineage, clipping/floor diagnostics, and source path mapping for reused results.
6. Optional model architecture graphic: state variables, fluxes, boundary conditions, and closures, if the model section reads too text-heavy.

## Completed Pre-Production Work

* Research Idea Brief accepted by the user.
* Literature / Novelty Mapping accepted by the user for entry into Model Specification.
* Idea log, project brief, open questions, hypotheses, literature map, novelty framing, prior-art risk matrix, and frozen corpus created.
* Model A candidate summary exists as exploratory background only.
* The active derivation file has been replaced by migrated Appendix A--B material.
* `docs/rendered/initial_model_derivation.pdf` has been generated from the derivation source.
* Selected `paper_latest` assets were imported by PR `#7` and recorded in `docs/reports/exploration/CODEX-REPORT-paper-latest-migration.md`, `paper/paper_latest_provenance.md`, and `paper/paper_latest_migration_manifest.tsv`.
* Migration hygiene was resolved by PR `#8`, including `pypdf` declaration, composite figure smoke tests, LaTeX figure path cleanup, dirty-source provenance, and large-cache deduplication.
* GPT review of the merged migration is recorded in `docs/reports/exploration/GPT-REVIEW-paper-latest-migration.md`.
* The legacy CPU solver model has been audited as migrated source material in `paper/solver/paper_latest_cpu/SOLVER_MODEL_AUDIT.md`.
* Issue #13 created a candidate canonical CPU solver scaffold in `paper/solver/canonical_cpu/` with explicit model branches.
* Issue #15 finalized candidate canonical default branch choices as reference-volume source scaling, effective-osmotic chi, normalized transport/accessibility closure, canonical-consistent floors, retained cell-center Robin boundary scheme, and no enthalpy advection.
* Issue #20 switched the official paper-reproduction route to `paper.solver.official_paper_solver`, which invokes `paper/solver/paper_latest_cpu/scan_optimized.py`, and added reduced Fig. 1/2/3/9 workflow smoke outputs under `results/figure_smoke_scan_optimized/`.
* On 2026-06-11 the user authorized entering paper-results production and continuing with `paper/figures/` as the initial result source set.
* No model or claim has been promoted to `docs/validated/`.

## Active Blockers and Limitations

### Production-language blockers

These do not block figure production, but they constrain manuscript claims and captions:

1. The replaced Appendix A--B derivation still needs scientific review before being described as a finalized model derivation.
2. Reconcile `J,u,theta,mu` notation with the migrated conservative variables `J,W=Ju,theta,m` in the manuscript.
3. Audit free-surface reactant flux signs using the integral conservation law before relying on sign-sensitive mechanistic claims.
4. Decide whether `m_b` remains explicit or `mu_b=0` is used as a global convention.
5. Audit whether `chi_1` is a strict free-energy derivative parameter or an effective osmotic interaction parameter.
6. Clearly state current-coordinate versus reference-coordinate material coefficient conventions.
7. Report accessibility, diffusivity, and mobility suppression functions, including floors and clipping, when they affect reused numerical figures.
8. Treat neglected enthalpy advection and any small-parameter assumptions as assumptions, not established consequences.
9. Keep homogeneous stability as a diagnostic unless and until the nonlinear spatial mechanism is independently established.

### Official scan_optimized paper-route limitations

1. Reduced Fig. 1/2/3/9 smoke checks are wiring checks only and do not establish physical accuracy, convergence, or figure validity.
2. The migrated `scan_optimized.py` path remains the official paper-reproduction route for production, but it is not a validated numerical implementation.
3. Existing figure-local solver copies are frozen provenance, not active solver definitions.
4. `results/solver_smoke/` outputs are non-evidence technical checks and do not establish oscillation, convergence, or front/barrier mechanism.
5. Candidate front/barrier observables exist in `paper/solver/canonical_cpu/evidence.py`, but they require manuscript-level acceptance and consistent use before becoming final figure definitions.

## Active Work Plan

Use concrete task names. Internal anchors may be added only for ordering.

1. Map Existing `paper/figures` Assets to Manuscript Figures.
2. Add Missing Mechanism Schematic and Observable-Definition Images.
3. Prepare Control and Provenance Supplementary Figures.
4. Draft Evidence-Bounded Result Captions for Fig. 1/2/3 and Supplementary Fig. 9.
5. Update `paper/main.tex` to include result figures only after figure paths, captions, and claim boundaries are recorded.

Detailed task files are tracked under `docs/tasks/production/`.

## Non-Bypassable Gates

* Do not move candidate material into `docs/validated/` before sanity checks and evidence are recorded.
* Do not treat migrated CPU solver behavior as verified repository numerics.
* Do not treat issue #20 reduced figure smoke outputs as numerical validation or paper evidence.
* Do not describe reused `paper/figures/` assets as newly reproduced unless a later task reruns and records reproduction checks.
* Do not treat numerical oscillation as evidence without grid/timestep checks and control cases unless the manuscript explicitly frames the figure as reused, provisional, or source-draft evidence.
* Do not draft strong manuscript novelty claims before literature, model, and claim-evidence matrices are populated and reviewed.
* Do not treat source appendix numerical notes as reproduced evidence until verified in this repo.

Promotion gates:

* Research Idea Brief exit (`G0_idea_brief`): completed.
* Literature / Novelty Mapping exit (`G1_literature`): completed for Model Specification entry.
* Model Specification exit (`G2_model`): not completed as a validation gate; superseded for paper-results production by user decision.
* Figure Evidence / Paper Results Production (`G6_figures`): active; requires figure-source mapping, evidence-bounded captions, and explicit status labels for reused assets.
* `docs/validated/`: requires sanity checks, explicit evidence, and updated claim-evidence records.
* Results: may be produced from `paper/figures/` under the current user-authorized production policy; validated-result language remains blocked.
* Figures: may be assembled for paper production if clearly source-mapped and claim-bounded.
* Manuscript drafting: may proceed for result sections after figure blueprint and source mapping are updated.
* Production tasks: active for paper figure and result-section preparation.

## Source-of-Truth Links

* `README.md`
* `AGENTS.md`
* `docs/project_state.md`
* `docs/workflow_eval.md`
* `docs/00_idea_log.md`
* `docs/01_project_brief.md`
* `docs/02_open_questions.md`
* `docs/03_hypotheses.md`
* `docs/04_literature_map.md`
* `docs/05_novelty_framing.md`
* `docs/06_prior_art_risk_matrix.md`
* `docs/07_g1_frozen_corpus.md`
* `docs/stages/stage_index.md`
* `docs/stages/06_figures/gate.md`
* `docs/claims/candidate_claim_evidence.md`
* `docs/model_candidates/model_A_initial_lcst_transport_barrier.md`
* `docs/derivations/initial_model_derivation.tex`
* `docs/validated/model_spec.md`
* `docs/validated/claim_evidence.md`
* `docs/manuscript/figure_blueprint.md`
* `docs/manuscript/paper_results_figure_plan.md`
* `docs/tasks/production/TASK-enter-paper-results-production.md`
* `docs/reports/production/CODEX-REPORT-enter-paper-results-production.md`
* `paper/paper_latest_provenance.md`
* `paper/paper_latest_migration_manifest.tsv`
* `paper/solver/paper_latest_cpu/SOLVER_MODEL_AUDIT.md`
* `paper/solver/official_paper_solver.py`
* `paper/solver/run_figure_smoke_checks.py`
* `paper/solver/canonical_cpu/README.md`
* `paper/solver/canonical_cpu/solver.py`
* `results/figure_smoke_scan_optimized/figure_smoke_summary.json`

## Update Protocol

Update this file whenever a task changes the project stage, blocker list, validation status, next recommended task, or workflow policy. Keep entries factual and repository-based. If evidence is missing, record the item as pending rather than inferring success.
