# Project State

## Current Stage

Stage: G1 -- Literature / Novelty Mapping

Previous stage: G0 -- Idea Brief completed after user accepted the project brief, central hypothesis, candidate claims, and uncertainty list.

Substage: Build a source-backed literature map and novelty-risk matrix before model-review or manuscript-claim work proceeds.

Model status: candidate notes exist only; model-review work is not active.

Numerics status: no production PDE solver; no verified simulation.

Manuscript status: idea/project-brief level only; no validated results for writing.

G1 scope: map the relevant literature, compare neighboring mechanisms, and identify novelty risks. G1 does not require model review, PDE implementation, numerical verification, figure generation, or manuscript drafting.

This document is a project-control snapshot for GPT and Codex workflows. It summarizes the current factual state of the repository without promoting candidate claims.

Stage details are tracked in docs/stages/stage_index.md.

## Completed Work

* G0 Idea Brief accepted by the user.
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

* `docs/04_literature_map.md` is not yet populated with traceable sources.
* Novelty risks have not been assessed against BZ gels, LCST hydrogels, thermochemical fronts, thermal runaway, transport-limited gels, and self-oscillating polymer systems.
* No claim-evidence item validated; validation is outside G1.
* `EXP-002-sanity-check-candidate-model` not completed, but this is a later model-gate blocker, not a G1 blocker.

## Next Recommended Tasks

1. Populate `docs/04_literature_map.md` with traceable sources and mechanism categories.
2. Separate similar mechanisms, competing mechanisms, and true novelty risks.
3. Keep all novelty statements provisional until the literature map is reviewed.
4. After G1 completion, explicitly choose whether to enter G2 model specification or continue literature refinement.
5. Run `EXP-002-sanity-check-candidate-model` only after the model-specification gate is explicitly opened.

## Non-Bypassable Gates

* Do not move candidate material into `docs/validated/` before sanity checks and evidence are recorded.
* Do not run model review while G1 literature mapping is active unless the user explicitly opens model-specification work.
* Do not write a production PDE solver before the model is sanity-checked.
* Do not treat numerical oscillation as evidence without grid/timestep checks and control cases.
* Do not draft strong manuscript novelty claims before the literature matrix and claim-evidence matrix are populated and reviewed.
* Do not treat source appendix numerical notes as reproduced evidence until verified in this repo.

Promotion gates:

* G0 exit: completed; requires a project brief, central hypothesis, candidate claims, and visible uncertainty list. G0 does not require Codex, TASK files, CODEX reports, Makefile verification, or CI.
* G1 exit: requires a populated literature map, traceable source matrix, mechanism comparison, and novelty-risk list.
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
* `docs/stages/stage_index.md`
* `docs/stages/00_idea/gate.md`
* `docs/stages/01_literature/gate.md`
* `docs/model_candidates/model_A_initial_lcst_transport_barrier.md`
* `docs/derivations/initial_model_derivation.tex`
* `docs/reports/exploration/CODEX-REPORT-EXP-001.md`
* `docs/tasks/TASK-TEMPLATE.md`
* `docs/reports/CODEX-REPORT-TEMPLATE.md`
* `docs/validated/model_spec.md`
* `docs/validated/claim_evidence.md`

## Update Protocol

Update this file whenever a task changes the project stage, blocker list, validation status, or next recommended task. Keep entries factual and repository-based. If evidence is missing, record the item as pending rather than inferring success.
