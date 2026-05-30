# Project State

## Current Stage

Stage: G0 -- Idea Brief

Legacy scaffold label: Stage: Idea / Early Exploration

Substage: ChatGPT-only conversion of idea into hypothesis and candidate claims

Model status: candidate notes exist only; no model-review task is currently recommended

Numerics status: no production PDE solver; no verified simulation

Manuscript status: idea/project-brief level only; no validated results for writing

G0 scope: ChatGPT organizes the initial idea into a project brief, central hypothesis, and candidate claims. Codex, TASK handoff, CODEX reports, Makefile verification, and implementation work are not required to complete G0.

This document is a project-control snapshot for GPT and Codex workflows. It summarizes the current factual state of the repository without promoting candidate claims.

Stage details are tracked in docs/stages/stage_index.md.

## Completed Work

* Idea log and project brief created.
* One-sentence central hypothesis recorded in `docs/01_project_brief.md`.
* Candidate hypotheses and claims recorded in `docs/03_hypotheses.md`.
* Open questions recorded in `docs/02_open_questions.md`.
* Model A candidate summary exists as exploratory background only.
* Initial derivation exists as exploratory background only in `docs/derivations/initial_model_derivation.tex`.
* EXP-001 report created.
* Derivation build succeeded in EXP-001.
* `docs/rendered/initial_model_derivation.pdf` has been generated from the derivation source.
* Project state control document created.
* Stage details are tracked in `docs/stages/stage_index.md`.
* No model or claim has been promoted to `docs/validated/`.

## Active Blockers

* G0 hypothesis/claim framing needs user or ChatGPT acceptance before the project moves to the next gate.
* `EXP-002-sanity-check-candidate-model` not completed, but this is a later model-gate blocker, not a G0 blocker.
* Literature map not populated, but this is a later literature/manuscript-risk task, not a G0 blocker.
* No claim-evidence item validated, but validation is outside G0.

## Next Recommended Tasks

1. Review `docs/01_project_brief.md` and `docs/03_hypotheses.md` as the G0 output.
2. If the hypothesis and candidate claims are accepted, mark G0 complete.
3. After G0 completion, explicitly choose the next active gate: literature/novelty mapping or model specification.
4. Run `EXP-002-sanity-check-candidate-model` only after the model-specification gate is explicitly opened.

## Non-Bypassable Gates

* Do not move candidate material into `docs/validated/` before sanity checks and evidence are recorded.
* Do not run model review while G0 is active unless the user explicitly opens model-specification work.
* Do not write a production PDE solver before the model is sanity-checked.
* Do not treat numerical oscillation as evidence without grid/timestep checks and control cases.
* Do not draft strong manuscript claims before literature matrix and claim-evidence matrix are populated.
* Do not treat source appendix numerical notes as reproduced evidence until verified in this repo.

Promotion gates:

* G0 exit: requires a project brief, central hypothesis, candidate claims, and visible uncertainty list. G0 does not require Codex, TASK files, CODEX reports, Makefile verification, or CI.
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
* `docs/stages/stage_index.md`
* `docs/stages/00_idea/gate.md`
* `docs/model_candidates/model_A_initial_lcst_transport_barrier.md`
* `docs/derivations/initial_model_derivation.tex`
* `docs/reports/exploration/CODEX-REPORT-EXP-001.md`
* `docs/tasks/TASK-TEMPLATE.md`
* `docs/reports/CODEX-REPORT-TEMPLATE.md`
* `docs/validated/model_spec.md`
* `docs/validated/claim_evidence.md`

## Update Protocol

Update this file whenever a task changes the project stage, blocker list, validation status, or next recommended task. Keep entries factual and repository-based. If evidence is missing, record the item as pending rather than inferring success.
