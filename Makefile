env:
	uv venv

rmenv:
	rm -rf .venv

install:
	uv sync --no-dev

install-dev:
	uv sync --extra dev

format:
	ruff check --select I --fix .
	ruff format .

.PHONY: env rmenv install install-dev format
.DEFAULT_GOAL := dev
