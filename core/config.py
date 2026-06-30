import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    USERNAME = os.getenv("USER_NAME")
    PASSWORD = os.getenv("PASS_WORD")
    BASE_URL = os.getenv("BASE_URL")

    BROWSER = os.getenv("BROWSER", "Chrome")
    ENVIRONMENT = os.getenv("ENVIRONMENT", "local")
    HEADLESS = os.getenv("HEADLESS", "False").lower() == "true"
    BROWSER = os.getenv("BROWSER", "Chrome")
    ENVIRONMENT = os.getenv("ENVIRONMENT", "local")

    CHROME_BIN = os.getenv("CHROME_BIN")
    CHROMEDRIVER_PATH = os.getenv("CHROMEDRIVER_PATH")
