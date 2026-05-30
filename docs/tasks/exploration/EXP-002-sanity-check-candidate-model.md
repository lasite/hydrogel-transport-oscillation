# EXP-002: G2 Model Specification and Sanity Check

## Task ID

`EXP-002`

## Stage

`G2 -- Model Specification`

## Objective

Check the initial LCST transport-barrier Model A for basic physical and mathematical consistency, explicitly using the G1 novelty-risk constraints.

The goal is not to validate the model. The goal is to determine whether the candidate model is sufficiently specified to support later analysis and verification tasks.

## Scientific or workflow context

G1 established that the project's novelty cannot be broad hydrogel oscillation. The model must instead support, or fail to support, the narrower candidate mechanism:

`single non-oscillatory exothermic reaction + LCST poroelastic collapse + transport/accessibility barrier -> spatial relaxation oscillator`

This task should identify whether the current candidate equations contain the necessary pieces to test that mechanism.

## Inputs

* `docs/project_state.md`
* `docs/05_novelty_framing.md`
* `docs/06_prior_art_risk_matrix.md`
* `docs/07_g1_frozen_corpus.md`
* `docs/model_candidates/model_A_initial_lcst_transport_barrier.md`
* `docs/derivations/initial_model_derivation.tex`

## Allowed files to read

* `docs/project_state.md`
* `docs/00_idea_log.md`
* `docs/01_project_brief.md`
* `docs/02_open_questions.md`
* `docs/03_hypotheses.md`
* `docs/04_literature_map.md`
* `docs/05_novelty_framing.md`
* `docs/06_prior_art_risk_matrix.md`
* `docs/07_g1_frozen_corpus.md`
* `docs/model_candidates/model_A_initial_lcst_transport_barrier.md`
* `docs/derivations/initial_model_derivation.tex`
* `docs/validated/claim_evidence.md`
* `AGENTS.md`
* `Makefile`

## Allowed files to modify

* `docs/reports/exploration/CODEX-REPORT-EXP-002.md`
* Optionally `docs/02_open_questions.md` if new unresolved questions are found.
* Optionally `docs/model_candidates/model_A_initial_lcst_transport_barrier.md` only for non-substantive clarification, TODO markers, or cross-reference notes. Do not change equations unless explicitly requested by the user.

## Forbidden actions

* Do not promote any model, derivation, result, or claim into `docs/validated/`.
* Do not write a production PDE solver.
* Do not run large simulations or parameter sweeps.
* Do not generate figures.
* Do not strengthen manuscript novelty claims.
* Do not alter core equations unless explicitly requested by the user.
* Do not treat source-appendix numerical notes as reproduced evidence.

## Checks

1. Units and dimensions.
2. Positivity of concentration and temperature.
3. Boundedness of collapse/swelling variables.
4. Well-mixed or homogeneous ODE limit.
5. Chemical subsystem non-oscillatory check or unresolved status.
6. No-reaction limit.
7. No-collapse limit.
8. No-transport-degradation limit.
9. No-accessibility-degradation limit.
10. Boundary-condition signs and physical meanings.
11. Distinction between reaction accessibility, diffusivity, permeability, and poroelastic collapse.
12. Minimal front/barrier observables.
13. Whether spatial barrier formation is represented.
14. Whether surface/bulk slow-manifold claims are represented, testable, or unsupported.
15. Whether SNIC scaling, hysteresis, penetration depth, and basin-size claims are still unvalidated.

## Deliverables

* `docs/reports/exploration/CODEX-REPORT-EXP-002.md`
* A table of variables and parameters that are defined, underdefined, or missing.
* A limiting-case checklist.
* A list of required model clarifications before G3 analysis or G4 numerics.
* A minimum-observable list for front/barrier verification.
* Recommended next task.

## Verification commands

```bash
make quickcheck
make derivations
```

If dependencies are missing in a fresh environment, run:

```bash
make install
make env-check
make quickcheck
make derivations
```

Record commands and exit codes in the report.

## Acceptance criteria

* Every equation has defined variables and parameters, or missing definitions are explicitly listed.
* Every coupling has a stated physical interpretation or unresolved status.
* At least five limiting cases are listed and interpreted.
* The report explicitly addresses the G1-derived mechanism constraints.
* The report identifies the minimum next verification or analysis task.
* No model or claim is promoted to validated status.

## Failure conditions

* The report treats candidate equations as validated.
* The report omits G1 novelty-risk constraints.
* The report changes model equations without explicit user authorization.
* The report creates solver code, figures, parameter sweeps, or manuscript claims.
* The report does not record verification commands and outcomes.

## Required CODEX-REPORT path

`docs/reports/exploration/CODEX-REPORT-EXP-002.md`

## User approval required before merge

Yes

## ChatGPT review required before merge

Yes
