# Literature Map

Status: G1 active; v0.1 populated with a 50-item candidate corpus.

Purpose: novelty matrix and gap analysis for the candidate LCST-gated transport-barrier relaxation oscillator.

Scope: literature from roughly 2006--2026, emphasizing Ximin He group, Anna C. Balazs group, BZ/self-oscillating gels, LCST/PNIPAM transport, thermo-responsive feedback oscillators, reaction-diffusion fronts, and hydrogel transport/permeability theory.

Boundary: this file is literature mapping only. It does not validate the model, equations, numerical results, figures, or manuscript claims.

## G1 working conclusion

The project should not claim to be the first self-oscillating hydrogel, autonomous hydrogel, or BZ-free oscillator in a broad sense. Those broad claims collide with BZ-gel literature, homeostatic hydrogel systems, and thermoresponsive feedback oscillators.

The provisional novelty window is narrower:

> A non-oscillatory exothermic Arrhenius reaction may become a relaxation oscillator when coupled to LCST poroelastic collapse because temperature-triggered collapse self-organizes a spatial transport and reaction-accessibility barrier that closes a delayed negative-feedback loop.

The key claim should therefore be framed as a mechanism claim, not a broad material-class claim.

## Allowed provisional novelty language

* LCST-gated transport-mediated relaxation oscillator.
* Thermo-chemo-poroelastic transport-barrier oscillator.
* Transport-coupled thermoresponsive delayed-feedback oscillator.
* Candidate mechanism for converting a non-oscillatory exothermic reaction into a spatial relaxation oscillator.

## High-risk or forbidden novelty language until much stronger evidence exists

* First self-oscillating hydrogel.
* First autonomous hydrogel oscillator.
* First self-regulating hydrogel.
* New class of self-oscillating gels.
* BZ-free self-oscillating gel, unless the nearest non-BZ responsive-gel oscillators are explicitly ruled out.
* Homeostatic hydrogel, unless the relationship to He/Aizenberg/Balazs 2012 and Zhang/Ikkala 2022 is made precise.

## Mechanism-family map

| Family | Oscillation or dynamics source | Feedback switch | Spatial/transport role | Risk to this project |
| ------ | ------------------------------ | --------------- | ---------------------- | -------------------- |
| BZ self-oscillating gels | Intrinsically oscillatory BZ chemistry | Chemical redox state changes gel swelling | Reaction-diffusion waves and gel swelling | Blocks broad claims about self-oscillating hydrogels. |
| He/Aizenberg/Balazs homeostatic materials | Exothermic catalytic reaction plus thermoresponsive gel feedback | Gel-actuated catalyst/reactant contact | Device geometry controls reaction access | Very close prior art for exothermic reaction + thermoresponsive feedback. |
| Photothermal thermoresponsive oscillators | Constant light plus thermal negative feedback | PNIPAm optical/thermal switching | Heat-transfer delay controls period | Close prior art for LCST delayed-feedback temperature oscillation. |
| Responsive-gel oscillators driven by non-oscillatory reactions | Non-oscillatory chemistry coupled to gel response | Responsive-gel phase/state feedback | Diffusion and gel swelling mediate delay | Directly threatens any simple non-BZ oscillator claim. |
| Autocatalytic fronts in gels | Autocatalytic reaction-diffusion front | pH/gelation/swelling front | Front transmits chemical information spatially | Distinguish sustained oscillation from one-shot or excitable fronts. |
| LCST/PNIPAm transport and poroelasticity | Not necessarily oscillatory | Temperature-driven swelling/collapse | Diffusion, permeability, poroelastic relaxation | Provides necessary physical basis for G2 model. |
| Hydrogel diffusion/permeability theory | Not oscillatory | Mesh size, swelling, permeability | Solute transport changes with network state | Prevents conflating diffusivity, permeability, and accessibility. |
| Thermal runaway / reaction fronts | Exothermic reaction and heat diffusion | Temperature-dependent reaction rate | Heat fronts and ignition/extinction | Clarifies whether behavior is thermal runaway/front rather than hydrogel feedback. |

## Fifty-paper candidate corpus v0.1

Trace status legend: `source-checked` means enough bibliographic information was confirmed from an opened source during G1 review; `source-linked` means a credible source or DOI/URL is listed but not fully audited; `doi-audit-needed` means the row should be verified before G1 exit.

| ID | Priority | Work | Family | Oscillation source | Feedback switch | Spatial/transport role | Relation to project | Trace status |
| -- | -------- | ---- | ------ | ------------------ | --------------- | ---------------------- | ------------------- | ------------ |
| G1-001 | P0 | He, Aizenberg, Kuksenok, Zarzar, Shastri, Balazs, Aizenberg, "Synthetic homeostatic materials with chemo-mechano-chemical self-regulation," Nature 487, 214--218 (2012), doi:10.1038/nature11223 | He/Aizenberg/Balazs homeostatic material | Exothermic catalytic reaction coupled to thermoresponsive gel | Gel-controlled catalyst/reactant contact; on/off reaction switching | Device-scale reaction access and heat feedback | Closest prior art for exothermic chemistry + thermoresponsive feedback; novelty must distinguish internal transport barrier from engineered microstructure contact switching. | source-checked |
| G1-002 | P0 | Zhao, Xuan, Qian, Alsaid, Hua, Jin, He, "Soft phototactic swimmer based on self-sustained hydrogel oscillator," Science Robotics 4, eaax7112 (2019), doi:10.1126/scirobotics.aax7112 | Ximin He soft robotics | Self-sustained hydrogel oscillator driving swimmer | Photothermal/thermoresponsive feedback | Hydrogel actuation and locomotion | Blocks broad "self-sustained hydrogel oscillator" novelty language. | source-checked via UCLA publication list; doi-audit-needed |
| G1-003 | P0 | Qian et al., "Artificial phototropism for omnidirectional tracking and harvesting of light," Nature Nanotechnology (2019) | Ximin He adaptive soft material | Light-responsive tracking, not primarily chemical oscillation | Feedback from photothermal/material response | Spatial light tracking and energy harvesting | Nearby autonomous/adaptive material framing; not the same transport-barrier oscillator. | source-checked via UCLA publication list; doi-audit-needed |
| G1-004 | P0 | Shastri et al., "An aptamer-functionalized chemomechanically modulated biomolecule catch-and-release system," Nature Chemistry 7, 447 (2015) | Ximin He / Aizenberg / Balazs chemomechanical release | No sustained oscillator required | Gel/mechanical state controls binding/release | Accessibility of molecular cargo is mechanically modulated | Relevant precedent for accessibility gating; not a thermal transport oscillator. | source-checked via UCLA publication list; doi-audit-needed |
| G1-005 | P0 | Sun et al., "Femtomol-level ultra-sensitive and high-selective chemical sensors based on hydrogel interferometer," Advanced Materials (2018) | Ximin He hydrogel sensing | Not oscillator | Swelling changes optical response | Hydrogel state becomes observable | Useful for diagnostic/observable design; not novelty collision for oscillator mechanism. | source-checked via UCLA publication list; doi-audit-needed |
| G1-006 | P0 | Qin et al., "Hydrogel interferometer for adaptive coloration and chemical sensing," Advanced Materials 30 (2018) | Ximin He hydrogel sensing | Not oscillator | Swelling controls optical interference | Converts swelling into readout | Useful for tracking collapse/transport observables. | source-checked via UCLA publication list; doi-audit-needed |
| G1-007 | P0 | Zhang et al., "Feedback-controlled hydrogels with homeostatic oscillations and dissipative signal transduction," Nature Nanotechnology 17, 1303--1310 (2022), doi:10.1038/s41565-022-01241-x | Thermoresponsive feedback hydrogel | Constant light plus delayed thermal negative feedback | PNIPAm phase transition modulates light transmission | Heat-transfer delay controls oscillation period | Extremely close prior art for LCST delayed-feedback temperature oscillation; project must distinguish chemical heat source and transport/reaction-accessibility barrier. | source-checked |
| G1-008 | P0 | Zhang et al., "Differential diffusion driven far-from-equilibrium shape-shifting of hydrogels," Nature Communications 12, 6155 (2021), doi:10.1038/s41467-021-26464-9 | Differential diffusion hydrogel | Non-oscillatory far-from-equilibrium transient | Programmed stress and water diffusion amplify shape change | Uneven water diffusion drives non-monotonic shape change | Important warning: transport can produce transient overshoot without sustained oscillation. | source-checked |
| G1-009 | P0 | Horvath, Szalai, Boissonade, De Kepper, "Oscillatory dynamics induced in a responsive gel by a non-oscillatory chemical reaction: experimental evidence," Soft Matter 7, 8462--8472 (2011), likely doi:10.1039/C1SM05402F | Responsive-gel oscillator | Non-oscillatory chemical reaction plus gel feedback | Responsive gel feeds back on chemistry | Diffusion/gel response mediates dynamics | Direct novelty threat: non-oscillatory reaction can induce gel oscillatory dynamics. Must compare explicitly. | source-checked through Nature 2012 reference list; doi-audit-needed |
| G1-010 | P0 | Yashin and Balazs, "Pattern formation and shape changes in self-oscillating polymer gels," Science 314, 798--801 (2006), doi:10.1126/science.1132412 | Balazs BZ gel model | Intrinsic BZ chemical oscillator | Redox-dependent swelling | Reaction-diffusion patterning and shape change | Blocks broad self-oscillating polymer-gel novelty; G2 must distinguish BZ chemical clock from thermal transport barrier. | source-checked through Nature 2012 reference list; doi-audit-needed |
| G1-011 | P0 | Yashin and Balazs, "Modeling polymer gels exhibiting self-oscillations due to the Belousov-Zhabotinsky reaction," Macromolecules (2006) | Balazs BZ gel model | Intrinsic BZ chemical oscillator | Redox-gel coupling | Gel swelling coupled to RD chemistry | Key modeling precedent; exact DOI must be audited. | doi-audit-needed |
| G1-012 | P0 | Yashin and Balazs, "Theoretical and computational modeling of self-oscillating polymer gels," Journal of Chemical Physics 126, 124707 (2007), doi:10.1063/1.2672951 | Balazs BZ gel model | Intrinsic BZ chemical oscillator | Oregonator + gel mechanics | RD and swelling dynamics | G2 model should cite as canonical chemo-responsive gel modeling benchmark. | source-linked; doi-audit-needed |
| G1-013 | P0 | Kuksenok, Yashin, Balazs, "Three-dimensional model for chemoresponsive polymer gels undergoing the Belousov-Zhabotinsky reaction," Physical Review E 78, 041406 (2008), doi:10.1103/PhysRevE.78.041406 | Balazs BZ gel model | Intrinsic BZ chemical oscillator | Redox-swelling coupling | 3D gel deformation and chemical waves | Boundary/geometry comparison for later numerical modeling. | source-checked through Nature 2012 reference list |
| G1-014 | P0 | Yashin, Kuksenok, Balazs, "Modeling autonomously oscillating chemo-responsive gels," Progress in Polymer Science 35, 155--173 (2010) | Balazs BZ gel review/model | Intrinsic BZ chemical oscillator | Chemo-mechanical coupling | RD + gel swelling | Review-level benchmark for autonomous chemo-responsive gels. | source-checked through Nature 2012 reference list; doi-audit-needed |
| G1-015 | P0 | Jee, Bansagi, Taylor, Pojman, "Temporal Control of Gelation and Polymerization Fronts Driven by an Autocatalytic Enzyme Reaction," Angewandte Chemie International Edition (2016) | Autocatalytic front / gelation | Autocatalytic enzyme reaction front | pH/enzyme front triggers gelation/polymerization | Propagating front controls material transition | Distinguish one-shot front/gelling wave from sustained LCST transport-barrier oscillator. | source-linked via Pojman publication listing; doi-audit-needed |
| G1-016 | P0 | Paikar et al., "Spatiotemporal Regulation of Hydrogel Actuators by Autocatalytic Reaction Networks," Advanced Materials (2022) | Autocatalytic front hydrogel actuator | Autocatalytic reaction network | pH/chemical front activates hydrogel | Front propagates through gel/device | Strong front-actuator prior art; must separate excitable/front actuation from recurrent oscillation. | doi-audit-needed |
| G1-017 | P0 | Duzs et al., "Mechano-adaptive meta-gels through synergistic chemical and physical information-processing," Nature Communications 15, 8957 (2024), doi:10.1038/s41467-024-53368-1 | Reaction-diffusion meta-gel | Autocatalytic RD signal after mechanical trigger | Chemical circuit triggers downstream actuation | Long-range reaction-diffusion front | Strong modern RD-gel precedent; not a thermal relaxation oscillator but close in mechanism-comparison section. | source-checked |
| G1-018 | P0 | Richbourg and Peppas, "The swollen polymer network hypothesis: quantitative models of hydrogel swelling, stiffness, and solute transport," Progress in Polymer Science (2020) | Hydrogel transport theory | Not oscillator | Swelling controls stiffness and solute transport | Links network state to transport properties | Foundational for defining D(phi,T), permeability, swelling, and evidence standards. | doi-audit-needed |
| G1-019 | P0 | Yoon, Cai, Suo, Hayward, "Poroelastic swelling kinetics of thin hydrogel layers: comparison of theory and experiment," Soft Matter 6, 6004--6012 (2010), doi:10.1039/C0SM00434K | Poroelastic hydrogel | Not oscillator | Poroelastic swelling/collapse | Thin-layer swelling kinetics | Directly relevant to LCST skin/barrier timescale and thickness scaling. | source-checked |
| G1-020 | P0 | Yuan et al., "Thermoresponsive polymers with LCST transition: synthesis, characterization, and their impact on biomedical frontiers," RSC Applied Polymers 1, 158--189 (2023), doi:10.1039/D3LP00114H | LCST polymer review | Not oscillator | LCST phase transition | Thermoresponsive polymer collapse/hysteresis | Background for LCST transition, tunability, and PNIPAm hysteresis. | source-checked |
| G1-021 | P1 | Yoshida, "Self-oscillating gels driven by the Belousov-Zhabotinsky reaction as novel smart materials," Journal of Controlled Release (2010) | BZ self-oscillating gel review | Intrinsic BZ chemical oscillator | Redox-state gel swelling | Gel oscillates with BZ chemistry | Broad novelty blocker for self-oscillating gel language. | doi-audit-needed |
| G1-022 | P1 | Yoshida, "Evolution of self-oscillating polymer gels as autonomous polymer systems," NPG Asia Materials (2014) | BZ self-oscillating gel review | Intrinsic BZ chemical oscillator | Chemo-mechanical swelling | Autonomous polymer-system framing | Broad novelty blocker for autonomous polymer-system language. | doi-audit-needed |
| G1-023 | P1 | Maeda, Hara, Sakai, Yoshida, Hashimoto, "Self-walking gel," Advanced Materials 19, 3480--3484 (2007) | BZ gel actuator | Intrinsic BZ chemical oscillator | Asymmetric gel swelling | Chemical waves drive locomotion | Blocks broad actuation/self-motion novelty. | source-checked through Nature 2012 reference list; doi-audit-needed |
| G1-024 | P1 | Buskohl et al., "Belousov-Zhabotinsky autonomic hydrogel composites: regulating waves via asymmetry," Science Advances (2016) | BZ hydrogel composite | Intrinsic BZ chemical oscillator | Composite asymmetry regulates waves | Spatial material geometry controls waves | Relevant to geometry-dependent oscillation and wave control. | doi-audit-needed |
| G1-025 | P1 | Blanc et al., "Active pulsatile gels: from chemical microreactor to polymeric actuator," arXiv / later literature (2022+) | BZ active hydrogel | Intrinsic BZ chemical oscillator | BZ reaction-swelling coupling | Gel radius and Damkohler number control oscillation | Modern BZ hydrogel benchmark; compare swelling timescale vs chemistry period. | source-linked |
| G1-026 | P1 | Blanc et al., "Collective chemomechanical oscillations in active hydrogels," PNAS (2024) | BZ active hydrogel | Intrinsic BZ chemical oscillator | Chemical-mechanical oscillation | Collective coupling among gels | Modern benchmark for collective active-gel oscillations. | doi-audit-needed |
| G1-027 | P1 | Geher-Herczegh et al., "Delayed mechanical response to chemical kinetics in self-oscillating hydrogels," Macromolecules (2021) | BZ hydrogel delay | Intrinsic BZ chemical oscillator | Delay between chemistry and mechanics | Mechanical lag in gel response | Useful for phase-lag analysis; mechanism distinct from LCST barrier. | doi-audit-needed |
| G1-028 | P1 | Levin, Deegan, Sharon, "Oscillating membranes: modeling and controlling autonomous shape-transforming sheets," arXiv / related literature (2019) | Gel/membrane oscillator | Internal signaling in sheet | Programmed mechanical response | Thin-sheet geometry | Boundary case for autonomous shape oscillations, not necessarily transport-barrier chemistry. | source-linked |
| G1-029 | P1 | Webber and Montenegro-Johnson, "Oscillating chemical reactions enable communication between responsive hydrogels," arXiv (2025) | BZ-responsive hydrogel theory | Oscillating chemical reaction | Responsive hydrogel coupling | Transport and elastic deformation enable communication | New theory risk for hydrogels communicating via BZ-type chemistry. | source-linked |
| G1-030 | P1 | Thutupalli and Herminghaus, "Oscillation patterns in active emulsion networks," arXiv / active matter literature (2012) | BZ active droplets | Intrinsic BZ chemical oscillator | Inter-droplet chemical coupling | Activator/inhibitor exchange | Relevant as non-gel active oscillator boundary case. | source-linked |
| G1-031 | P1 | Kitahata et al., "Spontaneous motion of a droplet coupled with a chemical wave," arXiv / literature (2010) | BZ droplet propulsion | Intrinsic chemical wave | Marangoni coupling | Internal RD pattern drives motion | Boundary case for chemically powered soft motion. | source-linked |
| G1-032 | P1 | Xu et al., "Bioinspired self-resettable hydrogel actuators powered by a chemical fuel," ACS Applied Materials & Interfaces (2022) | Fuel-driven actuator | Chemical fuel / transient cycle | Self-resetting feedback | Hydrogel actuation | Distinguish self-resetting one/few-cycle behavior from sustained oscillation. | doi-audit-needed |
| G1-033 | P1 | Zhang et al., "Homogeneous freestanding luminescent perovskite organogel with superior water stability," Advanced Materials (2019) | Ximin He materials | Not oscillator | Gel material platform | Not central to transport oscillator | Low mechanism priority; keep only if He corpus context is needed. | source-checked via UCLA publication list |
| G1-034 | P1 | Choi et al., "Hydrocipher: Bioinspired dynamic structural color-based cryptographic surface," Advanced Optical Materials (2019) | Ximin He dynamic hydrogel interface | Not oscillator | Responsive structural-color state | Surface/hydrogel response | Useful for He group context; not a novelty collision for oscillator mechanism. | source-checked via UCLA publication list |
| G1-035 | P1 | Qin, Sun, Hua, He, "Bioinspired structural color sensors based on responsive soft materials," Current Opinion in Solid State and Materials Science 23, 13--27 (2019) | Ximin He review | Not oscillator | Responsive soft material optical readout | Hydrogel state sensing | Useful for observables and response readout. | source-checked via UCLA publication list |
| G1-036 | P1 | Futscher et al., "The role of backbone hydration of PNIPAM across the volume phase transition," Scientific Reports (2017) | PNIPAm LCST physics | Not oscillator | Hydration/dehydration transition | Microscopic LCST mechanism | Helps define thermal collapse assumptions. | doi-audit-needed |
| G1-037 | P1 | Friesen et al., modified Flory-Rehner theory for thermotropic swelling of microgels (2022) | LCST swelling thermodynamics | Not oscillator | Temperature-dependent swelling | Equilibrium/transition model | Candidate source for G2 swelling function. | doi-audit-needed |
| G1-038 | P1 | Axpe et al., "A multiscale model for solute diffusion in hydrogels" (2019) | Solute diffusion in hydrogels | Not oscillator | Mesh/swelling controls diffusion | Solute diffusivity | Use to avoid arbitrary D(phi,T) choices. | doi-audit-needed |
| G1-039 | P1 | Offeddu et al., relationship between permeability and diffusivity in PEG hydrogels (2018) | Hydrogel permeability/diffusivity | Not oscillator | Network state controls transport | Distinguishes permeability and diffusivity | Critical for defining transport barrier correctly. | doi-audit-needed |
| G1-040 | P1 | Zustiak et al., solute diffusion in PEG-DA hydrogels (2010) | Hydrogel solute diffusion | Not oscillator | Mesh-size-dependent diffusion | Solute transport baseline | Background for permeability/diffusion estimates. | doi-audit-needed |
| G1-041 | P1 | Caccavo et al., "PoroViscoElastic model to describe hydrogels' behavior," Materials Science and Engineering C (2017) | Poro-viscoelastic hydrogel | Not oscillator | Poro-viscoelastic response | Deformation/transport coupling | If LCST collapse is slow or hysteretic, pure diffusion may be insufficient. | doi-audit-needed |
| G1-042 | P1 | Louf et al., "Poroelastic shape relaxation of hydrogel particles" (2021) | Poroelastic relaxation | Not oscillator | Poroelastic fluid migration | Shape relaxation timescale | Helps compare barrier relaxation time to thermal/reaction time. | doi-audit-needed |
| G1-043 | P1 | Dimitriyev, Chang, Goldbart, Fernandez-Nieves, "Swelling thermodynamics and phase transitions of polymer gels" (2019) | Gel phase transition theory | Not oscillator | Swelling thermodynamics | Phase separation / volume transition | Useful theory background for LCST collapse and phase coexistence. | source-linked |
| G1-044 | P1 | Warren et al., "Porous PNIPAm hydrogels: overcoming diffusion-governed actuation," Sensors and Actuators A (2020) | PNIPAm porous actuation | Not oscillator | Porosity accelerates thermal actuation | Diffusion-governed response | Relevant to whether collapsed surface layer is transport-limited. | doi-audit-needed |
| G1-045 | P2 | Li, Miao, Tsang, "Self-regulated photoresponsive heterogeneous PNIPAM hydrogel actuators," arXiv (2024) | Photoresponsive PNIPAm actuator | Constant light / material feedback | Heterogeneous PNIPAm response | Geometry controls actuation | Modern boundary case for self-regulated PNIPAm actuation. | source-linked |
| G1-046 | P2 | Gray et al., adaptive hydrogels with spatiotemporal stiffening using pH-modulating enzymes (2025) | Enzyme-adaptive gel | pH enzyme dynamics | pH-mediated material transition | Spatiotemporal stiffening | Recent boundary case; verify before using in manuscript. | doi-audit-needed |
| G1-047 | P2 | Korevaar et al., pathway complexity in supramolecular polymerization and hydrogel signal integration (2020) | Dissipative material / signal integration | Chemical pathway dynamics | Assembly/disassembly response | Not necessarily transport barrier | Background for non-equilibrium materials, less direct. | doi-audit-needed |
| G1-048 | P2 | Feng et al., propagation dynamics of thermal runaway fronts (2024) | Thermal runaway fronts | Exothermic heat release | Arrhenius thermal feedback | Heat front propagation | Non-hydrogel analogy; useful for distinguishing thermal runaway from LCST-gated oscillator. | doi-audit-needed |
| G1-049 | P2 | Zhao et al., initiation and propagation of curved reaction front in solids (2022) | Reaction/thermal front | Exothermic front | Reaction-heat coupling | Front geometry | Non-hydrogel analogy for thermochemical front behavior. | doi-audit-needed |
| G1-050 | P2 | Das et al. or recent PNIPAM review literature (2024) | PNIPAm review | Not oscillator | LCST polymer background | Materials choice and LCST tuning | Background only; replace with exact reviewed source after DOI audit. | doi-audit-needed |

## Legacy foundation papers to keep outside the 2006--2026 corpus

| Work | Why it remains necessary |
| ---- | ------------------------ |
| Heskins and Guillet, PNIPAm LCST work (1968) | Historical source for PNIPAm lower critical solution temperature behavior. |
| Tanaka and Fillmore, swelling kinetics of gels (1979) | Classical swelling timescale and diffusion-limited gel kinetics. |
| Peppas and Reinhart, solute diffusion in hydrogels (1983) | Mesh-size / solute-size / diffusivity baseline. |
| Yoshida et al., "Self-Oscillating Gel" (1996) | Foundational BZ-gel self-oscillation novelty blocker. |
| Pojman et al., frontal polymerization / thermochemical front literature (1990s) | Background for exothermic reaction fronts and thermal runaway analogies. |

## Novelty-risk matrix

| Candidate project claim | Closest prior art | Risk level | Required narrowing |
| ----------------------- | ----------------- | ---------- | ------------------ |
| A single non-oscillatory exothermic reaction can generate oscillations when coupled to LCST collapse. | He/Aizenberg/Balazs 2012; Horvath et al. 2011; Zhang/Ikkala 2022 | Very high | State that the proposed mechanism is specifically LCST-gated transport and reaction-accessibility barrier formation, not generic homeostasis or responsive-gel oscillation. |
| The oscillation is hydrogel self-oscillation. | Yoshida BZ gels; Balazs BZ models; He 2019 swimmer | Very high | Avoid broad self-oscillating hydrogel claims; say candidate transport-mediated relaxation oscillator. |
| The mechanism is not BZ-like. | BZ gels, BZ active hydrogels, BZ droplets | Medium | Distinguish absence of intrinsic chemical clock and prove oscillator disappears when transport degradation or collapse gating is removed. |
| The mechanism is not just a photothermal delayed oscillator. | Zhang/Ikkala 2022; He photothermal/soft robotics work | High | Emphasize reaction-generated heat and reactant-accessibility/transport shutdown rather than external light attenuation. |
| The mechanism is a spatial PDE/front mechanism. | Jee 2016; Paikar 2022; Duzs 2024; thermal runaway fronts | High | Show sustained closed cycle, recurrent front/barrier motion, and controls distinguishing from one-shot fronts or excitable waves. |
| LCST collapse creates a transport barrier. | Hydrogel diffusion/permeability literature; Yoon 2010; Richbourg/Peppas 2020 | Medium | Define whether barrier means diffusivity reduction, permeability reduction, reaction accessibility reduction, or all three. |
| Homogeneous ODE is insufficient. | Thermochemical/feedback oscillator literature | Medium | Demonstrate model-specific contrast between homogeneous limit and spatial LCST barrier dynamics. |

## Immediate G1 gaps before exit

1. DOI audit all `doi-audit-needed` rows.
2. Replace weak P2 placeholders with exact source-backed entries or remove them.
3. Add BibTeX keys for every retained paper.
4. Freeze a smaller P0/P1 corpus of approximately 20--30 papers for the manuscript introduction and reviewer-risk analysis.
5. For each candidate claim in `docs/validated/claim_evidence.md`, add nearest-prior-art risk but do not mark any claim as validated.
6. Decide whether G1 should continue into a full literature review task or whether the project should open G2 model specification with the current novelty constraints.

## Current G1 status

This file now contains a populated initial literature map and novelty-risk matrix, but G1 is not complete. Completion requires DOI/source audit and user or ChatGPT acceptance of the final retained corpus.
