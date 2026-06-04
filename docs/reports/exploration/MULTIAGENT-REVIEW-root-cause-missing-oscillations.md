# Multi-Agent Review: Root Cause of Missing Oscillations

Status: completed for issue #18

Conclusion label: root cause partially identified

No model or claim was promoted to validated status.

## Scope

Reviewed the bounded root-cause diagnostic outputs under:

* `results/root_cause_missing_oscillations/`
* `paper/solver/canonical_cpu/root_cause.py`
* `paper/solver/canonical_cpu/run_root_cause_checks.py`

The review assessed whether the task identifies why the final canonical model
settles into hot nonuniform steady states or clipping-contaminated excursions
instead of a clean relaxation oscillation.

## Reviewer verdicts

### Physics Cause Reviewer

Verdict: pass with limitations

The physical diagnosis is supported locally but should remain `root cause
partially identified`.

Supported points:

* The clipping-free reference `search_N31_Da1_BiT0p2` shows geometric collapse
  without a strong functional `A,D,M` barrier.
* The same reference approaches source/loss and supply/consumption balance.
* `J^beta R` source scaling for `beta = 0, 0.5, 1` does not recover a clean
  oscillator near the selected reference.
* High-amplitude cases are contaminated by clipping and cannot be treated as
  mechanism evidence.

Limitations:

* The `A,D,M < 0.5` functional-barrier threshold is diagnostic-only.
* Tail steady balance is a symptom of the non-oscillatory attractor, not by
  itself a unique physical cause.

Minimum next change:

Define a functional-barrier model or observable tied to actual source/flux
reduction before broadening parameter search.

### Budget and Timescale Reviewer

Verdict: pass with limitations

The budget evidence supports a local diagnosis:

* clean reference source/loss tail ratio: approximately `0.9998`;
* clean reference supply/source tail ratio: approximately `1.0000`;
* clean reference source tail/global peak: approximately `0.9934`;
* clean reference functional barrier is weak, with `min A = 0.727`,
  `min D/D0 = 0.899`, and `min M/M0 = 0.948`.

The reviewer identified `perturb_Bi_c_2` as an important contaminated clue:

* it has source tail/global peak near `0.201`;
* it has a nonzero functional skin;
* it shows short heuristic cycles;
* it also has `299` clipping/projection events.

Interpretation:

This case suggests a delayed loop may be nearby in parameter space, but it is
not clean evidence.

Minimum next change:

Add phase-resolved source/loss/supply diagnostics and fail-fast clipping gates
before changing model closure.

### Numerical Artifact Reviewer

Verdict: reject as numerical evidence; accept as diagnostic artifact analysis

No clean oscillation exists in the root-cause output package.

Artifact findings:

* `perturb_Bi_c_2` has three heuristic cycles but `299` clipping/projection
  events.
* `search_N31_Da8_BiT0p2` and `perturb_Gamma_A_2p5` receive
  `oscillatory_nonuniform` labels from the loose classifier, but the evidence
  cycle rule rejects them and they have thousands of clipping/floor events.
* Nonfinite counts are zero, but clipping/projection counts remain the relevant
  contamination signal because the solver projects states before flux
  evaluation.
* Boundary and inventory signs appear internally consistent, but residuals are
  diagnostic-grade only.

Minimum next check:

Run a one-parameter `Bi_c` bracket around the contaminated high-supply case with
fail-fast rejection on any raw `logJ` bound hit, phi-ceiling hit, `u_floor` hit,
nonfinite source/flux, or negative raw inventory.

### Adversarial Reviewer

Verdict: root cause partially identified

Strong objections:

* The main barrier claim relies on one clipping-free reference and a
  diagnostic, not physically derived, threshold.
* `J^beta R` only rules out source scaling as decisive near the selected
  reference.
* Solver classification is weaker than the evidence gate; apparent oscillatory
  labels must not be used as evidence.
* Boundary damping or oversupply remains unresolved because only the
  cell-center Robin branch is available.
* High-amplitude cases remain explainable by positivity/floor projection.

Minimum next change:

Define a flux-budget-based functional barrier observable, then run one
clipping-free barrier-strengthening test around `search_N31_Da1_BiT0p2`.

## Final review assessment

Overall verdict: pass as a bounded root-cause diagnostic; fail as numerical
evidence.

The reviewers agree that the report should say:

```text
root cause partially identified
```

The strongest supported diagnosis is:

```text
At the clipping-free reference, geometric collapse does not become a strong
functional transport/accessibility barrier before the trajectory settles into
source/loss and supply/consumption balance. Cases that move toward a larger
excursion activate clipping/projection and cannot be used as mechanism
evidence.
```

## Required next decision

The next task should not regenerate figures or run a broad scan. It should
choose one narrow path:

1. define a flux-budget-based functional barrier observable;
2. run a fail-fast `Bi_c` bracket around the contaminated high-supply clue;
3. propose one physically motivated candidate repair to the accessibility or
   transport closure, requiring human/ChatGPT approval before becoming
   canonical.

No model or claim was promoted to validated status.
