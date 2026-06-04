# Multi-Agent Review: Convergence and Control Evidence

Status: completed for issue #16

Readiness label: not evidence ready

No model or claim was promoted to validated status.

## Scope

Reviewed the first formal convergence/control evidence attempt generated from
the final canonical solver under:

* `paper/solver/canonical_cpu/`
* `results/evidence_convergence_control/`

The review assessed whether the result establishes a transport-barrier
relaxation-oscillation mechanism. It does not.

## Reviewer Verdicts

### Physics Mechanism Reviewer

Verdict: fail

Reason: the controls cannot establish the intended transport-barrier mechanism
because there is no positive oscillatory reference case. The suite reports
`evidence_passed: false` and `readiness_label: not evidence ready`.

Key points:

* no clipping-free run had at least five post-transient cycles;
* the selected reference case is explicitly non-oscillatory;
* the no-barrier control remains non-oscillatory, so there is no oscillatory
  baseline from which barrier removal can demonstrate mechanism loss;
* no-accessibility-only and no-diffusivity/mobility-only controls are skipped
  because those branches are not exposed by the final solver.

### Numerical Convergence Reviewer

Verdict: fail

Reason: convergence was quantified only for a non-oscillatory reference, so
period, cycle stability, and front/barrier oscillation convergence remain
untested.

Key points:

* the selected reference has `theta_complete_cycles = 0` and no period;
* the default case reports clipping/floor interventions and cannot be used as
  evidence;
* convergence runs at `N = 51, 101, 201` are clipping-free but non-oscillatory;
* time-step and tolerance checks are stable, but only for the same
  non-oscillatory reference.

### Data Provenance Reviewer

Initial verdict: pass with limitations

The reviewer found strict JSON, complete run bundles, and no paper-figure cache
overwrite, but flagged three provenance limitations:

* per-run summaries recorded each run directory as the suite outdir;
* reruns could overwrite an existing evidence directory without an explicit
  overwrite flag;
* SciPy version was not recorded in evidence-suite metadata.

Repair applied:

* `run_evidence_checks` now requires `--overwrite` to replace an existing
  non-final evidence directory;
* suite and per-run metadata record the same suite outdir;
* suite metadata records NumPy and SciPy versions;
* the evidence suite was regenerated after the repair.

Final provenance check:

* strict JSON parse succeeds;
* driver source hashes match current files;
* suite outdir is consistent in suite and run summaries;
* SciPy metadata is recorded;
* `paper/figures/**` caches were not overwritten.

Final verdict: pass with limitations

### Adversarial Reviewer

Verdict: pass with limitations as an honest negative evidence attempt

Reason: the evidence package correctly stops short of claiming mechanism
evidence.

Adversarial explanations remain unresolved:

* large-amplitude search cases involve clipping/floor interventions;
* no face-value boundary reconstruction comparison is available;
* oscillation detection is based on mean observables and does not establish a
  robust spatial front/barrier attractor;
* the bounded search might miss a physically justified oscillatory region, but
  broad search is not allowed without human/ChatGPT decision;
* mechanism-isolating controls for accessibility-only and transport-only
  suppression are unavailable.

## Final Review Assessment

Overall verdict: fail as mechanism evidence; pass as a documented negative
evidence attempt.

The output package is auditable, but it does not support figure regeneration or
claim promotion. The correct next step is a human/ChatGPT decision on whether to
revise the model, add mechanism-isolating controls, or define a new bounded
physically justified search.

No model or claim was promoted to validated status.

