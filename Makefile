SHELL := /bin/bash

.PHONY: venv install freeze run clean clean-pyc help

.venv:
	python3 -m venv .venv
	. .venv/bin/activate; python -m pip install --upgrade pip

venv: .venv ## Create a local virtual environment and upgrade pip

install: .venv requirements.txt ## Install dependencies from requirements.txt
	.venv/bin/pip install -r requirements.txt

freeze: .venv ## Freeze current environment to requirements.txt
	.venv/bin/pip freeze > requirements.txt

run: .venv ## Run a script: make run W=week1-assignment S=main.py
	@if [ -z "$(W)" ] || [ -z "$(S)" ]; then \
	  echo "Usage: make run W=week1-assignment S=script.py"; \
	  exit 1; \
	fi
	.venv/bin/python ai-engineer-assignment/$(W)/$(S)

clean: ## Remove Python caches
	find . -name '__pycache__' -type d -prune -exec rm -rf {} + -o -name '*.pyc' -delete

clean-pyc: ## Strict purge of all pycache & compiled Python artifacts
	find . -type d -name '__pycache__' -prune -exec rm -rf {} +
	find . -name '*.py[co]' -delete

help: ## Show this help
	@echo "Targets: venv, install, freeze, run, clean, clean-pyc"
	@echo "Examples:"
	@echo "  make venv"
	@echo "  make install"
	@echo "  make run W=week1-assignment S=main.py"
	@echo "  make clean-pyc"
