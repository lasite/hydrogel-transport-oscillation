# Gate: G2 Model Specification

## Status

active

## Purpose

Convert the candidate Model A material into a clear, auditable model specification before analysis, numerics, or validated claims depend on it.

G2 is not yet a numerical-production gate. Its purpose is to determine whether the candidate equations and assumptions are sufficiently defined and physically consistent to test the G1 novelty mechanism.

## G1 constraints carried into G2

G2 must test the mechanism implied by:

* `docs/05_novelty_framing.md`
* `docs/06_prior_art_risk_matrix.md`
* `docs/07_g1_frozen_corpus.md`

The model must be assessed against these G1-derived questions:

1. Is the chemical subsystem non-oscillatory by itself?
2. Is a homogeneous ODE or well-mixed limit derivable, and what does it predict?
3. Is LCST collapse necessary for the claimed oscillator?
4. Are transport degradation and/or reaction-accessibility degradation necessary?
5. Are diffusivity, permeability, and reaction accessibility clearly distinguished?
6. Is there a measurable front/barrier observable?
7. Is the claimed surface/bulk slow-manifold structure represented or at least testable?
8. Are SNIC-like scaling, hysteresis, penetration-depth, and basin-size claims marked unvalidated until reproduced?

## Required outputs

* Candidate model summary reviewed against G1 constraints.
* Organized derivation source reviewed for variable/parameter definitions.
* Defined state variables, parameters, units, and material functions.
* Boundary-condition sign and physical-meaning audit.
* Limiting-case checklist.
* Explicit list of undefined quantities or assumptions.
* Minimum front/barrier observables required for later verification.
* G2 sanity-check report.

## Acceptance criteria

* Equations are preserved from user-provided derivation or explicitly marked TODO.
* Every state variable and parameter used in the model has a definition or is listed as unresolved.
* Dimensional consistency, positivity, boundedness, and limiting cases have been checked at the specification level.
* The model distinguishes reaction accessibility, diffusivity, permeability, and poroelastic swelling/collapse when these are used.
* The well-mixed or homogeneous limit is derived, scoped, or explicitly marked incomplete.
* No model, derivation, or claim is moved into `docs/validated/`.
* The report identifies the minimum next verification task.

## Evidence

* EXP-001 is complete.
* `docs/model_candidates/model_A_initial_lcst_transport_barrier.md` exists.
* `docs/derivations/initial_model_derivation.tex` exists.
* `docs/05_novelty_framing.md` exists.
* `docs/06_prior_art_risk_matrix.md` exists.
* `docs/07_g1_frozen_corpus.md` exists.
* EXP-002 is not complete.

## Blockers

* `EXP-002-sanity-check-candidate-model` not completed.
* Homogeneous ODE limit incomplete.
* Boundary-condition sign convention unresolved.
* Material functions not fully specified.
* Front/barrier observables not finalized.

## Next tasks

* Create or revise a G2 model-specification task that uses G1 constraints.
* Run `EXP-002-sanity-check-candidate-model` only if its scope is updated to include G1 novelty-risk constraints.
* Resolve notation, boundary-condition signs, material functions, and minimum observables.

## Promotion rule

Do not promote Model A to `docs/validated/` until this gate is complete, sanity checks are recorded, and claim-evidence entries are updated with explicit evidence.
