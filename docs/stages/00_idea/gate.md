# Gate: G0 Idea Brief

## Status

active

## Purpose

Ensure the project idea is explicit, bounded, recoverable, and governed by a reliable GPT/Codex/Git handoff protocol before deeper modeling or verification work proceeds.

## Required outputs

* Central hypothesis recorded.
* Physical mechanism chain recorded.
* Distinction from known oscillator classes recorded as candidate framing.
* Open uncertainty list recorded.
* TASK handoff template hardened for ChatGPT-to-Codex transfer.
* CODEX-REPORT template hardened for Codex-to-ChatGPT review.
* Scaffold verification command reproducible from a fresh checkout.
* Repository visibility intentionally confirmed before unpublished manuscript material accumulates.

## Acceptance criteria

* The idea is stated without claiming validation.
* The central mechanism is distinguishable from BZ gels, external photothermal feedback, and pre-patterned catalytic switching at the hypothesis level.
* Current uncertainty is visible in repository files.
* TASK files explicitly specify objective, context, inputs, allowed files, forbidden actions, deliverables, verification commands, acceptance criteria, failure conditions, and report requirements.
* CODEX-REPORT files explicitly record base commit, final commit, files changed, commands run with exit codes, environment, artifacts, checks passed, checks failed, known limitations, and recommended next task.
* `make quickcheck` or an equivalent documented command can be run after following the repository setup instructions.

## Evidence

* `docs/00_idea_log.md`
* `docs/01_project_brief.md`
* `docs/02_open_questions.md`
* `docs/03_hypotheses.md`
* `docs/tasks/README.md`
* `docs/reports/README.md`
* `Makefile`
* `pyproject.toml`

## Blockers

* TASK and CODEX-REPORT protocol templates are not yet strict enough.
* Fresh-checkout verification is not yet fully documented.
* Repository visibility needs intentional confirmation for unpublished research material.
* Literature map is not populated.

## Next tasks

* Harden the TASK and CODEX-REPORT protocol templates.
* Add or document an environment setup path for `make quickcheck`.
* Confirm and document whether the repository should be private or public during pre-submission work.
* Do not run `EXP-002-sanity-check-candidate-model` until G0 exits and the model gate is explicitly opened.

## Promotion rule

Idea framing can inform later model and literature work, but it cannot promote any model or claim to validated status. Model-review work is paused while G0 idea-brief protocol hardening is the active stage.
