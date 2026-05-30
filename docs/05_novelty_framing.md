# Novelty Framing Memo

Status: G1 working document; candidate framing only.

Purpose: convert the user-accepted idea brief and the G1 literature map into a focused novelty argument. This file does not validate the model, equations, numerical results, figures, or manuscript claims.

Primary source for this memo: user-provided research-significance note, May 2026, plus `docs/04_literature_map.md` v0.1.

## Core positioning

The project should not be framed as another demonstration that hydrogels can oscillate. That broad phenomenon is already established by BZ gels, photothermal self-shadowing systems, optically gated thermoresponsive gels, mechanically switched homeostatic materials, and feedback-controlled soft robots.

The candidate contribution is narrower and more theoretical:

> A single non-oscillatory exothermic reaction may be converted into a self-sustained relaxation oscillator by the hydrogel's own LCST poroelastic collapse, because collapse creates a spatial transport and reaction-accessibility barrier that quenches the heat source and enables recovery.

The intended significance is therefore a mechanism-level claim:

> The feedback source is not an external optical path, a discrete catalyst-bearing microstructure, an electronic controller, or an intrinsically oscillatory BZ chemical clock. It is a material-internal reaction--transport--phase-transition feedback loop organized by spatial gradients and surface exchange.

## Safe one-sentence novelty claim

Candidate wording:

> This work investigates a material-internal route by which a single non-oscillatory exothermic reaction can drive relaxation oscillations in an LCST hydrogel through the self-organization of a collapsed surface transport barrier.

This wording is intentionally narrower than `new hydrogel oscillator` or `first autonomous hydrogel oscillator`.

## Longer significance statement

Candidate wording:

> Existing hydrogel oscillators often obtain negative feedback by modulating an external energy or reaction pathway, for example through optical self-shadowing, light-transmittance switching, catalyst-bearing microstructures, or explicit sensing-control loops. In contrast, the mechanism considered here asks whether a single non-oscillatory exothermic reaction can be converted into a sustained relaxation oscillator by the hydrogel's own LCST poroelastic collapse. In this picture, collapse is not merely an actuation response. It creates a spatial transport and reaction-accessibility barrier that suppresses reactant supply and heat generation, while cooling and reswelling restore the reactive state. The contribution is therefore not the observation of gel oscillation per se, but the identification and analysis of a material-internal, spatially organized feedback route to autonomous chemo-thermo-poroelastic oscillation.

## Chinese working statement

候选表述：

> 本研究的意义不在于再次证明水凝胶可以振荡，而在于提出并分析一种由材料内部空间输运自组织产生的振荡机制：单一放热反应本身并非振荡反应，但其与 LCST 孔弹性塌缩耦合后，塌缩表层会形成反应物输运和反应可及性屏障，从而把 Arrhenius 热失控转化为可逆的前沿型 relaxation oscillation。与 BZ 凝胶、光热自遮挡振荡器或微结构催化开关不同，这里的反馈开关由凝胶内部的空间相变和输运退化自发生成；因此，该机制不仅解释了何时出现自振荡，也说明了为什么均匀态线性稳定性不足以预测空间 PDE 的吸引子结构。

## Mechanism contrast table

| System class | Feedback switch location | Energy input | Main prior contribution | How current project must differ |
| ------------ | ------------------------ | ------------ | ----------------------- | ------------------------------- |
| BZ self-oscillating gels | Intrinsic oscillatory chemistry embedded in gel | BZ chemical free energy | Demonstrates autonomous chemo-mechanical gel oscillations | Current chemistry must be non-oscillatory; oscillation must arise from material-mediated transport feedback. |
| Balazs BZ gel models | Oregonator/redox chemistry coupled to swelling | BZ reaction | Provides canonical reaction-diffusion-mechanics gel modeling | Current model must avoid hiding an intrinsic chemical oscillator in the kinetics. |
| SMARTS / He-Aizenberg-Balazs homeostatic material | Catalyst-bearing microstructures move into or out of nutrient layer | Exothermic catalytic reaction | Demonstrates chemo-mechano-chemical homeostasis | Current switch must be an internally formed transport/accessibility barrier, not an explicit moving catalyst microstructure. |
| Photothermal self-shadowing systems | Deformation blocks or redirects light | External constant light | Converts steady light into oscillatory mechanical output | Current feedback must not require external optical geometry or self-shadowing. |
| Zhang/Ikkala thermoresponsive feedback hydrogels | PNIPAm transmittance switch plus heat-transfer delay | External light | Demonstrates delayed thermal feedback and homeostatic oscillation | Current heat source must be chemical and coupled to reactant transport/accessibility. |
| Somatosensory hydrogel/control systems | Conductive sensing plus external control circuit | External light plus controller | Demonstrates closed-loop sensing-actuation | Current oscillator must be material-internal rather than controller-mediated. |
| Autocatalytic front hydrogels | Chemical front triggers gelation or actuation | Autocatalytic reaction network | Demonstrates spatial reaction-diffusion programming in gels | Current cycle must be sustained/recurrent and LCST transport-barrier mediated, not a one-shot front. |

## Candidate novelty claims

These are not validated claims. They define what later G2/G3 work must test.

### N1. Material-internal transport-barrier feedback

Candidate claim:

> LCST collapse creates a collapsed shell that reduces reactant transport and/or reaction accessibility, thereby forming the negative-feedback switch internally.

What this adds over prior art:

* The switch is neither optical nor a discrete microstructure.
* The feedback variable is a spatially localized material state.
* The barrier is the mechanism, not merely a side effect of actuation.

Required later evidence:

* Spatial profiles of temperature, reactant concentration, and collapse variable.
* A barrier observable that tracks diffusivity, permeability, accessibility, or reactant flux.
* Controls removing transport degradation, accessibility degradation, or LCST collapse.

### N2. Non-oscillatory chemistry becomes rhythmic through material feedback

Candidate claim:

> The reaction chemistry is not intrinsically oscillatory; the oscillation arises only after coupling to LCST phase transition, transport delay, and boundary exchange.

What this adds over BZ gels:

* The chemical subsystem alone should not support an oscillatory clock.
* The material response and spatial transport reorganize the dynamics.

Required later evidence:

* Homogeneous reaction-only and reaction-heat limits.
* Well-mixed ODE comparison.
* Demonstration that the same kinetics do not oscillate without LCST/transport coupling.

### N3. Thermal runaway is converted into spatial self-limitation

Candidate claim:

> LCST collapse turns local Arrhenius amplification into a self-limiting front/barrier process rather than global thermal runaway.

What this adds over simple negative-feedback language:

* The negative feedback has a physical carrier: a collapsed transport barrier.
* The mechanism localizes heat generation and reactant access near a surface/front.

Required later evidence:

* Parameter regimes showing cold steady state, hot/runaway state, and bounded oscillation.
* Spatial comparison of heat generation and reactant flux during collapse.
* Evidence that the collapsed region shuts down the heat source before global collapse invades the bulk.

### N4. Spatial structure generates the slow manifold

Candidate claim:

> The relaxation cycle is organized by a surface slow manifold generated by boundary exchange, LCST collapse, and poroelastic transport buffering, not by a pre-existing autonomous 0D oscillator.

What this adds over standard reduced-ODE framing:

* The slow manifold is an emergent spatial object.
* Surface and bulk trajectories can occupy different effective branches.
* The attractor is organized by spatial separation and exchange conditions.

Required later evidence:

* Surface vs bulk phase portraits.
* Fast variable / slow variable separation, for example fast swelling ratio and slower temperature/reactant fields.
* Evidence that a low-dimensional homogeneous reduction misses the observed attractor organization.

### N5. Homogeneous linear stability is not sufficient

Candidate claim:

> Homogeneous steady-state linear stability may be useful but is not sufficient to predict the actual spatial PDE attractor.

What this adds over standard Hopf/linear-stability analysis:

* A spatial front/barrier cycle may exist or disappear through global events not captured by local eigenvalues.
* Homogeneous branches may be absent or misleading in parameter regions where the PDE has structured dynamics.

Required later evidence:

* Explicit homogeneous steady-state and linear-stability analysis.
* Comparison against PDE attractors.
* Identification of where local stability predicts, fails to predict, or only bounds the observed oscillation.

### N6. Falsifiable signatures separate the mechanism from mere numerical oscillation

Candidate claim:

> The mechanism predicts signatures such as LCST-front penetration depth, critical slowing near an oscillation boundary, and initial-condition-dependent hysteresis between a front cycle and hot/runaway state.

What this adds over visual oscillation:

* It gives reviewers concrete ways to falsify the mechanism.
* It separates sustained relaxation oscillation from damped transients or numerical artifacts.

Required later evidence:

* Period scaling near an exit boundary, including a test against square-root and logarithmic laws.
* Initial-condition basin maps.
* Grid/timestep convergence for period, front position, and cycle amplitude.

## Model-internal quantitative claims from the current draft that require later audit

The user-provided significance note includes specific model-internal claims. These should be treated as draft hypotheses until reproduced in repository-controlled analysis.

| Draft claim | Current status | Required later action |
| ----------- | -------------- | --------------------- |
| LCST front penetration depth around `xi_LCST ~ 0.885`. | Unverified in repo. | Reproduce from model outputs or remove from manuscript. |
| Bulk fraction remains below LCST and prevents global collapse. | Unverified in repo. | Define bulk/surface metric and show profiles. |
| Homogeneous collapsed-only subregion covers about 51% of displayed parameter plane. | Unverified in repo. | Recompute parameter-plane classification. |
| Cycle exits near upper `S_chi` boundary through SNIC-like event. | Unverified in repo. | Fit period scaling and compare alternatives. |
| Cycle basin covers about 13% of initial-condition grid in one cell/parameter regime. | Unverified in repo. | Reproduce basin computation and archive script/config. |
| Sharp jump near `theta_0* ~ 2.4`. | Unverified in repo. | Reproduce initial-condition sweep. |

## Manuscript language rules

### Allowed before validation

* `candidate mechanism`
* `we investigate`
* `we test whether`
* `the model suggests`
* `provisional novelty window`
* `transport-barrier-mediated feedback`
* `material-internal delayed feedback`

### Avoid before validation

* `we demonstrate experimentally`
* `we prove`
* `first self-oscillating hydrogel`
* `new class of self-oscillating gels`
* `universal mechanism`
* `linear stability predicts the cycle`
* `validated transport barrier`

## G1 implication for G2

G2 model specification should not merely ask whether the candidate equations oscillate. It should be designed to test whether the proposed novelty mechanism survives:

1. Is the chemical subsystem non-oscillatory by itself?
2. Is LCST collapse necessary?
3. Is transport/accessibility degradation necessary?
4. Is the oscillator spatial rather than homogeneous?
5. Is the slow manifold generated by surface/bulk separation?
6. Are predicted signatures such as critical slowing and hysteresis reproducible?

## Current status

This file defines the candidate novelty framing for G1. It is ready for prior-art risk audit but not ready to support manuscript novelty claims without source audit and later model evidence.
