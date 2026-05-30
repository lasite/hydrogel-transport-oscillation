# Gate: 03 Analysis

## Status

blocked

## Purpose

Prevent numerical work from starting before basic mathematical and physical checks are complete.

## Required outputs

* Homogeneous ODE limit.
* Linear stability interpretation with assumptions.
* At least five limiting cases.
* Front/barrier observable definitions.
* Boundary-condition sign audit.

## Acceptance criteria

* Analysis follows the organized candidate model.
* Homogeneous and spatial mechanisms are explicitly compared.
* Claims remain candidate unless supported by recorded evidence.

## Evidence

* Linear stability material exists in `docs/derivations/initial_model_derivation.tex`.
* Open questions identify missing homogeneous ODE and boundary-condition checks.

## Blockers

* Model sanity check is pending.
* Homogeneous ODE dynamical system is incomplete.
* Front/barrier observables are not finalized.

## Next tasks

* Complete EXP-002.
* Derive the homogeneous ODE limit.
* Define collapsed skin thickness, barrier strength, and front position.

## Promotion rule

Do not begin numerical validation tasks until analysis blockers are resolved or explicitly scoped as TODOs with human approval.
