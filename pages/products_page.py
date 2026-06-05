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
