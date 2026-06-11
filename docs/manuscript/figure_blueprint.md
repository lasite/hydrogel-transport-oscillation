# Figure Blueprint

Status: active for paper-results production

Production decision: the user authorized continued use of existing `paper/figures/` result assets as the initial manuscript figure source set. This blueprint records how those assets should be used and which missing images should be added before result-section drafting.

No model or claim is promoted to validated status by this blueprint.

## Production Figure 1: Homogeneous stability and linear diagnostics

Source bundle: `paper/figures/fig01/`

Composite output:

* `paper/figures/fig01/Figure/fig1/fig1.pdf`
* `paper/figures/fig01/Figure/fig1/fig1.png`

Script route:

* `paper/figures/fig01/scripts/make_fig1.py`
* panel scripts `make_fig1a.py` through `make_fig1f.py`

Content:

* bifurcation diagram versus `Bi_T`;
* leading eigenvalue real/imaginary parts;
* dispersion relation;
* `Da--Bi_T` stability map;
* `S_chi--Bi_T` stability map;
* period / eigenvalue diagnostic versus `Da`.

Bounded claim:

The homogeneous and linearized diagnostics identify candidate thermal-collapse feedback regimes and parameter neighborhoods for spatial PDE study. They do not by themselves establish the nonlinear spatial relaxation-oscillation mechanism.

Caption constraint:

Use diagnostic language: “homogeneous stability diagnostic,” “candidate Hopf/monotone regimes,” “linearized dispersion,” and “parameter regions explored.” Avoid saying that Fig. 1 proves the PDE oscillator.

## Production Figure 2: PDE regime maps and front-region geography

Source bundle: `paper/figures/fig02/`

Composite output:

* `paper/figures/fig02/Figure/fig2/fig2.pdf`
* `paper/figures/fig02/Figure/fig2/fig2.png`

Script route:

* `paper/figures/fig02/scripts/make_fig2.py`
* panel scripts `make_fig2a.py` through `make_fig2d.py`

Content:

* regime classification on `(Bi_T, S_chi)`;
* regime classification on `(Bi_T, Da)`;
* oscillation period map in the LCST-front regime;
* maximum polymer-fraction map with `phi = 0.5` contour.

Bounded claim:

The imported PDE maps show a candidate region where front-like LCST collapse and oscillatory behavior co-occur in the source result set.

Caption constraint:

State that the panels are reused paper-source numerical assets unless and until a repository reproduction task records full convergence/control evidence.

## Production Figure 3: Representative spatial dynamics and barrier structure

Source bundle: `paper/figures/fig03/`

Composite output:

* `paper/figures/fig03/Figure/fig3/fig3.pdf`
* `paper/figures/fig03/Figure/fig3/fig3.png`

Script route:

* `paper/figures/fig03/scripts/make_fig3.py`
* panel scripts `make_fig3a.py` through `make_fig3i.py`

Content:

* regime-resolved kymographs for `J` and `theta`;
* phase-portrait or profile-derived diagnostics;
* spatial envelopes and derived front/barrier indicators.

Bounded claim:

Representative source trajectories are consistent with the proposed picture in which a surface-localized LCST collapse/front reorganizes transport and reaction access.

Caption constraint:

Do not overclaim causality from kymographs alone. Pair this figure with a new observable-definition figure and a control comparison before using it as central mechanism evidence.

## Supplementary or Appendix Figure 9: Spinodal-style instability demonstration

Source bundle: `paper/figures/fig09/`

Composite output:

* `paper/figures/fig09/Figure/fig7/fig7.pdf`
* `paper/figures/fig09/Figure/fig7/fig7.png`

Script route:

* `paper/figures/fig09/scripts/make_fig7.py`
* panel scripts `make_fig7a.py` through `make_fig7d.py`

Content:

* spinodal-demonstration `J(x,t)` kymograph;
* selected spatial profiles;
* spectral-growth diagnostic;
* Fourier power spectrum.

Bounded claim:

The figure illustrates a distinct instability diagnostic from the source draft. It should remain supplementary unless the main text needs to discuss thermodynamic spinodal behavior separately from the relaxation-oscillation mechanism.

Caption constraint:

Do not conflate spinodal patterning with the main transport-barrier relaxation cycle.

## Required New Figure A: Mechanism schematic

Priority: high

Recommended location:

* `paper/figures/fig00/` or `paper/figures/mechanism/`

Purpose:

Show the proposed physical cycle in one reader-facing schematic: open swollen gel, reaction and heat release, LCST collapse at/near the surface, transport/accessibility barrier formation, reactant starvation, cooling, and reopening.

Required visual elements:

* bath reactant supply;
* exothermic reaction zone;
* temperature rise;
* collapsed surface skin;
* reduced diffusivity/permeability/accessibility;
* reactant depletion behind the barrier;
* recovery path after cooling.

Claim supported:

The central hypothesis is a transport-induced relaxation-oscillation loop, not a purely homogeneous chemical oscillator.

## Required New Figure B: Cycle snapshot montage

Priority: high

Recommended location:

* add as new main Fig. 4, or convert existing Fig. 3 into a paired Fig. 3/4 sequence.

Purpose:

Show 4--6 snapshots over one representative cycle using existing trajectory data: ignition/heating, skin collapse, barrier/reaction starvation, cooling, reopening/recharge.

Required panels:

* `J(x)` or `phi(x)` profiles;
* `theta(x)` profiles;
* `u(x)` profiles;
* accessibility `A(phi)` or reaction rate `R(x)`;
* front position marker if accepted.

Claim supported:

The time ordering of collapse, transport barrier, reactant depletion, and reopening is consistent with a relaxation cycle.

## Required New Figure C: Front and barrier observable definitions

Priority: high

Recommended location:

* supplementary methods figure, or main-text inset if space allows.

Purpose:

Define observables before they are used in captions or result text.

Required definitions:

* collapsed-skin threshold;
* front position;
* collapsed-skin thickness;
* barrier strength, for example `1 - min A` or an integrated suppression measure;
* reactant penetration depth;
* phase lag between heat source, temperature, collapse, and reactant depletion.

Claim supported:

The manuscript measures a transport barrier rather than relying only on qualitative kymographs.

## Required New Figure D: Control comparison

Priority: high

Recommended location:

* supplementary figure, with one main-text panel if space allows.

Purpose:

Demonstrate that the observed source-result behavior depends on the coupled mechanism.

Minimum controls:

* baseline/source result;
* no reaction (`Da = 0`);
* no LCST coupling (`S_chi = 0`);
* no barrier / constant transport-accessibility branch;
* optional strict-chi and current-volume-source sensitivities.

Claim supported:

The oscillation is tied to reaction--heat--collapse--transport coupling, not only to generic thermal feedback or plotting/classification choices.

## Required New Figure E: Provenance and numerical-status support

Priority: medium

Recommended location:

* supplementary information.

Purpose:

Make reuse of `paper/figures/` defensible and auditable.

Required content:

* table or diagram mapping each final figure to source figure path, script path, data path, and cache/provenance hash when available;
* reduced smoke route summary;
* clipping/floor diagnostic status when available;
* explicit statement that repository smoke checks are wiring checks unless later reproduction evidence is added.

Claim supported:

The manuscript figure package is source-mapped and status-labeled.

## Optional New Figure F: Model architecture graphic

Priority: medium

Purpose:

Show the state variables and couplings in a compact model diagram: `J`, `W=Ju`, `theta`, chemical potential `m`, solvent flux `q`, reactant flux `n`, heat flux `h`, accessibility `A(phi)`, diffusivity `D(phi)`, mobility `M(phi)`, and boundary exchange terms.

Use this if the model section becomes too dense or if reviewers need a visual map of equations and closures.

## Immediate figure-production order

1. Create the source-mapping/provenance table for existing Fig. 1/2/3/9.
2. Add the mechanism schematic.
3. Add the front/barrier observable-definition graphic.
4. Add the cycle snapshot montage.
5. Add control comparison and provenance supplement.
6. Draft final captions only after steps 1--5 establish figure boundaries.
