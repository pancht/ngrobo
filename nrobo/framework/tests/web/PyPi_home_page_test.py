"""
@author: Panchdev Singh Chauhan
@email: erpanchdev@gmail.com
"""

import pytest
from pages.PagePyPiHome import PagePyPiHome


class TestPyPiHomePage:

    @pytest.mark.unit
    @pytest.mark.skip(reason="Test is not yet complete")
    def test_must_a_failure(self, driver, logger):
        logger.info("This test will fail for sure")
        driver.get("https://google.com")
        raise Exception("Must a fail test")

    @pytest.mark.unit
    def test_this_will_pass_always(self, driver, logger):
        logger.info("this test will pass always")
        driver.get("https://google.com")

    @pytest.mark.unit
    @pytest.mark.skip
    def test_pass_app_name_from_commandline(self, logger, app):
        logger.info(f"Appname={app}")

    @pytest.mark.unit
    @pytest.mark.skip
    def test_pass_url_username_password_from_commandline_example(
        self, driver, logger, url, username, password
    ):
        logger.info(f"URL={url}, Username={username} and Password={password}")
        driver.get(url)

    @pytest.mark.sanity
    def test_google_branding_displayed_on_home_page(self, driver, logger):
        # Instantiate page object
        page_pypi_home = PagePyPiHome(driver, logger)
        # call page method
        page_pypi_home.open()

        # Asset test condition
        assert page_pypi_home.search_button_present() == True

    @pytest.mark.regression
    def test_nrobo_package_is_available_on_pypi_org(self, driver, logger):
        page_pypi_home = PagePyPiHome(driver, logger)

        page_pypi_home.open()

        page_pypi_home.type_search_keyword("nrobo")

        page_search = page_pypi_home.search()

        # put a checkpoint
        assert page_search.nrobo_link_is_present()

    @pytest.mark.xfail
    @pytest.mark.skip(reason="Wanted to skip it for easy demonstration")
    def test_this_will_fail_for_sure(self, driver, logger):
        raise Exception("Must fail")
