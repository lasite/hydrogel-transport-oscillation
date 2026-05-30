# CODEX Report: TASK-G0-001

## Task ID

TASK-G0-001: Harden G0 Idea Brief Workflow Protocol

## Base commit

`99dbdf8f5ae2c1531987d59af9ba9a55b1cd846a`

## Final commit

The commit containing this report. The exact SHA is recorded in the final Codex handoff because a Git commit cannot contain its own content-addressed hash.

## Branch or worktree name

`codex/project-state-control`

## Files changed

Created:

* `docs/tasks/TASK-TEMPLATE.md`
* `docs/reports/CODEX-REPORT-TEMPLATE.md`
* `docs/reports/exploration/CODEX-REPORT-G0-001.md`

Modified:

* `AGENTS.md`
* `Makefile`
* `README.md`
* `docs/project_state.md`
* `docs/reports/README.md`
* `docs/stages/00_idea/gate.md`
* `docs/tasks/README.md`

## Summary of changes

* Added a strict TASK template requiring stage, context, read/modify scope, forbidden actions, verification, acceptance criteria, failure conditions, report path, and review requirements.
* Added a strict CODEX report template requiring base/final commit metadata, branch, command exit codes, environment, artifacts, failures, limitations, deviations, and forbidden-action compliance.
* Added `make install` and `make env-check` so a fresh checkout has a clear setup and environment verification path.
* Updated README, AGENTS, project state, task docs, report docs, and the G0 gate to make the ChatGPT -> Codex -> Git -> verification -> ChatGPT review loop explicit.
* Recorded that G0 is active and model review is paused until G0 exits or the user explicitly opens G2 model work.

## Commands run

| Command | Exit code |
| ------- | --------- |
| `git status --short --branch && git rev-parse HEAD && git branch --show-current` | 0 |
| `sed -n '1,240p' docs/project_state.md` | 0 |
| `sed -n '1,260p' docs/stages/stage_index.md && sed -n '1,240p' docs/stages/00_idea/gate.md` | 0 |
| `sed -n '1,260p' AGENTS.md && sed -n '1,240p' docs/tasks/README.md` | 0 |
| `sed -n '1,260p' docs/reports/README.md && sed -n '1,220p' Makefile && sed -n '1,220p' pyproject.toml` | 0 |
| `sed -n '1,260p' README.md` | 0 |
| `sed -n '1,220p' docs/00_idea_log.md` | 0 |
| `sed -n '1,220p' docs/01_project_brief.md` | 0 |
| `sed -n '1,260p' docs/02_open_questions.md` | 0 |
| `sed -n '1,260p' docs/03_hypotheses.md` | 0 |
| `rg --files docs/tasks docs/reports \| sort` | 0 |
| `git ls-files docs/model_candidates docs/derivations docs/validated src tests paper results data \| sort \| sed -n '1,220p'` | 0 |
| `. .venv/bin/activate && make env-check` | 0 |
| `. .venv/bin/activate && make quickcheck` | 2 |
| `. .venv/bin/activate && make quickcheck` | 0 |
| `git diff --check && uname -sr && . .venv/bin/activate && python --version && git diff --name-only` | 0 |
| `. .venv/bin/activate && make env-check` | 0 |
| `. .venv/bin/activate && make quickcheck` | 0 |

## Environment

OS if known: Linux 6.6.87.2-microsoft-standard-WSL2

Python version: Python 3.12.3

Dependency setup command used: existing uv-created `.venv` from the repository environment; fresh checkouts should run `make install` or an equivalent environment setup before `make quickcheck`.

## Artifacts produced

* `docs/tasks/TASK-TEMPLATE.md`
* `docs/reports/CODEX-REPORT-TEMPLATE.md`
* `docs/reports/exploration/CODEX-REPORT-G0-001.md`

## Checks passed

* `make env-check` passed in the active `.venv`.
* `make quickcheck` passed after preserving the legacy stage label expected by the existing scaffold test.
* Final reruns of `make env-check` and `make quickcheck` passed after creating this report.
* `git diff --check` passed.

## Checks failed

* First `make quickcheck` run failed because `tests/test_repo_structure.py` expected the existing text `Stage: Idea / Early Exploration` in `docs/project_state.md`.
* The failure was resolved by adding a legacy scaffold label while keeping the current active stage as `G0 -- Idea Brief`.

## Known limitations

* `docs/stages/stage_index.md` was read but not modified because it was not in the allowed file list for this task.
* The report identifies the final commit as the commit containing this report; the final handoff records the exact SHA.

## Deviations from task instructions

No model review was performed. No `EXP-002-sanity-check-candidate-model` work was run.

The only compatibility adjustment was adding a legacy stage label to `docs/project_state.md` so the existing scaffold test remains valid while the current stage is recorded as G0.

## Forbidden actions avoided

Forbidden actions were avoided.

No files under `docs/model_candidates/`, `docs/derivations/`, `docs/validated/`, `src/`, `tests/`, `paper/`, `results/`, or `data/` were modified.

No PDE solver, simulation, figure, model equation edit, model sanity review, or validation promotion was performed.

No model or claim was promoted to validated status.

## Recommended next task

ChatGPT should review the hardened G0 task/report protocol and decide whether G0 can exit or whether another G0 workflow task is needed before opening G2 model work.
