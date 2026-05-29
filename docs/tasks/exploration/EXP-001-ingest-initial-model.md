# EXP-001: Ingest and organize the initial model derivation

## Objective

Insert the user's preliminary model derivation into the repository without changing its scientific content.

## Inputs

* User-provided initial derivation.
* `docs/model_candidates/model_A_initial_lcst_transport_barrier.md`
* `docs/derivations/initial_model_derivation.tex`

## Allowed files to modify

* `docs/model_candidates/model_A_initial_lcst_transport_barrier.md`
* `docs/derivations/initial_model_derivation.tex`
* `docs/02_open_questions.md`
* `docs/03_hypotheses.md`
* `docs/reports/exploration/CODEX-REPORT-EXP-001.md`

## Forbidden changes

* Do not invent new equations.
* Do not simplify the model unless explicitly asked.
* Do not move the model into `docs/validated/`.
* Do not write production solver code.

## Deliverables

1. Organized LaTeX derivation.
2. Markdown summary of variables, equations, assumptions, and open issues.
3. List of missing definitions or ambiguous terms.
4. Exploration report.

## Verification commands

```bash
make quickcheck
make derivations
```

## Acceptance criteria

* The user's equations are preserved.
* All undefined variables are listed.
* All assumptions are explicitly separated from equations.
* The derivation compiles if LaTeX is available.
* No claim is marked validated.
