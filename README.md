# SauceDemo UI Automation Framework

A UI automation framework for testing [SauceDemo](https://www.saucedemo.com/) built with Python, Selenium and Pytest.

The project demonstrates a production-like approach to building a maintainable UI automation framework.

## Tech Stack

- Python 3.12
- Selenium
- Pytest
- Page Object Model
- Docker
- Allure
- GitHub Actions
- Ruff
- uv
- Telegram Bot API

## Getting Started

Create a local configuration from the example:

```bash
cp .env.example .env
```

The `.env.example` file contains the public test credentials provided by SauceDemo.

Install dependencies:

```bash
make sync
```

Run tests locally:

```bash
make test
```

Generate Allure results:

```bash
make test_report
```

Open the Allure report:

```bash
make allure_report
```

Run tests in Docker with Allure results:

```bash
make docker_test_report
```

## CI

Every pull request and every push to `main` triggers the CI pipeline.

The workflow validates code style with Ruff, runs UI tests in Docker, uploads Allure artifacts and sends Telegram notifications with the build status.


## Failure Diagnostics

For failed UI tests, the framework automatically attaches:

- screenshot;
- current URL;
- HTML page source;
- browser console logs.

These artifacts are included in Allure results and help investigate failures without rerunning tests locally.
