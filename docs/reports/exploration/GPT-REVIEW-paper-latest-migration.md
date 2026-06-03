# GPT Review: paper_latest Migration

## Review target

Repository: `lasite/hydrogel-transport-oscillation`

Migration pull request: `#7`, merged into `main` as merge commit `539374dd5997cc475221d419ed9106647a11e036`.

Original task: GitHub issue `#6`, migration of selected `paper_latest` manuscript, figure/data/script, and CPU solver assets.

## Review conclusion

The migration is useful as a provenance import and should now be treated as imported source material for Model Specification review.

The migration does not validate the model, the linear-stability diagnostic, the PDE attractor interpretation, the figure data, the CPU solver, or any manuscript claim. The imported files are audit material only.

No model or claim was promoted to validated status.

## Scope that was successfully imported

The repository now contains separated manuscript fragments for the migrated model section and stability section under `paper/sections/`, plus a full appendix fragment under `paper/appendix/`.

The repository now contains grouped bundles for requested Figures 1, 2, 3, and the requested Figure 9. The migration report records that requested Figure 9 maps to the source draft's internal `fig7` spinodal appendix figure.

The repository now contains the source CPU model script and homogeneous/stability helper under `paper/solver/paper_latest_cpu/`.

The repository now contains a provenance note and source-to-destination manifest. This is the right structural choice for preserving the prior draft without promoting it to the active manuscript.

## Migration-hygiene blockers

These blockers concern repository integration and auditability. They are not physics-validation blockers, but they must be resolved before the imported material is clean enough to serve as a stable source reference.

1. LaTeX graphic paths are not integrated into the new repository layout.

   `paper/sections/linear_stability.tex` still uses `\includegraphics{fig1.pdf}`. The migrated figure file is stored under `paper/figures/fig01/Figure/fig1/fig1.pdf`. Similarly, `paper/appendix/appendix.tex` still uses `\includegraphics{fig7.pdf}` while the migrated Figure 9 bundle stores it under `paper/figures/fig09/Figure/fig7/fig7.pdf`. The original migration task required paths inside migrated LaTeX and plotting scripts to be relative to the new repository layout.

2. Figure smoke tests did not pass.

   The Codex report records that the four composite plotting scripts for Figures 1, 2, 3, and 9 all failed with exit code 1 because the current environment lacks `pypdf`. The PR therefore preserves plotting scripts but does not yet demonstrate that composite figure generation works in this repository.

3. Source provenance is not reconstructable enough.

   The provenance note records source HEAD `2afd850` but also records that the source `paper_latest` working tree was dirty at migration time. The exact dirty-state content is therefore not recoverable from HEAD alone. The report should record the concrete `git status --short` output and either a source diff/stat for migrated files or checksums of migrated sources and data.

4. Two large duplicate cache files need a repository-size decision.

   The report records both `paper/figures/fig02/data/fig2/cache.npz` and `paper/figures/fig03/data/fig2/cache.npz` at 96,403,852 bytes each. They are close to GitHub's 100 MB hard limit and appear to duplicate a shared cache. They should be deduplicated, moved to a shared data location, moved to Git LFS, or explicitly justified with checksums and a repository-size decision.

5. The migration report metadata is incomplete.

   `docs/reports/exploration/CODEX-REPORT-paper-latest-migration.md` still says `Final commit: Pending at report creation.` It should be updated to the actual final commit information.

6. Section-title mismatch needs explicit resolution.

   The original task requested `III. LINEAR STABILITY ANALYSIS`. The merged branch migrates a source section titled `III. HOMOGENEOUS STABILITY DIAGNOSTIC` and states that it corresponds to the requested linear-stability material. This may be correct if the local draft was renamed, but the report should explicitly document whether the source title differs from the PDF/uploaded draft title and why the mapped section is the intended one.

## Scientific review issues to carry into Model Specification

These are not migration-hygiene issues. They should become part of the next Model Specification review after the import is cleaned.

1. Reconcile variables and notation.

   The migrated model section uses conservative variables `J`, `W=Ju`, `theta`, and algebraic potential `m`; the existing Model A candidate summary uses `J`, `u`, `theta`, and `mu`. A single notation and state-vector convention is required before any model specification can be accepted.

2. Audit free-surface flux signs.

   The migrated model section uses total reactant flux `n = u q - delta D_ref u_xi` and surface condition `n|_1 = Bi_c (u-1)`. The earlier candidate summary already flags the free-surface reactant-flux sign convention as unresolved. This must be checked by integrating the reactant conservation law over the slab and verifying bath-to-gel flux signs.

3. Audit material closures.

   The migrated model includes `A_min`, `D_min`, clipped porosity/accessibility factors, and a distinction between reference-coordinate and current-coordinate material coefficients. These closures need a material-function audit before they become the active model.

4. Keep imported numerical notes unvalidated.

   The migrated appendix includes numerical-method and spinodal-verification material. Those notes remain imported evidence only; they are not reproduced results in this repository.

## Reset project status

Stage: Model Specification.

Substage: post-`paper_latest` source-material import and triage.

Model status: candidate only. A prior-draft model section, stability diagnostic section, and appendix now exist in the repository, but they have not been reconciled with Model A or accepted as the current model.

Numerics status: production PDE implementation remains blocked. The migrated CPU script is preserved as source material only, not as repository production code.

Figure status: migrated generated figures and plotting scripts are exploratory source assets only. Composite figure generation is not yet verified because the figure smoke tests failed at PDF assembly.

Manuscript status: no current manuscript draft is active. The migrated sections are fragments for audit and future reuse only.

## Work plan

1. Resolve `paper_latest` migration hygiene.

   Fix relative paths, figure smoke-test dependency handling, provenance of the dirty source tree, large cache duplication, report metadata, and section-title mapping.

2. Reconcile the migrated draft model with Model A.

   Produce one auditable candidate model specification that resolves variables, conservation variables, flux signs, boundary conditions, material functions, nondimensional groups, and limiting cases.

3. Rebuild the Model Specification blocker list.

   Include conservation checks, free-surface flux signs, `mu`/`m` convention, `m_b` convention, `chi(theta,phi)` derivative consistency, material coefficient coordinate convention, accessibility/diffusivity/mobility floors, `Pe_T` neglect, well-mixed limit, no-reaction limit, no-collapse limit, no-transport-degradation limit, front/barrier observables, and the status of homogeneous stability as a diagnostic rather than sufficient evidence.

4. Only after the above tasks pass, design the minimal numerical-verification stage.

   Parameter scans, figure evidence, and manuscript drafting remain blocked until the Model Specification gate passes and a minimal verification plan is accepted.
