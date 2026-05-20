import time

import pytest

from core.config import Config
from pages.login_page import LoginPage


class TestLogin:
    def test_login(self, driver):
        page = LoginPage(driver)

        page.open()
        page.login(Config.USERNAME, Config.PASSWORD)

    @pytest.mark.parametrize(
        "username,password,case_id",
        [
            (Config.USERNAME, "random", "wrong_password"),
            (Config.USERNAME, "123456", "numeric_password"),
            (Config.USERNAME, "", "empty_password"),
            ("wrong_user", Config.PASSWORD, "wrong_username"),
        ],
    )
    def test_wrong_username_or_password(self, driver, username, password, case_id):
        page = LoginPage(driver)

        page.open()
        page.login(Config.USERNAME, "random")
        assert "Username and password do not match any user in this service" in page.get_error_text()
        time.sleep(10)