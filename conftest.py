"""
nrobo conftest.py file.
Doc: https://docs.pytest.org/en/latest/reference/reference.html#request
Doc: https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/python/tests/browsers/test_chrome.py
Doc2: https://docs.pytest.org/en/7.1.x/example/simple.html

Contains fixtures for nrobo framework
"""
import os

import pytest
from selenium import webdriver

import nrobo.cli.cli_constansts
from nrobo.cli.nglobals import __APP_NAME__, __USERNAME__, __PASSWORD__, __URL__, __BROWSER__, Browsers
from nrobo.util.common import Common
from nrobo.cli.cli_constansts import nCLI as CLI
import os.path as path

global __APP_NAME__, __USERNAME__, __PASSWORD__, __URL__, __BROWSER__


def process_browser_config_options(_config_path):
    """
    process browser config options from the <_config_path>
    and return list of those.

    If file not found, then raise exception.

    """
    if not _config_path:
        return []

    if path.exists(_config_path):
        """if path exists"""

        # read file and store it's content in a list
        _config_options = []
        with open(_config_path, "r") as f:
            _config_options.append(str(f.readline()).strip())

        return _config_options
    else:
        raise Exception(f"Chrome config file does not exist at path <{_config_path}>!!!")


def pytest_addoption(parser):
    """
    Pass different values to a test function, depending on command line options

    Doc: https://docs.pytest.org/en/7.1.x/example/simple.html
    :param parser:
    :return:
    """
    parser.addoption(
        f"--{CLI.BROWSER}", help="""
    Target browser name. Default is chrome.
    Options could be:
        chrome | firefox | safari | edge.
        (Only chrome is supported at present.)
    """
    )
    parser.addoption(f"--{CLI.APP}", help="Name of your app project under test")
    parser.addoption(f"--{CLI.URL}", help="Link of application under test.yaml")
    parser.addoption(f"--{CLI.USERNAME}", help="Username for login", default="")
    parser.addoption(f"--{CLI.PASSWORD}", help="Password for login", default="")
    parser.addoption(f"--{CLI.BROWSER_CONFIG}", help="Browser config file path for setting requested options")


@pytest.fixture()
def url(request):
    # Global fixture returning app url
    # Access pytest command line options
    # Doc: https://docs.pytest.org/en/7.1.x/example/simple.html
    return request.config.getoption(f"--{CLI.URL}")


@pytest.fixture()
def app(request):
    # Global fixture returning app name
    # Access pytest command line options
    # Doc: https://docs.pytest.org/en/7.1.x/example/simple.html
    return request.config.getoption(f"--{CLI.APP}")


@pytest.fixture()
def username(request):
    # Global fixture returning admin username
    # Access pytest command line options
    # Doc: https://docs.pytest.org/en/7.1.x/example/simple.html
    return request.config.getoption(f"--{CLI.USERNAME}")


@pytest.fixture()
def password(request):
    # Global fixture returning admin password
    # Access pytest command line options
    # Doc: https://docs.pytest.org/en/7.1.x/example/simple.html
    return request.config.getoption(f"--{CLI.PASSWORD}")


@pytest.fixture(scope='function')
def driver(request):
    """
    Fixture for instantiating driver for given browser.
    Doc: https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/python/tests/browsers/test_chrome.py
    Doc2: https://docs.pytest.org/en/7.1.x/example/simple.html

    """
    # Access pytest command line options
    # Doc: https://docs.pytest.org/en/7.1.x/example/simple.html
    browser = request.config.getoption(f"--{CLI.BROWSER}")

    _driver = None

    if browser == Browsers.CHROME:
        """if browser requested is chrome"""

        # Chrome Flags for Tooling
        # Doc: https://github.com/GoogleChrome/chrome-launcher/blob/main/docs/chrome-flags-for-tools.md
        # Command line switches
        # Doc: https://peter.sh/experiments/chromium-command-line-switches/
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-automation"])

        # enable/disable chrome options from a file
        _chrome_config_path = request.config.getoption(f"--{CLI.BROWSER_CONFIG}")
        _chrome_config_options = process_browser_config_options(_chrome_config_path)

        # Common.write_text_to_file("config.chrome.txt", _chrome_config_options)
        # exit(1)

        # apply chrome options
        for _option in _chrome_config_options:
            options.add_argument(_option)

        # current test function name
        # Doc: https://docs.pytest.org/en/latest/reference/reference.html#request
        test_method_name = request.node.name
        from nrobo.cli.cli_constansts import REPORT_TYPES
        log_path = REPORT_TYPES.REPORT_DIR + os.sep + test_method_name + REPORT_TYPES.LOG_EXTENTION

        service = webdriver.ChromeService(log_output=log_path)
        _driver = webdriver.Chrome(options=options, service=service)
    elif browser == Browsers.CHROME_HEADLESS:
        """if browser requested is chrome"""

        # Chrome Flags for Tooling
        # Doc: https://github.com/GoogleChrome/chrome-launcher/blob/main/docs/chrome-flags-for-tools.md
        # Command line switches
        # Doc: https://peter.sh/experiments/chromium-command-line-switches/
        # Doc: https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/python/tests/browsers/test_chrome.py
        options = webdriver.ChromeOptions()
        options.add_argument('--headless=new')

        # enable/disable chrome options from a file
        _chrome_config_path = request.config.getoption(f"--{CLI.BROWSER_CONFIG}")
        _chrome_config_options = process_browser_config_options(_chrome_config_path)

        # apply chrome options
        for _option in _chrome_config_options:
            options.add_argument(_option)

        # current test function name
        # Doc: https://docs.pytest.org/en/latest/reference/reference.html#request
        test_method_name = request.node.name
        from nrobo.cli.cli_constansts import REPORT_TYPES
        log_path = REPORT_TYPES.REPORT_DIR + os.sep + test_method_name + REPORT_TYPES.LOG_EXTENTION

        service = webdriver.ChromeService(log_output=log_path)
        _driver = webdriver.Chrome(options=options, service=service)

    # yield driver instance to calling test method
    yield _driver

    # quit the browser
    _driver.quit()
