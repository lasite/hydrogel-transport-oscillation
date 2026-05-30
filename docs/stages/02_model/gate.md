# Gate: G2 Model

## Status

paused

## Purpose

Ensure Model A is organized and sanity-checked before analysis, numerics, or validation claims depend on it. This gate is not currently active because the project is in G0 idea-brief protocol hardening.

## Required outputs

* Candidate model summary.
* Organized derivation source.
* Defined variables and parameters.
* Boundary-condition sign audit.
* Limiting-case checklist.
* EXP-002 sanity-check report.

## Acceptance criteria

* Equations are preserved from user-provided derivation or explicitly marked TODO.
* Undefined variables and assumptions are listed.
* Dimensional consistency, positivity, boundedness, and limiting cases have been checked.
* No model is moved into `docs/validated/`.

## Evidence

* EXP-001 is complete.
* `docs/model_candidates/model_A_initial_lcst_transport_barrier.md` exists.
* `docs/derivations/initial_model_derivation.tex` exists.
* EXP-002 is not complete.

## Blockers

* G0 idea-brief protocol hardening is the active stage.
* `EXP-002-sanity-check-candidate-model` is intentionally paused.
* Homogeneous ODE limit incomplete.
* Boundary-condition sign convention unresolved.
* Material functions not fully specified.

## Next tasks

* Do not run `EXP-002-sanity-check-candidate-model` while G0 is active.
* Re-open this model gate only after G0 exits or the user explicitly creates a model-gate task.

## Promotion rule

Do not promote Model A to `docs/validated/` until this gate is re-opened, sanity checks are completed, and evidence is recorded.
