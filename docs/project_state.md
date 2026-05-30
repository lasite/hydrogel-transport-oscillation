# Project State

## Current Stage

Stage: G0 -- Idea Brief

Legacy scaffold label: Stage: Idea / Early Exploration

Substage: Workflow-protocol stabilization before model-gate work

Model status: candidate only, not validated

Numerics status: no production PDE solver; no verified simulation

Manuscript status: blueprint/skeleton only; no validated results for writing

Workflow protocol status: G0 hardening in progress; ChatGPT defines and reviews tasks, Codex implements only within TASK scope, and CODEX reports are required for handoff.

This document is a project-control snapshot for GPT and Codex workflows. It summarizes the current factual state of the repository without promoting candidate claims.

Stage details are tracked in docs/stages/stage_index.md.

## Completed Work

* Idea log and project brief created.
* Open questions and hypotheses created.
* Model A candidate summary created.
* Initial derivation ingested into `docs/derivations/initial_model_derivation.tex`.
* EXP-001 report created.
* Derivation build succeeded in EXP-001.
* `docs/rendered/initial_model_derivation.pdf` has been generated from the derivation source.
* Project state control document created.
* Stage details are tracked in `docs/stages/stage_index.md`.
* No model or claim has been promoted to `docs/validated/`.

## Active Blockers

* `EXP-002-sanity-check-candidate-model` not completed.
* G0 protocol hardening needs ChatGPT review before model-gate work resumes.
* Literature map not populated.
* Homogeneous ODE limit incomplete.
* Boundary-condition sign convention unresolved.
* Material functions not fully specified.
* Front/barrier observables not finalized.
* Source appendix numerical claims not independently reproduced.
* No verified numerical simulation.
* No claim-evidence item validated.
* Fresh checkouts need dependency setup before `make quickcheck`; use `make install` or an equivalent project environment setup.

## Next Recommended Tasks

1. Complete `TASK-G0-001` and record the CODEX report.
2. Ask ChatGPT to review the hardened G0 task/report protocol.
3. Exit G0 only after its gate criteria are satisfied and recorded.
4. Run `EXP-002-sanity-check-candidate-model` only after G0 exits or the user explicitly opens G2 model work.

## Non-Bypassable Gates

* Do not move candidate material into `docs/validated/` before sanity checks and evidence are recorded.
* Do not run model review while G0 protocol stabilization is active unless the user explicitly opens G2.
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
* `docs/tasks/TASK-TEMPLATE.md`
* `docs/reports/CODEX-REPORT-TEMPLATE.md`
* `docs/validated/model_spec.md`
* `docs/validated/claim_evidence.md`

## Update Protocol

Update this file whenever a task changes the project stage, blocker list, validation status, or next recommended task. Keep entries factual and repository-based. If evidence is missing, record the item as pending rather than inferring success.
