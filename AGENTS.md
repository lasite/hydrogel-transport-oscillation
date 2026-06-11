# AGENTS.md

## Project role

You are assisting with a theoretical soft-matter physics research project on hydrogel self-oscillation driven by coupled reaction, heat release, LCST poroelastic collapse, and transport degradation.

The repository is the source of truth. Prior chat history is not the source of truth.

This repository supports interaction with a physics expert. Optimize for physical correctness, auditability, falsifiability, and evidence-bounded manuscript production. Do not turn routine physical reasoning into programmer-centric ceremony.

## Current stage

Active stage: Paper Results Production

Internal anchor: `G6_figures`

Research Idea Brief and Literature / Novelty Mapping have been accepted by the user. The user has authorized continued use of the imported `paper/figures/` result assets for paper-results production. The model remains candidate-only and unvalidated unless a later validation gate explicitly records evidence.

During Paper Results Production, prioritize figure-source mapping, caption-bounded claims, missing explanatory images, observable definitions, provenance, and manuscript figure assembly. Do not write a new production PDE solver unless the user explicitly opens a scoped numerical-verification or solver-reproduction task.

Do not assume:

* the model is finalized;
* the mechanism is proven;
* the equations are dimensionally consistent;
* the observed oscillation is already verified in this repository;
* linear stability analysis is sufficient;
* the PDE attractor structure is known;
* reused `paper/figures/` assets are newly reproduced evidence.

## Operating principles

* Formality only at state transitions.
* Physics-first everywhere else.
* Concrete task names first; internal anchors such as `G6_figures` are secondary labels.
* A task name should state the actual issue, for example `Map Existing Paper Figures to Claims`, `Draft Evidence-Bounded Figure Captions`, `Add Front-Observable Definition Graphic`, or `Prepare Control Comparison Supplement`.
* Use structure to prevent false promotion of claims, not to replace physical reasoning.

## Work modes

### Physics note

Use a physics note for non-state-changing theoretical review, derivation sketches, physical intuition, critique, option comparison, figure interpretation, or caption-boundary reasoning.

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

For paper-results production and figure work, also read:

* `docs/manuscript/figure_blueprint.md`;
* `docs/manuscript/paper_results_figure_plan.md`;
* `paper/paper_latest_migration_manifest.tsv` when provenance or source mapping is involved.

If the task changes or reviews model equations, also read:

* `docs/model_candidates/model_A_initial_lcst_transport_barrier.md`;
* `docs/derivations/initial_model_derivation.tex`.

If the task changes novelty framing, manuscript claims, captions, or evidence requirements, also read:

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

Proposed equations, closures, material functions, nondimensionalizations, boundary conventions, observable definitions, or figure interpretations may be suggested only when marked as candidate, proposed, or TODO, with assumptions and required checks stated explicitly.

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

Paper-results production constraints:

* Reused `paper/figures/` assets may be used for manuscript production by user decision.
* Reused assets must be source-mapped and caption-bounded.
* Treat SNIC scaling, hysteresis, penetration-depth, basin-size, and phase-lag claims as unvalidated unless reproduced or explicitly framed as candidate/source-draft results.
* Distinguish reaction accessibility, diffusivity, permeability, and poroelastic collapse in captions and text.
* Define front/barrier observables before using them as central evidence.

## Coding rules

At this stage:

* Do not write a new production PDE solver unless explicitly scoped.
* Do not create large simulations unless a task specifically authorizes result reproduction or verification.
* Do not create large datasets without a provenance and storage decision.
* Figure assembly, schematic creation, caption drafting, source mapping, and lightweight diagnostic extraction are allowed when scoped by the production task.

If code is added later:

* Keep code modular.
* Put reusable code under `src/`.
* Put runnable scripts under `scripts/` or figure-local `paper/figures/*/scripts/` when appropriate.
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

If `latexmk` is unavailable, `make derivations` should report a warning and continue during exploratory or production-planning work.

For reduced figure-route smoke checks, run:

```bash
make figure-smoke
```

`make figure-smoke` remains a wiring check only; it does not validate numerical results.

## Reporting rules

At the end of each Codex task, report:

* files created or modified;
* commands run with exit codes;
* whether checks passed;
* known TODOs;
* recommended next task.

When applicable, include this exact statement:

No model or claim was promoted to validated status.
