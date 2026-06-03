# Legacy CPU Solver Model Audit

Status: audit material only

Validation: not validated

This document records what the migrated legacy CPU solver actually solves. It is
not a model-specification gate, not numerical evidence, and not a production
solver approval.

No model or claim was promoted to validated status.

## Audited code path

Primary source:

* `paper/solver/paper_latest_cpu/scan_optimized.py`
* `paper/solver/paper_latest_cpu/linear_stability_1d.py`

The copied figure-script solver files under `paper/figures/fig01/scripts/`,
`paper/figures/fig02/scripts/`, `paper/figures/fig03/scripts/`, and
`paper/figures/fig09/scripts/` currently have the same SHA-256 checksum as the
primary `scan_optimized.py` migrated solver source at the time of this audit.
They are retained for migration provenance and figure reproducibility, not as
independent model definitions.

## State vector

The BDF state vector in `scan_optimized.py` is:

```text
y = [logJ_0 ... logJ_{N-1}, W_0 ... W_{N-1}, theta_0 ... theta_{N-1}]
```

where:

* `logJ` is the positivity transform for the swelling ratio `J`;
* `W = J u` is the conservative reactant content per reference volume;
* `u = W / J` is reconstructed as the current-volume reactant concentration;
* `theta` is the dimensionless temperature excess.

The solver reconstructs:

```text
J = exp(clip(logJ, log(phi_p0 * 1.02), log(6.0)))
u = max(W / J, u_floor)
phi = phi_from_J(J, p)
```

This means the trajectory integration is written in `logJ` and `W`, while many
diagnostics and plotting routines consume the reconstructed `J`, `u`, and
`theta` fields.

## Flux convention

The finite-volume faces are ordered in increasing `xi`. The free surface is the
right boundary. Positive surface flux is therefore outward from the gel into the
bath.

The implemented face fluxes are:

```text
q = -M m_x
n = u q - delta D u_x
h = -alpha K theta_x
```

At the free surface:

```text
q_N = Bi_mu (m_N - m_b)
n_N = Bi_c (u_N - 1)
h_N = Bi_T theta_N
```

With this convention, bath-to-gel reactant supply has negative outward flux:
when `u_N < 1`, `n_N < 0`, and the finite-volume term `-(n_N - n_0) / dx`
increases `W`.

## RHS actually advanced

The semidiscrete RHS in `rhs_mol_logJ` is:

```text
logJ_t = -(q_{i+1/2} - q_{i-1/2}) / (dx J_i)
         - Bi_J_vol (m_local_i - m_b) / J_i

W_t = -(n_{i+1/2} - n_{i-1/2}) / dx
      - Da J_i R_i
      + B_vol (J_i - W_i)
      + Bi_c_vol (J_i - W_i)

theta_t = (-(h_{i+1/2} - h_{i-1/2}) / dx + Da J_i R_i) / C_i
          - B_Tvol theta_i
```

The default volumetric exchange parameters are zero:

```text
B_vol = 0
B_Tvol = 0
Bi_c_vol = 0
Bi_J_vol = 0
```

Those source terms are therefore optional numerical/model variants, not part of
the default surface-exchange trajectory.

## Chemical potential variants

The default `model_version` is `v0`.

In `v0`, the local chemical potential uses an effective osmotic chi closure:

```text
m_mix = log(1 - phi) + phi + chi phi^2
chi = chi_inf + S_chi theta + chi1 phi
```

The strict derivative variants subtract:

```text
phi^2 (1 - phi) chi1
```

Those variants are selected by `v1_first_principles` or
`v1_metric_corrected_optional`.

Important limitation: the name `v1_first_principles` is only a local code label.
It should not be read as a fully first-principles model until geometry,
source-scaling, reference-volume, and boundary-condition issues are separately
audited.

## Transport and accessibility closures

The default legacy `v0` closures are power-law porosity suppressions:

```text
accessibility = max(1 - phi, 1e-12)^m_act + a_floor
mobility      = M0 [max(1 - phi, 1e-12)^m_mob + mu_floor]
diffusivity   = D0 [max(1 - phi, 1e-12)^m_diff + d_floor]
```

The `v1_*` variants use normalized porosity closures with floors `A_min` and
`D_min`, and optional `power`, `mackie_meares`, or `free_volume` forms.

These functions are candidate closures. Their material justification and
parameter ranges remain unresolved model-specification blockers.

## Source scaling

The reaction source is implemented as:

```text
Da * J * R
```

This is a current-volume-style source scaling. It is a core model assumption and
may conflict with an immobilized catalyst/reference-volume interpretation. This
must be resolved before using legacy solver data as model evidence.

## Heat advection and `Pe_T`

`Pe_T` is present in the parameter dataclass and in conservation diagnostics, but
enthalpy advection is not active in the RHS advanced by `rhs_mol_logJ`.

The diagnostic `max_enthalpy_advection_to_conduction_ratio` estimates a possible
omitted-advection scale only when `Pe_T != 0`; it does not add advection to the
trajectory.

## Positivity and clipping interventions

The solver contains the following positivity/clipping interventions:

* `logJ` is clipped in the RHS and output reconstruction to
  `[log(phi_p0 * 1.02), log(6.0)]`;
* `phi_from_J` imposes a hard ceiling `phi < 0.995`;
* `u = max(W / J, u_floor)` clips low reconstructed reactant concentration;
* `reaction_rate` uses `u_eff = max(u, u_floor)`;
* the Arrhenius exponent is clipped to `[-arrh_exp_cap, arrh_exp_cap]`;
* porosity, normalized porosity, Mackie-Meares ratios, and free-volume ratios
  use `np.clip`;
* plotting/data consumers may receive clipped `J`, `u`, and `phi` outputs.

These interventions are not evidence of physical regularity. They must be
reported with any future numerical result that uses this solver.

## Boundary approximation limitations

The surface exchange laws are implemented at boundary faces using the adjacent
cell-center values. They are effectively cell-center Robin approximations, not a
separate resolved boundary layer.

The homogeneous diagnostic in `linear_stability_1d.py` is a lumped diagnostic
with local bulk dispersion corrections. It is not the full spectrum of the
finite-volume PDE with Robin boundaries.

## Parameter provenance

Default values in `Params` are solver defaults and may differ from values in any
paper table or draft text. Future generated data must persist the full `Params`
object used for the run.

The solver now exposes:

```python
params_to_dict(p)
save_params_json(p, path)
```

for full parameter serialization.

## Lightweight audit diagnostics

The solver now exposes a non-invasive diagnostic path:

```python
data = simulate(p, include_audit=True)
diagnostics = data["audit_diagnostics"]
```

or:

```python
data = simulate(p, include_raw_state=True)
diagnostics = solver_audit_diagnostics(data, p)
```

The diagnostic report includes:

* `min_raw_logJ`, `max_raw_logJ`;
* low/high `logJ` clipping counts and fractions;
* `min_W`;
* `min_raw_u = min(W / J_raw)`;
* fraction of cells/times where `u` is clipped to `u_floor`;
* `max_phi_before_clip` and counts above the `phi_from_J` hard ceiling;
* non-finite counts for `J`, `W`, `u`, `theta`, source, and flux values;
* surface flux statistics for `q`, `nflux`, and `h`;
* full serialized `Params`.

By default, `simulate(p)` keeps the legacy trajectory path and default returned
fields. Raw-state and audit diagnostics are opt-in.

## Current model blockers

Before legacy solver data can be used as evidence, the project still must:

1. decide whether the canonical model uses the `v0` effective-chi closure or a
   strict derivative closure;
2. resolve current-volume versus reference-volume reaction source scaling;
3. audit free-surface flux signs against integral conservation;
4. distinguish reaction accessibility, diffusivity, permeability, and
   poroelastic collapse as separate physical closures;
5. define front/barrier observables before numerical validation;
6. reproduce any oscillation, phase diagram, or spinodal claim with convergence
   and control cases inside this repository.
