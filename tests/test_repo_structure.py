from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


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


def test_agents_scientific_guardrail():
    agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    assert "Do not invent equations" in agents


def test_validated_model_not_yet_validated():
    model_spec = (ROOT / "docs/validated/model_spec.md").read_text(encoding="utf-8")
    assert "not yet validated" in model_spec


def test_project_state_records_early_exploration_stage():
    project_state = (ROOT / "docs/project_state.md").read_text(encoding="utf-8")
    assert "Stage: Idea / Early Exploration" in project_state
