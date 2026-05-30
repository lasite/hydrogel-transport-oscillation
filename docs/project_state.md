# Project State

## Current Stage

Stage: G0 — Idea Brief

Substage: Idea framing and workflow-protocol stabilization

Model status: candidate notes exist only; no model-review task is currently recommended

Numerics status: no production PDE solver; no verified simulation

Manuscript status: idea/project-brief level only; no validated results for writing

This document is a project-control snapshot for GPT and Codex workflows. It summarizes the current factual state of the repository without promoting candidate claims.

Stage details are tracked in docs/stages/stage_index.md.

## Completed Work

* Idea log and project brief created.
* Open questions and hypotheses created.
* Model A candidate summary exists as exploratory background only.
* Initial derivation exists as exploratory background only in `docs/derivations/initial_model_derivation.tex`.
* EXP-001 report created.
* Derivation build succeeded in EXP-001.
* `docs/rendered/initial_model_derivation.pdf` has been generated from the derivation source.
* No model or claim has been promoted to `docs/validated/`.

## Active Blockers

* G0 idea-brief exit criteria are not yet hardened into a machine-checkable gate.
* TASK handoff and CODEX-REPORT templates need stricter required fields.
* Verification environment is not yet fully reproducible from a single command.
* Repository visibility should be intentionally confirmed before unpublished manuscript work accumulates.
* Literature map not populated.
* No claim-evidence item validated.
* No verified numerical simulation.
* Current local quickcheck is blocked at the pytest step unless `pytest` is installed in the active Python environment.

## Next Recommended Tasks

1. Harden the G0 idea-brief gate and workflow protocol before model review.
2. Add explicit TASK and CODEX-REPORT templates with allowed files, forbidden actions, failure conditions, command exit codes, environment, and artifact records.
3. Add an environment check or install target so `make quickcheck` is reproducible from a fresh checkout.
4. Confirm repository visibility is intentional for unpublished research material.
5. Keep Model A and derivation material labeled as exploratory background until G0 exits and a later model gate is explicitly opened.

## Non-Bypassable Gates

* Do not move candidate material into `docs/validated/` before sanity checks and evidence are recorded.
* Do not start model-review or production solver work while G0 idea-brief protocol hardening is the active stage.
* Do not write a production PDE solver before the model is sanity-checked.
* Do not treat numerical oscillation as evidence without grid/timestep checks and control cases.
* Do not draft strong manuscript claims before literature matrix and claim-evidence matrix are populated.
* Do not treat source appendix numerical notes as reproduced evidence until verified in this repo.

Promotion gates:

* G0 exit: requires a stable idea brief, explicit uncertainty list, hardened TASK/CODEX-REPORT protocol, and reproducible scaffold checks.
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
* `docs/validated/model_spec.md`
* `docs/validated/claim_evidence.md`

## Update Protocol

Update this file whenever a task changes the project stage, blocker list, validation status, or next recommended task. Keep entries factual and repository-based. If evidence is missing, record the item as pending rather than inferring success.
