# Paper

This directory contains placeholder manuscript files plus selected migrated
materials from the sibling `paper_latest` draft.

Formal manuscript writing should begin after the model and core claims have been organized, sanity-checked, and at least preliminarily verified.

Migrated material is kept as provenance-bearing source material, not as a
validated manuscript claim:

* `sections/`: extracted manuscript fragments from the draft.
* `appendix/`: extracted appendix fragment from the draft.
* `figures/`: selected figure assets, data, and plotting scripts.
* `solver/`: official paper-reproduction smoke entry point, migrated CPU model
  script, and historical diagnostic helpers from the draft.
* `paper_latest_migration_manifest.tsv`: exact source-to-destination mapping.
* `paper_latest_provenance.md`: source project and migration notes.

The official paper-reproduction solver route is
`paper.solver.official_paper_solver`, which invokes
`paper/solver/paper_latest_cpu/scan_optimized.py`. Reduced Fig. 1/2/3/9 smoke
checks can be run with:

```bash
python -m paper.solver.run_figure_smoke_checks
```

These checks only confirm that reduced workflows start, call
`scan_optimized.py`, and write expected artifact classes. They are not
full-resolution figure reproduction and are not numerical validation.
