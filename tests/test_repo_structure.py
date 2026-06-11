from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read_text(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_core_docs_exist():
    assert (ROOT / "docs/00_idea_log.md").exists()
    assert (ROOT / "docs/01_project_brief.md").exists()
    assert (ROOT / "docs/03_hypotheses.md").exists()
    assert (ROOT / "docs/project_state.md").exists()


def test_model_candidate_and_derivation_exist():
    assert (
        ROOT / "docs/model_candidates/model_A_initial_lcst_transport_barrier.md"
    ).exists()
    assert (ROOT / "docs/derivations/initial_model_derivation.tex").exists()


def test_task_files_exist():
    assert (
        ROOT / "docs/tasks/exploration/EXP-001-ingest-initial-model.md"
    ).exists()
    assert (ROOT / "docs/tasks/production/TASK-enter-paper-results-production.md").exists()
    assert (ROOT / "docs/tasks/TASK-TEMPLATE.md").exists()


def test_agents_scientific_guardrail():
    agents = read_text("AGENTS.md")
    assert "Do not silently promote newly proposed equations" in agents
    assert "No model or claim was promoted to validated status" in agents


def test_validated_model_not_yet_validated():
    model_spec = read_text("docs/validated/model_spec.md")
    assert "not yet validated" in model_spec


def test_project_state_records_paper_results_production_stage():
    project_state = read_text("docs/project_state.md")
    assert "Stage: Paper Results Production" in project_state
    assert "Internal anchor: `G6_figures`" in project_state
    assert "paper/figures/" in project_state
    assert "No model or claim has been promoted to `docs/validated/`" in project_state


def test_workflow_principles_are_recorded():
    readme = read_text("README.md")
    agents = read_text("AGENTS.md")
    assert "Formality only at state transitions" in readme
    assert "Physics-first everywhere else" in readme
    assert "Paper Results Production" in readme
    assert "Formality only at state transitions" in agents
    assert "Physics-first everywhere else" in agents
    assert "Paper Results Production" in agents


def test_stage_index_records_active_figure_production_stage():
    stage_index = read_text("docs/stages/stage_index.md")
    assert "Human-readable stage" in stage_index
    assert "Internal anchor" in stage_index
    assert "Paper Results Production / Figure Evidence Package" in stage_index
    assert "G6_figures" in stage_index
    assert "active" in stage_index


def test_figure_gate_is_active_but_bounded():
    gate = read_text("docs/stages/06_figures/gate.md")
    assert "active" in gate
    assert "source mapping" in gate or "source-mapped" in gate
    assert "No model or claim has been promoted to validated status" in gate


def test_figure_blueprint_and_plan_record_missing_images():
    blueprint = read_text("docs/manuscript/figure_blueprint.md")
    plan = read_text("docs/manuscript/paper_results_figure_plan.md")
    assert "Required New Figure A: Mechanism schematic" in blueprint
    assert "Required New Figure C: Front and barrier observable definitions" in blueprint
    assert "paper/figures/fig01/" in plan
    assert "paper/figures/fig02/" in plan
    assert "paper/figures/fig03/" in plan
    assert "paper/figures/fig09/" in plan
    assert "control comparison" in plan.lower()


def test_candidate_claims_are_not_validated_claims():
    validated_claims = read_text("docs/validated/claim_evidence.md")
    candidate_claims = read_text("docs/claims/candidate_claim_evidence.md")
    assert "Status: no validated claim evidence" in validated_claims
    assert "Status: candidate; not validated" in candidate_claims


def test_physics_note_template_exists():
    note_template = ROOT / "docs/notes/PHYSICS-NOTE-TEMPLATE.md"
    assert note_template.exists()
    assert "No model or claim is promoted by this note" in note_template.read_text(
        encoding="utf-8"
    )


def test_candidate_canonical_solver_path_is_documented():
    assert (ROOT / "paper/solver/official_paper_solver.py").exists()
    assert (ROOT / "paper/solver/run_figure_smoke_checks.py").exists()
    assert (ROOT / "paper/solver/canonical_cpu/README.md").exists()
    assert (ROOT / "paper/solver/canonical_cpu/solver.py").exists()
    project_state = read_text("docs/project_state.md")
    assert "candidate canonical CPU solver scaffold" in project_state
    assert "official paper-reproduction route" in project_state


def test_production_transition_report_exists_and_preserves_validation_boundary():
    report = read_text("docs/reports/production/CODEX-REPORT-enter-paper-results-production.md")
    assert "Paper Results Production" in report
    assert "No model or claim was promoted to validated status." in report
