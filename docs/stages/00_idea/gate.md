# Gate: G0 Idea Brief

## Status

active

## Purpose

Ensure the project idea is explicit, bounded, recoverable, and governed by a reliable GPT/Codex/Git handoff protocol before deeper modeling or verification work proceeds.

At the current G0 protocol-hardening step, the ChatGPT -> Codex -> Git -> verification -> ChatGPT review loop must also be explicit and auditable.

## Required outputs

* Central hypothesis recorded.
* Physical mechanism chain recorded.
* Distinction from known oscillator classes recorded as candidate framing.
* Open uncertainty list recorded.
* TASK template requires scope, forbidden actions, acceptance criteria, failure conditions, report path, and review requirements.
* CODEX report template records commits, branch, commands with exit codes, environment, artifacts, limitations, and forbidden-action compliance.
* Fresh-checkout verification path is documented.

## Acceptance criteria

* The idea is stated without claiming validation.
* The central mechanism is distinguishable from BZ gels, external photothermal feedback, and pre-patterned catalytic switching at the hypothesis level.
* Current uncertainty is visible in repository files.
* New tasks can be audited against `docs/tasks/TASK-TEMPLATE.md`.
* Completed Codex work can be audited against `docs/reports/CODEX-REPORT-TEMPLATE.md`.
* Model review remains paused unless G0 exits or the user explicitly opens G2 model work.

## Evidence

* `docs/00_idea_log.md`
* `docs/01_project_brief.md`
* `docs/02_open_questions.md`
* `docs/03_hypotheses.md`
* `docs/tasks/TASK-TEMPLATE.md`
* `docs/reports/CODEX-REPORT-TEMPLATE.md`
* `README.md`
* `AGENTS.md`

## Blockers

* TASK and CODEX-REPORT protocol templates are not yet strict enough.
* Fresh-checkout verification is not yet fully documented.
* Repository visibility needs intentional confirmation for unpublished research material.
* Literature map is not populated.
* ChatGPT review of the hardened G0 protocol is pending.

## Next tasks

* Keep `docs/project_state.md` current.
* Ask ChatGPT to review the hardened G0 protocol.
* Do not run `EXP-002-sanity-check-candidate-model` until G0 exits or the user explicitly opens G2.

## Promotion rule

Idea framing can inform later model and literature work, but it cannot promote any model or claim to validated status. Model-review work is paused while G0 idea-brief protocol hardening is the active stage.
