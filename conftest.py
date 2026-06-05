import pytest

from core.config import Config
from core.driver_factory import get_driver
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


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
