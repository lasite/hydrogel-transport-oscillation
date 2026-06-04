# Project State

## Current Stage

Stage: Model Specification

Internal anchor: `G2`

Previous stages:

* Research Idea Brief (`G0`) completed after user accepted the project brief, central hypothesis, candidate claims, and uncertainty list.
* Literature / Novelty Mapping (`G1`) completed after user accepted the novelty framing and prior-art risk matrix; the frozen literature corpus was created for Model Specification.

Substage: official paper-reproduction route switched to migrated `scan_optimized.py`; reduced smoke wiring checks completed; formal evidence generation pending.

Model status: candidate only. The active long derivation source at `docs/derivations/initial_model_derivation.tex` now mechanically copies the migrated Appendix A `Model Construction` and Appendix B `Nondimensionalization` material from `paper/appendix/appendix.tex`. The material has not yet received ChatGPT scientific review and no model is validated.

Numerics status: the official paper-reproduction route now uses `paper.solver.official_paper_solver`, which directly invokes the migrated `paper/solver/paper_latest_cpu/scan_optimized.py` script. Reduced Fig. 1/2/3/9 smoke checks exist under `paper/solver/run_figure_smoke_checks.py` and `results/figure_smoke_scan_optimized/`. These checks only confirm workflow wiring and expected artifact classes; they are not full-resolution reproduction, numerical validation, or paper evidence. The issue #15 candidate canonical CPU solver path under `paper/solver/canonical_cpu/` remains available for audit and regression context, but it is no longer the official paper-reproduction entry point.

Figure status: selected generated figures, data, and plotting scripts have been imported as exploratory source assets. Migration hygiene resolved the missing `pypdf` dependency and composite figure smoke tests now pass as repository assembly checks only. Issue #20 added reduced Fig. 1/2/3/9 workflow smoke checks through `scan_optimized.py`; these checks do not validate the figure data, numerical results, or mechanism claims.

Manuscript status: no current manuscript draft is active. The migrated `paper/sections/` and `paper/appendix/` files are fragments for audit and future reuse only, not an accepted manuscript.

Model Specification scope: convert the candidate Model A material and the imported `paper_latest` source material into a single auditable model specification. This stage reviews equations, variables, material functions, units, limiting cases, boundary conditions, and minimum observables. It does not perform production PDE implementation, numerical verification, parameter scans, evidence-backed figure generation, or manuscript drafting.

This document is a project-control snapshot for GPT and Codex workflows. It summarizes the current factual state of the repository without promoting candidate claims.

Stage details are tracked in `docs/stages/stage_index.md`.

## Workflow Structure

Current workflow policy:

* Formality only at state transitions.
* Physics-first everywhere else.
* Use concrete task names first; internal anchors such as `G2` are secondary labels.
* Use full TASK files and CODEX reports for repository edits, verification runs, and state transitions.
* Use lightweight physics notes for non-state-changing theoretical reasoning.

## Completed Pre-Model-Specification Work

* Research Idea Brief accepted by the user.
* Literature / Novelty Mapping accepted by the user for entry into Model Specification.
* Idea log, project brief, open questions, hypotheses, literature map, novelty framing, prior-art risk matrix, and frozen corpus created.
* Model A candidate summary exists as exploratory background only.
* The earlier EXP-001 derivation organization is retained as historical workflow context, but the active derivation file has now been replaced by migrated Appendix A--B material.
* EXP-001 report created; derivation build succeeded in EXP-001.
* `docs/rendered/initial_model_derivation.pdf` has been generated from the derivation source.
* Selected `paper_latest` assets have been imported by PR `#7` and recorded in `docs/reports/exploration/CODEX-REPORT-paper-latest-migration.md`, `paper/paper_latest_provenance.md`, and `paper/paper_latest_migration_manifest.tsv`.
* Migration hygiene was resolved by PR `#8`, including `pypdf` declaration, composite figure smoke tests, LaTeX figure path cleanup, dirty-source provenance, and large-cache deduplication.
* `docs/derivations/initial_model_derivation.tex` has been replaced with the migrated Appendix A--B model-construction and nondimensionalization source material for ChatGPT review.
* GPT review of the merged migration is recorded in `docs/reports/exploration/GPT-REVIEW-paper-latest-migration.md`.
* The legacy CPU solver model has been audited as migrated source material in `paper/solver/paper_latest_cpu/SOLVER_MODEL_AUDIT.md`, with opt-in diagnostics for clipping, positivity, surface fluxes, non-finite values, and full `Params` serialization.
* Issue #13 created a candidate canonical CPU solver scaffold in `paper/solver/canonical_cpu/`, with explicit model branches for source scaling, chi closure, transport closure, floors, boundary scheme, and diagnostic-only heat advection status.
* Issue #15 finalized the paper-solver default branch choices as reference-volume source scaling, effective-osmotic chi, normalized transport/accessibility closure, canonical-consistent floors, retained cell-center Robin boundary scheme, and no enthalpy advection. Legacy current-volume and strict-derivative branches remain only as non-canonical controls.
* Short non-evidence smoke outputs were written under `results/solver_smoke/` for grid/time/source-scaling and simple control checks. These outputs are technical smoke material only, not claim evidence.
* Issue #20 switched the official paper-reproduction route to `paper.solver.official_paper_solver`, which invokes `paper/solver/paper_latest_cpu/scan_optimized.py`, and added reduced Fig. 1/2/3/9 workflow smoke outputs under `results/figure_smoke_scan_optimized/`.
* No model or claim has been promoted to `docs/validated/`.

## Superseded or Historical Work

The previous ChatGPT review at `docs/reports/exploration/GPT-REVIEW-G2-001.md` is retained as a historical artifact only. It is superseded by the workflow reset and must not be treated as current Model Specification progress, accepted blocker state, or validated evidence.

The imported `paper_latest` draft material is historical source material. It must not be treated as a current manuscript, validated model, reproduced numerical evidence, or accepted claim-evidence package.

## Active Blockers

### Derivation-review blockers

These must be resolved before the replaced derivation can serve as the basis of a candidate model specification.

1. ChatGPT must scientifically review the replaced Appendix A--B derivation.
2. The review must check conserved variables, state-vector consistency, flux signs, boundary conditions, material functions, and nondimensional groups.
3. Any scientific issues found by review must remain candidate or unresolved until explicitly accepted by the user.

### Model-Specification blockers

The blocker list must be rebuilt from the ChatGPT review of the replaced derivation. Known issues to include in that review are:

1. Reconcile `J,u,theta,mu` notation with the migrated conservative variables `J,W=Ju,theta,m`.
2. Audit free-surface reactant flux signs using the integral conservation law.
3. Decide whether `m_b` remains explicit or `mu_b=0` is used as a global convention.
4. Audit the `chi(theta,phi)` derivative and whether `chi_1` is a strict free-energy parameter or an effective osmotic interaction parameter.
5. Audit current-coordinate versus reference-coordinate material coefficients.
6. Audit accessibility, diffusivity, and mobility suppression functions, including floors and clipping.
7. Justify or remove neglected enthalpy advection and any small-parameter assumptions.
8. Define front position, collapsed skin thickness, barrier strength, and minimum observables before numerical validation.
9. Keep homogeneous stability as a diagnostic unless and until the nonlinear spatial mechanism is independently established.

Standing constraints remain:

* No claim-evidence item is validated.
* Production PDE implementation remains blocked.
* Numerical verification remains blocked.
* Parameter scans remain blocked.
* Evidence-backed figure generation remains blocked.
* Manuscript drafting remains blocked.

### Legacy CPU solver blockers

The legacy CPU solver audit makes the existing code path more inspectable, but
the following issues remain blockers before any generated data can become
evidence:

1. Decide whether the canonical model keeps the legacy `v0` effective-osmotic-chi closure or branches to a strict-derivative closure.
2. Resolve whether `Da * J * R` is an acceptable current-volume source scaling for the intended immobilized-catalyst interpretation.
3. Treat `Pe_T` as inactive in the RHS unless a later task explicitly changes the model.
4. Report `logJ`, `phi`, and `u` clipping/floor interventions with any future numerical result.
5. Treat boundary exchange laws as cell-center Robin approximations until a boundary-condition audit accepts or replaces them.
6. Keep imported figure caches and solver-generated draft outputs unvalidated until reproduced with convergence and control cases.

### Official scan_optimized paper-route blockers

The official paper-reproduction route now invokes the migrated
`scan_optimized.py` script, but it is not a validated numerical
implementation. Current blockers before paper evidence:

1. The reduced Fig. 1/2/3/9 smoke checks are wiring checks only and do not establish physical accuracy, convergence, or figure validity.
2. The migrated `scan_optimized.py` path still needs scientific review against the active derivation before it can be treated as a numerical implementation of the candidate model.
3. The issue #15 candidate canonical CPU solver path is now superseded for paper reproduction, but remains historical audit context.
4. Transport/accessibility floors, clipping, and material-function assumptions must be reported with any future run.
5. Existing figure-local solver copies are frozen provenance, not active solver definitions.
6. `results/solver_smoke/` outputs are non-evidence technical checks and do not establish oscillation, convergence, or front/barrier mechanism.
7. Minimum front position, collapsed skin thickness, barrier strength, and phase-lag observables remain undefined for formal numerical validation.

## Active Work Plan

Use concrete task names. Internal anchors may be added only for ordering.

1. Request ChatGPT Scientific Review of Replaced Model A Derivation.
2. Request ChatGPT Review of the Legacy, candidate canonical, and official `scan_optimized.py` paper-route solver notes.
3. Rebuild the Model Specification Blocker List from derivation and solver-review results.
4. Define Minimum Front/Barrier Observables.
5. Decide whether formal convergence/control-case numerical verification should use the official `scan_optimized.py` route as-is, or first require a model-specification reconciliation task.

Detailed task files are tracked under `docs/tasks/exploration/`.

## Non-Bypassable Gates

* Do not move candidate material into `docs/validated/` before sanity checks and evidence are recorded.
* Do not write a production PDE solver before the model is sanity-checked.
* Do not treat migrated CPU solver behavior as verified repository numerics.
* Do not treat issue #20 reduced figure smoke outputs as numerical validation or paper evidence.
* Do not treat numerical oscillation as evidence without grid/timestep checks and control cases.
* Do not treat imported figure data or generated figures as evidence-backed results until reproduced or explicitly accepted under an evidence gate.
* Do not draft strong manuscript novelty claims before literature, model, and claim-evidence matrices are populated and reviewed.
* Do not treat source appendix numerical notes as reproduced evidence until verified in this repo.

Promotion gates:

* Research Idea Brief exit (`G0`): completed; requires a project brief, central hypothesis, candidate claims, and visible uncertainty list.
* Literature / Novelty Mapping exit (`G1`): completed for Model Specification entry; requires populated literature map, novelty framing, prior-art risk matrix, and frozen retained corpus.
* Model Specification exit (`G2`): requires a reconciled model specification, sanity-check report, defined variables/parameters, limiting cases, boundary-condition audit, material-function audit, and minimum observables. It does not validate numerical claims.
* `docs/validated/`: requires sanity checks, explicit evidence, and updated claim-evidence records.
* Numerical implementation: requires a sanity-checked model, boundary-condition audit, and defined observables.
* Results: require reproducible scripts or notebooks, control cases, and convergence checks.
* Figures: require validated or clearly labeled exploratory outputs.
* Manuscript drafting: requires populated literature and claim-evidence matrices.
* Production tasks: require at least one validated target claim or a clearly scoped manuscript-production need.

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
* `docs/stages/02_model/gate.md`
* `docs/notes/README.md`
* `docs/notes/PHYSICS-NOTE-TEMPLATE.md`
* `docs/claims/candidate_claim_evidence.md`
* `docs/model_candidates/model_A_initial_lcst_transport_barrier.md`
* `docs/derivations/initial_model_derivation.tex`
* `docs/validated/model_spec.md`
* `docs/validated/claim_evidence.md`
* `docs/tasks/TASK-TEMPLATE.md`
* `docs/tasks/exploration/TASK-resolve-paper-latest-migration-hygiene.md`
* `docs/tasks/exploration/TASK-reconcile-migrated-draft-model-with-model-A.md`
* `docs/reports/CODEX-REPORT-TEMPLATE.md`
* `docs/reports/exploration/CODEX-REPORT-paper-latest-migration.md`
* `docs/reports/exploration/CODEX-REPORT-resolve-paper-latest-migration-hygiene.md`
* `docs/reports/exploration/CODEX-REPORT-replace-initial-model-derivation-from-paper-appendix.md`
* `docs/reports/exploration/CODEX-REPORT-audit-freeze-legacy-cpu-solver-model.md`
* `docs/reports/exploration/GPT-REVIEW-paper-latest-migration.md`
* `paper/paper_latest_provenance.md`
* `paper/paper_latest_migration_manifest.tsv`
* `paper/solver/paper_latest_cpu/SOLVER_MODEL_AUDIT.md`
* `paper/solver/official_paper_solver.py`
* `paper/solver/run_figure_smoke_checks.py`
* `paper/solver/canonical_cpu/README.md`
* `paper/solver/canonical_cpu/solver.py`
* `docs/reports/exploration/MULTIAGENT-REVIEW-paper-solver.md`
* `docs/reports/exploration/CODEX-REPORT-convert-legacy-solver-to-paper-grade.md`
* `docs/reports/exploration/MULTIAGENT-REVIEW-final-paper-solver.md`
* `docs/reports/exploration/CODEX-REPORT-finalize-paper-solver-reference-source-effective-chi.md`
* `results/figure_smoke_scan_optimized/figure_smoke_summary.json`
* `docs/tasks/exploration/TASK-use-scan-optimized-official-paper-solver.md`
* `docs/reports/exploration/CODEX-REPORT-use-scan-optimized-official-paper-solver.md`

## Update Protocol

Update this file whenever a task changes the project stage, blocker list, validation status, next recommended task, or workflow policy. Keep entries factual and repository-based. If evidence is missing, record the item as pending rather than inferring success.
