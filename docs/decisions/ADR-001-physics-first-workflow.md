# ADR-001: Physics-First Workflow with Formality Reserved for State Transitions

## Status

Accepted

## Context

The repository uses Git as the source of truth, ChatGPT as the theory-planning and review interface, and Codex as the repository-editing, command-execution, and verification interface.

The previous workflow protected against false validation, but some routine theoretical work risked becoming over-formalized. Excessive template use can shift attention away from physical consistency, limiting cases, conservation laws, and mechanism falsifiability.

The user also requested concrete task names that describe the physics or workflow content, rather than relying on abstract stage codes such as `G0`, `G1`, or `G2`.

## Decision

Adopt the following workflow principles:

* Formality only at state transitions.
* Physics-first everywhere else.
* Concrete task names first; internal stage anchors are secondary labels.

Full TASK files and CODEX reports are required when repository files change, commands are run, or project state, gate status, validation status, claim evidence, numerical evidence, figure evidence, or manuscript text may change.

Non-state-changing physical reasoning should use lightweight physics notes. These notes may propose candidate equations, interpretations, or checks, but must not promote claims or validated status.

## Alternatives considered

1. Keep full formal task protocol for every interaction.
2. Remove most structure and rely on chat context.
3. Keep formal gates but introduce lightweight physics notes for routine reasoning.

Alternative 3 was selected because it preserves safeguards around validation while reducing friction during physical reasoning.

## Consequences

The workflow should become easier to use with a physics expert while retaining auditability at gate transitions.

Codex tasks remain constrained and report-driven. ChatGPT reviews remain physics-first unless a state transition is being prepared.

Future tasks should be named by their concrete content, for example `Resolve Free-Surface Reactant Boundary-Condition Convention` or `Define Front and Barrier Observables`.

## Follow-up checks

* `make quickcheck` should verify the presence of physics-note and workflow-evaluation structure.
* Stale stage assertions should be removed from tests.
* Candidate claims should not live as substantive evidence inside `docs/validated/`.
* Workflow retrospectives should record whether the new split reduces friction without allowing claim promotion.
