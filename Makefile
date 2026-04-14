.PHONY: install-dev test lint format hooks run check

install-dev:
	python -m pip install --upgrade pip
	pip install -e ".[dev]"

test:
	pytest

lint:
	ruff check src tests

format:
	ruff check --fix src tests
	ruff format src tests

hooks:
	pre-commit install
	pre-commit run --all-files

run:
	python -m uvicorn --app-dir src app.main:app --reload

check:
	ruff check src tests
	ruff format --check src tests
	pytest
