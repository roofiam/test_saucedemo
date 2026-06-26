import platform
from pathlib import Path

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
                f"Browser={Config.BROWSER}",
                f"Headless={Config.HEADLESS}",
                f"Python={platform.python_version()}",
                f"OS={platform.system()}",
                f"Base URL={Config.BASE_URL}",
            ]
        ),
        encoding="utf-8",
    )


@pytest.fixture(scope="function")
def driver():
    driver = get_driver()
    yield driver
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
