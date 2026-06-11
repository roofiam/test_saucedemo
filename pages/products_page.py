from selenium.webdriver.support.select import Select

from locators.products_page import *
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

    def add_first_product_to_cart(self):
        self.click(ADD_TO_CART_BUTTON)

    def remove_product_from_cart(self):
        self.click(REMOVE_BUTTON)

    def get_cart_badge_text(self):
        return self.find_visible(CART_BADGE).text

    def is_cart_badge_displayed(self):
        return self.is_displayed(CART_BADGE)

    def sort_by_name_az(self):
        Select(self.find_visible(SORT_DROPDOWN)).select_by_value("az")

    def sort_by_name_za(self):
        Select(self.find_visible(SORT_DROPDOWN)).select_by_value("za")

    def sort_by_price_low_to_high(self):
        Select(self.find_visible(SORT_DROPDOWN)).select_by_value("lohi")

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

    def open_first_product(self):
        self.find_all(PRODUCT_NAMES)[0].click()

        return ProductDetailsPage(self.driver)

    def is_add_to_cart_button_displayed(self):
        return self.is_displayed(ADD_TO_CART_BUTTON)

    def is_remove_button_displayed(self):
        return self.is_displayed(REMOVE_BUTTON)

    def open_sort_dropdown(self):
        self.click(SORT_DROPDOWN)

    def is_sort_dropdown_expanded(self):
        return False

    def open_sidebar(self):
        self.click(MENU_BUTTON)

    def is_sidebar_displayed(self):
        return self.is_displayed(SIDEBAR_CLOSE_BUTTON)

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

    def open_twitter_link(self):
        self.click(TWITTER_LINK)

    def open_facebook_link(self):
        self.click(FACEBOOK_LINK)

    def open_linkedin_link(self):
        self.click(LINKEDIN_LINK)

    def get_current_url(self):
        return self.driver.current_url

    def click_all_items_sidebar_link(self):
        self.click(ALL_ITEMS_LINK)

    def click_about_sidebar_link(self):
        self.click(ABOUT_LINK)

    def click_logout_sidebar_link(self):
        self.click(LOGOUT_LINK)

    def click_reset_app_state_link(self):
        self.click(RESET_APP_STATE_LINK)

    def get_current_url(self):
        return self.driver.current_url
