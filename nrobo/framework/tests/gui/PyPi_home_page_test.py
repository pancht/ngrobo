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
        page_demo = PagePyPiHome(driver, logger)
        # call page method
        page_demo.open_home_page()

        # Asset test condition
        assert page_demo.exist_branding_image() == True
