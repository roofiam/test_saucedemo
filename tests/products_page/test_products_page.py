import allure
import pytest


@allure.feature("Products")
class TestProductsPage:
    @allure.story("Products page")
    @allure.title("Products page is opened")
    def test_products_page_is_opened(self, products_page):
        assert products_page.is_opened()

    @allure.story("Products list")
    @allure.title("Products are displayed")
    def test_products_are_displayed(self, products_page):
        assert products_page.get_products_count() > 0

    @allure.story("Cart")
    @allure.title("User can add product to cart")
    def test_add_product_to_cart(self, products_page):
        assert products_page.is_add_to_cart_button_displayed()

        products_page.add_first_product_to_cart()

        assert products_page.get_cart_badge_text() == "1"
        assert products_page.is_remove_button_displayed()

    @allure.story("Cart")
    @allure.title("User can remove product from cart")
    def test_remove_product_from_cart(self, products_page):
        products_page.add_first_product_to_cart()

        assert products_page.get_cart_badge_text() == "1"
        assert products_page.is_remove_button_displayed()

        products_page.remove_product_from_cart()

        assert products_page.wait_cart_badge_disappeared()
        assert products_page.is_add_to_cart_button_displayed()

    @allure.story("Sorting")
    @allure.title("Products can be sorted by {sort_name}")
    @pytest.mark.parametrize(
        "sort_name,sort_method,get_items,reverse",
        [
            pytest.param(
                "name A to Z",
                "sort_by_name_az",
                "get_product_names",
                False,
                id="Name A to Z",
            ),
            pytest.param(
                "name Z to A",
                "sort_by_name_za",
                "get_product_names",
                True,
                id="Name Z to A",
            ),
            pytest.param(
                "price low to high",
                "sort_by_price_low_to_high",
                "get_product_prices",
                False,
                id="Price low to high",
            ),
            pytest.param(
                "price high to low",
                "sort_by_price_high_to_low",
                "get_product_prices",
                True,
                id="Price high to low",
            ),
        ],
    )
    def test_products_sorting(
        self,
        products_page,
        sort_name,
        sort_method,
        get_items,
        reverse,
    ):
        getattr(products_page, sort_method)()

        items = getattr(products_page, get_items)()

        assert items == sorted(items, reverse=reverse)

    @allure.story("Product details")
    @allure.title("Product details match product card")
    def test_product_details_match_product_card(self, products_page):
        product_name = products_page.get_first_product_name()
        product_description = products_page.get_first_product_description()
        product_price = products_page.get_first_product_price()
        product_image = products_page.get_first_product_image_url()

        product_details_page = products_page.open_first_product()

        assert product_details_page.is_opened()
        assert product_details_page.get_product_name() == product_name
        assert product_details_page.get_product_description() == product_description
        assert product_details_page.get_product_price() == product_price
        assert product_details_page.get_product_image_url() == product_image

    @allure.story("Sorting")
    @allure.title("Sort dropdown opens options after arrow click")
    @pytest.mark.xfail(
        reason="Known bug: sort dropdown arrow click does not open the filter options"
    )
    def test_sort_dropdown_arrow_click_opens_options(self, products_page):
        products_page.open_sort_dropdown()

        assert products_page.is_sort_dropdown_expanded()
