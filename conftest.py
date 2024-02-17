"""
=====================CAUTION=======================
DO NOT DELETE THIS FILE SINCE IT IS PART OF NROBO
FRAMEWORK AND IT MAY CHANGE IN THE FUTURE UPGRADES
OF NROBO FRAMEWORK. THUS, TO BE ABLE TO SAFELY UPGRADE
TO LATEST NROBO VERSION, PLEASE DO NOT DELETE THIS
FILE OR ALTER ITS LOCATION OR ALTER ITS CONTENT!!!
===================================================


@author: Panchdev Singh Chauhan
@email: erpanchdev@gmail.com
"""
import os
import sys

import pytest

# Add host's project path to sys path for module searching...
sys.path.append(os.path.join(os.path.dirname(__file__), ''))


def ensure_logs_dir_exists():
    """checks if driver logs dir exists. if not creates on the fly."""
    from nrobo.cli.cli_constants import NREPORT
    from nrobo.main import EnvKeys
    from pathlib import Path

    _log_driver_file = Path(os.environ[EnvKeys.EXEC_DIR]) / NREPORT.REPORT_DIR / NREPORT.LOG_DIR_DRIVER

    if not _log_driver_file.exists():
        """ensure driver logs dir"""
        try:
            os.makedirs(_log_driver_file)
        except FileExistsError as e:
            pass

    _test_logs_dir = Path(os.environ[EnvKeys.EXEC_DIR]) / NREPORT.REPORT_DIR / NREPORT.LOG_DIR_TEST
    if not _test_logs_dir.exists():
        """ensure test logs dir"""
        try:
            os.makedirs(_test_logs_dir)
        except FileExistsError as e:
            pass

    _screenshot_dir = Path(os.environ[EnvKeys.EXEC_DIR]) / NREPORT.REPORT_DIR / NREPORT.SCREENSHOTS_DIR
    if not _screenshot_dir.exists():
        """ensure screenshots dir"""
        try:
            os.makedirs(_screenshot_dir)
        except FileExistsError as e:
            pass

    _allure_dir = Path(os.environ[EnvKeys.EXEC_DIR]) / NREPORT.ALLURE_REPORT_PATH
    if not _allure_dir.exists():
        """ensure allure dir"""
        try:
            os.makedirs(_allure_dir)
        except FileExistsError as e:
            pass


def read_browser_config_options(_config_path):
    """
    process browser config options from the <_config_path>
    and return list of those.

    If file not found, then raise exception.

    """
    import os.path as path

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


def _log(msg: str):
    from nrobo.util.common import Common as logger

    file = "conftest.md"
    content = None
    try:
        content = logger.read_file_as_string(file)
    except FileNotFoundError as e:
        logger.write_text_to_file(file, "")
        content = ""

    content = content + "\n" + msg

    logger.write_text_to_file(file, content)


def pytest_addoption(parser):
    """
    Pass different values to a test function, depending on command line options

    :param parser:
    :return:
    """
    from nrobo.cli.cli_constants import nCLI

    _log("Call from ADDOPTION")

    group = parser.getgroup("nrobo header options")
    group.addoption(
        f"--{nCLI.BROWSER}", help="""
    Target browser name. Default is chrome.
    Options could be:
        chrome | firefox | safari | edge.
        (Only chrome is supported at present.)
    """
    )
    group.addoption(f"--{nCLI.APP}", help="Name of your app project under test")
    group.addoption(f"--{nCLI.URL}", help="Link of application under test.yaml")
    group.addoption(f"--{nCLI.USERNAME}", help="Username for login", default="")
    group.addoption(f"--{nCLI.PASSWORD}", help="Password for login", default="")
    group.addoption(f"--{nCLI.BROWSER_CONFIG}", help="Browser config file path for setting requested options")
    group.addoption(f"--{nCLI.PACKAGES}", help="Browser config file path for setting requested options")
    group.addoption(f"--{nCLI.GRID}", help="Url of remote selenium grid server")

    # ini option
    parser.addini(f"{nCLI.APP}", type="string",
                  help="Name of your app project under test")
    parser.addini(f"{nCLI.URL}", type='string',
                  help="Link of application under test.yaml")
    parser.addini(f"{nCLI.USERNAME}", type="string",
                  help="Username for login")
    parser.addini(f"{nCLI.PASSWORD}", type='string',
                  help="Password for login")
    parser.addini(f"{nCLI.BROWSER_CONFIG}", type='string',
                  help="Browser config file path for setting requested options")
    parser.addini(f"{nCLI.BROWSER_CONFIG}", type='string',
                  help="Browser config file path for setting requested options")
    parser.addini(f"{nCLI.PACKAGES}", type='string',
                  help="Browser config file path for setting requested options")
    parser.addini(f"--{nCLI.GRID}", type='string', help="Url of remote selenium grid server")


@pytest.fixture()
def url(request):
    # Global fixture returning app url
    # Access pytest command line options

    from nrobo.cli.cli_constants import nCLI

    return request.config.getoption(f"--{nCLI.URL}")


@pytest.fixture()
def app(request):
    from nrobo.cli.cli_constants import nCLI
    # Global fixture returning app name
    # Access pytest command line options
    return request.config.getoption(f"--{nCLI.APP}")


@pytest.fixture()
def username(request):
    from nrobo.cli.cli_constants import nCLI
    # Global fixture returning admin username
    # Access pytest command line options
    return request.config.getoption(f"--{nCLI.USERNAME}")


@pytest.fixture()
def password(request):
    from nrobo.cli.cli_constants import nCLI
    # Global fixture returning admin password
    # Access pytest command line options
    return request.config.getoption(f"--{nCLI.PASSWORD}")


@pytest.fixture(scope='function')
def driver(request):
    """
    Instantiating driver for given browser.
    """
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service as ChromeService
    from webdriver_manager.chrome import ChromeDriverManager
    from nrobo.main import EnvKeys
    from nrobo.cli.cli_constants import nCLI
    from nrobo.util.constants import CONST
    from nrobo.cli.nglobals import Browsers
    from nrobo.cli.formatting import STYLE

    _log("Call from DRIVER")

    # Access pytest command line options
    browser = request.config.getoption(f"--{nCLI.BROWSER}")

    # get and set url
    _url = request.config.getoption(f"--{nCLI.URL}")
    os.environ[EnvKeys.URL] = _url if _url else CONST.EMPTY
    # get grid url
    _grid_server_url = request.config.getoption(f"--{nCLI.GRID}")

    # initialize driver with None
    _driver = None

    # Set driver log name
    # current test function name
    test_method_name = request.node.name
    from nrobo.cli.cli_constants import NREPORT
    ensure_logs_dir_exists()
    _driver_log_path = NREPORT.REPORT_DIR + os.sep + \
                       NREPORT.LOG_DIR_DRIVER + os.sep + \
                       test_method_name + NREPORT.LOG_EXTENTION

    if browser == Browsers.CHROME:
        """if browser requested is chrome"""

        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-automation"])

        # enable/disable chrome options from a file
        _browser_options = read_browser_config_options(request.config.getoption(f"--{nCLI.BROWSER_CONFIG}"))
        # apply chrome options
        [options.add_argument(_option) for _option in _browser_options]

        if _grid_server_url:
            """Get instance of remote webdriver"""
            _driver = webdriver.Remote(_grid_server_url,
                                       options=options)
        else:
            """Get instance of local chrom driver"""
            _driver = webdriver.Chrome(options=options,
                                       service=ChromeService(
                                           ChromeDriverManager().install(),
                                           log_output=_driver_log_path))
    elif browser == Browsers.CHROME_HEADLESS:
        """if browser requested is chrome"""

        options = webdriver.ChromeOptions()
        options.add_argument('--headless=new')

        # enable/disable chrome options from a file
        _browser_options = read_browser_config_options(
            request.config.getoption(f"--{nCLI.BROWSER_CONFIG}"))
        # apply chrome options
        [options.add_argument(_option) for _option in _browser_options]

        if _grid_server_url:
            """Get instance of remote webdriver"""
            _driver = webdriver.Remote(_grid_server_url,
                                       options=options)
        else:
            """Get instance of local chrom driver"""
            _driver = webdriver.Chrome(options=options,
                                       service=ChromeService(
                                           ChromeDriverManager().install(),
                                           log_output=_driver_log_path))
    elif browser == Browsers.SAFARI:
        """if browser requested is safari"""

        options = webdriver.SafariOptions()
        options.add_argument("ShowOverlayStatusBar=YES")

        # enable/disable chrome options from a file
        _browser_options = read_browser_config_options(
            request.config.getoption(f"--{nCLI.BROWSER_CONFIG}"))
        # apply Safari options
        [options.add_argument(_option) for _option in _browser_options]

        if _grid_server_url:
            """Get instance of remote webdriver"""
            _driver = webdriver.Remote(_grid_server_url,
                                       options=options)
        else:
            """Get instance of local chrom driver"""
            _service = webdriver.SafariService(service_args=["--diagnose"])
            _driver = webdriver.Safari(options=options, service=_service)

    elif browser in [Browsers.FIREFOX, Browsers.FIREFOX_HEADLESS]:
        """if browser requested is firefox"""

        options = webdriver.FirefoxOptions()

        if browser == Browsers.FIREFOX_HEADLESS:
            options.add_argument("-headless")

        # enable/disable chrome options from a file
        _browser_options = read_browser_config_options(
            request.config.getoption(f"--{nCLI.BROWSER_CONFIG}"))
        # apply Safari options
        [options.add_argument(_option) for _option in _browser_options]

        if _grid_server_url:
            """Get instance of remote webdriver"""
            _driver = webdriver.Remote(_grid_server_url,
                                       options=options)
        else:
            """Get instance of local firefox driver"""
            _service = webdriver.FirefoxService(log_output=_driver_log_path, service_args=['--log', 'debug'])
            _driver = webdriver.Firefox(options=options, service=_service)
    elif browser == Browsers.EDGE:
        """if browser requested is microsoft edge"""

        options = webdriver.EdgeOptions()

        # enable/disable chrome options from a file
        _browser_options = read_browser_config_options(
            request.config.getoption(f"--{nCLI.BROWSER_CONFIG}"))
        # apply Safari options
        [options.add_argument(_option) for _option in _browser_options]

        if _grid_server_url:
            """Get instance of remote webdriver"""
            _driver = webdriver.Remote(_grid_server_url, options=options)
        else:
            """Get instance of local firefox driver"""
            _service = webdriver.EdgeService(log_output=_driver_log_path)
            _driver = webdriver.Edge(options=options, service=_service)
    elif browser == Browsers.IE:
        """if browser requested is microsoft internet explorer"""

        if sys.platform != "win32":
            """No need to proceed"""
            from nrobo.cli.tools import console
            console.rule("IE support available on WIN32 platform only! Quiting test run.")
            console.print(
                """Please note that the Internet Explorer (IE) 11 desktop application ended support for certain operating systems on June 15, 2022. Customers are encouraged to move to Microsoft Edge with IE mode.""")
            exit(1)

        options = webdriver.IeOptions()

        # enable/disable chrome options from a file
        _browser_options = read_browser_config_options(
            request.config.getoption(f"--{nCLI.BROWSER_CONFIG}"))
        # apply Safari options
        [options.add_argument(_option) for _option in _browser_options]

        if _grid_server_url:
            """Get instance of remote webdriver"""
            _driver = webdriver.Remote(_grid_server_url, options=options)
        else:
            """Get instance of local firefox driver"""
            _service = webdriver.IeService(log_output=_driver_log_path)
            _driver = webdriver.Ie(options=options)
    else:
        from nrobo.cli.tools import console
        console.rule(f"[{STYLE.HLRed}]DriverNotConfigured Error!")
        console.print(f"[{STYLE.HLRed}]Driver not configured in nrobo for browser <{browser}>")
        exit(1)

    # store web driver ref in request
    request.node.funcargs['driver'] = _driver
    # yield driver instance to calling test method
    yield _driver

    # quit the browser
    _driver.quit()


@pytest.fixture(scope='function')
def logger(request):
    """
    Instantiate logger instance for each test
    """
    _log("Call from LOGGER")

    import logging

    test_method_name = request.node.name
    from nrobo.cli.cli_constants import NREPORT
    ensure_logs_dir_exists()

    # Setup logger for tests
    logger = logging.getLogger('selenium')
    logger.setLevel(logging.DEBUG)
    _test_logs_path = NREPORT.REPORT_DIR + os.sep + \
                      NREPORT.LOG_DIR_TEST + os.sep + \
                      test_method_name + NREPORT.LOG_EXTENTION
    handler = logging.FileHandler(_test_logs_path)
    logger.addHandler(handler)
    logging.getLogger('selenium.webdriver.remote').setLevel(logging.WARN)
    logging.getLogger('selenium.webdriver.common').setLevel(logging.DEBUG)

    # yield logger instance to calling test method
    yield logger


def pytest_report_header(config):
    """
    Returns console header
    """
    _log("Call from REPORT HEADER")

    from nrobo.main import EnvKeys

    return f"{os.environ[EnvKeys.APP]}" + " test summary".title()


# set up a hook to be able to check if a test has failed
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Make report with screenshot attached
    """
    _log("Call from RUNTEST BEFORE")

    outcome = yield
    report = outcome.get_result()

    _log("Call from RUNTEST AFTER")

    from datetime import datetime
    from nrobo.util.constants import CONST
    from nrobo.cli.cli_constants import NREPORT
    import pytest_html
    import allure
    from nrobo.util.common import Common

    # test_fn = item.obj
    # docstring = getattr(test_fn, '__doc__')
    # if docstring:
    #     report.nodeid = docstring  # replace __doc__ string with nodeid

    extras = getattr(report, 'extras', [])
    if report.when == 'call':
        xfail = hasattr(report, 'wasxfail')
        if (report.failed and not xfail) \
                or (report.passed and not xfail):
            # Get test method identifier
            node_id = item.nodeid
            # Get reference to test method
            feature_request = item.funcargs['request']
            # Get driver reference from test method by calling driver(request) fixture
            driver = feature_request.getfixturevalue('driver')

            # replace unwanted chars from node id, datetime and prepare a good name for screenshot file
            screenshot_filename = f'{node_id}_{datetime.today().strftime("%Y-%m-%d_%H:%M")}_{Common.generate_random_numbers(1000, 9999)}.png' \
                .replace(CONST.FORWARD_SLASH, CONST.UNDERSCORE) \
                .replace(CONST.SCOPE_RESOLUTION_OPERATOR, CONST.UNDERSCORE) \
                .replace(CONST.COLON, CONST.EMPTY).replace('.py', CONST.EMPTY)

            # Attach screenshot to allure report
            allure.attach(
                # Not working. Still work in progress...
                driver.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )

            # Attach screenshot to html report
            screenshot_filepath = NREPORT.REPORT_DIR + os.sep + NREPORT.SCREENSHOTS_DIR + os.sep + screenshot_filename
            screenshot_relative_path = NREPORT.SCREENSHOTS_DIR + os.sep + screenshot_filename

            # Create and save screenshot at <screenshot_filepath>
            driver.save_screenshot(screenshot_filepath)

            # get base64 screenshot
            # failure_screen_shot = driver.get_screenshot_as_base64()

            # attach screenshot with html report. Use relative path to report directory
            extras.append(pytest_html.extras.image(screenshot_relative_path))
            # add relative path to screenshot in the html report
            extras.append(pytest_html.extras.url(screenshot_relative_path))

        # update the report.extras
        report.extras = extras


def pytest_configure(config):
    """
    Description
        configure pytest.
    """

    _log("Call from CONFIGURE")

    # add custom markers
    config.addinivalue_line("markers", "sanity: marks as sanity test")
    config.addinivalue_line("markers", "regression: mark as regression test")
    config.addinivalue_line("markers", "ui: mark as ui test")
    config.addinivalue_line("markers", "api: mark as api tests")
    config.addinivalue_line("markers", "nogui: mark as NOGUI tests")
    config.addinivalue_line("markers", "unit: mark as unit test")


def pytest_metadata(metadata):
    """
    Description
        pytest metadata
    """
    _log("Call from METADATA")
    # pop all the python environment table data
    # metadata.pop("Packages", None)
    # metadata.pop("Platform", None)
    # metadata.pop("Plugins", None)
    # metadata.pop("Python", None)
