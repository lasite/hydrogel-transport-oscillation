PYTHON ?= python3
PYTEST ?= $(PYTHON) -m pytest

.PHONY: install env-check quickcheck test derivations clean

install:
	$(PYTHON) -m pip install -e .

env-check:
	$(PYTHON) -c "import numpy, scipy, matplotlib, pytest; print('Environment check passed.')"

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
