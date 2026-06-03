# Project State

## Current Stage

Stage: Model Specification

Internal anchor: `G2`

Previous stages:

* Research Idea Brief (`G0`) completed after user accepted the project brief, central hypothesis, candidate claims, and uncertainty list.
* Literature / Novelty Mapping (`G1`) completed after user accepted the novelty framing and prior-art risk matrix; the frozen literature corpus was created for Model Specification.

Substage: post-`paper_latest` source-material import and triage.

Model status: candidate only. The repository now contains migrated prior-draft model text, homogeneous/stability diagnostic text, appendices, selected figures, figure data, plotting scripts, and CPU solver source from `paper_latest`, but these materials have not been reconciled with Model A and no model is validated.

Numerics status: no production PDE solver; no verified simulation. The migrated CPU script under `paper/solver/paper_latest_cpu/` is preserved as source/provenance material only.

Figure status: selected generated figures, data, and plotting scripts have been imported as exploratory source assets. Composite figure generation is not yet verified in this repository because the migration report records plotting smoke-test failures at PDF assembly due to missing `pypdf`.

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
* Initial derivation exists as exploratory background only in `docs/derivations/initial_model_derivation.tex`.
* EXP-001 report created; derivation build succeeded in EXP-001.
* `docs/rendered/initial_model_derivation.pdf` has been generated from the derivation source.
* Selected `paper_latest` assets have been imported by PR `#7` and recorded in `docs/reports/exploration/CODEX-REPORT-paper-latest-migration.md`, `paper/paper_latest_provenance.md`, and `paper/paper_latest_migration_manifest.tsv`.
* GPT review of the merged migration is recorded in `docs/reports/exploration/GPT-REVIEW-paper-latest-migration.md`.
* No model or claim has been promoted to `docs/validated/`.

## Superseded or Historical Work

The previous ChatGPT review at `docs/reports/exploration/GPT-REVIEW-G2-001.md` is retained as a historical artifact only. It is superseded by the workflow reset and must not be treated as current Model Specification progress, accepted blocker state, or validated evidence.

The imported `paper_latest` draft material is historical source material. It must not be treated as a current manuscript, validated model, reproduced numerical evidence, or accepted claim-evidence package.

## Active Blockers

### Migration-hygiene blockers

These must be resolved before the imported source material is clean enough to serve as a stable reference for Model Specification.

1. Migrated LaTeX fragments still contain figure paths that do not resolve from the new repository layout without an external wrapper or `\graphicspath` convention.
2. Figure composite plotting smoke tests failed because `pypdf` is missing from the current environment or dependency declaration.
3. The source `paper_latest` tree was dirty during migration; the exact dirty-state provenance is not fully reconstructable from the recorded source HEAD alone.
4. Two near-100 MB cache files appear duplicated under Figure 2 and Figure 3 bundles and require a repository-size decision.
5. The migration report metadata still needs the final merged commit information.
6. The title mismatch between requested `III. LINEAR STABILITY ANALYSIS` and migrated `III. HOMOGENEOUS STABILITY DIAGNOSTIC` needs explicit mapping or correction.

### Model-Specification blockers

The blocker list must be rebuilt from a fresh reconciliation of Model A and the migrated draft. Known issues to include in that review are:

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

## Active Work Plan

Use concrete task names. Internal anchors may be added only for ordering.

1. Resolve `paper_latest` Migration Hygiene.
2. Reconcile Migrated Draft Model with Model A.
3. Rebuild the Model Specification Blocker List.
4. Define Minimum Front/Barrier Observables.
5. Prepare Minimal Numerical Verification Design only after the Model Specification gate passes.

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
* `docs/reports/exploration/GPT-REVIEW-paper-latest-migration.md`
* `paper/paper_latest_provenance.md`
* `paper/paper_latest_migration_manifest.tsv`

## Update Protocol

Update this file whenever a task changes the project stage, blocker list, validation status, next recommended task, or workflow policy. Keep entries factual and repository-based. If evidence is missing, record the item as pending rather than inferring success.
