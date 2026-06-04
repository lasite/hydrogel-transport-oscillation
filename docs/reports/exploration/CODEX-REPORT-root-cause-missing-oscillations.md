# CODEX Report: Root Cause of Missing Oscillations

## Concrete task name

Diagnose the Physical Root Cause of Missing Oscillations in the Final Canonical
Model

## Task ID or slug

issue-18-root-cause-missing-oscillations

## Stage

Model diagnosis after failed convergence/control evidence attempt

## Conclusion label

root cause partially identified

## Scope

This task analyzed why the final canonical model from issue #15 and the formal
evidence attempt from issue #16 do not produce a clipping-free relaxation
oscillation.

The diagnostic work used:

* existing issue #16 run bundles under `results/evidence_convergence_control/`;
* the final canonical solver under `paper/solver/canonical_cpu/`;
* new diagnostic-only branches and bounded local perturbation cases;
* new diagnostic outputs under `results/root_cause_missing_oscillations/`.

No production parameter scan was run. No paper figure cache was regenerated.

## Canonical defaults unchanged

The final canonical defaults remain:

```text
source_scaling = reference_volume
chi_closure = effective_osmotic_chi
transport_closure = normalized_porosity_power
floor_scheme = canonical_consistent
boundary_scheme = cell_center_robin
enthalpy_advection = false
```

The new branches are diagnostic-only:

* `accessibility_constant`: set `A(phi)=1` while retaining `D/M` suppression;
* `transport_constant`: set `D/M` constant while retaining `A(phi)`;
* `diffusivity_constant`: set only `D` constant;
* `mobility_constant`: set only `M` constant;
* `diagnostic_J_beta`: use `S_R = J^beta R` for `beta = 0, 0.5, 1`.

## Outputs

Main summary:

* `results/root_cause_missing_oscillations/suite_summary.json`
* `results/root_cause_missing_oscillations/diagnostic_summary.csv`

Representative per-case diagnostics:

* `results/root_cause_missing_oscillations/existing_runs/search_N31_Da1_BiT0p2/mechanism_diagnostics.json`
* `results/root_cause_missing_oscillations/existing_runs/search_N31_Da4_BiT0p2/mechanism_diagnostics.json`
* `results/root_cause_missing_oscillations/new_runs/diagnostic_accessibility_constant/run_summary.json`
* `results/root_cause_missing_oscillations/new_runs/diagnostic_transport_constant/run_summary.json`

Functional-barrier relationship output:

* `results/root_cause_missing_oscillations/barrier_relationship_samples.csv`
* `results/root_cause_missing_oscillations/barrier_relationship.png`

## Ranked root causes

### 1. Functional barrier is weak or too late at the clipping-free reference

The selected clipping-free reference from issue #16 remains the most important
diagnostic case:

```text
case_id = search_N31_Da1_BiT0p2
classification = steady_hot_nonuniform
theta_complete_cycles = 0
clipping_total = 0
```

At this reference, the geometric collapse metric reports a full surface/domain
skin, but the functional barrier metric reports no functional skin:

| Metric | Value |
| ------ | ----- |
| max geometric skin thickness | 1.0 |
| max functional skin thickness | 0.0 |
| min A | 0.7267 |
| min D/D0 | 0.8990 |
| min M/M0 | 0.9482 |
| source tail / global peak | 0.9934 |

Interpretation: the current `A,D,M` closures do not shut down reaction or
transport before the trajectory settles. The previous geometric collapsed-skin
observable overstates functional barrier formation for the clipping-free
reference.

### 2. The late-time state is a steady flux balance, not a reset loop

At the same clipping-free reference:

| Budget ratio | Value |
| ------------ | ----- |
| source / heat loss, tail mean | 0.9998 |
| reactant supply / source, tail mean | 1.0000 |

Interpretation: heat generation balances heat loss and surface supply balances
reaction consumption. The model lacks a delayed negative feedback and recovery
reset strong enough to form a relaxation loop in this local regime.

### 3. The legacy `J R` source factor is not decisive by itself

The diagnostic source-scaling family did not produce a clipping-free oscillator:

| Case | beta or branch | Oscillatory | Clipping | theta amplitude |
| ---- | -------------- | ----------- | -------- | --------------- |
| diagnostic_source_beta_0 | beta = 0 | false | 0 | 0.00543 |
| diagnostic_source_beta_0p5 | beta = 0.5 | false | 0 | 0.00625 |
| diagnostic_source_beta_1 | beta = 1 | false | 0 | 0.00655 |
| sensitivity_current_volume_source | legacy current-volume | false | 0 | 0.00549 |

Interpretation: `J R` changes amplitude modestly near this reference, but it
does not restore a clean oscillatory attractor. It remains a possible legacy
artifact or modeling choice, not a positive mechanism.

### 4. Single-channel barrier removal does not reveal a hidden oscillator

| Case | Removed feedback | Oscillatory | Clipping | source tail / peak |
| ---- | ---------------- | ----------- | -------- | ------------------ |
| diagnostic_accessibility_constant | A suppression | false | 0 | 0.9996 |
| diagnostic_transport_constant | D/M suppression | false | 0 | 0.9951 |
| diagnostic_diffusivity_constant | D suppression | false | 0 | 0.9951 |
| diagnostic_mobility_constant | M suppression | false | 0 | 0.9934 |

Interpretation: near the selected reference, no single suppressive channel
isolates a missing oscillatory feedback. The issue is more basic: the
functional barrier never becomes strong enough before steady balance.

### 5. High-amplitude cases are contaminated by projection/clipping

Representative high-amplitude cases:

| Case | theta amplitude | Oscillatory flag | Complete cycles | Clipping |
| ---- | --------------- | ---------------- | --------------- | -------- |
| search_N31_Da4_BiT0p2 | 1.115 | false | 0 | 6076 |
| search_N31_Da8_BiT0p2 | 2.339 | false by cycle count | 0 | 7372 |
| perturb_Bi_c_2 | 2.007 | true by heuristic | 3 | 299 |
| perturb_Gamma_A_2p5 | 2.343 | false by cycle count | 0 | 8964 |

Interpretation: stronger forcing can create large excursions, but those
excursions are inseparable from positivity/projection interventions in the
current solver. `perturb_Bi_c_2` is the most useful contaminated clue because
it shows partial source shutdown and short heuristic cycles, but it still fails
the evidence gate because clipping is nonzero and the complete-cycle count is
below the issue #16 evidence requirement. These cases should be treated as
diagnostic artifacts, not mechanism evidence.

## Budget and timescale diagnosis

The clipping-free reference does not show source shutdown:

* source tail / global peak is approximately `0.993`;
* `A,D,M` remain close to unity;
* tail heat generation and heat loss are nearly equal;
* tail reactant supply and reaction consumption are nearly equal.

Reducing surface supply (`Bi_c = 0.2`) produces a colder, nearly steady case
with no geometric or functional skin. Increasing surface supply (`Bi_c = 2`)
produces larger excursions but also clipping. Increasing `Gamma_A` or lowering
`Bi_T` similarly drives clipping-dominated high-temperature behavior rather
than a clean relaxation cycle.

The working diagnosis is therefore:

```text
negative feedback is too weak or too late in the clipping-free regime;
when made stronger indirectly through forcing, the solver hits clipping before
it reaches a clean physical relaxation loop.
```

## Geometry versus functional barrier

The old geometric threshold `J <= 0.9 J_init` can mark collapse even when the
actual closure values remain weakly suppressed. At the clipping-free reference:

```text
max geometric skin thickness = 1.0
max functional skin thickness = 0.0
```

The current proposed functional-barrier observable is:

```text
functional barrier cell if A < 0.5 or D/D0 < 0.5 or M/M0 < 0.5
```

This threshold is diagnostic-only and is not physically derived. Future tasks
should replace it with a flux-budget-based barrier observable tied to actual
source or transport reduction instead of a fixed closure-value threshold.

## Answers to issue #18 causal questions

1. `S_R = R` versus `J R`: not decisive by itself in the bounded diagnostic
   family. `J^beta R` for `beta = 0, 0.5, 1` remains non-oscillatory and
   clipping-free near the reference.
2. `A,D,M` closures: likely primary issue. They do not create strong functional
   suppression in the clean reference before steady balance forms.
3. Surface reactant supply: changing `Bi_c` changes regime, but the low-supply
   case is cold/steady and the high-supply case is clipping-contaminated.
4. Heat loss / Arrhenius feedback: stronger heating or weaker cooling pushes
   toward clipping rather than clean reset; stronger cooling suppresses collapse.
5. LCST/osmotic sensitivity: increasing `S_chi` drives clipping/floor
   interventions without producing clean cycles in this local test.
6. Boundary scheme / Lagrangian transport: not identified as the dominant root
   cause here, but still unresolved because only the cell-center Robin branch is
   available.
7. Front/barrier observables: yes, the geometric observable is misleading for
   functional barrier formation.
8. Legacy artifacts: high-amplitude behavior remains consistent with clipping
   or hidden regularization artifacts; it is not clean evidence.

## Recommended narrow next step

Do not run a broad parameter scan next.

Recommended next task:

*Define a flux-budget-based functional barrier observable and run a fail-fast
one-parameter `Bi_c` bracket around the contaminated high-supply clue. Reject any
case with raw `logJ` bound hits, phi-ceiling hits, `u_floor` hits, nonfinite
source/flux values, or negative raw inventory.*

Only after that diagnostic step should the project propose a candidate
model-repair task for a sharper accessibility or transport closure.

## What not to do next

* Do not regenerate manuscript figures.
* Do not broaden the parameter search before a model-repair decision.
* Do not treat `search_N31_Da8_BiT0p2`, `perturb_Bi_c_2`, or
  `perturb_Gamma_A_2p5` as oscillation evidence while clipping is active.
* Do not promote `diagnostic_J_beta` or any new diagnostic transport closure to
  canonical defaults.
* Do not move anything into `docs/validated/`.

## Files created or modified

Created:

* `paper/solver/canonical_cpu/root_cause.py`
* `paper/solver/canonical_cpu/run_root_cause_checks.py`
* `tests/test_root_cause_diagnostics.py`
* `results/root_cause_missing_oscillations/**`
* `docs/reports/exploration/CODEX-REPORT-root-cause-missing-oscillations.md`
* `docs/reports/exploration/MULTIAGENT-REVIEW-root-cause-missing-oscillations.md`

Modified:

* `paper/solver/canonical_cpu/solver.py`
* `tests/test_canonical_solver.py`
* `docs/project_state.md`

## Commands run

| Command | Exit code |
| ------- | --------- |
| `. .venv/bin/activate && python -m pytest tests/test_canonical_solver.py::test_diagnostic_accessibility_constant_branch_only_removes_reaction_accessibility_barrier tests/test_canonical_solver.py::test_diagnostic_transport_constant_branch_only_removes_diffusivity_and_mobility_barriers tests/test_canonical_solver.py::test_diagnostic_J_beta_source_scaling_interpolates_reference_and_current_volume_sources -q` | 1 before implementation, then 0 |
| `. .venv/bin/activate && python -m pytest tests/test_root_cause_diagnostics.py -q` | 2 before implementation, then 0 |
| `. .venv/bin/activate && python -m paper.solver.canonical_cpu.run_root_cause_checks --outdir results/root_cause_missing_oscillations --overwrite` | 1 before JSON serialization fix, then 0 |
| `. .venv/bin/activate && python -m py_compile $(find paper/solver scripts tests -name '*.py' -print \| sort)` | 0 |
| `. .venv/bin/activate && python -m pytest tests/test_canonical_solver.py tests/test_evidence_observables.py tests/test_root_cause_diagnostics.py -q` | 0, 35 passed |
| `. .venv/bin/activate && make quickcheck` | 0, 46 passed |
| `git diff --check` | 0 |

`make derivations` was not run because no `.tex` files were modified.

## Checks passed

* root-cause diagnostic driver completed with `root cause partially identified`;
* relevant solver/evidence/root-cause tests passed;
* full scaffold quickcheck passed;
* whitespace check passed;
* `paper/figures/**` was not modified.

## Checks failed

Initial red tests and one first-pass driver failure were expected development
steps:

* missing diagnostic branches in `CanonicalParams`;
* missing root-cause module;
* non-serializable `CanonicalParams` objects in the first suite summary draft.

All were fixed before final verification.

## Known limitations

* The functional-barrier threshold `0.5` is diagnostic-only.
* No alternative boundary scheme was implemented.
* The high-amplitude cases are not evidence because they use clipping/floor
  interventions.
* Root cause is partially identified, not proven uniquely.

## Next recommended task

First create a diagnostic task that defines a flux-budget-based functional
barrier observable and runs a fail-fast `Bi_c` bracket around the contaminated
high-supply clue. If that confirms a clean near-loop route, then create a
candidate model-repair task for a sharper physically motivated functional
barrier closure.

No model or claim was promoted to validated status.
