from core.config import Config


class LoginData:

    INVALID_CREDENTIALS = [
        ("wrong_user", Config.PASSWORD),
        (Config.USERNAME, "456"),
    ]

    EMPTY_USERNAME = [
        ("", "any_password"),
    ]

    EMPTY_PASSWORD = [
        ("any_user", ""),
    ]

    LOCKED_USER = [
        ("locked_out_user", "secret_sauce"),
    ]
