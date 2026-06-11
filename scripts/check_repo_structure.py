from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "AGENTS.md",
    "Makefile",
    "pyproject.toml",
    "docs/00_idea_log.md",
    "docs/project_state.md",
    "docs/workflow_eval.md",
    "docs/01_project_brief.md",
    "docs/02_open_questions.md",
    "docs/03_hypotheses.md",
    "docs/04_literature_map.md",
    "docs/05_novelty_framing.md",
    "docs/06_prior_art_risk_matrix.md",
    "docs/07_g1_frozen_corpus.md",
    "docs/dead_ends.md",
    "docs/stages/stage_index.md",
    "docs/stages/02_model/gate.md",
    "docs/stages/06_figures/gate.md",
    "docs/notes/README.md",
    "docs/notes/PHYSICS-NOTE-TEMPLATE.md",
    "docs/claims/README.md",
    "docs/claims/candidate_claim_evidence.md",
    "docs/model_candidates/README.md",
    "docs/model_candidates/model_A_initial_lcst_transport_barrier.md",
    "docs/derivations/README.md",
    "docs/derivations/initial_model_derivation.tex",
    "docs/validated/README.md",
    "docs/validated/model_spec.md",
    "docs/validated/claim_evidence.md",
    "docs/tasks/README.md",
    "docs/tasks/TASK-TEMPLATE.md",
    "docs/tasks/exploration/EXP-001-ingest-initial-model.md",
    "docs/tasks/exploration/EXP-002-sanity-check-candidate-model.md",
    "docs/tasks/verification/README.md",
    "docs/tasks/production/README.md",
    "docs/tasks/production/TASK-enter-paper-results-production.md",
    "docs/reports/README.md",
    "docs/reports/CODEX-REPORT-TEMPLATE.md",
    "docs/reports/exploration/README.md",
    "docs/reports/verification/README.md",
    "docs/reports/production/README.md",
    "docs/reports/production/CODEX-REPORT-enter-paper-results-production.md",
    "docs/decisions/README.md",
    "docs/decisions/ADR-000-template.md",
    "docs/decisions/ADR-001-physics-first-workflow.md",
    "docs/manuscript/figure_blueprint.md",
    "docs/manuscript/paper_results_figure_plan.md",
    "docs/manuscript/manuscript_blueprint.md",
    "docs/manuscript/revision_checklist.md",
    "src/hydrogel_oscillation/__init__.py",
    "tests/test_repo_structure.py",
    "scripts/check_repo_structure.py",
    "scripts/build_derivations.py",
    "configs/README.md",
    "configs/default.yaml",
    "data/README.md",
    "results/README.md",
    "paper/README.md",
    "paper/solver/__init__.py",
    "paper/solver/official_paper_solver.py",
    "paper/solver/run_figure_smoke_checks.py",
    "paper/solver/canonical_cpu/README.md",
    "paper/solver/canonical_cpu/solver.py",
    "paper/main.tex",
    "paper/supplement.tex",
    "paper/refs.bib",
]


def read_text(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def check_required_files() -> list[str]:
    return [path for path in REQUIRED_FILES if not (ROOT / path).exists()]


def check_content_invariants() -> list[str]:
    errors: list[str] = []

    project_state = read_text("docs/project_state.md")
    if "Stage: Paper Results Production" not in project_state:
        errors.append("docs/project_state.md must record the active stage as Paper Results Production.")
    if "Internal anchor: `G6_figures`" not in project_state:
        errors.append("docs/project_state.md must retain G6_figures as an internal anchor.")
    if "No model or claim has been promoted to `docs/validated/`" not in project_state:
        errors.append("docs/project_state.md must record that no model or claim is validated.")
    if "paper/figures/" not in project_state:
        errors.append("docs/project_state.md must record paper/figures as the active result source set.")

    for path in ["README.md", "AGENTS.md"]:
        text = read_text(path)
        if "Paper Results Production" not in text:
            errors.append(f"{path} must record Paper Results Production as the active stage.")
        if "Formality only at state transitions" not in text:
            errors.append(f"{path} must include the workflow principle: Formality only at state transitions.")
        if "Physics-first" not in text:
            errors.append(f"{path} must include the workflow principle: Physics-first.")
        if "Concrete task names" not in text and "concrete task names" not in text:
            errors.append(f"{path} must require concrete task names.")
        if "validated" not in text:
            errors.append(f"{path} must retain validation-boundary language.")

    stage_index = read_text("docs/stages/stage_index.md")
    if "Human-readable stage" not in stage_index or "Internal anchor" not in stage_index:
        errors.append("docs/stages/stage_index.md must separate human-readable stage names from internal anchors.")
    if "Paper Results Production / Figure Evidence Package" not in stage_index:
        errors.append("docs/stages/stage_index.md must include the active Paper Results Production row.")

    figure_gate = read_text("docs/stages/06_figures/gate.md")
    if "active" not in figure_gate:
        errors.append("docs/stages/06_figures/gate.md must mark the figure gate active for production.")
    if "source mapping" not in figure_gate and "source-mapped" not in figure_gate:
        errors.append("docs/stages/06_figures/gate.md must require source mapping.")

    figure_blueprint = read_text("docs/manuscript/figure_blueprint.md")
    if "Required New Figure A: Mechanism schematic" not in figure_blueprint:
        errors.append("docs/manuscript/figure_blueprint.md must list the mechanism schematic as a required new figure.")

    figure_plan = read_text("docs/manuscript/paper_results_figure_plan.md")
    if "paper/figures/fig01/" not in figure_plan or "paper/figures/fig03/" not in figure_plan:
        errors.append("docs/manuscript/paper_results_figure_plan.md must map existing paper figure assets.")

    task_template = read_text("docs/tasks/TASK-TEMPLATE.md")
    if "Concrete task name" not in task_template:
        errors.append("docs/tasks/TASK-TEMPLATE.md must require a concrete task name.")
    if "PHYSICS-NOTE-TEMPLATE" not in task_template:
        errors.append("docs/tasks/TASK-TEMPLATE.md must point non-state-changing work to the physics-note template.")

    validated_model = read_text("docs/validated/model_spec.md")
    if "not yet validated" not in validated_model:
        errors.append("docs/validated/model_spec.md must still state that the model is not yet validated.")

    validated_claims = read_text("docs/validated/claim_evidence.md")
    if "Status: no validated claim evidence" not in validated_claims:
        errors.append("docs/validated/claim_evidence.md must not contain candidate claim evidence as validated content.")

    candidate_claims = read_text("docs/claims/candidate_claim_evidence.md")
    if "Status: candidate; not validated" not in candidate_claims:
        errors.append("docs/claims/candidate_claim_evidence.md must mark claims as candidate and unvalidated.")

    report = read_text("docs/reports/production/CODEX-REPORT-enter-paper-results-production.md")
    if "No model or claim was promoted to validated status." not in report:
        errors.append("The production transition report must retain the required validation statement.")

    return errors


def main() -> int:
    missing = check_required_files()
    errors = check_content_invariants()

    if missing:
        print("Missing required scaffold files:")
        for path in missing:
            print(f"- {path}")

    if errors:
        print("Repository structure/content invariant errors:")
        for error in errors:
            print(f"- {error}")

    if missing or errors:
        return 1

    print("Repository scaffold and workflow structure check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
