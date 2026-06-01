# AGENTS.md

## Project role

You are assisting with an early-stage theoretical soft-matter physics research project on hydrogel self-oscillation driven by coupled reaction, heat release, LCST poroelastic collapse, and transport degradation.

The repository is the source of truth. Prior chat history is not the source of truth.

This repository supports interaction with a physics expert. Optimize for physical correctness, auditability, and falsifiability. Do not turn routine physical reasoning into programmer-centric ceremony.

## Current stage

Active stage: Model Specification

Internal anchor: `G2`

Research Idea Brief and Literature / Novelty Mapping have been accepted by the user. The model remains candidate-only and unvalidated.

During Model Specification, prioritize model specification, variable definitions, units, material functions, boundary-condition signs, limiting cases, and minimum observables. Do not write a production PDE solver unless the user explicitly opens a later numerical-verification stage.

Do not assume:

* the model is finalized;
* the mechanism is proven;
* the equations are dimensionally consistent;
* the observed oscillation is already verified;
* linear stability analysis is sufficient;
* the PDE attractor structure is known.

## Operating principles

* Formality only at state transitions.
* Physics-first everywhere else.
* Concrete task names first; internal anchors such as `G2` are secondary labels.
* A task name should state the actual issue, for example `Resolve Reactant Boundary Flux Convention`, `Reaudit Composition-Dependent Mixing Potential`, or `Define Front and Barrier Observables`.
* Use structure to prevent false promotion of claims, not to replace physical reasoning.

## Work modes

### Physics note

Use a physics note for non-state-changing theoretical review, derivation sketches, physical intuition, critique, or option comparison.

A physics note may be written in chat or placed under `docs/notes/`. It should normally contain: question, physics intuition, candidate derivation or equations, assumptions, limiting or failure cases, and next action.

A physics note must not change project stage, validation status, claim evidence, executable behavior, figures, or manuscript claims.

### Codex task

Use a full TASK file when repository files will be modified, commands will be run, or a handoff report is needed.

Every Codex task should have:

* concrete task name;
* internal stage anchor if needed;
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

### Gate or state transition

Use full formal review for any change that affects project stage, gate status, validation status, claim evidence, numerical evidence, figure evidence, or manuscript text.

State-transition work must update `docs/project_state.md` and the relevant gate, decision, report, or evidence file. If evidence is missing, record the item as pending rather than inferring success.

## Required reading

Before any work, read:

* `docs/project_state.md`;
* the assigned task file or note request;
* files explicitly listed as inputs or allowed-to-modify files.

If the task changes or reviews model equations, also read:

* `docs/model_candidates/model_A_initial_lcst_transport_barrier.md`;
* `docs/derivations/initial_model_derivation.tex`.

If the task changes novelty framing, manuscript claims, or evidence requirements, also read:

* `docs/04_literature_map.md`;
* `docs/05_novelty_framing.md`;
* `docs/06_prior_art_risk_matrix.md`;
* `docs/07_g1_frozen_corpus.md`;
* `docs/claims/candidate_claim_evidence.md`.

## Math documentation rules

* Markdown files are for summaries, task definitions, reports, and short equations only.
* Long derivations must go into `.tex` files under `docs/derivations/`.
* Do not put long derivations in task files or reports.
* If you edit `.tex` derivations, run `make derivations`.
* Markdown files should link to the corresponding `.tex` source and rendered PDF when available.
* Do not edit generated PDFs directly.

## Scientific rules

Do not silently promote newly proposed equations into the model.

Proposed equations, closures, material functions, nondimensionalizations, or boundary conventions may be suggested only when marked as candidate, proposed, or TODO, with assumptions and required checks stated explicitly.

Do not move any model, derivation, result, or claim into `docs/validated/` unless the relevant gate requires it and evidence is recorded.

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

Model Specification constraints from the Literature / Novelty Mapping stage:

* Verify that the chemical subsystem is non-oscillatory by itself or mark this unresolved.
* Distinguish reaction accessibility, diffusivity, permeability, and poroelastic collapse.
* Define front/barrier observables before numerical validation.
* Treat SNIC scaling, hysteresis, penetration-depth, and basin-size claims as unvalidated until reproduced in this repository.

## Coding rules

At this stage:

* Do not write a production PDE solver.
* Do not create large simulations.
* Do not create large datasets.
* Only create minimal scaffolding, sanity-check scripts, symbolic checks, or toy exploratory scripts when explicitly requested by the task.

If code is added later:

* Keep code modular.
* Put reusable code under `src/`.
* Put runnable scripts under `scripts/`.
* Put tests under `tests/`.
* Put parameters under `configs/`.

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

At the end of each Codex task, report:

* files created or modified;
* commands run with exit codes;
* whether checks passed;
* known TODOs;
* recommended next task.

When applicable, include this exact statement:

No model or claim was promoted to validated status.
