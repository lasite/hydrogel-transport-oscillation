# CODEX Report: PROJECT-STATE

## Task ID

GitHub issue #1: Add centralized project state document for AI workflow control

## Files changed

* `docs/project_state.md`
* `AGENTS.md`
* `README.md`
* `scripts/check_repo_structure.py`
* `tests/test_repo_structure.py`
* `docs/reports/exploration/CODEX-REPORT-PROJECT-STATE.md`

## Summary

Created a centralized project-control document that records the current stage, completed work, active blockers, next recommended tasks, non-bypassable gates, source-of-truth links, and update protocol.

The document keeps Model A and all project claims in candidate status. No equations, derivations, production solvers, or validated files were modified.

## Commands run

```bash
make quickcheck
make derivations
git diff --check
```

## Results

`make quickcheck` ran the scaffold checker successfully, then failed at the pytest step because the active Python environment does not have `pytest` installed.

`make derivations` succeeded. `latexmk` reported that `docs/rendered/initial_model_derivation.pdf` is already up to date.

`git diff --check` reported no whitespace errors.

## Checks passed

* Repository scaffold check passed.
* `make derivations` passed.
* Diff whitespace check passed.

## Checks failed

* Pytest portion of `make quickcheck` failed with `/usr/bin/python3: No module named pytest`.

## Known limitations

* `EXP-002-sanity-check-candidate-model` is still pending.
* Literature map is still not populated.
* Homogeneous ODE limit, boundary-condition signs, material functions, and front/barrier observables remain unresolved.
* Source appendix numerical claims are still not independently reproduced.

## Next recommended task

Run `EXP-002-sanity-check-candidate-model`.
