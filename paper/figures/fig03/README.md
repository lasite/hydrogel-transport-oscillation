# Migrated Figure 3

Status: migrated asset bundle, not validated.

Source: `../paper_latest/paper_latest/Figure/fig3`,
`../paper_latest/paper_latest/data/fig3`, the shared Figure 2 cache needed by
the copied helper, and corresponding `scripts/fig3*` builders.

## Layout

* `Figure/fig3/`: generated PDF/PNG panels and composite figure.
* `data/fig3/`: cached data used by Figure 3 scripts.
* `data/fig2/cache.npz`: shared cache required by the migrated Figure 3 helper.
  This path is a relative symlink to `../shared/` data to avoid storing a
  duplicate near-100 MB file.
* `scripts/`: figure builders and helper scripts copied from the source draft.

The original relative layout is preserved so the copied scripts can be run from
this figure bundle without path rewrites.

## Solver status

The local `scripts/scan_optimized.py` copy is frozen provenance for the migrated
figure bundle. It is not the active official solver definition. Reduced
non-evidence smoke runs use `paper.solver.official_paper_solver`, which routes
to `paper/solver/paper_latest_cpu/scan_optimized.py`. This figure-local solver
copy must remain a historical source artifact, not an independent model
definition.
