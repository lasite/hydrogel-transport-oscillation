# TASK: Replace Initial Model Derivation from Migrated Appendix and Request ChatGPT Review

## Concrete task name

Replace Initial Model Derivation from Migrated Appendix and Request ChatGPT Review

## Task ID or slug

`replace-initial-model-derivation-from-paper-appendix`

## Human-readable stage

Model Specification

## Internal stage anchor

`G2_model`

## Objective

Replace `docs/derivations/initial_model_derivation.tex` with the complete model-construction and nondimensionalization material from `paper/appendix/appendix.tex`, then prepare the result for ChatGPT scientific review.

This task reflects the user clarification that Model A was derived from the draft model in `paper/appendix/appendix.tex`. The goal is therefore not to treat the old `docs/derivations/initial_model_derivation.tex` and the migrated appendix as independent model sources. The migrated appendix is the source of the current Model A derivation.

The output remains candidate model-source material only. This task does not validate the model, numerical results, figures, mechanisms, or manuscript claims.

## Scientific or workflow context

The previous task framing asked Codex to reconcile Model A with the migrated draft. The user clarified that Model A is actually based on the draft appendix model. The repository should therefore make `docs/derivations/initial_model_derivation.tex` match the migrated appendix source before ChatGPT performs the scientific review.

The source material to preserve is the complete Appendix A and Appendix B content from `paper/appendix/appendix.tex`:

* `\section{Model Construction}` / `\label{app:model}`;
* `\section{Nondimensionalization}` / `\label{app:nondim}`.

The replacement should copy this material faithfully, not rewrite the equations or silently resolve scientific issues. Any wrapper, preamble, macro, or heading changes needed for the derivation file to compile must be documented as mechanical formatting changes.

No model or claim was promoted to validated status.

## Inputs

* `docs/project_state.md`.
* `docs/reports/exploration/GPT-REVIEW-paper-latest-migration.md`.
* `docs/reports/exploration/CODEX-REPORT-paper-latest-migration.md`.
* `docs/reports/exploration/CODEX-REPORT-resolve-paper-latest-migration-hygiene.md`, if the migration-hygiene PR has been merged.
* `docs/model_candidates/model_A_initial_lcst_transport_barrier.md`.
* `docs/derivations/initial_model_derivation.tex`.
* `paper/appendix/appendix.tex`.
* `paper/sections/model.tex` only as a cross-check against the extracted appendix model summary.

## Allowed files to read

* `README.md`.
* `AGENTS.md`.
* `docs/project_state.md`.
* `docs/stages/02_model/gate.md`.
* `docs/stages/stage_index.md`.
* `docs/model_candidates/model_A_initial_lcst_transport_barrier.md`.
* `docs/derivations/initial_model_derivation.tex`.
* `docs/reports/exploration/GPT-REVIEW-paper-latest-migration.md`.
* `docs/reports/exploration/CODEX-REPORT-paper-latest-migration.md`.
* `docs/reports/exploration/CODEX-REPORT-resolve-paper-latest-migration-hygiene.md`, if present.
* `paper/appendix/appendix.tex`.
* `paper/sections/model.tex`.

## Allowed files to modify

* `docs/derivations/initial_model_derivation.tex`.
* `docs/model_candidates/model_A_initial_lcst_transport_barrier.md`, only to update ingestion/provenance text saying that the active Model A derivation now comes from `paper/appendix/appendix.tex` Appendix A--B.
* `docs/project_state.md`, only if the next task or blocker list needs to reflect that ChatGPT review is pending.
* `docs/stages/stage_index.md`, only if the next task label changes.
* A CODEX report at `docs/reports/exploration/CODEX-REPORT-replace-initial-model-derivation-from-paper-appendix.md`.

## Forbidden actions

* Do not edit, simplify, correct, or reinterpret the model equations during the copy.
* Do not silently resolve boundary-condition, material-function, nondimensionalization, or notation issues.
* Do not move any file into `docs/validated/`.
* Do not claim that the model is validated.
* Do not write or refactor a production PDE solver.
* Do not run large simulations, parameter scans, or figure-generation jobs.
* Do not treat migrated figure data or CPU solver outputs as reproduced evidence.
* Do not begin manuscript drafting.
* Do not use OCR or PDF extraction when the LaTeX source exists.

## Required replacement behavior

1. Replace the body of `docs/derivations/initial_model_derivation.tex` with a self-contained LaTeX derivation document built from `paper/appendix/appendix.tex` Appendix A--B.
2. Extract the complete content from `\section{Model Construction}` through the end of `\section{Nondimensionalization}`, stopping before the next appendix section, for example the linear-stability appendix section.
3. Preserve the source equations, labels, prose, assumptions, and subsection structure as source material.
4. Add only mechanical document wrapper material required for compilation, such as document class, packages, macro definitions, title, and a short provenance note.
5. If any label or macro must be adjusted for standalone compilation, record the exact change and reason in the CODEX report.
6. Do not include linear-stability, numerical-method, spinodal-verification, or later appendix sections in `initial_model_derivation.tex` unless they are needed only as cross-references in comments.
7. Leave unresolved scientific issues unresolved for ChatGPT review rather than editing the model.

## Deliverables

1. `docs/derivations/initial_model_derivation.tex` fully replaced by the Appendix A--B model construction and nondimensionalization source material.
2. A provenance note in the derivation file or nearby comments identifying `paper/appendix/appendix.tex` as the source.
3. Optional update to `docs/model_candidates/model_A_initial_lcst_transport_barrier.md` clarifying that Model A is derived from the migrated appendix model.
4. Optional update to `docs/project_state.md` marking ChatGPT review of the replaced derivation as the next required Model Specification action.
5. A CODEX report with:
   * source section boundaries used;
   * exact files modified;
   * any mechanical wrapper/macro/label changes;
   * verification commands and exit codes;
   * explicit statement that no scientific corrections were made;
   * explicit request for ChatGPT review.

## ChatGPT review handoff requirements

The CODEX report must include a section titled `For ChatGPT Review` listing the review questions that remain after replacement. At minimum, include:

1. Are the conserved variables and state vector internally consistent?
2. Are the solvent, reactant, and heat flux sign conventions consistent with the integral conservation laws?
3. Are the free-surface boundary conditions physically and dimensionally consistent?
4. Is the `chi(T,phi)` chemical-potential derivative handled consistently?
5. Are current-coordinate and reference-coordinate material coefficients clearly distinguished?
6. Are accessibility, diffusivity, and mobility suppression functions physically justified as candidate closures?
7. Are all nondimensional groups defined with correct dimensions and signs?
8. Which parts should enter the eventual candidate model specification, and which should remain unresolved?

Codex must not answer these scientific review questions as final authority. They are for ChatGPT review after the replacement task.

## Verification commands

At minimum:

```bash
make derivations
```

```bash
make quickcheck
```

```bash
git diff --check
```

No numerical simulation verification is expected in this task.

## Acceptance criteria

* `docs/derivations/initial_model_derivation.tex` contains the complete model-construction and nondimensionalization material from `paper/appendix/appendix.tex` Appendix A--B.
* Linear-stability and numerical appendix sections are not copied into `initial_model_derivation.tex`.
* The derivation file compiles or `make derivations` records a non-scientific environment failure.
* Any changes relative to the source appendix text are mechanical and documented.
* The task explicitly hands the replaced derivation back to ChatGPT for scientific review.
* No model, numerical result, figure, or claim is promoted to validated status.
* `make quickcheck` passes.

## Failure conditions

* The source section boundaries in `paper/appendix/appendix.tex` cannot be identified unambiguously.
* The replacement requires changing equations or scientific content to compile.
* Macro or label conflicts cannot be resolved mechanically.
* The task discovers that the migrated appendix lacks part of the intended model construction or nondimensionalization; in that case, record the gap and stop before inventing replacement content.
* Any production solver or parameter scan is introduced.
* Any claim is moved into `docs/validated/`.

## Required CODEX-REPORT path

`docs/reports/exploration/CODEX-REPORT-replace-initial-model-derivation-from-paper-appendix.md`

## User approval required before merge

Yes

## ChatGPT review required before merge

Yes
