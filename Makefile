env:
	uv venv

rmenv:
	rm -rf .venv

install:
	uv sync --no-dev

install-dev:
	uv sync --extra dev

export:
	uv export --format requirements-txt --no-hashes > .\requirements.txt

format:
	ruff check --select I --fix .
	ruff format .

.PHONY: env rmenv install install-dev export format
.DEFAULT_GOAL := dev
