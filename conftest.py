import pytest
from core.driver_factory import get_driver
from pages.login_page import LoginPage


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
