# Gate: 05 Parameter Scan

## Status

blocked

## Purpose

Ensure parameter scans are meaningful and reproducible rather than exploratory noise.

## Required outputs

* Verified baseline numerical case.
* Scan axes and ranges.
* Classification criteria.
* Reproducible output paths.
* Failure and artifact checks.

## Acceptance criteria

* The baseline simulation has passed controls and convergence checks.
* Scan criteria correspond to defined observables.
* Results can be regenerated.

## Evidence

* No verified numerical baseline exists.
* No parameter-scan task exists.

## Blockers

* Numerics gate blocked.
* No validated observables or control cases.

## Next tasks

* Complete minimal numerical verification before defining scan grids.

## Promotion rule

Do not build phase diagrams until a verified numerical baseline and classification criteria exist.
