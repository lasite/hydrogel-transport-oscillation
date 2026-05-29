# Hypotheses

## H1. Transport-barrier relaxation oscillator

Status: candidate

Claim:
LCST collapse creates a transient surface barrier that shuts off reactant supply or reaction accessibility, converting Arrhenius thermal runaway into a relaxation oscillation.

Required evidence:

* PDE simulation or reduced front model;
* phase lag between temperature, collapse, and reactant flux;
* recurrence in a bounded limit cycle;
* comparison to well-mixed ODE.

Possible falsification:

* oscillation persists even without spatial transport degradation;
* oscillation disappears under grid refinement;
* same behavior occurs in a homogeneous ODE;
* barrier does not form before reaction shuts off.

## H2. Homogeneous linear stability is insufficient

Status: candidate

Claim:
Linear stability of the homogeneous state does not determine the nonlinear spatial attractor because the oscillation depends on finite-amplitude LCST collapse and moving transport fronts.

Required evidence:

* homogeneous linear stability or ODE analysis;
* PDE simulation showing oscillatory attractor despite homogeneous prediction;
* front or barrier diagnostics.

Possible falsification:

* linear instability fully predicts onset and period;
* no distinct spatial barrier observable exists.

## H3. The mechanism is distinct from BZ gel and external photothermal feedback

Status: candidate

Claim:
The feedback switch is generated internally by spatial phase transition and transport degradation rather than by oscillatory chemistry, external light, or prepatterned catalysts.

Required evidence:

* literature matrix;
* model comparison;
* clear distinction in introduction.

## H4. Accessibility and diffusivity degradation are both barrier mechanisms

Status: candidate

Claim:
The factors `(1 - phi)^m_act` and `(1 - phi)^m_diff` encode two separable shutdown mechanisms: reduced reaction accessibility and reduced reactant transport. Either may be necessary for a robust LCST transport barrier.

Required evidence:

* control analysis with no accessibility degradation;
* control analysis with no diffusivity degradation;
* front/barrier diagnostics for each control;
* comparison of heat release and reactant flux phase lag.

Possible falsification:

* the same oscillation persists unchanged when either degradation factor is removed;
* no measurable transport or accessibility barrier forms during collapse.

## H5. Hopf and spinodal instabilities are distinct candidate mechanisms

Status: candidate

Claim:
The homogeneous long-wave Hopf mode and the finite-wavenumber spinodal mode represent distinct instabilities; self-oscillation should not be identified with spinodal decomposition unless the finite-wavenumber mode is shown to organize the observed cycle.

Required evidence:

* dispersion relation across relevant branches;
* limiting case with reaction disabled and temperature fixed above LCST;
* comparison of instability timescales with the oscillation period;
* spatial spectra or front diagnostics during the oscillatory regime.

Possible falsification:

* finite-wavenumber spinodal growth controls the observed oscillation onset and period;
* no separate long-wave oscillatory mode exists in the candidate parameter regime.
