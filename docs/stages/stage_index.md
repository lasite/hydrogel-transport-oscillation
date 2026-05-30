# Stage Index

| Stage | Status | Main output | Gate file | Main blocker | Next task |
| ----- | ------ | ----------- | --------- | ------------ | --------- |
| `00_idea` | active | Stable idea log, project brief, central hypothesis, and open uncertainty list | `docs/stages/00_idea/gate.md` | Initial idea still needs sanity-checked model support | Keep project state current while running `EXP-002-sanity-check-candidate-model` |
| `01_literature` | not_started | Populated novelty matrix and gap analysis | `docs/stages/01_literature/gate.md` | `docs/04_literature_map.md` is a template only | Create a literature-map exploration task |
| `02_model` | active | Candidate Model A summary and organized derivation | `docs/stages/02_model/gate.md` | `EXP-002-sanity-check-candidate-model` not completed | Run `EXP-002-sanity-check-candidate-model` |
| `03_analysis` | blocked | Homogeneous ODE limit, stability interpretation, limiting cases, and barrier diagnostics | `docs/stages/03_analysis/gate.md` | Model sanity check and homogeneous ODE limit are incomplete | Derive the homogeneous ODE limit after EXP-002 |
| `04_numerics` | blocked | Minimal verified numerical experiment design | `docs/stages/04_numerics/gate.md` | No sanity-checked model and no finalized observables | Define front/barrier observables before numerical validation |
| `05_parameter_scan` | blocked | Reproducible scan plan and phase-diagram criteria | `docs/stages/05_parameter_scan/gate.md` | No verified numerical baseline | Complete minimal numerical verification first |
| `06_figures` | blocked | Evidence-backed figure set | `docs/stages/06_figures/gate.md` | No validated results or reproducible outputs | Wait for verified results and figure blueprints |
| `07_writing` | blocked | Manuscript draft with evidence-bounded claims | `docs/stages/07_writing/gate.md` | Literature and claim-evidence matrices are not populated | Populate literature and claim-evidence matrices |
| `08_review` | blocked | Internal review responses and revision plan | `docs/stages/08_review/gate.md` | No manuscript draft exists | Start only after writing gate passes |
| `09_submission` | blocked | Submission-ready manuscript package | `docs/stages/09_submission/gate.md` | No reviewed manuscript or final checks | Start only after review gate passes |
