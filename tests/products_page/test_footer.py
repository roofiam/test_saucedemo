class TestFooter:

    def test_twitter_link_opens_correct_page(self, products_page):
        windows_before = products_page.get_windows_count()

        products_page.open_twitter_link()

        assert products_page.get_windows_count() == windows_before + 1

        products_page.switch_to_new_window()

        try:
            current_url = products_page.get_current_url().lower()

            assert "twitter" in current_url or "x.com" in current_url
        finally:
            products_page.close_current_window()

    def test_facebook_link_opens_correct_page(self, products_page):
        windows_before = products_page.get_windows_count()

        products_page.open_facebook_link()

        assert products_page.get_windows_count() == windows_before + 1

        products_page.switch_to_new_window()

        try:
            current_url = products_page.get_current_url().lower()

            assert "facebook" in current_url
        finally:
            products_page.close_current_window()

    def test_linkedin_link_opens_correct_page(self, products_page):
        windows_before = products_page.get_windows_count()

        products_page.open_linkedin_link()

        assert products_page.get_windows_count() == windows_before + 1

        products_page.switch_to_new_window()

        try:
            current_url = products_page.get_current_url().lower()

            assert "linkedin" in current_url
        finally:
            products_page.close_current_window()
