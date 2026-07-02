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

clean_allure:
	rm -rf allure-results allure-report

test_report: clean_allure
	uv run pytest --alluredir=allure-results

allure_report:
	allure serve allure-results

docker_test_report: clean_allure
	HOST_UID=$$(id -u) HOST_GID=$$(id -g) docker compose run --rm tests uv run pytest --alluredir=allure-results

docker_rebuild_report:
	HOST_UID=$$(id -u) HOST_GID=$$(id -g) docker compose build --no-cache
	HOST_UID=$$(id -u) HOST_GID=$$(id -g) docker compose run --rm tests uv run pytest --alluredir=allure-results
