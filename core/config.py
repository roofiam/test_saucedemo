import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    USERNAME = os.getenv("USER_NAME")
    PASSWORD = os.getenv("PASS_WORD")
    BASE_URL = os.getenv("BASE_URL")
