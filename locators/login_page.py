from selenium.webdriver.common.by import By

USERNAME_INPUT = (By.ID, "user-name")
PASSWORD_INPUT = (By.ID, "password")
LOGIN_BUTTON = (By.ID, "login-button")

ERROR_MESSAGE = (By.XPATH, "//h3[@data-test='error']")
ERROR_CLOSE_BUTTON = (By.CSS_SELECTOR, "[data-test='error-button']")
