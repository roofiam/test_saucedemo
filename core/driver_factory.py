from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from core.config import Config


def get_driver():
    options = webdriver.ChromeOptions()

    if Config.HEADLESS:
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
    else:
        options.add_argument("--start-maximized")

    options.add_argument("--disable-features=PasswordLeakDetection")
    options.add_argument("--disable-features=PasswordManagerOnboarding")

    options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False,
        },
    )

    if Config.CHROME_BIN:
        options.binary_location = Config.CHROME_BIN

    if Config.CHROMEDRIVER_PATH:
        service = Service(Config.CHROMEDRIVER_PATH)
        return webdriver.Chrome(service=service, options=options)

    return webdriver.Chrome(options=options)
