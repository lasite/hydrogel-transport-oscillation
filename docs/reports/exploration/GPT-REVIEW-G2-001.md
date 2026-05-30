# GPT Review G2-001: Model A Specification Review

Status: G2 review by ChatGPT; no code generation or execution.

Date: 2026-05-30

## Scope

This review examines the existing candidate Model A and derivation for equation structure, conservation form, dimensional consistency, boundary conditions, internal consistency, and physical plausibility.

This is not a validation report. No model, equation, instability, numerical result, or manuscript claim is promoted to `docs/validated/`.

## Sources reviewed

* `docs/project_state.md`
* `docs/model_candidates/model_A_initial_lcst_transport_barrier.md`
* `docs/derivations/initial_model_derivation.tex`
* `docs/05_novelty_framing.md`
* `docs/06_prior_art_risk_matrix.md`
* `docs/07_g1_frozen_corpus.md`

## Executive judgment

The candidate model has the right high-level structure for the proposed mechanism:

* a swelling equation driven by solvent chemical-potential gradients;
* a conservative reactant balance for `J u` with solvent advection, diffusion, and reaction consumption;
* a heat equation with conduction and an exothermic Arrhenius source;
* collapse-dependent reaction-accessibility and transport-degradation factors.

However, the model is not yet specification-complete. It should not enter numerical implementation or validated-claim status until several G2 blockers are resolved.

The highest-priority blockers are:

1. Free-surface reactant boundary conditions are inconsistent between full flux form and compact form.
2. Gradient-energy regularization requires explicit continuous boundary conditions, not only ghost-cell implementation notes.
3. The solvent chemical potential may be incomplete when `chi` depends on polymer fraction.
4. The heat equation uses `C(J) theta_t` rather than a conservative enthalpy balance; this needs justification.
5. The homogeneous ODE / well-mixed dynamical system is not fully derived.
6. The model lacks formal front/barrier observables needed to test the novelty mechanism.

## Equation-structure review

### 1. Kinematics and domain

The kinematic definition is coherent: `J = dx/dX` and `phi = phi_p0 / J`. This makes polymer volume fraction decrease under swelling and increase under collapse.

The model currently states `J > 0`, but the transport and accessibility factors require the stronger domain condition:

```text
J >= phi_p0, equivalently 0 < phi <= 1.
```

If `J < phi_p0`, then `1 - phi` becomes negative, and terms such as `(1 - phi)^m_act`, `(1 - phi)^m_diff`, and `(1 - phi)^m_mob` can become undefined or change sign when exponents are non-integer or odd. This is a model-domain condition, not a numerical detail.

Required G2 action: state the admissible domain explicitly and identify whether the PDE, boundary conditions, or material functions enforce it.

### 2. Swelling / solvent equation

The swelling equation is written in conservative form:

```text
J_t = partial_x [ M(J,theta) partial_x m ]
q = - M partial_x m
J_t + q_x = 0
```

This is internally consistent. In a closed no-flux domain, total swelling volume `int J dx` would be conserved. With a Robin surface flux, total `J` changes only through the surface exchange term, which is physically reasonable for a gel exchanging solvent with a bath.

Open issue: because the chemical potential includes a gradient-energy term, `m = f(J,theta) - ell^2 J_xx`, the continuous problem needs an additional natural boundary condition for `J`, commonly a condition such as `J_x = 0` at boundaries. The numerical-method notes impose this through ghost cells, but the continuous boundary-condition section does not state it as part of the model specification.

Required G2 action: add explicit continuous boundary conditions for the gradient term and clarify their physical interpretation.

### 3. Reactant equation and conservation

The dimensional reactant balance is conservative:

```text
partial_t(J c) + partial_X N_c = - J R
N_c = c Q_s - D_c c_X
```

The nondimensional version is also conservative if the full flux is used:

```text
partial_t(J u) + partial_x (u q - delta D u_x) = - Da J Rhat.
```

This structure is correct for reactant inventory per reference volume. The reaction consumption term and advective solvent flux are physically meaningful.

Major inconsistency: the free-surface reactant boundary condition appears in two forms.

Full flux form:

```text
u q - delta D u_x = Bi_c (u - 1)
```

Compact form:

```text
D u_x = Bi_c (1 - u)
```

The compact form omits both the advective term `u q` and the prefactor `delta`. It is only equivalent under extra assumptions such as `q = 0` and a redefinition of `D` or `Bi_c`. Those assumptions are not stated and are generally incompatible with swelling-driven solvent exchange.

This issue directly affects reactant supply, global reactant balance, and the proposed transport-barrier mechanism.

Required G2 action: choose one boundary convention, preferably the full total-flux condition, and propagate it consistently through the compact model, homogeneous limit, and linearization.

### 4. Heat equation

The heat equation has the intended exothermic source:

```text
C(J) theta_t = partial_x [ K(J) theta_x ] + Da J Rhat
```

The sign of heat generation is consistent with reactant consumption if `Delta T_* = (-Delta H_r) c_b / C_*` and the reaction is exothermic.

Two specification issues remain.

First, the compact system absorbs `alpha` into `K`, while the explicit nondimensional system writes `alpha K theta_x`. This is acceptable only if the compact notation clearly states that `K` has been rescaled. The boundary conditions should use the same convention.

Second, the heat storage term is `C_eff(J) T_t`, not `partial_t[C_eff(J) T]` or a full enthalpy balance. Because `J` changes in time and solvent exchange is central to the proposed mechanism, this approximation requires physical justification. The model also neglects enthalpy advection under `Pe_T << 1`, but the expected range and consequences of `Pe_T` are not yet justified.

Required G2 action: document whether heat capacity is treated as a quasi-static local coefficient, whether missing `C_J J_t` terms are negligible, and when enthalpy advection may be ignored.

## Free energy and chemical potential review

The free energy consists of elastic, mixing, and gradient terms. The elastic contribution and its derivative are structurally plausible:

```text
Psi_el = G/2 (J^2 - 1 - 2 ln J)
mu_el proportional to J - J^{-1}
```

The mixing chemical potential requires further audit because `chi` is allowed to depend on polymer volume fraction:

```text
chi(theta,phi) = chi_infty + S_chi theta + chi_1 phi.
```

The current chemical-potential expression uses:

```text
mu_mix / (RT/v_s) = ln(1 - phi) + phi + chi(theta,phi) phi^2.
```

For concentration-dependent `chi`, a variational derivative generally produces extra terms involving derivatives of `chi` with respect to composition. It is not yet clear whether the current expression assumes `chi` is held fixed during differentiation, whether the `chi_1 phi` form has been folded into an effective expression, or whether terms are missing.

This is a high-priority specification issue because `f_J` controls spinodal behavior, the swelling equation, and the linear-stability matrix.

Required G2 action: rederive `mu_mix` explicitly for `chi(theta,phi) = chi_infty + S_chi theta + chi_1 phi`, or mark the current expression as a phenomenological chemical potential rather than a strict derivative of the stated free energy.

## Boundary-condition review

### Symmetry plane

The symmetry-plane conditions are physically reasonable:

```text
q = 0
reactant total flux = 0
theta_x = 0
```

These enforce no solvent, reactant, or heat flux across the midplane.

### Free surface

Solvent exchange sign is plausible:

```text
q = Bi_mu (m - m_b)
```

If the internal chemical potential exceeds the bath value, positive outward solvent flux reduces local `J`, consistent with `J_t + q_x = 0`.

Reactant exchange is the main boundary-condition blocker. The full flux sign is plausible:

```text
n = u q - delta D u_x = Bi_c (u - 1)
```

If `u < 1`, then `n < 0`, meaning inward reactant supply from the bath. This is consistent with the global balance. The compact condition must be reconciled with this.

Heat exchange is plausible but notation-dependent:

```text
-alpha K theta_x = Bi_T theta
```

For `theta > 0`, this gives outward heat loss. The compact form should preserve the same sign and scaling.

Gradient-energy boundary conditions remain incomplete in the continuous statement.

## Conservation-law review

### Solvent / swelling inventory

With `J_t + q_x = 0`, the integral balance is:

```text
d/dt int_0^1 J dx = - q(1) + q(0).
```

Since `q(0)=0`, solvent content changes only through the surface. This is physically appropriate.

### Reactant inventory

Using the full flux `n = u q - delta D u_x`, the integral balance is:

```text
d/dt int_0^1 J u dx = - n(1) - int_0^1 Da J Rhat dx.
```

This is physically appropriate: bath supply and reaction consumption are the only global terms. If the compact diffusive-only boundary condition is used instead, this balance changes and may become inconsistent with solvent advection.

### Heat inventory

With no enthalpy advection and with the compact heat equation, the integral balance is approximately:

```text
d/dt int C(J) theta dx = - heat_loss + int Da J Rhat dx
```

But because the PDE is `C(J) theta_t`, this is not exactly the time derivative of `int C(J) theta dx` when `J_t != 0`. This is acceptable only as an approximation with stated assumptions.

## Dimensional and nondimensional consistency

Most nondimensional groups are plausible:

* `Da` compares reaction to swelling/permeation time.
* `delta = D0 / (M0 mu_*)` compares solute diffusion to swelling/permeation transport.
* `alpha = tau_s / tau_T` compares swelling/permeation time to thermal diffusion time.
* `Bi_mu`, `Bi_c`, and `Bi_T` represent surface exchange strengths.

Remaining issues:

1. The parameter table lists `D_0` as a core parameter, while the summary lists `delta`. The final specification should decide whether `D_0` appears only through `delta` or remains independently meaningful.
2. Compact notation absorbs `delta` and `alpha` into material functions, but boundary conditions and parameter tables still use explicit `delta` and `alpha` elsewhere.
3. The reaction order `n` is general in the appendix but fixed to `n=1` in the compact model. G2 should choose a final version.
4. The approximation `T/T_infty approx 1` in the chemical potential should be tied to `epsilon_T << 1` and checked against the parameter range.

## Linear-stability and homogeneous-limit review

The recorded homogeneous steady balances are coherent:

```text
m(J0,theta0) = m_b
Bi_c(1-u0) = Da J0 Rhat0
Bi_T theta0 = Da J0 Rhat0
```

These follow from the full flux sign convention when the domain is treated as a lumped slab.

The `A0` matrix entries appear structurally consistent with the stated lumped balances. The coupling signs make physical sense: Arrhenius heating gives positive thermal feedback, while swelling/collapse can reduce reactant availability and heat source.

The `D2` and `D4` matrices are plausible in the uniform-gradient-free limit. In the reactant equation, the advective coupling from `u q` cancels the `u0 J_t` contribution when the conserved variable is `J u`, which explains why the `u` diffusion row is diagonal at `k^2` order.

However, the full homogeneous ODE system is still not derived. The document states this explicitly. This is a blocker for G2 exit because the novelty claim depends on showing that the reaction subsystem or homogeneous reduction is not already an oscillator.

Required G2 action: derive the homogeneous ODE as a dynamical system, including surface exchange terms and the same boundary sign convention used in the PDE.

## Physical-reasonableness review

The proposed mechanism is physically plausible but not yet established.

Plausible pieces:

* Arrhenius heat generation can amplify temperature.
* LCST-like increase of `chi` with temperature can drive collapse.
* Collapse-dependent factors can reduce reaction accessibility and diffusion.
* Surface exchange can provide delayed recovery and reactant re-ingestion.

Unresolved or speculative pieces:

* The chemical subsystem has not been proven non-oscillatory by itself.
* The collapsed transport barrier has not been defined as an observable.
* The model does not yet show that transport degradation is necessary rather than incidental.
* The surface slow manifold is not yet derived or operationally defined.
* SNIC scaling, hysteresis, penetration depth, and basin-size claims remain unverified source-appendix claims.

## Priority blocker list

### P0 blockers before G2 exit

1. Reconcile free-surface reactant boundary conditions.
2. Add continuous boundary conditions for the gradient-energy term.
3. Reaudit `mu_mix` for composition-dependent `chi`.
4. Derive or explicitly bound the homogeneous ODE / well-mixed limit.
5. Define admissible domain: `J >= phi_p0`, `0 < phi <= 1`, and `1 + epsilon_T theta > 0`.
6. Define front/barrier observables.

### P1 blockers before numerical implementation

1. Specify final material functions `M(J,theta)`, `D(J,theta)`, `K(J)`, and `C(J)`.
2. Decide whether reaction order is fixed at `n=1`.
3. Justify `Pe_T << 1` and neglected enthalpy advection.
4. Justify heat storage approximation when `J_t != 0`.
5. Clarify whether `m_b=0` is a convention or a physical bath condition.

### P2 blockers before manuscript claims

1. Reproduce or remove source-appendix numerical claims.
2. Compare full PDE mechanism to homogeneous stability results.
3. Confirm critical slowing and hysteresis signatures using repository-controlled scripts.
4. Complete DOI/BibTeX cleanup from G1 before drafting final introduction claims.

## Recommended next task

Create a focused G2 follow-up task:

`G2-001: Resolve model-specification blockers`

Minimum deliverables:

1. A boundary-condition convention document.
2. A corrected or justified chemical-potential derivation.
3. A homogeneous ODE derivation.
4. A material-function table.
5. A front/barrier observable definition.

No production solver should be written before these items are resolved.

## Final status

G2 review has begun. The model has a plausible mechanism-level structure, but it does not yet pass G2. The current status remains candidate-only, unvalidated, and unsuitable for numerical production or manuscript-level claims.
