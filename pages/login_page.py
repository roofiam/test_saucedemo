from locators.login_page import *
from core.config import Config


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(Config.BASE_URL)

    def login(self, username, password):
        self.driver.find_element(*USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*LOGIN_BUTTON).click()

    def get_error_text(self):
        return self.driver.find_element(*ERROR_MESSAGE).text

    def is_error_displayed(self):
        return len(self.driver.find_elements(*ERROR_MESSAGE)) > 0

    def close_error(self):
        self.driver.find_element(*ERROR_CLOSE_BUTTON).click()

    def username_has_error_state(self):
        return "error" in self.driver.find_element(*USERNAME_INPUT).get_attribute("class")

    def password_has_error_state(self):
        return "error" in self.driver.find_element(*PASSWORD_INPUT).get_attribute("class")
