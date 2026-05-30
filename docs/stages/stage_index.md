# Stage Index

| Stage | Status | Main output | Gate file | Main blocker | Next task |
| ----- | ------ | ----------- | --------- | ------------ | --------- |
| `G0_idea_brief` | complete | Project brief, central hypothesis, candidate claims, and open uncertainty list | `docs/stages/00_idea/gate.md` | None | Completed after user acceptance |
| `G1_literature` | complete | Literature map, novelty framing, prior-art risk matrix, and frozen G2 corpus | `docs/stages/01_literature/gate.md` | None for G2 entry; DOI/BibTeX cleanup remains before manuscript drafting | Completed after user acceptance |
| `G2_model` | active | Candidate Model A specification, sanity-check report, variable definitions, limiting cases, boundary-condition audit, and G1-risk-aligned mechanism tests | `docs/stages/02_model/gate.md` | Model A has not yet been sanity checked against G1 novelty-risk constraints | Create and run G2 model-specification / sanity-check task |
| `G3_analysis` | blocked | Homogeneous ODE limit, stability interpretation, limiting cases, and barrier diagnostics | `docs/stages/03_analysis/gate.md` | Model gate is not complete | Start only after G2 model gate passes |
| `G4_numerics` | blocked | Minimal verified numerical experiment design | `docs/stages/04_numerics/gate.md` | No sanity-checked model and no finalized observables | Start only after model and analysis gates justify numerics |
| `G5_parameter_scan` | blocked | Reproducible scan plan and phase-diagram criteria | `docs/stages/05_parameter_scan/gate.md` | No verified numerical baseline | Complete minimal numerical verification first |
| `G6_figures` | blocked | Evidence-backed figure set | `docs/stages/06_figures/gate.md` | No validated results or reproducible outputs | Wait for verified results and figure blueprints |
| `G7_writing` | blocked | Manuscript draft with evidence-bounded claims | `docs/stages/07_writing/gate.md` | Literature and claim-evidence matrices are not populated with validated evidence | Populate claim-evidence matrix only after model and verification gates |
| `G8_review` | blocked | Internal review responses and revision plan | `docs/stages/08_review/gate.md` | No manuscript draft exists | Start only after writing gate passes |
| `G9_submission` | blocked | Submission-ready manuscript package | `docs/stages/09_submission/gate.md` | No reviewed manuscript or final checks | Start only after review gate passes |
