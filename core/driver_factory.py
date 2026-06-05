from selenium import webdriver


def get_driver():
    options = webdriver.ChromeOptions()

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

    return webdriver.Chrome(options=options)
