PYTHON ?= python3
.PHONY: run test format-check
run:
	$(PYTHON) scripts/run_demo.py

test:
	cd projects/mobility-quality && $(PYTHON) -m unittest -v
	cd evidence/data-quality && $(PYTHON) -m unittest -v

format-check:
	$(PYTHON) -m black --check projects/mobility-quality/*.py scripts/*.py
