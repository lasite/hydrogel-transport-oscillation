# Model A: Initial LCST Transport-Barrier Mechanism

Status: candidate
Confidence: low
Validation: not yet performed

## Ingestion status

The active Model A derivation source has been replaced from the migrated
`paper_latest` appendix model material:

* `docs/derivations/initial_model_derivation.tex`

The derivation now mechanically copies Appendix A, `Model Construction`, and
Appendix B, `Nondimensionalization`, from:

* `paper/appendix/appendix.tex`

The rendered derivation, when available, is:

* `docs/rendered/initial_model_derivation.pdf`

This summary records variables, parameters, equations, assumptions, and open
issues. It does not validate the model. Scientific review of the replaced
derivation is pending.

## Purpose

This model candidate is intended to test whether a non-oscillatory Arrhenius exothermic reaction can become a front-type relaxation oscillator when coupled to LCST poroelastic collapse and transport degradation.

## Physical system

The candidate model describes a planar thermoresponsive gel slab of reference half-thickness `H_0`. A Lagrangian coordinate `xi = X/H_0` spans the symmetry plane `xi = 0` to the free surface `xi = 1`. The free surface contacts a well-mixed bath with fixed temperature `T_infty` and reactant concentration `c_b`.

The gel contains an immobilized catalyst for an exothermic irreversible reaction.

## Primary state variables

Do not assume this list is final:

* `J(x,t)` or `J(xi,t)`: local swelling ratio.
* `u(x,t) = c/c_b`: normalized reactant concentration.
* `theta(x,t) = (T - T_infty)/Delta T_*`: dimensionless temperature excess.

Dependent variables and fields:

* `phi = phi_p0 / J`: polymer volume fraction.
* `mu` or `m`: solvent chemical potential, dimensional or nondimensional depending on context.
* `q`: solvent flux.
* `Rhat`: dimensionless reaction rate.
* `M`, `D`, `K`, `C`: mobility, reactant diffusivity, thermal conductivity, and heat capacity functions.

## Equation structure

The compact nondimensional PDE structure is:

1. Swelling equation driven by solvent chemical-potential gradients.
2. Reactant conservation for `u J`, including solvent advection, diffusion, and reaction consumption.
3. Heat equation with conduction and Arrhenius heat source.

The reaction rate has an Arrhenius factor multiplied by a collapse-dependent accessibility factor:

```text
Rhat = u (1 - phi)^m_act exp[Gamma_A theta / (1 + epsilon_T theta)]
```

The appendix also gives a general reaction-order form with `u^n`; the compact model corresponds to `n = 1`.

## Transport and accessibility degradation

The model includes collapse-dependent suppression factors:

* reaction accessibility: `(1 - phi)^m_act`;
* reactant diffusivity: `(1 - phi)^m_diff`;
* solvent mobility: `(1 - phi)^m_mob`.

These encode the proposed barrier mechanism as `J -> phi_p0`, `phi -> 1`.

## Free energy and LCST coupling

The solvent chemical potential is derived from:

* neo-Hookean elastic energy;
* Flory-Huggins mixing energy;
* gradient-energy regularization.

The interaction parameter is represented as:

```text
chi(theta, phi) = chi_infty + S_chi theta + chi_1 phi
```

This is the model's LCST-like thermo-swelling coupling.

## Boundary conditions

At the symmetry plane:

* no solvent flux;
* no reactant flux;
* no heat flux.

At the free surface:

* Robin solvent exchange through chemical potential;
* Robin reactant exchange with the bath;
* heat exchange with the environment.

Open issue: the compact boundary-condition notation and the full flux notation should be reconciled carefully, especially the sign convention for reactant flux and the use of `mu_b = 0` versus a general `m_b`.

## Homogeneous state and linear stability

The source derivation defines uniform steady states by chemical-potential balance, reactant supply-reaction balance, and heat-loss-reaction balance.

Linearization around a uniform base state gives:

```text
sigma yhat = A(k) yhat
A(k) = A_0 + k^2 D_2 + k^4 D_4
```

Candidate instability mechanisms:

* `k = 0` Hopf-type instability from thermal Arrhenius feedback coupled to collapse-reactant negative feedback.
* finite-wavenumber spinodal instability when the thermodynamic derivative `f_J < 0`.

This analysis is candidate evidence only. It does not establish the nonlinear spatial attractor.

## Assumptions recorded from the derivation

* Planar slab geometry.
* Lagrangian one-dimensional coordinate.
* Well-mixed bath with fixed `T_infty` and `c_b`.
* Immobilized catalyst.
* Exothermic irreversible reaction.
* Compact model uses first-order reactant dependence.
* Enthalpy advection is neglected when `Pe_T << 1`.
* Some nondimensionalization steps use `epsilon_T << 1`.
* Gradient regularization is included through an interface length `ell`.
* The derivation includes numerical-method notes, but this repository does not implement a PDE solver in EXP-001.

## Parameters appearing in the derivation

Core groups:

* `Da`: Damkohler number.
* `Bi_mu`: surface permeation Biot number.
* `Bi_c`: surface reactant Biot number.
* `Bi_T`: thermal exchange number.
* `S_chi`: LCST sensitivity.
* `Gamma_A`: Arrhenius sensitivity.
* `delta`: diffusion / permeation ratio.
* `alpha`: thermal / swelling time ratio.
* `ell`: interface regularization length.
* `Omega_e`: elastic / mixing energy ratio.
* `phi_p0`: reference polymer fraction.
* `chi_infty`, `chi_1`: Flory-Huggins interaction parameters.
* `epsilon_T`: nonlinear Arrhenius correction.
* `m_act`, `m_diff`, `m_mob`: exponents for accessibility, diffusivity, and mobility suppression.

## Undefined or unclear items

* Whether the final model should use only `n = 1` or keep the general reaction order `n`.
* Exact forms of `C(J)`, `K(J)`, and any temperature dependence in `M(J,theta)` or `D(J,theta)`.
* Consistent notation for `mu` versus `m`, and `xi` versus `x`.
* Consistent sign convention for free-surface reactant flux.
* Whether `mu_b = 0` is a convention or whether `m_b` should remain explicit.
* Physical justification and expected range for `Pe_T << 1`.
* Physical justification and expected range for `epsilon_T << 1`.
* Definition of LCST front position, collapsed skin thickness, and barrier strength.
* Whether the source appendix's spinodal verification has been independently reproduced.

## Required sanity checks

* dimensional consistency;
* positivity of concentration and temperature;
* boundedness of `J` and `phi`;
* well-mixed ODE limit;
* no-reaction limit;
* no-collapse or fixed-`J` limit;
* no-transport-degradation limit;
* no-accessibility-feedback limit;
* boundary-condition sign check;
* grid refinement, if simulations are later introduced;
* front/barrier observable definition.

## Current TODO

Request ChatGPT scientific review of the replaced Appendix A--B derivation,
then rebuild the Model Specification blocker list before treating any equation,
parameter set, instability, or numerical observation as validated.
