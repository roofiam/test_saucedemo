import pytest

from core.config import Config
from tests.login_page.data.credentials import Credentials


class TestLoginPage:
    def test_successful_login(self, login_page):
        login_page.login(Config.USERNAME, Config.PASSWORD)

        assert login_page.is_logged_in()

    def test_login_and_logout_flow(self, login_page):
        login_page.login(Config.USERNAME, Config.PASSWORD)

        assert login_page.is_logged_in()

        login_page.logout()

        assert login_page.is_login_page()

    @pytest.mark.parametrize("username,password", Credentials.INVALID_CREDENTIALS)
    def test_invalid_login(self, login_page, username, password):
        login_page.login(username, password)

        assert login_page.is_error_displayed()
        assert login_page.is_login_page()

    @pytest.mark.parametrize(
        "username,password,expected_error",
        Credentials.VALIDATION_ERRORS,
    )
    def test_login_validation_error(
        self,
        login_page,
        username,
        password,
        expected_error,
    ):
        login_page.login(username, password)

        assert expected_error.lower() in login_page.get_error_text().lower()

    def test_error_message_can_be_closed(self, login_page):
        login_page.login("wrong_user", "wrong_pass")

        assert login_page.is_error_displayed()

        login_page.close_error()

        assert not login_page.is_error_displayed()

    def test_input_error_state(self, login_page):
        username, password = Credentials.INVALID_CREDENTIALS[0]

        login_page.login(username, password)

        assert login_page.username_has_error_state()
        assert login_page.password_has_error_state()

    def test_error_message_disappears_after_successful_login(self, login_page):
        username, password = Credentials.INVALID_CREDENTIALS[0]

        login_page.login(username, password)

        assert login_page.is_error_displayed()

        login_page.login(Config.USERNAME, Config.PASSWORD)

        assert login_page.is_logged_in()
        assert not login_page.is_error_displayed()

    def test_password_field_is_masked(self, login_page):
        assert login_page.get_password_input_type() == "password"
