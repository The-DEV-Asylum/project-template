.PHONY: install test lint run build docker-run clean

install:
	python -m pip install -e '.[dev]'

test:
	pytest

lint:
	ruff check .

run:
	python -m dev_asylum_project

build:
	python -m build

docker-run:
	docker compose up --build --abort-on-container-exit

clean:
	rm -rf .pytest_cache .ruff_cache .venv build dist *.egg-info src/*.egg-info
