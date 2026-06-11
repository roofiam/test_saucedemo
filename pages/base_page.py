from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def find_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def find_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    def click(self, locator, timeout=10):
        self.find_clickable(locator, timeout).click()

    def type(self, locator, text, timeout=10):
        el = self.find_visible(locator)
        el.clear()
        el.send_keys(text)

    def is_displayed(self, locator, timeout=10):
        try:
            self.find_visible(locator, timeout)
            return True
        except TimeoutException:
            return False

    def wait_invisible(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    def get_windows_count(self):
        return len(self.driver.window_handles)

    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def close_current_window(self):
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
