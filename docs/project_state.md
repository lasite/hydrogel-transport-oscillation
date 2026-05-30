# Project State

## Current Stage

Stage: G1 -- Literature / Novelty Mapping

Previous stage: G0 -- Idea Brief completed after user accepted the project brief, central hypothesis, candidate claims, and uncertainty list.

Substage: Literature map v0.1, novelty framing memo, and prior-art risk matrix created; source/DOI audit and corpus freeze pending.

Model status: candidate notes exist only; model-review work is not active.

Numerics status: no production PDE solver; no verified simulation.

Manuscript status: idea/project-brief level only; no validated results for writing.

G1 scope: map the relevant literature, compare neighboring mechanisms, identify novelty risks, and constrain allowed novelty language. G1 does not require model review, PDE implementation, numerical verification, figure generation, or manuscript drafting.

This document is a project-control snapshot for GPT and Codex workflows. It summarizes the current factual state of the repository without promoting candidate claims.

Stage details are tracked in docs/stages/stage_index.md.

## Completed Work

* G0 Idea Brief accepted by the user.
* Idea log and project brief created.
* One-sentence central hypothesis recorded in `docs/01_project_brief.md`.
* Candidate hypotheses and claims recorded in `docs/03_hypotheses.md`.
* Open questions recorded in `docs/02_open_questions.md`.
* `docs/04_literature_map.md` populated with G1 literature map v0.1.
* G1 literature map v0.1 includes a 50-item candidate corpus, mechanism-family map, novelty-risk matrix, and allowed/forbidden novelty language.
* `docs/05_novelty_framing.md` created from the user-provided research-significance memo and G1 literature-map constraints.
* `docs/06_prior_art_risk_matrix.md` created to map candidate novelty claims to nearest prior-art families, risk levels, required narrowing, and later evidence requirements.
* Model A candidate summary exists as exploratory background only.
* Initial derivation exists as exploratory background only in `docs/derivations/initial_model_derivation.tex`.
* EXP-001 report created.
* Derivation build succeeded in EXP-001.
* `docs/rendered/initial_model_derivation.pdf` has been generated from the derivation source.
* Project state control document created.
* Stage details are tracked in `docs/stages/stage_index.md`.
* No model or claim has been promoted to `docs/validated/`.

## Active Blockers

* DOI/source audit is needed for all `doi-audit-needed` rows in `docs/04_literature_map.md`.
* The G1 corpus is not yet frozen; weak P2 placeholder rows should be verified, replaced, or removed.
* Novelty framing and prior-art risk matrix need user or ChatGPT acceptance before G1 can exit.
* No claim-evidence item validated; validation is outside G1.
* `EXP-002-sanity-check-candidate-model` not completed, but this is a later model-gate blocker, not a G1 blocker.

## Next Recommended Tasks

1. Audit DOI/source metadata in `docs/04_literature_map.md`.
2. Freeze a smaller P0/P1 corpus of approximately 20--30 papers for manuscript introduction and reviewer-risk analysis.
3. Review and accept or revise `docs/05_novelty_framing.md` and `docs/06_prior_art_risk_matrix.md`.
4. Keep all novelty statements provisional until the retained corpus and risk matrix are accepted.
5. After G1 completion, explicitly choose whether to enter G2 model specification or continue literature refinement.
6. Run `EXP-002-sanity-check-candidate-model` only after the model-specification gate is explicitly opened.

## Non-Bypassable Gates

* Do not move candidate material into `docs/validated/` before sanity checks and evidence are recorded.
* Do not run model review while G1 literature mapping is active unless the user explicitly opens model-specification work.
* Do not write a production PDE solver before the model is sanity-checked.
* Do not treat numerical oscillation as evidence without grid/timestep checks and control cases.
* Do not draft strong manuscript novelty claims before the literature matrix and claim-evidence matrix are populated and reviewed.
* Do not treat source appendix numerical notes as reproduced evidence until verified in this repo.

Promotion gates:

* G0 exit: completed; requires a project brief, central hypothesis, candidate claims, and visible uncertainty list. G0 does not require Codex, TASK files, CODEX reports, Makefile verification, or CI.
* G1 exit: requires a populated literature map, traceable source matrix, mechanism comparison, novelty-risk list, DOI/source audit, and user or ChatGPT acceptance of the retained corpus.
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
