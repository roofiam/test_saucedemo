from core.config import Config
from locators.login_page import USERNAME_INPUT, PASSWORD_INPUT, LOGIN_BUTTON, ERROR_MESSAGE
from pages.base_page import BasePage


class LoginPage(BasePage):

    def open(self):
        self.driver.get(Config.BASE_URL)

    def enter_username(self, username):
        self.type(USERNAME_INPUT, username)

    def enter_password(self, password):
        self.type(PASSWORD_INPUT, password)

    def click_login(self):
        self.click(LOGIN_BUTTON)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_text(self):
        return self.find(ERROR_MESSAGE).text
