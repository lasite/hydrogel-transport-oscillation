# G1 Frozen Core Literature Corpus

Status: G1 exit corpus frozen for transition into G2 model specification.

Purpose: record the retained P0/P1 literature set after the initial 50-item literature pool, DOI/source audit, and novelty-risk review.

Boundary: this document freezes the literature basis for G2 model-specification constraints. It does not validate any model, derivation, simulation, or manuscript claim.

## Audit policy

The initial `docs/04_literature_map.md` v0.1 was intentionally broad and included weak P2 placeholders. For G2 entry, the core corpus is restricted to papers or preprints that are directly relevant to at least one of the following:

1. BZ and chemo-mechano-gel oscillators.
2. Ximin He / Aizenberg / Balazs feedback and hydrogel systems.
3. Thermoresponsive or LCST delayed-feedback hydrogel oscillators.
4. Non-oscillatory reaction plus responsive-gel feedback.
5. Reaction-diffusion or autocatalytic front hydrogel actuation.
6. LCST/PNIPAm, poroelasticity, diffusion, permeability, and transport-barrier physics.
7. Photothermal or geometric self-shadowing systems that delimit novelty language.

Audit status legend:

* `doi-locked`: DOI or article identifier is recorded with high confidence from publisher, author page, DOI string, or prior G1 web/deep-research source.
* `source-linked`: the paper is retained because a traceable author/publisher/arXiv source identifies it, but DOI metadata still needs final BibTeX cleanup before manuscript submission.
* `arXiv-linked`: preprint retained for mechanism comparison only.
* `core-risk`: must be cited or explicitly discussed in any novelty argument.

## Frozen corpus table

| ID | Status | Work | Family | Why retained for G2 |
| -- | ------ | ---- | ------ | ------------------- |
| C01 | doi-locked; core-risk | He, Aizenberg, Kuksenok, Zarzar, Shastri, Balazs, Aizenberg, "Synthetic homeostatic materials with chemo-mechano-chemical self-regulation," Nature 487, 214--218 (2012), doi:10.1038/nature11223 | SMARTS / Ximin He / Aizenberg / Balazs | Closest prior art for exothermic chemistry plus thermoresponsive homeostatic feedback. G2 must distinguish continuous collapsed-shell transport gating from catalyst-bearing microstructure switching. |
| C02 | doi-locked; core-risk | Zhao, Xuan, Qian, Alsaid, Hua, Jin, He, "Soft phototactic swimmer based on self-sustained hydrogel oscillator," Science Robotics 4, eaax7112 (2019), doi:10.1126/scirobotics.aax7112 | Ximin He hydrogel oscillator | Blocks broad `self-sustained hydrogel oscillator` novelty language. G2 must avoid claiming hydrogel self-oscillation as the novelty. |
| C03 | source-linked; core-risk | Qian et al., "Artificial Phototropism for Omnidirectional Tracking and Harvesting of Light," Nature Nanotechnology (2019) | Ximin He adaptive/photothermal soft material | Delimits photothermal adaptive-material framing and external light-powered feedback. |
| C04 | source-linked; core-risk | Shastri et al., "An Aptamer-functionalized Chemomechanically-modulated Biomolecule Catch-and-release System," Nature Chemistry 7, 447 (2015) | Ximin He / Aizenberg / Balazs chemomechanical release | Shows mechanical/material state can gate molecular accessibility. G2 must define accessibility degradation carefully. |
| C05 | source-linked | Sun et al., "Femtomol-level Ultra-sensitive and High-selective Chemical Sensors Based on Hydrogel Interferometer," Advanced Materials (2018) | Ximin He hydrogel sensing | Retained for possible experimental observables of swelling/collapse state. Not a novelty collision for the oscillator. |
| C06 | source-linked | Qin et al., "Hydrogel Interferometer for Adaptive Coloration and Chemical Sensing," Advanced Materials 30 (2018) | Ximin He hydrogel sensing | Retained for diagnostic and readout ideas. |
| C07 | doi-locked; core-risk | Zhang et al., "Feedback-controlled hydrogels with homeostatic oscillations and dissipative signal transduction," Nature Nanotechnology 17, 1303--1310 (2022), doi:10.1038/s41565-022-01241-x | Thermoresponsive feedback hydrogel | Very close prior art for LCST delayed thermal feedback. G2 must distinguish chemical heat and reactant transport/accessibility shutdown from optical transmittance feedback. |
| C08 | doi-locked; core-risk | Zhang et al., "Differential diffusion driven far-from-equilibrium shape-shifting of hydrogels," Nature Communications 12, 6155 (2021), doi:10.1038/s41467-021-26464-9 | Differential diffusion hydrogel dynamics | Forces G2 to distinguish sustained relaxation oscillation from transient overshoot or damped diffusion-driven deformation. |
| C09 | source-linked; core-risk | Horvath, Szalai, Boissonade, De Kepper, "Oscillatory dynamics induced in a responsive gel by a non-oscillatory chemical reaction: experimental evidence," Soft Matter 7, 8462--8472 (2011), candidate doi:10.1039/C1SM05402F | Non-oscillatory reaction plus responsive gel | Direct collision with the phrase `non-oscillatory reaction induces oscillation`. G2 must narrow the novelty to LCST transport-barrier and surface/bulk slow-manifold mechanism. |
| C10 | doi-locked; core-risk | Yashin and Balazs, "Pattern formation and shape changes in self-oscillating polymer gels," Science 314, 798--801 (2006), doi:10.1126/science.1132412 | Balazs BZ gel | Canonical BZ gel modeling and broad self-oscillating polymer-gel novelty blocker. |
| C11 | source-linked; core-risk | Yashin and Balazs, "Modeling polymer gels exhibiting self-oscillations due to the Belousov-Zhabotinsky reaction," Macromolecules (2006) | Balazs BZ gel model | Retained as a modeling precedent for BZ-driven gel oscillations. Final DOI/BibTeX cleanup required before manuscript. |
| C12 | doi-locked; core-risk | Yashin and Balazs, "Theoretical and computational modeling of self-oscillating polymer gels," Journal of Chemical Physics 126, 124707 (2007), doi:10.1063/1.2672951 | Balazs BZ gel model | Canonical chemo-responsive gel modeling framework. G2 should contrast with non-BZ, LCST transport-barrier mechanism. |
| C13 | doi-locked; core-risk | Kuksenok, Yashin, Balazs, "Three-dimensional model for chemoresponsive polymer gels undergoing the Belousov-Zhabotinsky reaction," Physical Review E 78, 041406 (2008), doi:10.1103/PhysRevE.78.041406 | Balazs BZ gel model | Geometry and boundary-condition precedent for gel chemo-mechanics. |
| C14 | source-linked; core-risk | Yashin, Kuksenok, Balazs, "Modeling autonomously oscillating chemo-responsive gels," Progress in Polymer Science 35, 155--173 (2010) | Balazs BZ gel review/model | Review-level source for autonomous chemo-responsive gels. DOI cleanup required. |
| C15 | source-linked; core-risk | Yoshida, "Self-oscillating gels driven by the Belousov-Zhabotinsky reaction as novel smart materials," Journal of Controlled Release (2010) | BZ self-oscillating gel review | Required novelty blocker for all broad self-oscillating-gel language. |
| C16 | doi-locked; core-risk | Yoshida, "Evolution of self-oscillating polymer gels as autonomous polymer systems," NPG Asia Materials 6, e107 (2014), candidate doi:10.1038/am.2014.32 | BZ self-oscillating gel review | Required novelty blocker for autonomous polymer-system language. |
| C17 | source-linked | Maeda, Hara, Sakai, Yoshida, Hashimoto, "Self-walking gel," Advanced Materials 19, 3480--3484 (2007) | BZ gel actuator | Retained to delimit self-motion/self-walking gel claims. |
| C18 | doi-locked; core-risk | Buskohl et al., "Belousov-Zhabotinsky autonomic hydrogel composites: regulating waves via asymmetry," Science Advances (2016), candidate doi:10.1126/sciadv.1500888 | BZ hydrogel composites | Retained for geometry/asymmetry control of BZ waves and actuation. |
| C19 | arXiv-linked; core-risk | Blanc et al., "Active pulsatile gels: from chemical microreactor to polymeric actuator," arXiv:2201.08273 (2022) | BZ active gel | Modern BZ gel data/modeling; important for timescale comparison between swelling and chemical period. |
| C20 | arXiv-linked | Webber and Montenegro-Johnson, "Oscillating chemical reactions enable communication between responsive hydrogels," arXiv:2508.02399 (2025) | BZ-responsive hydrogel theory | Recent theory showing poroelastic transport plus BZ chemistry can couple responsive hydrogels. Boundary literature for modern reviewer context. |
| C21 | arXiv-linked; core-risk | Reeves, Carballido-Landeira, Perez-Mercader, "Coupling chemical networks to hydrogels controls oscillatory behavior," arXiv:1501.06196 (2015) | Chemical networks plus hydrogels | Directly relevant because it discusses hydrogel feedback creating or controlling oscillatory behavior in chemical networks. |
| C22 | source-linked; core-risk | Jee, Bansagi, Taylor, Pojman, "Temporal Control of Gelation and Polymerization Fronts Driven by an Autocatalytic Enzyme Reaction," Angewandte Chemie International Edition (2016) | Autocatalytic fronts / gelation | Retained to delimit one-shot front/gelling dynamics from sustained LCST-front relaxation cycles. |
| C23 | source-linked; core-risk | Paikar et al., "Spatiotemporal Regulation of Hydrogel Actuators by Autocatalytic Reaction Networks," Advanced Materials (2022) | Autocatalytic front hydrogel actuator | Retained as a close front-actuated hydrogel prior art. DOI cleanup required. |
| C24 | doi-locked; core-risk | Duzs et al., "Mechano-adaptive meta-gels through synergistic chemical and physical information-processing," Nature Communications 15, 8957 (2024), doi:10.1038/s41467-024-53368-1 | Reaction-diffusion meta-gel | Modern RD-gel mechanism comparison; distinguishes adaptive front processing from autonomous LCST transport-barrier oscillator. |
| C25 | doi-locked; core-risk | Richbourg and Peppas, "The swollen polymer network hypothesis: quantitative models of hydrogel swelling, stiffness, and solute transport," Progress in Polymer Science (2020), candidate doi:10.1016/j.progpolymsci.2020.101243 | Hydrogel swelling/transport theory | Required for defining swelling, stiffness, diffusion, and transport claims quantitatively. |
| C26 | doi-locked; core-risk | Yoon, Cai, Suo, Hayward, "Poroelastic swelling kinetics of thin hydrogel layers," Soft Matter 6, 6004--6012 (2010), doi:10.1039/C0SM00434K | Poroelastic hydrogel kinetics | Required for barrier-layer / surface-collapse timescale analysis. |
| C27 | doi-locked | Yuan et al., "Thermoresponsive polymers with LCST transition: synthesis, characterization, and impact on biomedical frontiers," RSC Applied Polymers 1, 158--189 (2023), doi:10.1039/D3LP00114H | LCST polymer review | Retained for LCST/PNIPAm background and terminology. |
| C28 | source-linked; core-risk | Axpe et al., "A multiscale model for solute diffusion in hydrogels" (2019) | Hydrogel diffusion theory | Retained for later D(phi,T) and mesh-size/diffusion constraints. DOI cleanup required. |
| C29 | source-linked; core-risk | Offeddu et al., relationship between permeability and diffusivity in hydrogels (2018) | Permeability/diffusivity | Retained because G2 must not conflate diffusivity, permeability, and reaction accessibility. DOI cleanup required. |
| C30 | arXiv-linked | Li, Miao, Tsang, "Self-regulated photoresponsive heterogeneous PNIPAM hydrogel actuators," arXiv:2412.11688 (2024) | Photoresponsive PNIPAm actuator | Retained as a recent boundary case for self-regulated PNIPAm actuation under fixed light. |

## Removed or demoted from the initial 50-item pool

The following categories from `docs/04_literature_map.md` v0.1 are not part of the frozen G2-entry corpus unless later verified:

* Weak P2 placeholder rows without clear DOI, publication status, or direct mechanism relevance.
* Generic PNIPAm reviews unless needed for LCST terminology.
* Non-hydrogel thermal-front papers unless G2 explicitly needs a thermal-runaway analogy.
* General soft-robotics or active-matter papers without hydrogel transport/accessibility relevance.
* Ximin He group publications that are valuable context but not mechanistically relevant to oscillator novelty.

## G2 constraints implied by the frozen corpus

G2 model specification must test the mechanism against the core risks identified here:

1. The chemical subsystem must be non-oscillatory by itself.
2. A homogeneous ODE or well-mixed limit must be derived or explicitly marked as incomplete.
3. LCST collapse must be necessary for the claimed oscillator.
4. Transport degradation and/or accessibility degradation must be necessary for the claimed oscillator.
5. Diffusivity, permeability, and reaction accessibility must not be conflated.
6. The model must define a measurable front/barrier observable.
7. The surface/bulk distinction must be represented if the paper claims a surface slow manifold.
8. Claims about SNIC scaling, hysteresis, penetration depth, and basin size must remain unvalidated until reproduced by repository-controlled analysis.

## G1 exit judgment

G1 can be considered complete for the purpose of entering G2 because:

* a broad literature map exists in `docs/04_literature_map.md`;
* novelty framing exists in `docs/05_novelty_framing.md`;
* claim-centered prior-art risks exist in `docs/06_prior_art_risk_matrix.md`;
* this file freezes the retained core corpus for G2;
* the user accepted the novelty framing and prior-art risk matrix.

Remaining DOI/BibTeX cleanup is still required before manuscript drafting, but it does not block G2 model specification.
