# Project State

## Current Stage

Stage: Model Specification

Internal anchor: `G2`

Previous stages:

* Research Idea Brief (`G0`) completed after user accepted the project brief, central hypothesis, candidate claims, and uncertainty list.
* Literature / Novelty Mapping (`G1`) completed after user accepted the novelty framing and prior-art risk matrix; the frozen literature corpus was created for Model Specification.

Substage: root-cause diagnosis after the failed convergence/control evidence
attempt completed; evidence not ready.

Model status: candidate only. The active long derivation source at `docs/derivations/initial_model_derivation.tex` now mechanically copies the migrated Appendix A `Model Construction` and Appendix B `Nondimensionalization` material from `paper/appendix/appendix.tex`. The material has not yet received ChatGPT scientific review and no model is validated.

Numerics status: final canonical CPU solver path exists, and the first formal convergence/control evidence attempt has been run under `results/evidence_convergence_control/`. The evidence attempt did not find a clipping-free oscillatory attractor with at least five complete post-transient cycles in the bounded `Da x Bi_T` search, so readiness is `not evidence ready`. Issue #18 then ran bounded root-cause diagnostics under `results/root_cause_missing_oscillations/`; the conclusion label is `root cause partially identified`. The dominant diagnosis is that geometric collapse can appear without a sufficiently strong functional `A,D,M` barrier at the clipping-free reference, while stronger forcing tends to enter clipping/projection. The migrated CPU script under `paper/solver/paper_latest_cpu/` is preserved as source/provenance material only. The final canonical CPU solver path under `paper/solver/canonical_cpu/` uses the issue #15 defaults `source_scaling = reference_volume`, `chi_closure = effective_osmotic_chi`, `transport_closure = normalized_porosity_power`, `floor_scheme = canonical_consistent`, `boundary_scheme = cell_center_robin`, and `enthalpy_advection = false`. The issue #16 and issue #18 outputs are not manuscript-ready evidence and do not open production parameter scans or figure regeneration.

Figure status: selected generated figures, data, and plotting scripts have been imported as exploratory source assets. Migration hygiene resolved the missing `pypdf` dependency and composite figure smoke tests now pass as repository assembly checks only; these checks do not validate the figure data or numerical results.

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
* Issue #16 generated the first convergence/control evidence attempt under `results/evidence_convergence_control/`. The bounded search produced no acceptable oscillatory working point; the selected clipping-free reference was non-oscillatory; required separate no-accessibility and no-diffusivity/permeability controls remain unavailable in the final solver branch set.
* Issue #18 generated bounded root-cause diagnostics under `results/root_cause_missing_oscillations/`. Diagnostic-only branches separate accessibility, diffusivity, mobility, transport, and `J^beta R` source scaling effects without changing canonical defaults. The root cause was partially identified as weak or late functional barrier formation in the clean reference plus clipping-contaminated high-amplitude regimes.
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

### Final canonical CPU solver blockers

The final canonical CPU solver path improves auditability but is not a
validated numerical implementation. Current blockers before paper evidence:

1. The issue #16 bounded `Da x Bi_T` search did not find a clipping-free oscillatory attractor with at least five complete post-transient cycles.
2. The canonical default point is non-oscillatory and reports clipping/floor interventions, so it cannot be used as paper evidence.
3. The selected clipping-free reference point is non-oscillatory across `N = 51, 101, 201` and time/tolerance checks.
4. Issue #18 diagnostic branches show that geometric collapse can overstate functional barrier formation: at the clipping-free reference, the geometric skin reaches the full domain while the functional `A,D,M` skin remains zero under the diagnostic threshold.
5. Stronger forcing or supply can create high-amplitude excursions, but those cases activate clipping/projection and cannot be mechanism evidence.
6. The final canonical path retains the cell-center Robin boundary approximation; closed-domain inventory and sign tests pass, but face-value reconstruction remains a possible later accuracy upgrade.
7. Existing figure-local solver copies are frozen provenance, not active solver definitions.
8. `results/solver_smoke/` outputs are non-evidence technical checks and do not establish oscillation, convergence, or front/barrier mechanism.

## Active Work Plan

Use concrete task names. Internal anchors may be added only for ordering.

1. Request ChatGPT Scientific Review of Replaced Model A Derivation.
2. Request ChatGPT Review of the Legacy and Final Canonical CPU Solver Audit.
3. Request human/ChatGPT decision on the issue #18 root-cause diagnosis.
4. Decide whether to revise the functional barrier closure, define a sharper barrier observable, or reduce the model to a smaller diagnostic system before any further search.
5. Rebuild the Model Specification Blocker List from derivation and solver-review results.
6. Refine front/barrier observables only after a plausible oscillatory working point exists.

Detailed task files are tracked under `docs/tasks/exploration/`.

## Non-Bypassable Gates

* Do not move candidate material into `docs/validated/` before sanity checks and evidence are recorded.
* Do not write a production PDE solver before the model is sanity-checked.
* Do not treat migrated CPU solver behavior as verified repository numerics.
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
* `paper/solver/canonical_cpu/README.md`
* `paper/solver/canonical_cpu/solver.py`
* `docs/reports/exploration/MULTIAGENT-REVIEW-paper-solver.md`
* `docs/reports/exploration/CODEX-REPORT-convert-legacy-solver-to-paper-grade.md`
* `docs/reports/exploration/MULTIAGENT-REVIEW-final-paper-solver.md`
* `docs/reports/exploration/CODEX-REPORT-finalize-paper-solver-reference-source-effective-chi.md`
* `results/evidence_convergence_control/suite_summary.json`
* `docs/reports/exploration/MULTIAGENT-REVIEW-convergence-control-evidence.md`
* `docs/reports/exploration/CODEX-REPORT-formal-convergence-control-evidence.md`
* `results/root_cause_missing_oscillations/suite_summary.json`
* `docs/reports/exploration/MULTIAGENT-REVIEW-root-cause-missing-oscillations.md`
* `docs/reports/exploration/CODEX-REPORT-root-cause-missing-oscillations.md`

## Update Protocol

Update this file whenever a task changes the project stage, blocker list, validation status, next recommended task, or workflow policy. Keep entries factual and repository-based. If evidence is missing, record the item as pending rather than inferring success.
