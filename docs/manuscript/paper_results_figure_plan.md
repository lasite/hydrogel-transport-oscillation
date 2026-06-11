# Paper Results Figure Plan

Status: active production plan

Stage: Paper Results Production (`G6_figures`)

Decision: the user authorized continuing with the existing `paper/figures/` result assets as the initial paper-results source set. This plan records source mapping, claim boundaries, and missing figures needed before result-section drafting.

No model or claim is promoted to validated status by this plan.

## Existing result assets to reuse

### Figure 1 source set: homogeneous stability and linear diagnostics

Primary source directory:

* `paper/figures/fig01/`

Composite outputs:

* `paper/figures/fig01/Figure/fig1/fig1.pdf`
* `paper/figures/fig01/Figure/fig1/fig1.png`

Primary scripts:

* `paper/figures/fig01/scripts/make_fig1.py`
* `paper/figures/fig01/scripts/make_fig1a.py`
* `paper/figures/fig01/scripts/make_fig1b.py`
* `paper/figures/fig01/scripts/make_fig1c.py`
* `paper/figures/fig01/scripts/make_fig1d.py`
* `paper/figures/fig01/scripts/make_fig1e.py`
* `paper/figures/fig01/scripts/make_fig1f.py`

Data/cache inputs:

* `paper/figures/fig01/data/fig1/panel_a.npz`
* `paper/figures/fig01/data/fig1/panel_b.npz`
* `paper/figures/fig01/data/fig1/panel_c.npz`
* `paper/figures/fig01/data/fig1/panel_d.npz`
* `paper/figures/fig01/data/fig1/panel_e.npz`
* `paper/figures/fig01/data/fig1/panel_f.npz`
* raw caches under `paper/figures/fig01/data/fig1/_raw_*.npz`

Manuscript role:

* Introduce the candidate homogeneous and linearized stability landscape.
* Motivate the parameter regions used for spatial PDE figures.

Claim boundary:

* Diagnostic figure only.
* It may motivate spatial simulations but must not be used alone as evidence for the nonlinear relaxation-oscillation mechanism.

Recommended caption wording:

* Use “homogeneous stability diagnostic,” “linearized dispersion,” “candidate regime,” and “working point.”
* Avoid “proves oscillation,” “establishes mechanism,” or “validated phase diagram.”

### Figure 2 source set: PDE regime maps

Primary source directory:

* `paper/figures/fig02/`

Composite outputs:

* `paper/figures/fig02/Figure/fig2/fig2.pdf`
* `paper/figures/fig02/Figure/fig2/fig2.png`

Primary scripts:

* `paper/figures/fig02/scripts/make_fig2.py`
* `paper/figures/fig02/scripts/make_fig2a.py`
* `paper/figures/fig02/scripts/make_fig2b.py`
* `paper/figures/fig02/scripts/make_fig2c.py`
* `paper/figures/fig02/scripts/make_fig2d.py`

Data/cache inputs:

* `paper/figures/fig02/data/fig2/panel_a.npz`
* `paper/figures/fig02/data/fig2/panel_b.npz`
* `paper/figures/fig02/data/fig2/panel_c.npz`
* `paper/figures/fig02/data/fig2/panel_d.npz`
* `paper/figures/fig02/data/fig4/fig4_grid_Bi_T_S_chi.npz`
* `paper/figures/fig02/data/fig4/fig4_grid_Bi_T_Da.npz`
* shared cache via `paper/figures/shared/data/fig2/cache.npz`

Manuscript role:

* Present the candidate source-result parameter region for LCST-front oscillatory behavior.
* Show how front formation and oscillation period vary across thermal and reaction parameters.

Claim boundary:

* Reused numerical source-result asset.
* It should be described as a candidate regime map unless the parameter scan is reproduced and verified in this repository.

Recommended caption wording:

* Use “source-result regime map,” “candidate LCST-front region,” and “period of classified oscillatory runs.”
* If used as a main figure, include a sentence that source mapping and reproduction status are provided in the supplementary provenance table.

### Figure 3 source set: representative spatial dynamics

Primary source directory:

* `paper/figures/fig03/`

Composite outputs:

* `paper/figures/fig03/Figure/fig3/fig3.pdf`
* `paper/figures/fig03/Figure/fig3/fig3.png`

Primary scripts:

* `paper/figures/fig03/scripts/make_fig3.py`
* `paper/figures/fig03/scripts/make_fig3a.py`
* `paper/figures/fig03/scripts/make_fig3b.py`
* `paper/figures/fig03/scripts/make_fig3c.py`
* `paper/figures/fig03/scripts/make_fig3d.py`
* `paper/figures/fig03/scripts/make_fig3e.py`
* `paper/figures/fig03/scripts/make_fig3f.py`
* `paper/figures/fig03/scripts/make_fig3g.py`
* `paper/figures/fig03/scripts/make_fig3h.py`
* `paper/figures/fig03/scripts/make_fig3i.py`

Data/cache inputs:

* `paper/figures/fig03/data/fig3/panel_a.npz`
* `paper/figures/fig03/data/fig3/panel_b.npz`
* `paper/figures/fig03/data/fig3/panel_c.npz`
* `paper/figures/fig03/data/fig3/panel_d.npz`
* `paper/figures/fig03/data/fig3/panel_e.npz`
* `paper/figures/fig03/data/fig3/panel_f.npz`
* `paper/figures/fig03/data/fig3/panel_g.npz`
* `paper/figures/fig03/data/fig3/panel_h.npz`
* `paper/figures/fig03/data/fig3/panel_i.npz`
* shared cache via `paper/figures/shared/data/fig2/cache.npz`

Manuscript role:

* Show representative spatial dynamics and derived front/barrier features.
* Provide the main visual bridge between parameter maps and mechanism interpretation.

Claim boundary:

* Kymographs and derived fields support qualitative consistency with a barrier-mediated relaxation cycle.
* They should be paired with explicit observable definitions and controls before being used as central mechanism evidence.

Recommended caption wording:

* Use “representative source trajectory,” “surface-localized collapse,” “spatially structured reaction/transport state,” and “consistent with.”
* Avoid “demonstrates causality” unless the control figure is included and referenced.

### Supplementary Figure 9 source set: spinodal demonstration

Primary source directory:

* `paper/figures/fig09/`

Composite outputs:

* `paper/figures/fig09/Figure/fig7/fig7.pdf`
* `paper/figures/fig09/Figure/fig7/fig7.png`

Primary scripts:

* `paper/figures/fig09/scripts/make_fig7.py`
* `paper/figures/fig09/scripts/make_fig7a.py`
* `paper/figures/fig09/scripts/make_fig7b.py`
* `paper/figures/fig09/scripts/make_fig7c.py`
* `paper/figures/fig09/scripts/make_fig7d.py`
* `paper/figures/fig09/scripts/spinodal_demo.py`

Data/cache inputs:

* `paper/figures/fig09/data/fig7/panel_a.npz`
* `paper/figures/fig09/data/fig7/panel_b.npz`
* `paper/figures/fig09/data/fig7/panel_c.npz`
* `paper/figures/fig09/data/fig7/panel_d.npz`
* `paper/figures/fig09/data/fig7/raw_simulation.npz`

Manuscript role:

* Supplementary diagnostic for spinodal-style instability behavior.
* Keep separate from the main relaxation-oscillation mechanism unless the text explicitly discusses thermodynamic patterning.

Claim boundary:

* Illustrative source-draft diagnostic, not primary evidence for the transport-barrier oscillation.

Recommended caption wording:

* Use “spinodal diagnostic” and “supplementary demonstration.”
* Do not conflate this with the relaxation-cycle mechanism.

## Missing images to add

### New Fig. 0 or Fig. 1: mechanism schematic

Priority: high

Purpose:

Make the central hypothesis readable before dense numerical figures.

Required visual sequence:

1. Swollen open gel in contact with reactant bath.
2. Reactant enters and reacts on immobilized catalyst.
3. Exothermic heating raises `theta`.
4. LCST collapse forms a surface skin/front.
5. Accessibility, diffusivity, and mobility are suppressed in the collapsed region.
6. Reactant starvation reduces heat release.
7. Cooling and swelling reopen the barrier.

Suggested output paths:

* `paper/figures/fig00/Figure/fig0/fig0.pdf`
* `paper/figures/fig00/Figure/fig0/fig0.png`

### New main or supplementary figure: cycle snapshot montage

Priority: high

Purpose:

Convert kymograph evidence into a time-ordered physical cycle.

Required panels:

* 4--6 representative times across one cycle.
* `J(x)` or `phi(x)` profile.
* `theta(x)` profile.
* `u(x)` profile.
* accessibility `A(phi)` or reaction rate `R(x)` profile.
* front marker and surface-skin region shading if definitions are accepted.

Suggested source:

* Existing Fig. 3 trajectory caches, or the shared Fig. 2 working-point cache.

Suggested output paths:

* `paper/figures/fig04/Figure/fig4/fig4.pdf`
* `paper/figures/fig04/Figure/fig4/fig4.png`

### New methods/definition figure: front and barrier observables

Priority: high

Purpose:

Prevent ambiguous use of “front,” “skin,” “barrier,” and “penetration depth.”

Required visual elements:

* one annotated profile of `J`, `phi`, `A(phi)`, and `u`;
* collapse threshold line;
* front position marker;
* collapsed-skin thickness bracket;
* barrier-strength annotation;
* reactant penetration-depth marker;
* phase-lag schematic across one cycle.

Suggested output paths:

* `paper/figures/figS_observables/Figure/observables.pdf`
* `paper/figures/figS_observables/Figure/observables.png`

### New supplementary figure: control comparison

Priority: high

Purpose:

Show that the behavior depends on coupled reaction, LCST collapse, and transport/accessibility degradation.

Minimum controls:

* baseline source result;
* `Da = 0` no reaction;
* `S_chi = 0` no LCST coupling;
* constant no-barrier transport/accessibility branch;
* optional strict-chi derivative sensitivity;
* optional current-volume source-scaling sensitivity.

Suggested output paths:

* `paper/figures/figS_controls/Figure/controls.pdf`
* `paper/figures/figS_controls/Figure/controls.png`

Status note:

The canonical CPU evidence helpers already contain candidate controls, but the official paper route currently uses `scan_optimized.py`. The control figure should either use existing source caches if available or explicitly run a scoped, documented control-generation task.

### New supplementary figure or table: provenance and numerical-status map

Priority: medium

Purpose:

Make figure reuse transparent.

Required content:

* final figure ID;
* source output path;
* script path;
* data/cache path;
* source manifest hash when available;
* reproduction status;
* claim boundary.

Suggested output paths:

* `paper/figures/figS_provenance/Figure/provenance.pdf`
* `paper/figures/figS_provenance/Figure/provenance.png`
* or a LaTeX/Markdown table in supplementary material.

### Optional main-text model architecture graphic

Priority: medium

Purpose:

Help readers parse the PDE model and closures.

Required visual elements:

* state vector `J`, `W=Ju`, `theta`;
* chemical potential `m`;
* fluxes `q`, `n`, `h`;
* boundary exchanges `Bi_mu`, `Bi_c`, `Bi_T`;
* material closures `A(phi)`, `D(phi)`, `M(phi)`;
* heat-source and reactant-consumption coupling.

Suggested output paths:

* `paper/figures/fig_model_architecture/Figure/model_architecture.pdf`
* `paper/figures/fig_model_architecture/Figure/model_architecture.png`

## Proposed manuscript ordering

Preferred order if page budget allows:

1. Mechanism schematic.
2. Model architecture or compact equation schematic.
3. Homogeneous/linear diagnostic map from existing Fig. 1.
4. PDE regime maps from existing Fig. 2.
5. Representative spatial dynamics from existing Fig. 3.
6. Cycle snapshot montage.
7. Control comparison.
8. Supplementary spinodal diagnostic from existing Fig. 9.
9. Supplementary provenance/numerical-status table.

Compressed order if the manuscript needs fewer main figures:

1. Mechanism schematic.
2. Existing Fig. 1 as diagnostic setup.
3. Existing Fig. 2 as source-result regime map.
4. Existing Fig. 3 plus cycle montage as main mechanism evidence.
5. Controls, observables, spinodal, and provenance in supplement.

## Immediate next task

Create the missing mechanism schematic and observable-definition figure first. These two images are the highest leverage because they make the existing numerical result figures interpretable and reduce overclaiming risk.
