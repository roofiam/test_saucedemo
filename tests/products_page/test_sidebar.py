import allure


@allure.feature("Sidebar")
class TestSidebar:
    @allure.story("Sidebar menu")
    @allure.title("Sidebar contains expected menu items")
    def test_sidebar_contains_expected_items(self, products_page):
        products_page.open_sidebar()

        assert products_page.is_sidebar_displayed()

        assert products_page.get_sidebar_items() == [
            "All Items",
            "About",
            "Logout",
            "Reset App State",
        ]

        products_page.close_sidebar()

        assert products_page.wait_sidebar_closed()

    @allure.story("Navigation")
    @allure.title("All Items link opens products page")
    def test_sidebar_all_items_link_opens_products_page(self, products_page):
        products_page.open_sidebar()

        products_page.click_all_items_sidebar_link()

        assert products_page.is_opened()

    @allure.story("Navigation")
    @allure.title("About link opens Sauce Labs website")
    def test_sidebar_about_link_opens_sauce_labs_site(self, products_page):
        products_page.open_sidebar()

        products_page.click_about_sidebar_link()

        assert "saucelabs.com" in products_page.get_current_url()

    @allure.story("Navigation")
    @allure.title("Logout link opens login page")
    def test_sidebar_logout_link_opens_login_page(self, products_page):
        products_page.open_sidebar()

        products_page.click_logout_sidebar_link()

        assert "saucedemo.com" in products_page.get_current_url()
        assert "inventory" not in products_page.get_current_url()

    @allure.story("Application state")
    @allure.title("Reset App State removes cart badge")
    def test_sidebar_reset_app_state_removes_cart_badge(self, products_page):
        products_page.add_first_product_to_cart()

        assert products_page.get_cart_badge_text() == "1"

        products_page.open_sidebar()
        products_page.click_reset_app_state_link()

        assert products_page.wait_cart_badge_disappeared()
