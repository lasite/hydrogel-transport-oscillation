# Project State

## Current Stage

Stage: G2 -- Model Specification

Previous stages:

* G0 -- Idea Brief completed after user accepted the project brief, central hypothesis, candidate claims, and uncertainty list.
* G1 -- Literature / Novelty Mapping completed after user accepted the novelty framing and prior-art risk matrix; G1 frozen corpus created.

Substage: Model A specification and sanity-check preparation against G1 novelty-risk constraints.

Model status: candidate notes exist only; model-review/specification work is now active, but no model is validated.

Numerics status: no production PDE solver; no verified simulation.

Manuscript status: idea/project-brief level only; no validated results for writing.

G2 scope: convert the candidate Model A material into an auditable model specification. G2 reviews equations, variables, material functions, units, limiting cases, boundary conditions, and minimum observables. G2 does not perform production PDE implementation, numerical verification, figure generation, or manuscript drafting.

This document is a project-control snapshot for GPT and Codex workflows. It summarizes the current factual state of the repository without promoting candidate claims.

Stage details are tracked in docs/stages/stage_index.md.

## Completed Work

* G0 Idea Brief accepted by the user.
* G1 Literature / Novelty Mapping accepted by the user for entry into G2.
* Idea log and project brief created.
* One-sentence central hypothesis recorded in `docs/01_project_brief.md`.
* Candidate hypotheses and claims recorded in `docs/03_hypotheses.md`.
* Open questions recorded in `docs/02_open_questions.md`.
* `docs/04_literature_map.md` populated with G1 literature map v0.1.
* G1 literature map v0.1 includes a 50-item candidate corpus, mechanism-family map, novelty-risk matrix, and allowed/forbidden novelty language.
* `docs/05_novelty_framing.md` created from the user-provided research-significance memo and G1 literature-map constraints.
* `docs/06_prior_art_risk_matrix.md` created to map candidate novelty claims to nearest prior-art families, risk levels, required narrowing, and later evidence requirements.
* `docs/07_g1_frozen_corpus.md` created as the retained core corpus for G2 model specification.
* Model A candidate summary exists as exploratory background only.
* Initial derivation exists as exploratory background only in `docs/derivations/initial_model_derivation.tex`.
* EXP-001 report created.
* Derivation build succeeded in EXP-001.
* `docs/rendered/initial_model_derivation.pdf` has been generated from the derivation source.
* Project state control document created.
* Stage details are tracked in `docs/stages/stage_index.md`.
* No model or claim has been promoted to `docs/validated/`.

## Active Blockers

* Model A has not yet been sanity-checked against G1 novelty-risk constraints.
* Homogeneous ODE / well-mixed limit incomplete.
* Boundary-condition sign convention unresolved.
* Material functions not fully specified.
* Reaction accessibility, diffusivity, permeability, and poroelastic collapse are not yet fully separated at the specification level.
* Front/barrier observables not finalized.
* No claim-evidence item validated; validation is outside G2 until evidence is recorded.

## Next Recommended Tasks

1. Run a G2 model-specification / sanity-check task based on `docs/tasks/exploration/EXP-002-sanity-check-candidate-model.md` or its updated successor.
2. Audit variable and parameter definitions in `docs/model_candidates/model_A_initial_lcst_transport_barrier.md` and `docs/derivations/initial_model_derivation.tex`.
3. Derive, scope, or explicitly mark incomplete the homogeneous ODE / well-mixed limit.
4. Audit boundary-condition signs and physical meanings.
5. Define minimum front/barrier observables required to test the transport-barrier mechanism.
6. Do not promote any model or claim into `docs/validated/` until G2 evidence is recorded.

## Non-Bypassable Gates

* Do not move candidate material into `docs/validated/` before sanity checks and evidence are recorded.
* Do not write a production PDE solver before the model is sanity-checked.
* Do not treat numerical oscillation as evidence without grid/timestep checks and control cases.
* Do not draft strong manuscript novelty claims before literature, model, and claim-evidence matrices are populated and reviewed.
* Do not treat source appendix numerical notes as reproduced evidence until verified in this repo.

Promotion gates:

* G0 exit: completed; requires a project brief, central hypothesis, candidate claims, and visible uncertainty list. G0 does not require Codex, TASK files, CODEX reports, Makefile verification, or CI.
* G1 exit: completed for G2 entry; requires populated literature map, novelty framing, prior-art risk matrix, and frozen retained corpus. Remaining DOI/BibTeX cleanup is required before manuscript drafting.
* G2 exit: requires a model specification, sanity-check report, defined variables/parameters, limiting cases, boundary-condition audit, material-function audit, and minimum observables. G2 does not validate numerical claims.
* `docs/validated/`: requires sanity checks, explicit evidence, and updated claim-evidence records.
* Numerical implementation: requires a sanity-checked model, boundary-condition audit, and defined observables.
* Results: require reproducible scripts or notebooks, control cases, and convergence checks.
* Figures: require validated or clearly labeled exploratory outputs.
* Manuscript drafting: requires populated literature and claim-evidence matrices.
* Production tasks: require at least one validated target claim or a clearly scoped manuscript-production need.

## Source-of-Truth Links

* `README.md`
* `AGENTS.md`
* `docs/00_idea_log.md`
* `docs/01_project_brief.md`
* `docs/02_open_questions.md`
* `docs/03_hypotheses.md`
* `docs/04_literature_map.md`
* `docs/05_novelty_framing.md`
* `docs/06_prior_art_risk_matrix.md`
* `docs/07_g1_frozen_corpus.md`
* `docs/stages/stage_index.md`
* `docs/stages/00_idea/gate.md`
* `docs/stages/01_literature/gate.md`
* `docs/stages/02_model/gate.md`
* `docs/model_candidates/model_A_initial_lcst_transport_barrier.md`
* `docs/derivations/initial_model_derivation.tex`
* `docs/reports/exploration/CODEX-REPORT-EXP-001.md`
* `docs/tasks/TASK-TEMPLATE.md`
* `docs/reports/CODEX-REPORT-TEMPLATE.md`
* `docs/validated/model_spec.md`
* `docs/validated/claim_evidence.md`

## Update Protocol

Update this file whenever a task changes the project stage, blocker list, validation status, or next recommended task. Keep entries factual and repository-based. If evidence is missing, record the item as pending rather than inferring success.
