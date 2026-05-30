# Gate: G0 Idea Brief

## Status

active

## Purpose

Convert the initial idea into a clear project brief, central hypothesis, candidate claims, and visible uncertainty list before any literature, model-review, coding, or verification gate proceeds.

G0 is a ChatGPT-only conceptual framing gate. Codex, TASK handoff, CODEX reports, Makefile verification, and CI are not required to complete G0.

## Required outputs

* Central hypothesis recorded.
* Candidate claims recorded.
* Physical mechanism chain recorded.
* Distinction from known oscillator classes recorded as candidate framing.
* Open uncertainty list recorded.

## Acceptance criteria

* The idea is stated without claiming validation.
* The central hypothesis is explicit and falsifiable enough to guide later gates.
* Candidate claims are separated from validated claims.
* The central mechanism is distinguishable from BZ gels, external photothermal feedback, and pre-patterned catalytic switching at the hypothesis level.
* Current uncertainty is visible in repository files.

## Evidence

* `docs/00_idea_log.md`
* `docs/01_project_brief.md`
* `docs/02_open_questions.md`
* `docs/03_hypotheses.md`

## Blockers

* Hypothesis and candidate claims need user or ChatGPT acceptance before marking G0 complete.

## Next tasks

* Review `docs/01_project_brief.md` and `docs/03_hypotheses.md`.
* If accepted, mark G0 complete and explicitly choose the next active gate.
* Do not run `EXP-002-sanity-check-candidate-model` until the model-specification gate is explicitly opened.

## Promotion rule

Idea framing can guide later literature and model work, but it cannot promote any model or claim to validated status.
