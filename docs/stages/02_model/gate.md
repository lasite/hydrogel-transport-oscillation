# Gate: Model Specification

Internal anchor: `G2`

## Status

active

## Purpose

Convert the candidate Model A material into a clear, auditable model specification before analysis, numerics, or validated claims depend on it.

Model Specification is not a numerical-production gate. Its purpose is to determine whether the candidate equations and assumptions are sufficiently defined and physically consistent to test the novelty mechanism identified during Literature / Novelty Mapping.

## Literature / Novelty Mapping constraints carried into Model Specification

Model Specification must test the mechanism implied by:

* `docs/05_novelty_framing.md`
* `docs/06_prior_art_risk_matrix.md`
* `docs/07_g1_frozen_corpus.md`

The model must be assessed against these questions:

1. Is the chemical subsystem non-oscillatory by itself?
2. Is a homogeneous ODE or well-mixed limit derivable, and what does it predict?
3. Is LCST collapse necessary for the claimed oscillator?
4. Are transport degradation and/or reaction-accessibility degradation necessary?
5. Are diffusivity, permeability, and reaction accessibility clearly distinguished?
6. Is there a measurable front/barrier observable?
7. Is the claimed surface/bulk slow-manifold structure represented or at least testable?
8. Are SNIC-like scaling, hysteresis, penetration-depth, and basin-size claims marked unvalidated until reproduced?

## Required outputs

* Candidate model summary reviewed against novelty-risk constraints.
* Organized derivation source reviewed for variable/parameter definitions.
* Defined state variables, parameters, units, and material functions.
* Boundary-condition sign and physical-meaning audit.
* Limiting-case checklist.
* Explicit list of undefined quantities or assumptions.
* Minimum front/barrier observables required for later verification.
* Model Specification sanity-check report.

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

Use concrete physics task names. Internal anchors may be added only as secondary labels.

* Resolve Free-Surface Reactant Boundary-Condition Convention.
* Add Continuous Boundary Conditions for Gradient-Energy Regularization.
* Reaudit Composition-Dependent Mixing Chemical Potential.
* Derive or Scope the Homogeneous Well-Mixed Limit.
* Define Front and Barrier Observables.

## Promotion rule

Do not promote Model A to `docs/validated/` until this gate is complete, sanity checks are recorded, and claim-evidence entries are updated with explicit evidence.
