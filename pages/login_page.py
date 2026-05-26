from locators.login_page import *
from core.config import Config
from pages.base_page import BasePage


class LoginPage(BasePage):

    def open(self):
        self.driver.get(Config.BASE_URL)

    def login(self, username, password):
        self.type(USERNAME_INPUT, username)
        self.type(PASSWORD_INPUT, password)
        self.click(LOGIN_BUTTON)

    def logout(self):
        self.click(MENU_BUTTON)
        self.click(LOGOUT_BUTTON)

    def is_logged_in(self):
        return "inventory" in self.driver.current_url

    def is_login_page(self):
        return self.is_displayed(LOGIN_BUTTON)

    def is_error_displayed(self):
        return len(self.find_all(ERROR_MESSAGE)) > 0

    def get_error_text(self):
        return self.find_visible(ERROR_MESSAGE).text

    def close_error(self):
        self.click(ERROR_CLOSE_BUTTON)

    def username_has_error_state(self):
        return "error" in self.find(USERNAME_INPUT).get_attribute("class")

    def password_has_error_state(self):
        return "error" in self.find(PASSWORD_INPUT).get_attribute("class")

    def get_password_input_type(self):
        return self.find(PASSWORD_INPUT).get_attribute("type")
