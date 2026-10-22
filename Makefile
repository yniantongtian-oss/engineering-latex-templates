PYTHON ?= python3

.PHONY: all lint test check clean

all:
	@set -e; for dir in templates/*/; do \
		if [ -f "$$dir/Makefile" ]; then $(MAKE) -C "$$dir"; fi; \
	done

lint:
	$(PYTHON) scripts/lint_tex.py

test:
	$(PYTHON) -m unittest discover -s scripts -p 'test_*.py'

check: lint test all
	$(PYTHON) scripts/check_latex_log.py templates/*/main.log

clean:
	@for dir in templates/*/; do \
		if [ -f "$$dir/Makefile" ]; then $(MAKE) -C "$$dir" clean; fi; \
	done
