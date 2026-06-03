# paper_latest Migration Provenance

Status: migrated source material, not validated evidence.

## Source

Source project:

* `/home/kiki/code/Wang/paper_latest/paper_latest`

Source git HEAD at migration time:

* `2afd850`

The source working tree was dirty at migration time. This migration therefore
uses the current sibling working tree content rather than a clean committed
snapshot. The exact copied file mapping is recorded in
`paper/paper_latest_migration_manifest.tsv`.

## Selected scope

Migrated from the source draft:

* manuscript `II. MODEL`;
* manuscript `III. HOMOGENEOUS STABILITY DIAGNOSTIC`, corresponding to the
  requested linear-stability-analysis material;
* the full appendix fragment;
* manuscript Figures 1, 2, 3, and 9 with data and plotting scripts;
* the CPU model script and homogeneous/stability helper.

Not migrated:

* CUDA solvers;
* unrelated later-result figures;
* broad parameter-scan outputs outside the selected figure dependencies;
* unrelated manuscript sections.

## Figure numbering note

The requested manuscript Figure 9 corresponds to the ninth figure environment
in the source draft, the appendix spinodal-decomposition figure. In source file
names this bundle is called `fig7`, so the migrated bundle is stored under
`paper/figures/fig09/` while preserving internal `fig7` paths for script
compatibility.

## Validation status

These files are imported for audit and future review only. No model, claim,
figure, or numerical result is promoted to validated status by this migration.
