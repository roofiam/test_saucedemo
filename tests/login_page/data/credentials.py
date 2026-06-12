from core.config import Config


class Credentials:

    INVALID_CREDENTIALS = [
        ("wrong_user", Config.PASSWORD),
        (Config.USERNAME, "456"),
    ]

    VALIDATION_ERRORS = [
        ("", "any_password", "Username is required"),
        ("any_user", "", "Password is required"),
        ("locked_out_user", Config.PASSWORD, "locked out"),
    ]
