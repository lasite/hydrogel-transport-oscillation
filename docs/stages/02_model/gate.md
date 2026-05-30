# Gate: 02 Model

## Status

active

## Purpose

Ensure Model A is organized and sanity-checked before analysis, numerics, or validation claims depend on it.

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

* `EXP-002-sanity-check-candidate-model` not completed.
* Homogeneous ODE limit incomplete.
* Boundary-condition sign convention unresolved.
* Material functions not fully specified.

## Next tasks

* Run `EXP-002-sanity-check-candidate-model`.
* Resolve notation and boundary-condition questions.

## Promotion rule

Do not promote Model A to `docs/validated/` until sanity checks and evidence are recorded.
