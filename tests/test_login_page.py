import time

import pytest
from core.config import Config
from tests.data.login_data import LoginData


class TestLoginPage:


    def test_successful_login(self, login_page):
        login_page.login(Config.USERNAME, Config.PASSWORD)

        assert "inventory" in login_page.driver.current_url


    @pytest.mark.parametrize(
        "username,password",
        LoginData.INVALID_CREDENTIALS,
        ids=["wrong_user", "invalid_user"]
    )
    def test_invalid_login(self, login_page, username, password):
        login_page.login(username, password)

        assert login_page.get_error_text() != ""
        assert "inventory" not in login_page.driver.current_url

    def test_empty_username(self, login_page):
        username, password = LoginData.EMPTY_USERNAME[0]

        login_page.login(username, password)

        assert "Username is required" in login_page.get_error_text()


    def test_empty_password(self, login_page):
        username, password = LoginData.EMPTY_PASSWORD[0]

        login_page.login(username, password)

        assert "Password is required" in login_page.get_error_text()


    def test_error_message_can_be_closed(self, login_page):
        login_page.login("wrong_user", "wrong_pass")

        assert login_page.is_error_displayed()

        login_page.close_error()

        assert not login_page.is_error_displayed()


    def test_input_error_state(self, login_page):
        login_page.login("wrong_user", "wrong_pass")

        assert login_page.username_has_error_state()
        assert login_page.password_has_error_state()
