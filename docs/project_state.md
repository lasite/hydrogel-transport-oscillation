# Project State

## Current Stage

Stage: Idea / Early Exploration

Substage: Initial candidate model ingested; sanity check pending

Model status: candidate only, not validated

Numerics status: no production PDE solver; no verified simulation

Manuscript status: blueprint/skeleton only; no validated results for writing

This document is a project-control snapshot for GPT and Codex workflows. It summarizes the current factual state of the repository without promoting candidate claims.

## Completed Work

* Idea log and project brief created.
* Open questions and hypotheses created.
* Model A candidate summary created.
* Initial derivation ingested into `docs/derivations/initial_model_derivation.tex`.
* EXP-001 report created.
* Derivation build succeeded in EXP-001.
* `docs/rendered/initial_model_derivation.pdf` has been generated from the derivation source.
* No model or claim has been promoted to `docs/validated/`.

## Active Blockers

* `EXP-002-sanity-check-candidate-model` not completed.
* Literature map not populated.
* Homogeneous ODE limit incomplete.
* Boundary-condition sign convention unresolved.
* Material functions not fully specified.
* Front/barrier observables not finalized.
* Source appendix numerical claims not independently reproduced.
* No verified numerical simulation.
* No claim-evidence item validated.
* Current local quickcheck is blocked at the pytest step unless `pytest` is installed in the active Python environment.

## Next Recommended Tasks

1. Run `EXP-002-sanity-check-candidate-model`.
2. Create or run a literature-map task after or alongside sanity checking.
3. Derive the homogeneous ODE limit.
4. Audit boundary-condition signs.
5. Define front/barrier observables before numerical validation.
6. Only then design minimal numerical verification tasks.

## Non-Bypassable Gates

* Do not move candidate material into `docs/validated/` before sanity checks and evidence are recorded.
* Do not write a production PDE solver before the model is sanity-checked.
* Do not treat numerical oscillation as evidence without grid/timestep checks and control cases.
* Do not draft strong manuscript claims before literature matrix and claim-evidence matrix are populated.
* Do not treat source appendix numerical notes as reproduced evidence until verified in this repo.

Promotion gates:

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
* `docs/model_candidates/model_A_initial_lcst_transport_barrier.md`
* `docs/derivations/initial_model_derivation.tex`
* `docs/reports/exploration/CODEX-REPORT-EXP-001.md`
* `docs/validated/model_spec.md`
* `docs/validated/claim_evidence.md`

## Update Protocol

Update this file whenever a task changes the project stage, blocker list, validation status, or next recommended task. Keep entries factual and repository-based. If evidence is missing, record the item as pending rather than inferring success.
