# Migrated Figure 2

Status: migrated asset bundle, not validated.

Source: `../paper_latest/paper_latest/Figure/fig2`,
`../paper_latest/paper_latest/data/fig2`, selected cached grids from
`../paper_latest/paper_latest/data/fig4`, and corresponding figure scripts.

## Layout

* `Figure/fig2/`: generated PDF/PNG panels and composite figure.
* `data/fig2/`: cached data used directly by Figure 2 scripts. The large
  `cache.npz` path is a relative symlink to `../shared/` data to avoid storing
  a duplicate near-100 MB file.
* `data/fig4/`: supporting cached grids used by the migrated Figure 2 data
  helper.
* `scripts/`: figure builders and helper scripts copied from the source draft.

The original relative layout is preserved so the copied scripts can be run from
this figure bundle without path rewrites.
