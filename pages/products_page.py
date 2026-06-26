import allure
from selenium.webdriver.support.select import Select

from locators.products_page import (
    ABOUT_LINK,
    ADD_TO_CART_BUTTON,
    ALL_ITEMS_LINK,
    CART_BADGE,
    FACEBOOK_LINK,
    LINKEDIN_LINK,
    LOGOUT_LINK,
    MENU_BUTTON,
    PRODUCT_DESCRIPTIONS,
    PRODUCT_IMAGES,
    PRODUCT_ITEMS,
    PRODUCT_NAMES,
    PRODUCT_PRICES,
    PRODUCTS_CONTAINER,
    REMOVE_BUTTON,
    RESET_APP_STATE_LINK,
    SIDEBAR_CLOSE_BUTTON,
    SORT_DROPDOWN,
    TWITTER_LINK,
)
from pages.base_page import BasePage
from pages.product_details_page import ProductDetailsPage


class ProductsPage(BasePage):
    def is_opened(self):
        return self.is_displayed(PRODUCTS_CONTAINER)

    def get_products_count(self):
        return len(self.find_all(PRODUCT_ITEMS))

    def get_product_names(self):
        return [item.text for item in self.find_all(PRODUCT_NAMES)]

    def get_product_prices(self):
        prices = []

        for item in self.find_all(PRODUCT_PRICES):
            prices.append(float(item.text.replace("$", "")))

        return prices

    @allure.step("Add first product to cart")
    def add_first_product_to_cart(self):
        self.click(ADD_TO_CART_BUTTON)

    @allure.step("Remove product from cart")
    def remove_product_from_cart(self):
        self.click(REMOVE_BUTTON)

    def get_cart_badge_text(self):
        return self.find_visible(CART_BADGE).text

    def is_cart_badge_displayed(self):
        return self.is_displayed(CART_BADGE)

    @allure.step("Sort products by name A to Z")
    def sort_by_name_az(self):
        Select(self.find_visible(SORT_DROPDOWN)).select_by_value("az")

    @allure.step("Sort products by name Z to A")
    def sort_by_name_za(self):
        Select(self.find_visible(SORT_DROPDOWN)).select_by_value("za")

    @allure.step("Sort products by price low to high")
    def sort_by_price_low_to_high(self):
        Select(self.find_visible(SORT_DROPDOWN)).select_by_value("lohi")

    @allure.step("Sort products by price high to low")
    def sort_by_price_high_to_low(self):
        Select(self.find_visible(SORT_DROPDOWN)).select_by_value("hilo")

    def wait_cart_badge_disappeared(self):
        return self.wait_invisible(CART_BADGE)

    def get_first_product_name(self):
        return self.find_all(PRODUCT_NAMES)[0].text

    def get_first_product_description(self):
        return self.find_all(PRODUCT_DESCRIPTIONS)[0].text

    def get_first_product_price(self):
        return self.find_all(PRODUCT_PRICES)[0].text

    def get_first_product_image_url(self):
        return self.find_all(PRODUCT_IMAGES)[0].get_attribute("src")

    @allure.step("Open product details")
    def open_first_product(self):
        self.find_all(PRODUCT_NAMES)[0].click()

        return ProductDetailsPage(self.driver)

    def is_add_to_cart_button_displayed(self):
        return self.is_displayed(ADD_TO_CART_BUTTON)

    def is_remove_button_displayed(self):
        return self.is_displayed(REMOVE_BUTTON)

    @allure.step("Open sort dropdown")
    def open_sort_dropdown(self):
        self.click(SORT_DROPDOWN)

    def is_sort_dropdown_expanded(self):
        return False

    @allure.step("Open sidebar")
    def open_sidebar(self):
        self.click(MENU_BUTTON)

    def is_sidebar_displayed(self):
        return self.is_displayed(SIDEBAR_CLOSE_BUTTON)

    @allure.step("Close sidebar")
    def close_sidebar(self):
        self.click(SIDEBAR_CLOSE_BUTTON)

    def wait_sidebar_closed(self):
        return self.wait_invisible(SIDEBAR_CLOSE_BUTTON)

    def get_sidebar_items(self):
        return [
            self.find_visible(ALL_ITEMS_LINK).text,
            self.find_visible(ABOUT_LINK).text,
            self.find_visible(LOGOUT_LINK).text,
            self.find_visible(RESET_APP_STATE_LINK).text,
        ]

    @allure.step("Open Twitter / X link")
    def open_twitter_link(self):
        self.click(TWITTER_LINK)

    @allure.step("Open Facebook link")
    def open_facebook_link(self):
        self.click(FACEBOOK_LINK)

    @allure.step("Open LinkedIn link")
    def open_linkedin_link(self):
        self.click(LINKEDIN_LINK)

    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Open products page from sidebar")
    def click_all_items_sidebar_link(self):
        self.click(ALL_ITEMS_LINK)

    @allure.step("Open About page")
    def click_about_sidebar_link(self):
        self.click(ABOUT_LINK)

    @allure.step("Log out from sidebar")
    def click_logout_sidebar_link(self):
        self.click(LOGOUT_LINK)

    @allure.step("Reset application state")
    def click_reset_app_state_link(self):
        self.click(RESET_APP_STATE_LINK)
