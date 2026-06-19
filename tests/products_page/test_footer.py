import pytest


class TestFooter:
    @pytest.mark.parametrize(
        "open_method,expected_domains",
        [
            ("open_twitter_link", ("twitter", "x.com")),
            ("open_facebook_link", ("facebook",)),
            ("open_linkedin_link", ("linkedin",)),
        ],
    )
    def test_social_link_opens_correct_page(
        self,
        products_page,
        open_method,
        expected_domains,
    ):
        windows_before = products_page.get_windows_count()

        getattr(products_page, open_method)()

        assert products_page.get_windows_count() == windows_before + 1

        products_page.switch_to_new_window()

        try:
            current_url = products_page.get_current_url().lower()

            assert any(domain in current_url for domain in expected_domains)
        finally:
            products_page.close_current_window()
