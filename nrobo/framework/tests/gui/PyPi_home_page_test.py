"""
@author: Panchdev Singh Chauhan
@email: erpanchdev@gmail.com
"""
import pytest
from pages.PagePyPiHome import PagePyPiHome


class TestPyPiHomePage():

    @pytest.mark.sanity
    def test_google_branding_displayed_on_home_page(self, driver, logger):
        # Instantiate page object
        page_pypi_home = PagePyPiHome(driver, logger)
        # call page method
        page_pypi_home.open()

        # Asset test condition
        assert page_pypi_home.search_button_present() == True

