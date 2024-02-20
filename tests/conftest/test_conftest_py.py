import pytest


class TestConftestPy():

    @pytest.mark.unit
    def test_marker_unit(self, logger):
        """Verify unit marker: -m unit"""
        logger.info("Message from unit marker test.")

    @pytest.mark.ui
    def test_marker_ui(self, logger):
        """Verify ui marker: -m ui"""
        logger.info("Message from ui marker test.")

    @pytest.mark.regression
    def test_marker_regression(self, logger):
        """Verify regression marker: -m regression"""
        logger.info("Message from regression marker test.")

    @pytest.mark.sanity
    def test_marker_sanity(self, logger):
        """Verify sanity marker: -m sanity"""
        logger.info("Message from sanity marker test.")

    @pytest.mark.api
    def test_marker_api(self, logger):
        """Verify api marker: -m api"""
        logger.info("Message from api marker test.")

    @pytest.mark.nogui
    def test_marker_nogui(self, logger):
        """Verify nogui marker: -m nogui"""
        logger.info("Message from nogui marker test.")

    @pytest.mark.unit
    def test_cli_additional_args(self, driver, logger, app, url, username, password):
        """Verify additional cli arguments, app, url, username and password"""

        assert len(app) > 0
        assert len(url) > 0
        assert len(username) > 0
        assert len(password) > 0

        import logging
        assert isinstance(logger, logging.Logger)
        from selenium.webdriver.remote.webdriver import WebDriver
        assert isinstance(driver, WebDriver)