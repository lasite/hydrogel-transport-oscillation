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

## Hygiene update

Updated during `resolve-paper-latest-migration-hygiene` on 2026-06-03.

The source HEAD was rechecked and remained:

* `2afd850bc953bf10785fdd275c0a520a2ad0b2e1`

The concrete source dirty state reconstructed from
`/home/kiki/code/Wang/paper_latest/paper_latest` was:

```text
## main...origin/main
 M Figure/pub/fig2.pdf
 M Figure/pub/fig2.png
 M Figure/pub/fig4.pdf
 M Figure/pub/fig4.png
 M Figure/pub/fig5.pdf
 M Figure/pub/fig5.png
 M Figure/pub/fig6.pdf
 M Figure/pub/fig6.png
 M Figure/pub/fig7.pdf
 M Figure/pub/fig7.png
 D PLAN_section_IV.md
 M data/fig5/phase_timescales_WP.json
 M data/iv_c/lt_patch/sweep_summary.json
 M data/iv_c/phaseA/amplitude_results.json
 M data/iv_c/phaseA5/convergence_raw.json
 M data/iv_c/phaseB/period_raw.json
 M data/iv_c/phaseC/pde_bisection_log.json
 M data/iv_c/phaseC/pde_bisection_log_BiT006.json
 M data/iv_c/phaseD/BiT_slice_raw.json
 M data/iv_c/phaseD/main_grid_raw.json
 D draft_section_IV_A.tex
 D draft_section_IV_B.tex
 D draft_section_IV_C.tex
 D draft_section_IV_D.tex
 D draft_section_IV_all.tex
 M main.tex
 M scripts/linear_stability_1d.py
 M scripts/scan_optimized.py
?? Figure/fig2/
?? Figure/fig4/
?? Figure/fig5/
?? Figure/fig6/
?? Figure/fig7/
?? Figure/phase_diagram/
?? Figure/pub/multistab_phase_diagram.pdf
?? Figure/pub/multistab_phase_diagram.png
?? data/fig2/panel_a.npz
?? data/fig2/panel_b.npz
?? data/fig2/panel_c.npz
?? data/fig2/panel_d.npz
?? "data/fig4\" && cp E:wangpaper_latestpaper_latestarchivescrapdatagrid_25x25fig4_grid_Bi_T_Da.npz E:wangpaper_latestpaper_latestdatafig4\""
?? data/fig4/fig4_grid_Bi_T_Da.npz
?? data/fig4/fig4_grid_Bi_T_S_chi.npz
?? data/fig4/fig4_grid_smoke.npz
?? data/fig4/panel_a.npz
?? data/fig4/panel_b.npz
?? data/fig4/panel_c.npz
?? data/fig4/panel_d.npz
?? data/fig5/panel_a.npz
?? data/fig5/panel_b.npz
?? data/fig6/panel_a.npz
?? data/fig6/panel_b.npz
?? data/fig6/panel_c.npz
?? data/fig6/panel_d.npz
?? data/fig7/
?? data/iv_a/
?? data/phase_diagram/
?? reports/
?? scripts/compare_model_versions.py
?? scripts/cuda/
?? scripts/data/
?? scripts/fig2_style.py
?? scripts/fig4_data_cuda.py
?? scripts/fig4_style.py
?? scripts/fig5_style.py
?? scripts/fig6_style.py
?? scripts/fig7_data.py
?? scripts/fig7_style.py
?? scripts/iv_a_classify_and_aggregate.py
?? scripts/iv_a_cpu_baseline_g1_2.py
?? scripts/iv_a_diag_D1.py
?? scripts/iv_a_diag_tend.py
?? scripts/iv_a_g1_3_bench.py
?? scripts/iv_a_gpu_api_notes.md
?? scripts/iv_a_multistab_figure.py
?? scripts/iv_a_multistab_scan.py
?? scripts/iv_a_multistab_scan_cpu.py
?? scripts/iv_a_multistab_summary.py
?? scripts/iv_a_rerun_stragglers.py
?? scripts/iv_a_test_nearsnic_ICs.py
?? scripts/iv_a_test_nearsnic_tight.py
?? scripts/iv_a_validate_gpu_g1_2.py
?? scripts/make_fig2.py
?? scripts/make_fig2a.py
?? scripts/make_fig2b.py
?? scripts/make_fig2c.py
?? scripts/make_fig2d.py
?? scripts/make_fig4.py
?? scripts/make_fig4a.py
?? scripts/make_fig4b.py
?? scripts/make_fig4c.py
?? scripts/make_fig4d.py
?? scripts/make_fig5_composite.py
?? scripts/make_fig5a.py
?? scripts/make_fig5b.py
?? scripts/make_fig6_composite.py
?? scripts/make_fig6a.py
?? scripts/make_fig6b.py
?? scripts/make_fig6c.py
?? scripts/make_fig6d.py
?? scripts/make_fig7.py
?? scripts/make_fig7a.py
?? scripts/make_fig7b.py
?? scripts/make_fig7c.py
?? scripts/make_fig7d.py
?? scripts/make_slow_manifold_diagnostic_v1.py
?? scripts/oscillation_phase_diagram.py
?? scripts/plot_phase_diagram.py
?? scripts/profile_simulate.py
?? scripts/scan_ell0_biT.py
?? scripts/scan_floor_values.py
?? scripts/test_ell0.py
```

The migration manifest was expanded to include destination type, size, and
either SHA-256 checksum or symlink target for every migrated artifact. This
manifest is the audit record for migrated source files and large data files.

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

## Section title note

The user request referred to `III. LINEAR STABILITY ANALYSIS`. The current
source draft section title is `III. HOMOGENEOUS STABILITY DIAGNOSTIC`. The
migrated file `paper/sections/linear_stability.tex` preserves the source title
and is mapped to the requested linear-stability-analysis material because it is
the source draft's Section III immediately following `II. MODEL` and contains
the homogeneous/stability diagnostic text.

## Figure path convention

Migrated LaTeX fragments now use paths resolvable from the future `paper/`
manuscript context:

* Figure 1: `figures/fig01/Figure/fig1/fig1.pdf`
* Figure 9 source `fig7`: `figures/fig09/Figure/fig7/fig7.pdf`

## Large cache decision

The duplicated files `paper/figures/fig02/data/fig2/cache.npz` and
`paper/figures/fig03/data/fig2/cache.npz` had identical SHA-256 checksums:

* `98be3745de15b36fb254debed69e6c6aa4072fcc9df7ac8d5f1cf7f7bf84d825`

They were deduplicated to
`paper/figures/shared/data/fig2/cache.npz`. The original Figure 2 and Figure 3
paths are retained as relative symlinks so copied scripts can keep using their
original expected local cache path.

## Validation status

These files are imported for audit and future review only. No model, claim,
figure, or numerical result is promoted to validated status by this migration.
