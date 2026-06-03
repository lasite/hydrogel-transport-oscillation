# Migrated Figure 1

Status: migrated asset bundle, not validated.

Source: `../paper_latest/paper_latest/Figure/fig1`,
`../paper_latest/paper_latest/data/fig1`, and corresponding `scripts/fig1*`
plus shared style, stability, and CPU-model helpers needed by those scripts.

## Layout

* `Figure/fig1/`: generated PDF/PNG panels and composite figure.
* `data/fig1/`: cached data used by the plotting scripts.
* `scripts/`: figure builders and helper scripts copied from the source draft.

The original relative layout is preserved so the copied scripts can be run from
this figure bundle without path rewrites.

## Solver status

The local `scripts/scan_optimized.py` copy is frozen provenance for the migrated
figure bundle. It is not the active canonical solver definition. New
non-evidence smoke runs should use `paper/solver/canonical_cpu/`; future
paper-evidence regeneration must not rely on this figure-local solver copy as an
independent model definition.
