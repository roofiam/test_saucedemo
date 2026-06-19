sync:
	uv sync

lint_check:
	uv run ruff check .

lint_fix:
	uv run ruff check . --fix

format:
	uv run ruff format .

test:
	uv run pytest

all:
	uv run ruff check .
	uv run pytest

docker_build:
	docker compose build

docker_test:
	docker compose up

docker_test_rebuild:
	docker compose up --build

docker_down:
	docker compose down
