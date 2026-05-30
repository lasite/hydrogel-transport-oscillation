# Gate: 04 Numerics

## Status

blocked

## Purpose

Prevent solver work from outrunning model sanity checks and diagnostic design.

## Required outputs

* Minimal numerical task definition.
* Model parameters and observables specified.
* Control cases listed.
* Grid/timestep convergence criteria.
* Data and results storage rules.

## Acceptance criteria

* No production PDE solver is written before the model is sanity-checked.
* Numerical results are not treated as evidence without controls and convergence checks.
* Outputs are reproducible from scripts or notebooks.

## Evidence

* No verified numerical simulation exists.
* `configs/default.yaml` contains placeholders only.
* `docs/validated/claim_evidence.md` has no validated evidence.

## Blockers

* Model sanity check pending.
* Analysis gate blocked.
* Front/barrier observables not finalized.

## Next tasks

* Define observables.
* Design minimal verification tasks only after EXP-002 and analysis checks.

## Promotion rule

Do not start parameter scans or figures from exploratory numerical output until numerical verification is complete.
