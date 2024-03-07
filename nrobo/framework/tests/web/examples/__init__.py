import sys

import allure
import pytest


class Examples:

    @pytest.mark.sanity
    def test_this_is_marked_as_sanity_test(self, driver, logger):
        logger.info("This is a sanity test.")
        # Your sanity test logic will go below
        # ...
        # ...

    @pytest.mark.regression
    def test_this_is_marked_as_regression_test(self, driver, logger):
        logger.info("This is a regression test.")
        # Your regression test logic will go below
        # ...
        # ...

    @pytest.mark.ui
    def test_this_is_marked_as_ui_test(self, driver, logger):
        logger.info("This is a ui test.")
        # Your ui test logic will go below
        # ...
        # ...

    @pytest.mark.unit
    def test_this_is_marked_as_unit_test(self, driver, logger):
        logger.info("This is a unit test.")
        # Your unit test logic will go below
        # ...
        # ...

    @pytest.mark.nogui
    def test_this_is_marked_as_nogui_test(self, driver, logger):
        logger.info("This is a nogui test.")
        # Your gui test logic will go below
        # ...
        # ...

    @pytest.mark.api
    def test_this_is_marked_as_api_test(self, driver, logger):
        logger.info("This is a api test.")
        # Your api test logic will go below
        # ...
        # ...

    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_this_is_marked_as_flaky_test(self, driver, logger):
        logger.info("This is a flaky test. Test that may fail for the first time. If fails, run thrice.")
        # Your flaky test logic will go below
        # ...
        # ...

    @allure.title("Test Authentication")
    @allure.description(
        "This test attempts to log into the website using a login and a password. Fails if any error happens.\n\nNote "
        "that this test does not test 2-Factor Authentication.")
    @allure.description_html("This is an example of <bold>html</b> description.")
    @allure.tag("NewUI", "Essentials", "Authentication")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "John Doe")
    @allure.link("https://dev.example.com/", name="Website")
    @allure.issue("AUTH-123")
    @allure.testcase("TMS-456")
    def test_this_is_an_example_of_allure_description_links_and_other_metadata(self, driver, logger):
        logger.info("This is an example of allure description, links and other metadata")

    @pytest.mark.filterwarnings("ignore:api v1")
    def test_filter_warnings(self, driver, logger):
        logger.info("This is an example of filter warnings.")

    @pytest.mark.skip(reason="Reason for skipping this test")
    def test_skip(self, driver, logger):
        logger.info(f"skip the given test function with an optional reason. "
                    f"Example: skip(reason='no way of currently testing this') skips the test.")

    @pytest.mark.skipif(sys.platform == 'win32', reason="This is not intended to run on windows machine.")
    def test_skip_if_condition_is_met(self, driver, logger):
        logger.info("skip the given test function if any of the conditions evaluate to True. Example: "
                    "skipif(sys.platform == 'win32') skips the test if we are on the win32 platform.")

    @pytest.mark.xfail(sys.platform == 'win32', reason="This test will fail on windows.", raises=NotImplemented, run=False, strict=False)
    def test_expected_failure_if_condition_is_met(self, driver, logger):
        logger.info("""
        Parameters:
            condition (Union[bool, str]) – Condition for marking the test function as xfail (True/False or a condition string). If a bool, you also have to specify reason (see condition string).
            
            reason (str) – Reason why the test function is marked as xfail.
            
            raises (Type[Exception]) – Exception class (or tuple of classes) expected to be raised by the test function; other exceptions will fail the test. Note that subclasses of the classes passed will also result in a match (similar to how the except statement works).
            
            run (bool) – Whether the test function should actually be executed. If False, the function will always xfail and will not be executed (useful if a function is segfaulting).
            
            strict (bool) –
            
            If False the function will be shown in the terminal output as xfailed if it fails and as xpass if it passes. In both cases this will not cause the test suite to fail as a whole. This is particularly useful to mark flaky tests (tests that fail at random) to be tackled later.
            
            If True, the function will be shown in the terminal output as xfailed if it fails, but if it unexpectedly passes then it will fail the test suite. This is particularly useful to mark functions that are always failing and there should be a clear indication if they unexpectedly start to pass (for example a new release of a library fixes a known bug).
            
            Defaults to xfail_strict, which is False by default.
        """)

    @pytest.mark.parametrize("test_input, expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
    def test_parameterized(self, driver, logger):
        logger.info("""
            call a test function multiple times passing in different arguments in turn. 
            argvalues generally needs to be a list of values if argnames specifies only one name 
            or a list of tuples of values if argnames specifies multiple names. 
            
            Example: @parametrize('arg1', [1,2]) would lead to two calls of the decorated test function, 
            one with arg1=1 and another with arg1=2.
        """)

    @pytest.mark.usefixtures('driver', 'logger')
    def test_use_fixtures_example(self, driver, logger):
        logger.info("mark tests as needing all of the specified fixtures")

    @pytest.hookimpl(tryfirst=True)
    def test_tryfirst_hook(self, driver, logger):
        logger.info("mark a hook implementation function such that the plugin machinery will try to call it first/as "
                    "early as possible. DEPRECATED, use @pytest.hookimpl(tryfirst=True) instead.")

    @pytest.hookimpl(trylast=True)
    def test_trylast_hook(self, driver, logger):
        logger.info("mark a hook implementation function such that the plugin machinery will try to call it last/as "
                    "late as possible. DEPRECATED, use @pytest.hookimpl(trylast=True) instead.")




