# Tasks

Tasks are grouped by project stage and purpose:

* `exploration`: tasks that reduce uncertainty.
* `verification`: tasks that test candidate conclusions.
* `production`: tasks that produce paper materials.

The Git repository is the source of truth for task state. ChatGPT defines and reviews tasks. Codex implements only within the assigned task scope and must leave a CODEX report for handoff back to ChatGPT.

Current active stage: `G2 -- Model Specification`. G2 reviews model definitions, units, material functions, boundary conditions, limiting cases, and minimum observables. Production PDE solver work remains blocked until later gates.

Each task must define:

* Task ID;
* Stage;
* Objective;
* Scientific or workflow context;
* Inputs;
* Allowed files to read;
* Allowed files to modify;
* Forbidden actions;
* Deliverables;
* Verification commands;
* Acceptance criteria;
* Failure conditions;
* Required CODEX-REPORT path;
* Whether user approval is required before merge;
* Whether ChatGPT review is required before merge.

Missing acceptance criteria or missing failure conditions make a task invalid.

Use `docs/tasks/TASK-TEMPLATE.md` for new tasks.
