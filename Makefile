PYTHON ?= python3
PYTEST ?= $(PYTHON) -m pytest

.PHONY: quickcheck test derivations clean

quickcheck:
	$(PYTHON) scripts/check_repo_structure.py
	$(PYTEST) -q

test:
	$(PYTEST) -q

derivations:
	$(PYTHON) scripts/build_derivations.py

clean:
	rm -rf .pytest_cache
	find . -type d -name "__pycache__" -prune -exec rm -rf {} +
