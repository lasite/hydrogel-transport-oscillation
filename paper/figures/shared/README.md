# Shared Migrated Figure Data

Status: migrated source material, not validated evidence.

This directory stores large data files shared by more than one migrated figure
bundle. The original per-figure paths are preserved as relative symlinks when
scripts expect them.

## Shared files

* `data/fig2/cache.npz`: shared cache originally copied into both Figure 2 and
  Figure 3 bundles. The duplicated files had identical SHA-256 checksums and
  were deduplicated into this location during migration hygiene cleanup.

The symlinks are path-compatibility shims only; they do not validate the figure
data or associated numerical results.
