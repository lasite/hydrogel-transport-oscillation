# Section 2 v0.1 — Chemo-mechanical BZ-gel problem

Status: draft manuscript section, saved directly on `main` for iterative revision.

Source basis: current `glsm/` implementation and repository physics notes. The file uploaded as `yashin2007(1).pdf` appears, on inspection, to contain the CardiacEP-PINOS paper rather than the Yashin--Balazs 2007 BZ-gel paper; therefore this draft uses the solver's explicit Yashin--Balazs equation annotations as the model anchor and marks the paper-level equation citations for later verification against the correct PDF.

Citation-key status: provisional. Replace citation keys with the final Zotero / Better BibTeX keys after the literature map is finalized.

---

## 2. Chemo-mechanical BZ-gel problem

### 2.1. BZ gels as active chemo-mechanical media

Self-oscillating Belousov--Zhabotinsky (BZ) gels are active polymer systems in which reaction chemistry, solvent uptake, and network deformation are coupled. In the Yashin--Balazs modeling framework, the BZ reaction is represented by a two-variable Oregonator-type chemical subsystem embedded in a deformable polymer gel. The chemical state controls the local polymer--solvent affinity, while the gel deformation changes local polymer volume fraction and transport geometry. The prediction problem considered here is therefore not a scalar reaction--diffusion problem. It is a field-level chemo-mechanical problem in which chemical variables, displacement fields, and polymer volume fraction must remain mutually consistent over time.

The present study uses this model family as a simulation benchmark for physics-informed operator learning. The goal is not to infer a new constitutive law for BZ gels. The goal is to learn a surrogate for the already specified chemo-mechanical simulator and then test whether physics-informed operator training improves long-horizon prediction of the coupled fields.

### 2.2. State variables and nondimensional units

The simulated BZ-gel state is defined over a two-dimensional lattice of cell elements and nodes. Element-centered fields describe the chemical and volume-fraction state, while node-centered coordinates describe gel deformation. For machine-learning evaluation, the saved tensor state is written as five element-centered channels,

\[
X_t(x,y) = \left(u_t(x,y),\; v_t(x,y),\; \delta_{x,t}(x,y),\; \delta_{y,t}(x,y),\; \phi_t(x,y)\right),
\]

where \(u\) is the activator-like Oregonator variable, \(v\) is the oxidized-catalyst / recovery-like chemical variable, \(\delta_x\) and \(\delta_y\) are in-plane displacement components, and \(\phi\) is polymer volume fraction. The simulator stores the chemical variables on elements and reconstructs deformation from node positions. The learning problem uses the five-channel field representation because the operator model must predict both the chemical wave and the associated gel deformation.

The implementation follows the nondimensional convention used by the Yashin--Balazs model family: time is measured in units of \(T_0 = (k_3 H A)^{-1}\), length in units of \(L_0 = \sqrt{D_u T_0}\), and chemical concentrations are stored in Tyson--Fife mole-fraction form. The default solver parameter file records this scaling and identifies \(u=X/X_0\) and \(v=Z/Z_0\). In the current project, the main benchmark uses a 101 by 101 element grid, 200-frame trajectories, and five channels \((u,v,\delta_x,\delta_y,\phi)\). The principal evaluation data are generated for planar, centrifugal, spiral, and chaotic wave regimes.

### 2.3. Polymer-modified Oregonator chemistry

The chemical subsystem is a two-variable polymer-modified Oregonator. In the implementation, the local source terms are written as

\[
F(u,v,\phi) = (1-\phi)^2 u - u^2
- (1-\phi) f v\,\frac{u - q(1-\phi)^2}{u + q(1-\phi)^2},
\]

\[
G(u,v,\phi) = (1-\phi)^2 u - (1-\phi)v.
\]

These expressions reduce to the usual Tyson--Fife Oregonator form in the dilute-polymer limit \(\phi \rightarrow 0\). In the gel, \(\phi\) appears explicitly as a dilution factor in the reaction terms. The parameter \(q\) controls Oregonator stiffness, \(\epsilon\) sets the relative time scale for the \(v\) equation, and \(f\) is the stoichiometric factor. The current dataset generators commonly use \(f=0.9\), \(\epsilon=0.2\), and \(q=9.52\times 10^{-5}\) for the organized regimes, with separate parameter choices used for the chaotic regime.

The chemical fields are coupled to mechanics through \(\phi\) and through the redox-dependent polymer--solvent interaction. The reaction terms directly depend on \(\phi\), and the mechanical free energy depends on \(v\) through the osmotic pressure term. This is the main physical distinction between the present BZ-gel problem and a standard reaction--diffusion benchmark: the wave variables do not evolve on a fixed passive domain; they are coupled to a deforming material state.

### 2.4. Gel deformation, volume fraction, and osmotic pressure

The mechanical part of the solver follows a gel lattice-spring representation. The gel is represented by a rectangular array of nodes, and each element is bounded by four nodes. Element deformation is converted to a volumetric-change factor \(J\) using the two element diagonals,

\[
J(m) = \lambda_{\perp}\, \frac{|d_1(m) \times d_2(m)|}{2\Delta^2},
\]

where \(\lambda_{\perp}\) is the prescribed out-of-plane swelling factor and \(\Delta\) is the undeformed element edge length. Polymer volume fraction is then computed as

\[
\phi(m) = \frac{\phi_0}{J(m)}.
\]

Thus local stretching lowers \(\phi\), while local compression increases \(\phi\). The saved displacement channels \(\delta_x\) and \(\delta_y\) are therefore not auxiliary outputs; they determine the local volume fraction and influence the chemical evolution through \(\phi\).

The internal pressure combines Flory--Huggins osmotic mixing and network elasticity. The implementation uses

\[
\pi_{\mathrm{osm}}(\phi,v)
= -\left[\phi + \ln(1-\phi) + \chi(\phi)\phi^2\right] + \chi^{\ast}v\phi,
\]

with

\[
\chi(\phi) = \chi_0 + \chi_1\phi.
\]

The element pressure is then

\[
P(\phi,v) = \pi_{\mathrm{osm}}(\phi,v)
+ \frac{c_0 v_0 \phi}{2\phi_0}.
\]

The \(\chi^{\ast}v\phi\) term is the direct redox-to-swelling coupling: changes in the chemical variable \(v\) alter the osmotic pressure and therefore the deformation dynamics. The pressure field acts on surrounding nodes, while a lattice-spring term penalizes distortions of neighboring nodes. Nodal velocities are obtained from the internal force multiplied by a volume-fraction-dependent mobility. In the current Case-I geometry, the left wall can be pinned while the remaining boundaries are mechanically free.

### 2.5. Transport on a deforming gel

The activator field \(u\) is transported across deformed element edges. The solver separates the edge flux into a polymer-advection contribution and a self-diffusion contribution. The flux is computed on the current deformed geometry using edge vectors and neighboring element centers. This is important because the wave is not simply diffusing on a fixed Cartesian grid. Changes in node positions alter element geometry, local volume fraction, and the inter-element transport terms.

The implementation follows the Yashin--Balazs / gel-LSM convention in which the \(u\) equation receives reaction and flux contributions, while the \(v\) equation evolves locally through the Oregonator recovery term and dilution caused by volume change. In the explicit integration path, the simulator computes the current volume fraction, pressure, nodal force, nodal velocity, and deformed geometry; evaluates fluxes; integrates the reaction terms with an RK4 step; and finally updates \(u\), \(v\), node positions, and time. This operator-style split is a numerical implementation of the coupled chemo-mechanical evolution rather than a new physical model.

### 2.6. Benchmark wave regimes

The benchmark uses four simulated regimes: planar, centrifugal, spiral, and chaotic waves. These regimes are selected because they test different aspects of surrogate prediction.

Planar waves provide an organized front-propagation case. Centrifugal waves test source-driven radial expansion and geometric spreading. Spiral waves introduce rotating phase structure and are sensitive to phase drift during rollout. Chaotic waves provide the most irregular spatiotemporal case and are used to probe whether the surrogate can handle dynamics that are less predictable from a single organized pattern.

Each regime is represented by a single 200-frame trajectory on the main 101 by 101 grid. The operator models are trained and evaluated on moving five-frame input/output windows. Point-to-point evaluation uses ground-truth input windows and tests local reconstruction. Rollout evaluation seeds the model with the final five ground-truth frames of the original trajectory and recursively predicts a 100-frame out-of-distribution extension. This distinction is important for the paper: point-to-point prediction tests local learnability, while rollout tests whether predicted chemo-mechanical states remain stable when they become the model's own future inputs.

### 2.7. Prediction target and problem statement

The problem studied in this paper can be written as learning an evolution operator over five-channel BZ-gel states. Given an input history

\[
\mathcal{X}_{t:t+4} = (X_t, X_{t+1}, X_{t+2}, X_{t+3}, X_{t+4}),
\]

the model predicts a future window

\[
\widehat{\mathcal{X}}_{t+5:t+9}
= \mathcal{G}_{\theta}(\mathcal{X}_{t:t+4}).
\]

For point-to-point evaluation, each prediction window receives ground-truth inputs. For rollout evaluation, predicted fields are recursively inserted into the next input history. The central scientific test is whether the learned operator can preserve coupled chemical and mechanical wave structure under this recursive use.

In this formulation, the model output must be judged by more than global mean-squared error. Chemical channels, deformation channels, and polymer-volume-fraction errors can behave differently. A predicted wave can remain visually plausible while becoming phase-shifted relative to the ground truth. Likewise, small chemical errors can produce large mechanical inconsistencies when \(\phi\), pressure, and node displacement are coupled. For this reason, later sections report global errors together with per-channel, phase-position, deformation, runtime, and offline residual diagnostics.

### 2.8. Scope of the physical model

The present physical model is a simulation benchmark, not an experimental calibration study. It reproduces a two-dimensional, nondimensional BZ-gel model with polymer-modified Oregonator kinetics, redox-dependent swelling, Flory--Huggins / elastic pressure, lattice-spring mechanics, and deformable-edge activator transport. It does not include experimental image noise, unknown material heterogeneity, three-dimensional gel geometry, or inverse recovery of physical parameters. Those extensions are left for future work.

The scope is therefore deliberately narrow: the paper asks whether a physics-informed neural operator can act as a stable surrogate for this specified chemo-mechanical simulator. The answer is evaluated by comparing PINO with data-only FNO and coordinate-based PINN baselines across short-window prediction, long-horizon rollout, zero-shot regime transfer, and resolution transfer.

---

## Implementation anchors for Methods and Appendix

- `glsm/params.py`: nondimensional parameter bundle, Yashin--Balazs parameter notes, and solver units.
- `glsm/reaction.py`: polymer-modified Oregonator source terms \(F(u,v,\phi)\) and \(G(u,v,\phi)\).
- `glsm/mechanics.py`: element volume fraction, osmotic pressure, element pressure, nodal force, and nodal mobility.
- `glsm/diffusion.py`: activator interdiffusion and polymer-advection flux on the deforming element lattice.
- `glsm/simulator.py`: state layout, Case-I geometry, reaction/flux/mechanics update order, and rollout-relevant state evolution.
- `Data/BZ_simulation_files/data_generator_intrinsic.py`: planar and centrifugal intrinsic-source data generation.
- `Data/BZ_simulation_files/data_generator_spiral.py`: spiral data generation.
- `Data/BZ_simulation_files/data_generator_chaotic.py`: chaotic data generation.

## Revision notes

1. Replace the Yashin equation-number comments with exact citations after the correct Yashin--Balazs 2007 PDF is rechecked.
2. Decide whether to keep formulas in the main Section 2 or move some formulas to Methods / Appendix depending on target venue.
3. Verify final parameter values against the generated `dataset_info_*.txt` files after data regeneration.
4. Keep the language clear that the physics residuals used later are diagnostics on retained trajectories unless a full residual-ablation study is added.
