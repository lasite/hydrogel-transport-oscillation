# Stage Index

Use human-readable stage names in tasks, reports, and assistant exchanges. Internal anchors such as `G2` are retained only for ordering and traceability.

| Human-readable stage | Internal anchor | Status | Main output | Gate file | Main blocker | Next task |
| -------------------- | --------------- | ------ | ----------- | --------- | ------------ | --------- |
| Research Idea Brief | `G0_idea_brief` | complete | Project brief, central hypothesis, candidate claims, and open uncertainty list | `docs/stages/00_idea/gate.md` | None | Completed after user acceptance |
| Literature / Novelty Mapping | `G1_literature` | complete | Literature map, novelty framing, prior-art risk matrix, and frozen Model Specification corpus | `docs/stages/01_literature/gate.md` | None for Model Specification entry; DOI/BibTeX cleanup remains before manuscript drafting | Completed after user acceptance |
| Model Specification | `G2_model` | active; reset for fresh review | Fresh Model A review, rebuilt blocker list, variable definitions, limiting cases, boundary-condition audit, material-function audit, and minimum observables | `docs/stages/02_model/gate.md` | Model A has not been re-reviewed under the physics-first workflow | Re-review Candidate Model A from Scratch |
| Mechanism Analysis | `G3_analysis` | blocked | Homogeneous ODE limit analysis, stability interpretation, limiting cases, and barrier diagnostics | `docs/stages/03_analysis/gate.md` | Model Specification gate is not complete | Start only after Model Specification gate passes |
| Minimal Numerical Verification | `G4_numerics` | blocked | Minimal verified numerical experiment design | `docs/stages/04_numerics/gate.md` | No sanity-checked model and no finalized observables | Start only after model and analysis gates justify numerics |
| Parameter-Scan Evidence | `G5_parameter_scan` | blocked | Reproducible scan plan and phase-diagram criteria | `docs/stages/05_parameter_scan/gate.md` | No verified numerical baseline | Complete minimal numerical verification first |
| Figure Evidence Package | `G6_figures` | blocked | Evidence-backed figure set | `docs/stages/06_figures/gate.md` | No validated results or reproducible outputs | Wait for verified results and figure blueprints |
| Manuscript Writing | `G7_writing` | blocked | Manuscript draft with evidence-bounded claims | `docs/stages/07_writing/gate.md` | Literature and claim-evidence matrices are not populated with validated evidence | Populate claim-evidence matrix only after model and verification gates |
| Internal Review | `G8_review` | blocked | Internal review responses and revision plan | `docs/stages/08_review/gate.md` | No manuscript draft exists | Start only after writing gate passes |
| Submission Package | `G9_submission` | blocked | Submission-ready manuscript package | `docs/stages/09_submission/gate.md` | No reviewed manuscript or final checks | Start only after review gate passes |
