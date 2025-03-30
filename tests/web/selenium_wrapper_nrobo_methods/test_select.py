"""Select methods."""

import pytest
from selenium.webdriver.common.by import By

from nrobo.framework.pages import Page


class TestSelect:
    """Select method tests."""

    def test_get_all_select_options(self, driver, logger):
        """Example of getting all options from a dropdown"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")

        lnk_drop_down = (By.CSS_SELECTOR, "[href='/dropdown']")
        page.click(*lnk_drop_down)

        drd_drop_down_list = (By.ID, "dropdown")
        options = page.select(*drd_drop_down_list).options

        logger.info(f"Options=> {options}")

        for opt in options:
            logger.info(f"Text={opt.text} value={opt.get_attribute('value')}")

    def test_get_all_selected_options(self, driver, logger):
        """Example of getting all selected options from a multiselect dropdown"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")

        lnk_drop_down = (By.CSS_SELECTOR, "[href='/dropdown']")
        page.click(*lnk_drop_down)

        drd_drop_down_list = (By.ID, "dropdown")
        dropdown = page.select(*drd_drop_down_list)

        # select first option
        dropdown.select_by_index(1)

        selected_options = dropdown.all_selected_options

        logger.info(f"Options=> {len(selected_options)}")

        logger.info(f"Selected option=> {selected_options[0].get_attribute('value')}")

    def test_get_first_selected_options(self, driver, logger):
        """Example of getting first selected options from a multiselect dropdown"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")

        lnk_drop_down = (By.CSS_SELECTOR, "[href='/dropdown']")
        page.click(*lnk_drop_down)

        drd_drop_down_list = (By.ID, "dropdown")
        dropdown = page.select(*drd_drop_down_list)

        # select first option
        dropdown.select_by_index(1)

        selected_option = dropdown.first_selected_option

        logger.info(f"Selected option=> {selected_option.get_attribute('value')}")

    def test_select_an_option_by_value_from_a_dropdown(self, driver, logger):
        """Example of select an option by value from a dropdown"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")

        lnk_drop_down = (By.CSS_SELECTOR, "[href='/dropdown']")
        page.click(*lnk_drop_down)

        drd_drop_down_list = (By.ID, "dropdown")
        dropdown = page.select(*drd_drop_down_list)

        # select first option
        dropdown.select_by_value("1")

        page.wait_for_a_while(3)

    def test_select_an_option_by_index_from_a_dropdown(self, driver, logger):
        """Example of select an option by index from a dropdown"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")

        lnk_drop_down = (By.CSS_SELECTOR, "[href='/dropdown']")
        page.click(*lnk_drop_down)

        drd_drop_down_list = (By.ID, "dropdown")
        dropdown = page.select(*drd_drop_down_list)

        # select first option
        dropdown.select_by_index(2)

        page.wait_for_a_while(3)

    def test_select_an_option_by_visible_text_from_a_dropdown(self, driver, logger):
        """Example of select an option by visible text from a dropdown"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")

        lnk_drop_down = (By.CSS_SELECTOR, "[href='/dropdown']")
        page.click(*lnk_drop_down)

        drd_drop_down_list = (By.ID, "dropdown")
        dropdown = page.select(*drd_drop_down_list)

        # select first option
        dropdown.select_by_visible_text("Option 2")

        page.wait_for_a_while(3)

    @pytest.mark.xfail
    def test_deselect_all_options_from_a_dropdown(self, driver, logger):
        """Example of deselect all options from a dropdown"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")

        lnk_drop_down = (By.CSS_SELECTOR, "[href='/dropdown']")
        page.click(*lnk_drop_down)

        drd_drop_down_list = (By.ID, "dropdown")
        dropdown = page.select(*drd_drop_down_list)

        # select first option
        dropdown.select_by_visible_text("Option 2")
        page.wait_for_a_while(1)

        dropdown.deselect_all()

        page.wait_for_a_while(3)

    @pytest.mark.xfail
    def test_deselect_by_value_from_a_dropdown(self, driver, logger):
        """Example of deselect by value from a dropdown"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")

        lnk_drop_down = (By.CSS_SELECTOR, "[href='/dropdown']")
        page.click(*lnk_drop_down)

        drd_drop_down_list = (By.ID, "dropdown")
        dropdown = page.select(*drd_drop_down_list)

        # select first option
        dropdown.select_by_visible_text("Option 2")
        page.wait_for_a_while(1)

        dropdown.deselect_by_value("2")

        page.wait_for_a_while(3)

    @pytest.mark.xfail
    def test_deselect_by_index_from_a_dropdown(self, driver, logger):
        """Example of deselect by index from a dropdown"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")

        lnk_drop_down = (By.CSS_SELECTOR, "[href='/dropdown']")
        page.click(*lnk_drop_down)

        drd_drop_down_list = (By.ID, "dropdown")
        dropdown = page.select(*drd_drop_down_list)

        # select first option
        dropdown.select_by_visible_text("Option 2")
        page.wait_for_a_while(1)

        dropdown.deselect_by_index(2)

        page.wait_for_a_while(3)

    @pytest.mark.xfail
    def test_deselect_by_visible_text_from_a_dropdown(self, driver, logger):
        """Example of deselect by visible text from a dropdown"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")

        lnk_drop_down = (By.CSS_SELECTOR, "[href='/dropdown']")
        page.click(*lnk_drop_down)

        drd_drop_down_list = (By.ID, "dropdown")
        dropdown = page.select(*drd_drop_down_list)

        # select first option
        dropdown.select_by_visible_text("Option 2")
        page.wait_for_a_while(1)

        dropdown.deselect_by_visible_text("Option 2")

        page.wait_for_a_while(3)
