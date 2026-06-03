# CODEX Report: Resolve paper_latest Migration Hygiene

## Concrete task name

Resolve `paper_latest` Migration Hygiene

## Task ID or slug

`resolve-paper-latest-migration-hygiene`

## Human-readable stage

Model Specification

## Internal stage anchor

`G2_model`

## Base commit

`a7e44ee`

## Final commit

Pending at report creation.

## Branch or worktree name

`codex/resolve-paper-latest-migration-hygiene`

## Files changed

* `pyproject.toml`
* `paper/sections/linear_stability.tex`
* `paper/appendix/appendix.tex`
* `paper/figures/fig02/README.md`
* `paper/figures/fig03/README.md`
* `paper/figures/fig02/data/fig2/cache.npz`
* `paper/figures/fig03/data/fig2/cache.npz`
* `paper/figures/shared/README.md`
* `paper/figures/shared/data/fig2/cache.npz`
* `paper/paper_latest_provenance.md`
* `paper/paper_latest_migration_manifest.tsv`
* `docs/reports/exploration/CODEX-REPORT-paper-latest-migration.md`
* `docs/reports/exploration/CODEX-REPORT-resolve-paper-latest-migration-hygiene.md`

## Summary of changes

* Declared `pypdf` as a project dependency and installed it into the current
  `.venv` using `uv`.
* Updated migrated LaTeX fragment figure paths so they resolve from the future
  `paper/` manuscript context:
  * `figures/fig01/Figure/fig1/fig1.pdf`
  * `figures/fig09/Figure/fig7/fig7.pdf`
* Deduplicated the two identical near-100 MB Figure 2 cache files into
  `paper/figures/shared/data/fig2/cache.npz`.
* Preserved the old Figure 2 and Figure 3 local cache paths as symlinks for
  script compatibility.
* Expanded the migration manifest with destination kind, size, checksum, or
  symlink target.
* Expanded provenance with concrete source dirty status, section-title mapping,
  figure-path convention, and large-cache decision.
* Updated the original migration report with PR #7 merge metadata and the
  post-cleanup status.

## Commands run

| Command | Exit code |
| ------- | --------- |
| `git fetch origin --prune` | 0 |
| `git switch main && git pull --ff-only origin main && git switch -c codex/resolve-paper-latest-migration-hygiene` | 0 |
| `sha256sum paper/figures/fig02/data/fig2/cache.npz paper/figures/fig03/data/fig2/cache.npz` | 0 |
| `cmp -s paper/figures/fig02/data/fig2/cache.npz paper/figures/fig03/data/fig2/cache.npz` | 0 |
| `git -C /home/kiki/code/Wang/paper_latest/paper_latest status --short --branch` | 0 |
| `git -C /home/kiki/code/Wang/paper_latest/paper_latest rev-parse HEAD` | 0 |
| `git mv paper/figures/fig02/data/fig2/cache.npz paper/figures/shared/data/fig2/cache.npz` | 0 |
| `git rm paper/figures/fig03/data/fig2/cache.npz` | 0 |
| `ln -s ../../../shared/data/fig2/cache.npz ...` for Figure 2 and Figure 3 cache paths | 0 |
| `python3 ...` to regenerate `paper/paper_latest_migration_manifest.tsv` with audit metadata | 0 |
| `uv pip install --python .venv/bin/python -e .` | 0 |
| `cd paper/figures/fig01/scripts && timeout 60s python make_fig1.py` | 0 |
| `cd paper/figures/fig02/scripts && timeout 60s python make_fig2.py` | 0 |
| `cd paper/figures/fig03/scripts && timeout 60s python make_fig3.py` | 0 |
| `cd paper/figures/fig09/scripts && timeout 60s python make_fig7.py` | 0 |
| `python -m py_compile $(find paper/figures/fig01/scripts paper/figures/fig02/scripts paper/figures/fig03/scripts paper/figures/fig09/scripts paper/solver/paper_latest_cpu -name '*.py' -print \| sort)` | 0 |
| `make quickcheck` | 0 |
| `make derivations` | 0 |
| `git diff --check` | 0 |

## Environment

OS if known: Linux

Python version: Python 3.12.3 from `.venv`

Dependency setup command used:

```bash
uv pip install --python .venv/bin/python -e .
```

Installed plotting dependency:

* `pypdf==6.12.2`

## Artifacts produced

* Shared cache location: `paper/figures/shared/data/fig2/cache.npz`
* Cache compatibility symlinks:
  * `paper/figures/fig02/data/fig2/cache.npz`
  * `paper/figures/fig03/data/fig2/cache.npz`
* Expanded audit manifest: `paper/paper_latest_migration_manifest.tsv`
* Handoff report: `docs/reports/exploration/CODEX-REPORT-resolve-paper-latest-migration-hygiene.md`

## Checks passed

* The two duplicated cache files were byte-identical before deduplication.
* The retained shared cache has SHA-256:
  `98be3745de15b36fb254debed69e6c6aa4072fcc9df7ac8d5f1cf7f7bf84d825`.
* Migrated LaTeX figure paths resolve to existing files under `paper/`.
* Four composite figure smoke tests passed after `pypdf` was installed.
* `py_compile` passed for migrated figure scripts and CPU helper scripts.
* `make quickcheck` passed: 10 tests passed.
* `make derivations` passed with `latexmk`; derivation PDF was up to date.
* `git diff --check` passed.

## Checks failed

None after cleanup.

## Known limitations

* The source `paper_latest` tree remains dirty. The concrete dirty status is now
  recorded, but it is still a dirty-tree provenance import, not a clean tagged
  source release.
* The shared cache file is still 96,403,852 bytes. It is no longer duplicated,
  but remains above GitHub's recommended 50 MB threshold.
* The composite smoke tests confirm script execution and figure assembly only.
  They do not validate figure data, numerical results, model equations, or
  scientific claims.
* Verification-generated binary composite changes were not retained in this
  cleanup diff because this task is repository hygiene, not figure regeneration.

## Deviations from task instructions

None.

## Forbidden actions avoided

* No model equations, closures, nondimensionalization, captions, or scientific
  claims were edited.
* No imported material was moved into `docs/validated/`.
* No production PDE solver was written or refactored.
* No large simulations or new large datasets were created.
* No imported numerical output was described as reproduced or validated.
* No manuscript drafting was started.

No model or claim was promoted to validated status.

## Recommended next task

After human approval and ChatGPT review, continue with
`docs/tasks/exploration/TASK-reconcile-migrated-draft-model-with-model-A.md`.
