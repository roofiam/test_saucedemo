import pytest
from core.driver_factory import get_driver


@pytest.fixture(scope="function")
def driver():
    driver = get_driver()
    yield driver
    driver.quit()
