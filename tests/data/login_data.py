class LoginData:

    INVALID_CREDENTIALS = [
        ("wrong_user", "wrong_pass"),
        ("123", "456"),
    ]

    EMPTY_USERNAME = [
        ("", "any_password"),
    ]

    EMPTY_PASSWORD = [
        ("any_user", ""),
    ]
