# Migrated Manuscript Figure 9

Status: migrated asset bundle, not validated.

The current source draft does not contain a literal `fig9` source filename. Its
ninth LaTeX figure environment is the spinodal-decomposition appendix figure,
stored in the source project as `fig7`.

Source: `../paper_latest/paper_latest/Figure/fig7`,
`../paper_latest/paper_latest/data/fig7`, and corresponding `scripts/fig7*`
plus `spinodal_demo.py`.

## Layout

* `Figure/fig7/`: generated PDF/PNG panels and composite figure.
* `data/fig7/`: cached data used by the plotting scripts.
* `scripts/`: figure builders and helper scripts copied from the source draft.

The original source filename `fig7` is preserved inside this `fig09` bundle for
script compatibility and auditability.

## Solver status

The local `scripts/scan_optimized.py` copy is frozen provenance for the migrated
figure bundle. It is not the active canonical solver definition. New
non-evidence smoke runs and future paper-evidence regeneration should use
`paper/solver/canonical_cpu/`. This figure-local solver copy must remain a
historical source artifact, not an independent model definition.
