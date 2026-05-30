# AGENTS.md

## Project role

You are assisting with an early-stage theoretical soft-matter physics research project on hydrogel self-oscillation driven by coupled reaction, heat release, LCST poroelastic collapse, and transport degradation.

The repository is the source of truth. Prior chat history is not the source of truth.

## Current stage

The project is in the exploratory stage.

Current active gate: `G0 -- Idea Brief`.

The Git repository is the source of truth. ChatGPT defines and reviews tasks. Codex implements only within the assigned TASK scope and must produce a CODEX report for handoff back to ChatGPT.

Model review is paused until G0 exits or the user explicitly opens G2 model work.

Do not assume:

* the model is finalized;
* the mechanism is proven;
* the equations are dimensionally consistent;
* the observed oscillation is already verified;
* linear stability analysis is sufficient;
* the PDE attractor structure is known.

## Required reading before any task

Before working on any task, read:

* `docs/project_state.md`
* `docs/00_idea_log.md`
* `docs/01_project_brief.md`
* `docs/02_open_questions.md`
* `docs/03_hypotheses.md`
* the assigned task file under `docs/tasks/`

If the task involves equations, also read:

* `docs/model_candidates/model_A_initial_lcst_transport_barrier.md`
* `docs/derivations/initial_model_derivation.tex`

## Math documentation rules

* Markdown files are for summaries, task definitions, reports, and short equations only.
* Long derivations must go into `.tex` files under `docs/derivations/`.
* Do not put long derivations in task files or reports.
* If you edit `.tex` derivations, run `make derivations`.
* Markdown files should link to the corresponding `.tex` source and rendered PDF when available.
* Do not edit generated PDFs directly.

## Scientific rules

Do not invent equations that the user has not provided.

If equations are missing, use explicit TODO markers.

When reviewing or implementing a model, check:

* conserved quantities;
* dimensions and units;
* boundary conditions;
* limiting cases;
* well-mixed limit;
* passive or nonreactive limit;
* reaction-only limit;
* transport-only limit;
* LCST-collapse-only limit;
* whether a spatial barrier can form;
* whether the proposed oscillation requires spatial PDE dynamics rather than homogeneous ODE dynamics.

## Coding rules

At this stage:

* Do not write a production PDE solver.
* Do not create large simulations.
* Do not create large datasets.
* Only create minimal scaffolding, sanity-check scripts, or toy exploratory scripts when explicitly requested.

If code is added later:

* Keep code modular.
* Put reusable code under `src/`.
* Put runnable scripts under `scripts/`.
* Put tests under `tests/`.
* Put parameters under `configs/`.

## Task protocol

Every task should have:

* Task ID;
* Stage;
* objective;
* scientific or workflow context;
* inputs;
* allowed files to read;
* allowed files to modify;
* forbidden actions;
* deliverables;
* verification commands;
* acceptance criteria;
* failure conditions;
* required CODEX-REPORT path;
* whether user approval is required before merge;
* whether ChatGPT review is required before merge.

Missing acceptance criteria or missing failure conditions make a task invalid.

Every completed task should produce a report under `docs/reports/`.

## Verification commands

For scaffold-level checks, run:

```bash
make quickcheck
```

For derivation compilation, run:

```bash
make derivations
```

If `latexmk` is unavailable, `make derivations` should report a warning and continue during the exploratory stage.

## Reporting rules

At the end of each task, report:

* files created or modified;
* commands run;
* whether checks passed;
* known TODOs;
* recommended next task.
