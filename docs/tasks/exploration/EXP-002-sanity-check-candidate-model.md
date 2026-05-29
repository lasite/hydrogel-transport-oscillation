# EXP-002: Sanity-check Model A

## Objective

Check the initial LCST transport-barrier model for basic physical and mathematical consistency.

## Inputs

* `docs/model_candidates/model_A_initial_lcst_transport_barrier.md`
* `docs/derivations/initial_model_derivation.tex`

## Checks

1. Units and dimensions.
2. Positivity of concentration and temperature.
3. Boundedness of collapse variable.
4. Well-mixed ODE limit.
5. No-reaction limit.
6. No-collapse limit.
7. No-transport-degradation limit.
8. Boundary conditions.
9. Minimal observables.
10. Whether spatial barrier formation is represented.

## Deliverables

* `docs/reports/exploration/CODEX-REPORT-EXP-002.md`
* Proposed changes, but do not apply model changes unless explicitly requested.

## Verification commands

```bash
make quickcheck
make derivations
```

## Acceptance criteria

* Every equation has defined variables and parameters.
* Every coupling has a stated physical interpretation.
* At least five limiting cases are listed.
* The report identifies the minimum next verification task.
