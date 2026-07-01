sync:
	uv sync

lint_check:
	uv run ruff check .

lint_fix:
	uv run ruff check . --fix

lint_format:
	uv run ruff format .

test:
	uv run pytest

test_report:
	uv run pytest --alluredir=allure-results

allure_report:
	allure serve allure-results

docker_test_report:
	docker compose run --rm tests uv run pytest --alluredir=allure-results

docker_rebuild_test:
	docker compose build --no-cache
	docker compose run --rm tests uv run pytest
