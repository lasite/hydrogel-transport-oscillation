# Stage Index

| Stage | Status | Main output | Gate file | Main blocker | Next task |
| ----- | ------ | ----------- | --------- | ------------ | --------- |
| `G0_idea_brief` | active | Project brief, central hypothesis, candidate claims, and open uncertainty list | `docs/stages/00_idea/gate.md` | Hypothesis and candidate claims need user/ChatGPT acceptance | Review G0 outputs and mark G0 complete if accepted |
| `G1_literature` | not_started | Populated novelty matrix and gap analysis | `docs/stages/01_literature/gate.md` | `docs/04_literature_map.md` is a template only | Start only after G0 exits or as an explicitly scoped literature task |
| `G2_model` | paused | Candidate Model A summary and organized derivation | `docs/stages/02_model/gate.md` | G0 idea brief is still active | Do not run model review until G0 exits and G2 is explicitly opened |
| `G3_analysis` | blocked | Homogeneous ODE limit, stability interpretation, limiting cases, and barrier diagnostics | `docs/stages/03_analysis/gate.md` | Model gate is not active | Start only after G2 model gate passes |
| `G4_numerics` | blocked | Minimal verified numerical experiment design | `docs/stages/04_numerics/gate.md` | No sanity-checked model and no finalized observables | Start only after model and analysis gates justify numerics |
| `G5_parameter_scan` | blocked | Reproducible scan plan and phase-diagram criteria | `docs/stages/05_parameter_scan/gate.md` | No verified numerical baseline | Complete minimal numerical verification first |
| `G6_figures` | blocked | Evidence-backed figure set | `docs/stages/06_figures/gate.md` | No validated results or reproducible outputs | Wait for verified results and figure blueprints |
| `G7_writing` | blocked | Manuscript draft with evidence-bounded claims | `docs/stages/07_writing/gate.md` | Literature and claim-evidence matrices are not populated | Populate literature and claim-evidence matrices |
| `G8_review` | blocked | Internal review responses and revision plan | `docs/stages/08_review/gate.md` | No manuscript draft exists | Start only after writing gate passes |
| `G9_submission` | blocked | Submission-ready manuscript package | `docs/stages/09_submission/gate.md` | No reviewed manuscript or final checks | Start only after review gate passes |
