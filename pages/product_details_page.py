from locators.product_details_page import *
from pages.base_page import BasePage


class ProductDetailsPage(BasePage):

    def is_opened(self):
        return self.is_displayed(PRODUCT_DETAILS_CONTAINER)

    def get_product_name(self):
        return self.find_visible(PRODUCT_NAME).text

    def get_product_description(self):
        return self.find_visible(PRODUCT_DESCRIPTION).text

    def get_product_price(self):
        return self.find_visible(PRODUCT_PRICE).text

    def get_product_image_url(self):
        return self.find_visible(PRODUCT_IMAGE).get_attribute("src")
