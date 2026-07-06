from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from core.config import Config


def get_driver():
    options = webdriver.ChromeOptions()

    options.set_capability(
        "goog:loggingPrefs",
        {
            "browser": "ALL",
        },
    )

    if Config.HEADLESS:
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--user-data-dir=/tmp/chrome-user-data")
        options.add_argument("--data-path=/tmp/chrome-data")
        options.add_argument("--disk-cache-dir=/tmp/chrome-cache")
        options.add_argument("--disable-crash-reporter")
        options.add_argument("--disable-crashpad")
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
        Path("allure-results").mkdir(exist_ok=True)

        service = Service(
            executable_path=Config.CHROMEDRIVER_PATH,
            service_args=["--verbose"],
            log_output="allure-results/chromedriver.log",
        )

        return webdriver.Chrome(service=service, options=options)

    return webdriver.Chrome(options=options)
