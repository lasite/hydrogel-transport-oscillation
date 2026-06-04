# CODEX Report: Formal Convergence and Control Evidence

## Concrete task name

Generate Formal Convergence and Control-Case Evidence from the Final Paper
Solver

## Task ID or slug

issue-16-formal-convergence-control-evidence

## Human-readable stage

Minimal Numerical Verification -> Figure Evidence Preparation

## Internal stage anchor

`G2`

## Final solver commit/path

Solver path:

* `paper/solver/canonical_cpu/`

Evidence driver:

* `paper/solver/canonical_cpu/evidence.py`
* `paper/solver/canonical_cpu/run_evidence_checks.py`

Output directory:

* `results/evidence_convergence_control/`

## Canonical branch settings

```text
source_scaling = reference_volume
chi_closure = effective_osmotic_chi
transport_closure = normalized_porosity_power
floor_scheme = canonical_consistent
boundary_scheme = cell_center_robin
enthalpy_advection = false
```

## Baseline and search logic

The current final canonical default was run first as `baseline_default`.

Because it did not produce an acceptable oscillatory attractor and reported
clipping/floor interventions, a bounded local search was run over:

```text
Da = 0.5, 1.0, 2.0, 4.0, 8.0
Bi_T = 0.1, 0.2, 0.5
```

The search used the final canonical source and chi choices. Legacy branches were
used only as sensitivity controls.

## Observable definitions

The evidence driver computes:

* mean `J`, `theta`, `u`, and `W` inventory;
* tail oscillation period, amplitude, cycle count, and cycle CV;
* phase lags by cross-correlation on the final 40 percent of the run;
* collapsed cells using `J <= 0.9 * J_init`;
* collapsed skin thickness as the contiguous collapsed region measured inward
  from the free surface;
* front position as the inner edge of that surface collapsed region;
* reactant penetration depth as the contiguous surface region where `u >= 0.5`;
* barrier metrics from `A`, `D`, and `M`;
* heat-source localization as `max(abs(Da*S_R)) / mean(abs(Da*S_R))`;
* inventory residuals, clipping/floor counts, nonfinite counts, and surface
  flux summaries.

## Main result

Readiness label: not evidence ready

Evidence passed: false

Reason:

No clipping-free oscillatory attractor with at least five complete
post-transient cycles was found in the bounded `Da x Bi_T` search.

The selected reference case is:

```text
case_id = search_N31_Da1_BiT0p2
selection_reason = nonoscillatory_clipping_free_largest_theta_amplitude
theta_complete_cycles = 0
clipping_total = 0
```

## Convergence table

| Case | N | Oscillatory | theta amplitude | theta cycles | clipping total | W residual | heat residual |
| ---- | - | ----------- | --------------- | ------------ | -------------- | ---------- | ------------- |
| convergence_N51 | 51 | false | 0.004415 | 0 | 0 | 0.001314 | 1.05e-05 |
| convergence_N101 | 101 | false | 0.003742 | 0 | 0 | 0.001393 | 1.04e-05 |
| convergence_N201 | 201 | false | 0.003435 | 0 | 0 | 0.001434 | 1.04e-05 |

These runs are useful negative diagnostics, but they do not establish period or
cycle convergence because the reference is non-oscillatory.

## Time and tolerance checks

| Case | Oscillatory | theta amplitude | theta cycles | clipping total |
| ---- | ----------- | --------------- | ------------ | -------------- |
| time_half_max_step | false | 0.004415 | 0 | 0 |
| time_tighter_tolerance | false | 0.004415 | 0 | 0 |

The time/tolerance checks are stable for the non-oscillatory reference only.

## Control cases

| Case | Expected role | Result |
| ---- | ------------- | ------ |
| control_no_reaction | no self-heating oscillation | non-oscillatory, clipping-free |
| control_no_lcst | remove temperature-dependent LCST feedback | non-oscillatory, clipping-free |
| control_no_barrier | remove `A`, `D`, and `M` suppression | non-oscillatory, clipping-free |
| sensitivity_current_volume_source | legacy source scaling sensitivity | non-oscillatory, clipping-free |
| sensitivity_strict_chi | strict chi sensitivity | non-oscillatory, clipping-free |
| initial_condition_flat | initial-condition robustness | non-oscillatory, clipping-free |
| initial_condition_stronger | initial-condition robustness | non-oscillatory, clipping-free |

Skipped controls:

* no-accessibility-barrier-only;
* no-diffusivity/mobility-barrier-only.

These are skipped because the final solver does not yet expose branches that
disable only `A(phi)` or only `D/M` suppression.

## What Can Be Claimed

The repository can claim:

* the final canonical solver was exercised through a bounded evidence suite;
* no acceptable oscillatory working point was found in that bounded suite;
* several high-amplitude search cases involved clipping/floor interventions and
  cannot serve as evidence;
* a clipping-free non-oscillatory reference was tested across grid and
  time/tolerance changes;
* the current evidence package is auditable and negative.

The repository cannot claim:

* a self-sustained relaxation oscillation exists in the final canonical model;
* a transport/accessibility barrier drives an oscillatory attractor;
* front/barrier observables are converged for an oscillatory state;
* figure regeneration is justified;
* any model or claim is validated.

## Commands run

| Command | Exit code |
| ------- | --------- |
| `. .venv/bin/activate && python -m pytest tests/test_evidence_observables.py -q` | 0 |
| `. .venv/bin/activate && python -m pytest tests/test_canonical_solver.py -q` | 0 |
| `. .venv/bin/activate && python -m paper.solver.canonical_cpu.run_evidence_checks --outdir results/evidence_convergence_control --overwrite` | 0 |
| `. .venv/bin/activate && python` strict JSON / hash / metadata check for `results/evidence_convergence_control/**` | 0 |
| `. .venv/bin/activate && python -m py_compile $(find paper/solver scripts tests -name '*.py' -print \| sort)` | 0 |
| `. .venv/bin/activate && make quickcheck` | 0, 37 passed |
| `git diff --check` | 0 |

`make derivations` was not run because this task did not modify `.tex`
derivation files.

## Evidence Status

not evidence ready

## Next recommended task

Stop for human/ChatGPT decision. The next task should choose one of:

1. revise the model or numerical scheme;
2. expose separate accessibility-only and diffusivity/mobility-only controls;
3. define a new bounded, physically justified local search region.

Do not regenerate manuscript figures from this evidence package.

No model or claim was promoted to validated status.
