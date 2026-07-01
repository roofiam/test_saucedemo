import platform
from datetime import datetime
from pathlib import Path

import allure
import pytest

from core.config import Config
from core.driver_factory import get_driver
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


@pytest.hookimpl(tryfirst=True)
def pytest_sessionstart(session):
    results_dir = Path("allure-results")
    results_dir.mkdir(exist_ok=True)

    (results_dir / "environment.properties").write_text(
        "\n".join(
            [
                "Project=test_saucedemo",
                f"Environment={Config.ENVIRONMENT}",
                "Browser=Chrome",
                f"Headless={Config.HEADLESS}",
                f"Python={platform.python_version()}",
                f"OS={platform.system()}",
                f"Base URL={Config.BASE_URL}",
            ]
        ),
        encoding="utf-8",
    )


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        item.rep_call = report


def attach_failure_artifacts(driver):
    allure.attach(
        driver.get_screenshot_as_png(),
        name="screenshot",
        attachment_type=allure.attachment_type.PNG,
    )

    allure.attach(
        driver.current_url,
        name="current_url",
        attachment_type=allure.attachment_type.TEXT,
    )

    allure.attach(
        driver.page_source,
        name="page_source",
        attachment_type=allure.attachment_type.HTML,
    )

    try:
        browser_logs = driver.get_log("browser")
    except Exception as error:
        allure.attach(
            str(error),
            name="browser_console_logs_unavailable",
            attachment_type=allure.attachment_type.TEXT,
        )
        return

    if browser_logs:
        formatted_logs = []

        for log in browser_logs:
            timestamp = log.get("timestamp")

            if timestamp:
                timestamp = datetime.fromtimestamp(timestamp / 1000).strftime(
                    "%Y-%m-%d %H:%M:%S.%f"
                )[:-3]
            else:
                timestamp = "Unknown"

            formatted_logs.append(
                "\n".join(
                    [
                        f"Level: {log.get('level', 'UNKNOWN')}",
                        f"Source: {log.get('source', 'UNKNOWN')}",
                        f"Timestamp: {timestamp}",
                        "",
                        log.get("message", ""),
                        "=" * 100,
                    ]
                )
            )

        logs = "\n".join(formatted_logs)

    else:
        logs = "No browser console logs."

    allure.attach(
        logs,
        name="browser_console_logs",
        attachment_type=allure.attachment_type.TEXT,
    )


@pytest.fixture(scope="function")
def driver(request):
    driver = get_driver()

    yield driver

    if getattr(request.node, "rep_call", None) and request.node.rep_call.failed:
        attach_failure_artifacts(driver)

    driver.quit()


@pytest.fixture(scope="function")
def login_page(driver):
    page = LoginPage(driver)
    page.open()
    return page


@pytest.fixture(scope="function")
def products_page(login_page):
    login_page.login(Config.USERNAME, Config.PASSWORD)

    return ProductsPage(login_page.driver)
