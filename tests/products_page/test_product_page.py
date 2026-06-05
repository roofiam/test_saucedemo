class TestProductsPage:

    def test_products_page_is_opened(self, products_page):
        assert products_page.is_opened()

    def test_products_are_displayed(self, products_page):
        assert products_page.get_products_count() > 0

    def test_add_product_to_cart(self, products_page):
        products_page.add_first_product_to_cart()

        assert products_page.get_cart_badge_text() == "1"

    def test_remove_product_from_cart(self, products_page):
        products_page.add_first_product_to_cart()
        assert products_page.get_cart_badge_text() == "1"

        products_page.remove_product_from_cart()

        assert products_page.wait_cart_badge_disappeared()

    def test_sort_products_by_name_az(self, products_page):
        products_page.sort_by_name_az()

        product_names = products_page.get_product_names()

        assert product_names == sorted(product_names)

    def test_sort_products_by_name_za(self, products_page):
        products_page.sort_by_name_za()

        product_names = products_page.get_product_names()

        assert product_names == sorted(product_names, reverse=True)

    def test_sort_products_by_price_low_to_high(self, products_page):
        products_page.sort_by_price_low_to_high()

        product_prices = products_page.get_product_prices()

        assert product_prices == sorted(product_prices)

    def test_sort_products_by_price_high_to_low(self, products_page):
        products_page.sort_by_price_high_to_low()

        product_prices = products_page.get_product_prices()

        assert product_prices == sorted(product_prices, reverse=True)

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
