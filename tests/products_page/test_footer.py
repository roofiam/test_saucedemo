import allure
import pytest


@allure.feature("Footer")
class TestFooter:
    @allure.story("Social links")
    @allure.title("{link_name} link opens the correct page")
    @pytest.mark.parametrize(
        "link_name,open_method,expected_domains",
        [
            pytest.param(
                "Twitter / X",
                "open_twitter_link",
                ("twitter", "x.com"),
                id="Twitter / X",
            ),
            pytest.param(
                "Facebook",
                "open_facebook_link",
                ("facebook",),
                id="Facebook",
            ),
            pytest.param(
                "LinkedIn",
                "open_linkedin_link",
                ("linkedin",),
                id="LinkedIn",
            ),
        ],
    )
    def test_social_link_opens_correct_page(
        self,
        products_page,
        link_name,
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
