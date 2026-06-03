# TASK: Resolve `paper_latest` Migration Hygiene

## Concrete task name

Resolve `paper_latest` Migration Hygiene

## Task ID or slug

`resolve-paper-latest-migration-hygiene`

## Human-readable stage

Model Specification

## Internal stage anchor

`G2_model`

## Objective

Clean up the merged `paper_latest` provenance import so the migrated manuscript fragments, figure bundles, plotting scripts, data, CPU solver source, manifest, and report can serve as stable source material for later Model Specification review.

This task is repository hygiene and auditability work only. It must not validate model equations, numerical results, figures, mechanisms, or manuscript claims.

## Scientific or workflow context

PR `#7` imported selected prior-draft assets from the sibling `paper_latest` project. GPT review found that the import is useful but still has integration blockers: unresolved LaTeX figure paths, failed figure smoke tests due to missing `pypdf`, incomplete dirty-working-tree provenance, near-100 MB duplicate cache files, incomplete report metadata, and a section-title mismatch between the requested `III. LINEAR STABILITY ANALYSIS` and migrated `III. HOMOGENEOUS STABILITY DIAGNOSTIC`.

Resolving these issues is required before the imported draft can be used as a stable reference in the next Model Specification task.

No model or claim was promoted to validated status.

## Inputs

* GitHub issue `#6`.
* Merged PR `#7`.
* `docs/reports/exploration/CODEX-REPORT-paper-latest-migration.md`.
* `docs/reports/exploration/GPT-REVIEW-paper-latest-migration.md`.
* `paper/paper_latest_provenance.md`.
* `paper/paper_latest_migration_manifest.tsv`.
* `paper/sections/model.tex`.
* `paper/sections/linear_stability.tex`.
* `paper/appendix/appendix.tex`.
* `paper/figures/fig01/`.
* `paper/figures/fig02/`.
* `paper/figures/fig03/`.
* `paper/figures/fig09/`.
* `paper/solver/paper_latest_cpu/`.

## Allowed files to read

* `README.md`.
* `AGENTS.md`.
* `docs/project_state.md`.
* `docs/stages/stage_index.md`.
* `docs/tasks/TASK-TEMPLATE.md`.
* `docs/reports/exploration/CODEX-REPORT-paper-latest-migration.md`.
* `docs/reports/exploration/GPT-REVIEW-paper-latest-migration.md`.
* `paper/**`.
* Repository dependency files, Makefiles, and environment files if present.
* The sibling source tree `../paper_latest` only for provenance reconstruction and checksums.

## Allowed files to modify

* `paper/sections/model.tex` only if needed for path/comment consistency.
* `paper/sections/linear_stability.tex`.
* `paper/appendix/appendix.tex`.
* `paper/figures/fig01/README.md`.
* `paper/figures/fig02/README.md`.
* `paper/figures/fig03/README.md`.
* `paper/figures/fig09/README.md`.
* `paper/paper_latest_provenance.md`.
* `paper/paper_latest_migration_manifest.tsv`.
* `docs/reports/exploration/CODEX-REPORT-paper-latest-migration.md`.
* Dependency/environment files only if required to declare `pypdf` or equivalent plotting dependency.
* Files needed to remove or deduplicate the two large duplicate cache files, provided the report records the exact decision and mapping.
* A new handoff report at `docs/reports/exploration/CODEX-REPORT-resolve-paper-latest-migration-hygiene.md`.

## Forbidden actions

* Do not edit model equations, closures, nondimensionalization, captions, or scientific claims except for path/provenance comments required by this hygiene task.
* Do not promote imported material into `docs/validated/`.
* Do not write or refactor a production PDE solver.
* Do not run new large simulations or create new large datasets.
* Do not delete figure data unless replacing it with a documented shared location or Git LFS decision.
* Do not treat successful plotting as scientific validation.
* Do not begin manuscript drafting.

## Deliverables

1. Migrated LaTeX fragments either contain repository-relative figure paths or have a documented wrapper/`\graphicspath` convention that makes the paths resolvable from the future `paper/` manuscript context.
2. Plotting dependency handling is fixed: either `pypdf` is declared in repository dependencies, or composite scripts degrade gracefully by generating PNG and clearly skipping PDF assembly when `pypdf` is unavailable.
3. Figure composite smoke tests for Figures 1, 2, 3, and 9 are rerun and recorded.
4. Dirty-source provenance is expanded with the concrete `git status --short` output from `../paper_latest` and checksums or equivalent audit records for migrated source files and large data files.
5. The duplicate near-100 MB cache files are deduplicated, moved to a shared location, moved to Git LFS, or explicitly retained with checksum evidence and rationale.
6. Migration report metadata is updated with final merge or post-cleanup commit information.
7. The section-title mismatch is explicitly resolved in provenance/report text.
8. A CODEX report records commands, exit codes, changed files, decisions, and unresolved items.

## Verification commands

Run the lightest practical checks available after cleanup:

```bash
make quickcheck
```

```bash
make derivations
```

```bash
python -m py_compile $(find paper/figures/fig01/scripts paper/figures/fig02/scripts paper/figures/fig03/scripts paper/figures/fig09/scripts paper/solver/paper_latest_cpu -name '*.py' -print | sort)
```

Run the composite plotting smoke tests or documented equivalents:

```bash
cd paper/figures/fig01/scripts && timeout 60s python make_fig1.py
cd paper/figures/fig02/scripts && timeout 60s python make_fig2.py
cd paper/figures/fig03/scripts && timeout 60s python make_fig3.py
cd paper/figures/fig09/scripts && timeout 60s python make_fig7.py
```

If one of these commands cannot be run, record the exact reason and whether the failure is a dependency issue, path issue, data-size issue, or scientific/runtime issue.

## Acceptance criteria

* All migrated LaTeX figure references are resolvable under a documented repository-relative convention.
* Figure smoke tests either pass or have a documented, intentionally accepted skip path that still confirms PNG generation and missing-PDF dependency behavior.
* `paper_latest` dirty-source provenance is auditable beyond source HEAD alone.
* The large cache-file decision is explicit and reproducible.
* The `III. LINEAR STABILITY ANALYSIS` versus `III. HOMOGENEOUS STABILITY DIAGNOSTIC` mapping is recorded clearly.
* `make quickcheck` passes.
* No model, result, figure, or claim is promoted to validated status.

## Failure conditions

* Any migrated model equation or scientific claim is edited outside path/provenance context.
* Any production PDE solver work is introduced.
* Any imported numerical output is described as reproduced or validated without a verification task.
* Large data are deleted without preserving or documenting the source-to-destination mapping.
* The task cannot reconstruct enough source provenance to audit the imported dirty working tree; in that case, stop and request human review.

## Required CODEX-REPORT path

`docs/reports/exploration/CODEX-REPORT-resolve-paper-latest-migration-hygiene.md`

## User approval required before merge

Yes

## ChatGPT review required before merge

Yes
