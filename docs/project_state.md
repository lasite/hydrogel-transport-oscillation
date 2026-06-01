# Project State

## Current Stage

Stage: Model Specification

Internal anchor: `G2`

Previous stages:

* Research Idea Brief (`G0`) completed after user accepted the project brief, central hypothesis, candidate claims, and uncertainty list.
* Literature / Novelty Mapping (`G1`) completed after user accepted the novelty framing and prior-art risk matrix; the frozen literature corpus was created for Model Specification.

Substage: ChatGPT model review completed; P0 model-specification blockers identified.

Model status: candidate notes exist only; model-review/specification work is active, but no model is validated.

Numerics status: no production PDE solver; no verified simulation.

Manuscript status: idea/project-brief level only; no validated results for writing.

Model Specification scope: convert the candidate Model A material into an auditable model specification. This stage reviews equations, variables, material functions, units, limiting cases, boundary conditions, and minimum observables. It does not perform production PDE implementation, numerical verification, figure generation, or manuscript drafting.

This document is a project-control snapshot for GPT and Codex workflows. It summarizes the current factual state of the repository without promoting candidate claims.

Stage details are tracked in `docs/stages/stage_index.md`.

## Workflow Structure

Current workflow policy:

* Formality only at state transitions.
* Physics-first everywhere else.
* Use concrete task names first; internal anchors such as `G2` are secondary labels.
* Use full TASK files and CODEX reports for repository edits, verification runs, and state transitions.
* Use lightweight physics notes for non-state-changing theoretical reasoning.

This workflow policy changes only the project structure and working rules. It does not advance the model, validate claims, or open numerical-production work.

## Completed Work

* Research Idea Brief accepted by the user.
* Literature / Novelty Mapping accepted by the user for entry into Model Specification.
* Idea log, project brief, open questions, hypotheses, literature map, novelty framing, prior-art risk matrix, and frozen corpus created.
* Model A candidate summary exists as exploratory background only.
* Initial derivation exists as exploratory background only in `docs/derivations/initial_model_derivation.tex`.
* EXP-001 report created; derivation build succeeded in EXP-001.
* `docs/rendered/initial_model_derivation.pdf` has been generated from the derivation source.
* ChatGPT model review created at `docs/reports/exploration/GPT-REVIEW-G2-001.md`.
* No model or claim has been promoted to `docs/validated/`.

## Active Blockers

* Free-surface reactant boundary conditions are inconsistent between full flux form and compact form.
* Continuous boundary conditions for the gradient-energy term are not explicitly specified.
* The mixing chemical potential must be reaudited for composition-dependent `chi(theta, phi)`.
* Homogeneous ODE / well-mixed dynamical limit is incomplete.
* The admissible model domain is not fully stated, including `J >= phi_p0`, `0 < phi <= 1`, and `1 + epsilon_T theta > 0`.
* Front/barrier observables are not finalized.
* Material functions `M(J,theta)`, `D(J,theta)`, `K(J)`, and `C(J)` are not fully specified.
* Reaction accessibility, diffusivity, permeability, and poroelastic collapse are not yet fully separated at the specification level.
* No claim-evidence item validated; validation is outside Model Specification until evidence is recorded.

## Next Recommended Tasks

Use concrete task names. Internal anchors may be added only for ordering.

1. Resolve Free-Surface Reactant Boundary-Condition Convention.
2. Add Continuous Boundary Conditions for Gradient-Energy Regularization.
3. Reaudit Composition-Dependent Mixing Chemical Potential.
4. Derive or Scope the Homogeneous Well-Mixed Limit.
5. Define the Admissible Model Domain.
6. Define Front and Barrier Observables.
7. Do not promote any model or claim into `docs/validated/` until Model Specification evidence is recorded.

## Non-Bypassable Gates

* Do not move candidate material into `docs/validated/` before sanity checks and evidence are recorded.
* Do not write a production PDE solver before the model is sanity-checked.
* Do not treat numerical oscillation as evidence without grid/timestep checks and control cases.
* Do not draft strong manuscript novelty claims before literature, model, and claim-evidence matrices are populated and reviewed.
* Do not treat source appendix numerical notes as reproduced evidence until verified in this repo.

Promotion gates:

* Research Idea Brief exit (`G0`): completed; requires a project brief, central hypothesis, candidate claims, and visible uncertainty list.
* Literature / Novelty Mapping exit (`G1`): completed for Model Specification entry; requires populated literature map, novelty framing, prior-art risk matrix, and frozen retained corpus.
* Model Specification exit (`G2`): requires a model specification, sanity-check report, defined variables/parameters, limiting cases, boundary-condition audit, material-function audit, and minimum observables. It does not validate numerical claims.
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
* `docs/reports/CODEX-REPORT-TEMPLATE.md`

## Update Protocol

Update this file whenever a task changes the project stage, blocker list, validation status, next recommended task, or workflow policy. Keep entries factual and repository-based. If evidence is missing, record the item as pending rather than inferring success.
