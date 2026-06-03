# CODEX Report: Replace Initial Model Derivation from Migrated Appendix

## Concrete task name

Replace Initial Model Derivation from Migrated Appendix and Request ChatGPT Review

## Task ID or slug

`replace-initial-model-derivation-from-paper-appendix`

## Human-readable stage

Model Specification

## Internal stage anchor

`G2_model`

## Base commit

`0bc4d9f`

## Final commit

Implementation commit: `2ae8287`

## Branch or worktree name

`codex/reconcile-migrated-draft-model`

## Files changed

* `docs/derivations/initial_model_derivation.tex`
* `docs/rendered/initial_model_derivation.pdf`
* `docs/model_candidates/model_A_initial_lcst_transport_barrier.md`
* `docs/project_state.md`
* `docs/stages/stage_index.md`
* `docs/reports/exploration/CODEX-REPORT-replace-initial-model-derivation-from-paper-appendix.md`

## Summary of changes

`docs/derivations/initial_model_derivation.tex` was replaced with a
self-contained LaTeX document built from the migrated appendix source material.

Source boundaries used:

* Source file: `paper/appendix/appendix.tex`
* Start: line 6, `\section{Model Construction}`
* Included: Appendix A `Model Construction`
* Included: Appendix B `Nondimensionalization`
* Stop: before line 446, `\section{Homogeneous Diagnostic Derivation}`

Excluded sections:

* Appendix C `Homogeneous Diagnostic Derivation`
* Appendix D `Numerical Method`
* Appendix spinodal-decomposition verification

The model-candidate summary and project-state files were updated only to record
that the active Model A derivation now comes from migrated Appendix A--B and
that ChatGPT scientific review is pending.

## Mechanical wrapper and macro changes

The copied source material was not scientifically edited. The following
mechanical wrapper material was added so the derivation can compile standalone:

* `article` document class.
* Packages: `amsmath`, `amssymb`, `bm`, `geometry`.
* Macro definitions for symbols used by the appendix source:
  `\Ms`, `\Ds`, `\Cs`, `\Ks`, `\Da`, `\Bi`, `\Pe`, `\Rhat`, and `\pp`.
* Title, author, date, and a provenance note.
* `\begin{document}`, `\maketitle`, and `\end{document}`.

No equations, labels, scientific assumptions, or model closures were changed to
make the document compile.

## Commands run

| Command | Exit code |
| ------- | --------- |
| `git fetch origin --prune` | 0 |
| `git switch main && git pull --ff-only origin main && git switch -c codex/reconcile-migrated-draft-model` | 0 |
| mechanical extraction of `paper/appendix/appendix.tex` lines 6--445 into `docs/derivations/initial_model_derivation.tex` with standalone wrapper | 0 |
| `. .venv/bin/activate && make derivations` | 0 |
| `. .venv/bin/activate && make quickcheck` | 0 |
| `git diff --check` | 0 |
| `rg -n "^\\section\\{Homogeneous Diagnostic Derivation\\}\|^\\section\\{Numerical Method\\}\|^\\section\\{Spinodal Decomposition Verification\\}" docs/derivations/initial_model_derivation.tex \|\| true` | 0 |

## Environment

OS if known: Linux

Python version: Python 3.12.3 from `.venv`

Dependency setup command used: none during this task.

## Artifacts produced

* Updated LaTeX derivation source:
  `docs/derivations/initial_model_derivation.tex`
* Rendered derivation PDF:
  `docs/rendered/initial_model_derivation.pdf`

## Checks passed

* `make derivations` completed successfully.
* `make quickcheck` passed: 10 tests passed.
* `git diff --check` passed.
* The new derivation contains Appendix A--B only.
* Linear-stability, numerical-method, and spinodal-verification appendix
  sections are not copied into the active derivation file.
* The only occurrence of `Homogeneous Diagnostic Derivation` in the new
  derivation file is in the provenance note identifying the stop boundary.

## Checks failed

None.

## Warnings

`make derivations` reports unresolved citations inherited from the appendix
source:

* `Flory1953`
* `Hong2008`

These citations were preserved as source material. They should be resolved in a
future bibliography cleanup task rather than silently removed from the
derivation.

## Known limitations

* The replacement does not validate the equations.
* The replacement does not resolve boundary-condition signs, material closures,
  state-variable conventions, or nondimensionalization questions.
* The replaced derivation still requires ChatGPT scientific review before it can
  become an accepted candidate model specification.

## Deviations from task instructions

None.

## Forbidden actions avoided

* No model equations were edited, simplified, corrected, or reinterpreted.
* No boundary-condition, material-function, nondimensionalization, or notation
  issue was silently resolved.
* No file was moved into `docs/validated/`.
* No model or claim was marked validated.
* No production PDE solver was written or refactored.
* No simulations, parameter scans, or figure-generation jobs were run.
* No manuscript drafting was started.

No model or claim was promoted to validated status.

## For ChatGPT Review

Please review the replaced Appendix A--B derivation as candidate model-source
material. Do not treat the equations as validated.

Questions to answer:

1. Are the conserved variables and state vector internally consistent?
2. Are the solvent, reactant, and heat flux sign conventions consistent with
   the integral conservation laws?
3. Are the free-surface boundary conditions physically and dimensionally
   consistent?
4. Is the `chi(T,phi)` chemical-potential derivative handled consistently?
5. Are current-coordinate and reference-coordinate material coefficients
   clearly distinguished?
6. Are accessibility, diffusivity, and mobility suppression functions
   physically justified as candidate closures?
7. Are all nondimensional groups defined with correct dimensions and signs?
8. Which parts should enter the eventual candidate model specification, and
   which should remain unresolved?

## Recommended next task

Request ChatGPT scientific review of
`docs/derivations/initial_model_derivation.tex`, then rebuild the Model
Specification blocker list from that review.
