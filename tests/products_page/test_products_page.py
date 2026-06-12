import pytest


class TestProductsPage:

    def test_products_page_is_opened(self, products_page):
        assert products_page.is_opened()

    def test_products_are_displayed(self, products_page):
        assert products_page.get_products_count() > 0

    def test_add_product_to_cart(self, products_page):
        assert products_page.is_add_to_cart_button_displayed()

        products_page.add_first_product_to_cart()

        assert products_page.get_cart_badge_text() == "1"
        assert products_page.is_remove_button_displayed()

    def test_remove_product_from_cart(self, products_page):
        products_page.add_first_product_to_cart()

        assert products_page.get_cart_badge_text() == "1"
        assert products_page.is_remove_button_displayed()

        products_page.remove_product_from_cart()

        assert products_page.wait_cart_badge_disappeared()
        assert products_page.is_add_to_cart_button_displayed()

    @pytest.mark.parametrize(
        "sort_method,get_items,reverse",
        [
            ("sort_by_name_az", "get_product_names", False),
            ("sort_by_name_za", "get_product_names", True),
            ("sort_by_price_low_to_high", "get_product_prices", False),
            ("sort_by_price_high_to_low", "get_product_prices", True),
        ],
    )
    def test_products_sorting(self, products_page, sort_method, get_items, reverse):
        getattr(products_page, sort_method)()

        items = getattr(products_page, get_items)()

        assert items == sorted(items, reverse=reverse)

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

    @pytest.mark.xfail(
        reason="Known bug: sort dropdown arrow click does not open the filter options"
    )
    def test_sort_dropdown_arrow_click_opens_options(self, products_page):
        products_page.open_sort_dropdown()

        assert products_page.is_sort_dropdown_expanded()
