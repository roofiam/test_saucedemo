lint:
	uv run ruff check .

format:
	uv run ruff check . --fix

test:
	uv run pytest

docker-build:
	docker compose build

docker-test:
	docker compose up

docker-test-rebuild:
	docker compose up --build
