# CODEX Report: paper_latest Migration

## Concrete task name

Migrate Selected `paper_latest` Manuscript, Figure, Data, and CPU Solver Assets

## Task ID or slug

GitHub issue #6

## Human-readable stage

Model Specification / manuscript-source audit support

## Internal stage anchor

G2

## Base commit

`e5889a8`

## Final commit

Migration branch commit: `6a8e94551a4283b523bbf3a0bb8eca996070d202`

Merged by PR `#7` as merge commit:
`539374dd5997cc475221d419ed9106647a11e036`

Post-merge hygiene is recorded separately in
`docs/reports/exploration/CODEX-REPORT-resolve-paper-latest-migration-hygiene.md`.

## Branch or worktree name

`codex/migrate-paper-latest-assets`

## Files changed

Created or updated:

* `paper/README.md`
* `paper/sections/model.tex`
* `paper/sections/linear_stability.tex`
* `paper/sections/README.md`
* `paper/appendix/appendix.tex`
* `paper/appendix/README.md`
* `paper/figures/fig01/`
* `paper/figures/fig02/`
* `paper/figures/fig03/`
* `paper/figures/fig09/`
* `paper/solver/paper_latest_cpu/`
* `paper/paper_latest_provenance.md`
* `paper/paper_latest_migration_manifest.tsv`
* `docs/reports/exploration/CODEX-REPORT-paper-latest-migration.md`

The exact copied-file mapping is recorded in
`paper/paper_latest_migration_manifest.tsv`. After post-merge hygiene cleanup,
the manifest contains 141 audit mappings with destination type, size, and
checksum or symlink target.

## Summary of changes

Selected content was migrated from the sibling source project
`/home/kiki/code/Wang/paper_latest/paper_latest`.

Manuscript fragments:

| Source | Destination | Notes |
| ------ | ----------- | ----- |
| `main.tex:130-273` | `paper/sections/model.tex` | Source `II. MODEL`. |
| `main.tex:275-393` | `paper/sections/linear_stability.tex` | Source `III. HOMOGENEOUS STABILITY DIAGNOSTIC`, corresponding to the requested linear-stability-analysis material. |
| `main.tex:1385-2192` | `paper/appendix/appendix.tex` | Full appendix fragment, excluding final `\end{document}` wrapper line. |

Figure bundles:

| Requested figure | Source bundle | Destination |
| ---------------- | ------------- | ----------- |
| Figure 1 | `Figure/fig1`, `data/fig1`, `scripts/fig1*` | `paper/figures/fig01/` |
| Figure 2 | `Figure/fig2`, `data/fig2`, selected supporting grids from `data/fig4`, `scripts/fig2*` and helpers | `paper/figures/fig02/` |
| Figure 3 | `Figure/fig3`, `data/fig3`, shared Figure 2 cache, `scripts/fig3*` and helpers | `paper/figures/fig03/` |
| Figure 9 | Source ninth figure environment stored as `fig7` spinodal appendix figure | `paper/figures/fig09/` |

CPU model source:

| Source | Destination |
| ------ | ----------- |
| `scripts/scan_optimized.py` | `paper/solver/paper_latest_cpu/scan_optimized.py` |
| `scripts/linear_stability_1d.py` | `paper/solver/paper_latest_cpu/linear_stability_1d.py` |

## Commands run

| Command | Exit code |
| ------- | --------- |
| `git -C /home/kiki/code/Wang/paper_latest/paper_latest status --short --branch` | 0 |
| `git -C /home/kiki/code/Wang/paper_latest/paper_latest rev-parse --short HEAD` | 0 |
| `find ... -type f -printf '%s %p\n'` for selected source assets | 0 |
| `sed -n ... main.tex > paper/sections/*.tex` and `paper/appendix/appendix.tex` | 0 |
| `cp -a` and `cp` for selected figure, data, script, and solver assets | 0 |
| `git rm` for unrelated Figure 4 caches accidentally copied with the Figure 2 support grids | 0 |
| `python ...` for manifest generation | 127 |
| `python3 ...` for manifest generation | 0 |
| `. .venv/bin/activate && python -m py_compile ...` | 0 |
| `. .venv/bin/activate && cd paper/solver/paper_latest_cpu && python -c "..."` | 0 |
| `. .venv/bin/activate && cd paper/figures/fig01/scripts && timeout 60s python make_fig1.py` | 1 |
| `. .venv/bin/activate && cd paper/figures/fig02/scripts && timeout 60s python make_fig2.py` | 1 |
| `. .venv/bin/activate && cd paper/figures/fig03/scripts && timeout 60s python make_fig3.py` | 1 |
| `. .venv/bin/activate && cd paper/figures/fig09/scripts && timeout 60s python make_fig7.py` | 1 |
| `. .venv/bin/activate && make quickcheck` | 0 |
| `. .venv/bin/activate && make derivations` | 0 |
| `git diff --check` | 0 |

## Environment

OS if known: Linux

Python version: Python 3.12.3 from `.venv`

Dependency setup command used: none during this task. Existing `.venv` was used.

## Artifacts produced

* Migrated manuscript fragments under `paper/sections/` and `paper/appendix/`.
* Migrated figure bundles under `paper/figures/fig01/`, `fig02/`, `fig03/`, and
  `fig09/`.
* Migrated CPU source under `paper/solver/paper_latest_cpu/`.
* Migration provenance note at `paper/paper_latest_provenance.md`.
* Exact manifest at `paper/paper_latest_migration_manifest.tsv`.

## Checks passed

* Source project and source HEAD were recorded.
* Migrated source line ranges were confirmed in the extracted LaTeX fragments.
* 50 migrated Python scripts passed `py_compile`.
* CPU solver smoke check passed by importing `scan_optimized`, finalizing a tiny
  parameter object, and constructing the initial state.
* `make quickcheck` passed: 10 tests passed.
* `make derivations` passed with `latexmk`; derivation PDF was up to date.
* `git diff --check` passed.

## Checks failed

* A direct `python` command failed because the system has no unqualified
  `python` executable. Retried successfully with `python3` and with the repo
  virtual environment.
* Composite plotting scripts for Figures 1, 2, 3, and 9 failed at PDF assembly
  because `pypdf` was not installed in the current `.venv`. This dependency
  issue was resolved in the follow-up hygiene task by declaring `pypdf` and
  rerunning the smoke tests successfully.

## Known limitations

* The source `paper_latest` working tree was dirty at migration time, so these
  files reflect the current local working tree rather than a clean committed
  source snapshot.
* The originally duplicated near-100 MB Figure 2 cache was deduplicated in the
  follow-up hygiene task to `paper/figures/shared/data/fig2/cache.npz`, with
  Figure 2 and Figure 3 local paths retained as symlinks.
* The migrated CPU script is source material from the draft. It was not promoted
  to a production solver for this repository.
* The migrated figure outputs and data were not scientifically revalidated.

## Deviations from task instructions

* The requested Figure 9 has no literal `fig9` source filename in the current
  source draft. The ninth LaTeX figure environment is the appendix spinodal
  figure, stored as `fig7` in the source project. It was migrated under
  `paper/figures/fig09/` with internal `fig7` paths preserved.
* The report is placed under the repository's Codex report convention:
  `docs/reports/exploration/`, rather than a new top-level `reports/` directory.

## Forbidden actions avoided

* No model equations were edited.
* No production PDE solver was written.
* No files were moved into `docs/validated/`.
* No CUDA solver or unrelated later-result outputs were migrated.

No model or claim was promoted to validated status.

## Recommended next task

Continue with
`docs/tasks/exploration/TASK-reconcile-migrated-draft-model-with-model-A.md`
after human approval and ChatGPT review of the migration-hygiene cleanup.
