# CODEX Report: STAGE-SCAFFOLD

## Task ID

Stage scaffold: add explicit research-stage gates from idea to submission.

## Files created

* `docs/stages/README.md`
* `docs/stages/stage_index.md`
* `docs/stages/00_idea/README.md`
* `docs/stages/00_idea/gate.md`
* `docs/stages/01_literature/README.md`
* `docs/stages/01_literature/gate.md`
* `docs/stages/02_model/README.md`
* `docs/stages/02_model/gate.md`
* `docs/stages/03_analysis/README.md`
* `docs/stages/03_analysis/gate.md`
* `docs/stages/04_numerics/README.md`
* `docs/stages/04_numerics/gate.md`
* `docs/stages/05_parameter_scan/README.md`
* `docs/stages/05_parameter_scan/gate.md`
* `docs/stages/06_figures/README.md`
* `docs/stages/06_figures/gate.md`
* `docs/stages/07_writing/README.md`
* `docs/stages/07_writing/gate.md`
* `docs/stages/08_review/README.md`
* `docs/stages/08_review/gate.md`
* `docs/stages/09_submission/README.md`
* `docs/stages/09_submission/gate.md`
* `docs/reports/exploration/CODEX-REPORT-STAGE-SCAFFOLD.md`

## Files modified

* `docs/project_state.md`
* `README.md`

## Commands run

```bash
source .venv/bin/activate
make quickcheck
make derivations
```

## Checks passed or failed

Passed:

* `make quickcheck`
  * Repository scaffold check passed.
  * Pytest passed: 6 tests passed.
* `make derivations`
  * `latexmk` found no rebuild work to do.
  * `docs/rendered/initial_model_derivation.pdf` is up to date.

Failed:

* None.

## Next recommended task

Run `EXP-002-sanity-check-candidate-model`, then create or run a literature-map task.
