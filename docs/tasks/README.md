# Tasks

Tasks are grouped by project purpose:

* `exploration`: tasks that reduce uncertainty.
* `verification`: tasks that test candidate conclusions.
* `production`: tasks that produce paper materials.

The Git repository is the source of truth for task state. ChatGPT defines and reviews tasks. Codex implements only within the assigned task scope and must leave a CODEX report for handoff back to ChatGPT when repository files are changed or commands are run.

Current active stage: Model Specification. This stage reviews model definitions, units, material functions, boundary conditions, limiting cases, and minimum observables. Production PDE solver work remains blocked until later gates.

Use concrete task names that state the actual physics or workflow issue. Prefer names such as `Resolve Free-Surface Reactant Boundary-Condition Convention` over names that only expose an abstract code such as `G2-001`.

Use full task formalism only for Codex tasks and state transitions. Use `docs/notes/PHYSICS-NOTE-TEMPLATE.md` for non-state-changing physics-first reasoning.

Each Codex task must define:

* concrete task name;
* internal stage anchor, if needed;
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

Missing acceptance criteria or missing failure conditions make a Codex task invalid.

Use `docs/tasks/TASK-TEMPLATE.md` for new Codex tasks.
