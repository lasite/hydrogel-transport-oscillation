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
    "docs/01_project_brief.md",
    "docs/02_open_questions.md",
    "docs/03_hypotheses.md",
    "docs/04_literature_map.md",
    "docs/dead_ends.md",
    "docs/model_candidates/README.md",
    "docs/model_candidates/model_A_initial_lcst_transport_barrier.md",
    "docs/derivations/README.md",
    "docs/derivations/initial_model_derivation.tex",
    "docs/validated/README.md",
    "docs/validated/model_spec.md",
    "docs/validated/claim_evidence.md",
    "docs/tasks/README.md",
    "docs/tasks/exploration/EXP-001-ingest-initial-model.md",
    "docs/tasks/exploration/EXP-002-sanity-check-candidate-model.md",
    "docs/tasks/verification/README.md",
    "docs/tasks/production/README.md",
    "docs/reports/README.md",
    "docs/reports/exploration/README.md",
    "docs/reports/verification/README.md",
    "docs/reports/production/README.md",
    "docs/decisions/README.md",
    "docs/decisions/ADR-000-template.md",
    "docs/manuscript/figure_blueprint.md",
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
    "paper/main.tex",
    "paper/supplement.tex",
    "paper/refs.bib",
]


def main() -> int:
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).exists()]
    if missing:
        print("Missing required scaffold files:")
        for path in missing:
            print(f"- {path}")
        return 1

    print("Repository scaffold check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
