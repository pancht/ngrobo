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

from selenium.webdriver.common.by import By

from nrobo import EnvKeys

# Add host's project path to sys path for module searching...
sys.path.append(os.path.join(os.path.dirname(__file__), ''))

import logging
import os
import sys
from datetime import datetime

import allure
import pytest
import pytest_html
from nrobo.cli import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from nrobo.cli.nglobals import *
from nrobo.util.common import *
from nrobo.cli.cli_constants import *
import os.path as path
import nrobo.cli.detection as detect

from nrobo.util.constants import CONST
from nrobo.appium import AUTOMATION_NAMES, CAPABILITY
from selenium.common.exceptions import WebDriverException


def update_pytest_life_cycle_log(life_cycle_item: str, item_type: str = "fixture"):
    if detect.developer_machine():
        from nrobo import NROBO_PATHS
        Common.append_text_to_file(NROBO_PATHS.PYTEST_LIFE_CYCLE_LOGS,
                                   f"\n\n-----------------------\n"
                                   f"Calling from {life_cycle_item} {item_type}")


def update_pytest_life_cycle_log_with_value(value: str):
    if detect.developer_machine():
        from nrobo import NROBO_PATHS
        Common.append_text_to_file(NROBO_PATHS.PYTEST_LIFE_CYCLE_LOGS,
                                   f"\n{value}")


def ensure_logs_dir_exists():
    """checks if driver logs dir exists. if not creates on the fly."""
    from nrobo.cli.cli_constants import NREPORT
    from nrobo import EnvKeys, NROBO_PATHS
    _log_driver_file = NROBO_PATHS.EXEC_DIR / NREPORT.REPORT_DIR / NREPORT.LOG_DIR_DRIVER

    if not _log_driver_file.exists():
        """ensure driver logs dir"""
        try:
            os.makedirs(_log_driver_file)
        except FileExistsError as e:
            pass

    _test_logs_dir = NROBO_PATHS.EXEC_DIR / NREPORT.REPORT_DIR / NREPORT.LOG_DIR_TEST
    if not _test_logs_dir.exists():
        """ensure test logs dir"""
        try:
            os.makedirs(_test_logs_dir)
        except FileExistsError as e:
            pass

    _screenshot_dir = NROBO_PATHS.EXEC_DIR / NREPORT.REPORT_DIR / NREPORT.SCREENSHOTS_DIR
    if not _screenshot_dir.exists():
        """ensure screenshots dir"""
        try:
            os.makedirs(_screenshot_dir)
        except FileExistsError as e:
            pass

    _allure_dir = NROBO_PATHS.EXEC_DIR / NREPORT.ALLURE_REPORT_PATH
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


def add_capabilities_from_file(options):
    """Read capabilities from capability.yaml file

       and add them to the browser options <options>

       and return updated options"""
    from nrobo.util.common import Common
    from nrobo import NROBO_PATHS, Environment, EnvKeys
    if detect.production_machine() and not detect.developer_machine():
        capabilities = Common.read_yaml(NROBO_PATHS.EXEC_DIR / NROBO_PATHS.CAPABILITY_YAML)
    else:
        capabilities = Common.read_yaml(
            NROBO_PATHS.NROBO_DIR / NROBO_PATHS.NROBO / NROBO_PATHS.CAPABILITY_YAML)

    for k, v in capabilities.items():
        options.set_capability(k, v)

    return options


def get_appium_capabilities_from_file(cap_file_name):
    """Read appium capabilities from android_capability.yaml file

       return appium_capabilities"""
    from nrobo.util.common import Common
    from nrobo import NROBO_PATHS, Environment, EnvKeys
    if detect.production_machine() and not detect.developer_machine():
        capabilities = Common.read_yaml(NROBO_PATHS.EXEC_DIR / NROBO_PATHS.APPIUM / cap_file_name)
    else:
        capabilities = Common.read_yaml(
            NROBO_PATHS.EXEC_DIR / NROBO_PATHS.NROBO / NROBO_PATHS.APPIUM / cap_file_name)

    return capabilities


def pytest_addoption(parser):
    """
    Pass different values to a test function, depending on command line options

    :param parser:
    :return:
    """
    update_pytest_life_cycle_log("pytest_addoption", "hook")

    group = parser.getgroup("nrobo header options")
    # nRoBo appium options
    group.addoption(
        f"--{nCLI.APPIUM}", help=f"Tells nRoBo to trigger via appium client",
        action="store_true", default=False
    )
    group.addoption(
        f"--{nCLI.CAP}", help="File name of appium capability file."
                              "nRoBo will search the given capability file "
                              "in appium directory under project root folder."
    )

    # nRoBo webdriver options
    group.addoption(
        f"--{nCLI.BROWSER}", help="""
    Target browser name. Default is chrome.
    Options could be:
        chrome | firefox | safari | edge.
        (Only chrome is supported at present_release.)
    """
    )
    group.addoption(f"--{nCLI.APP}", help="Name of your app project under test")
    group.addoption(f"--{nCLI.REPORT_TITLE}", help="Defines HTML report title")
    group.addoption(f"--{nCLI.URL}", help="Link of application under test")
    group.addoption(f"--{nCLI.USERNAME}", help="Username for login", default="")
    group.addoption(f"--{nCLI.PASSWORD}", help="Password for login", default="")
    group.addoption(f"--{nCLI.BROWSER_CONFIG}", help="Browser config file path for setting requested options")
    group.addoption(f"--{nCLI.PACKAGES}", help="Browser config file path for setting requested options")
    group.addoption(f"--{nCLI.GRID}", help="Url of remote selenium grid server")
    group.addoption(f"--{nCLI.FULLPAGE_SCREENSHOT}",
                    help="Take full page screenshot", action="store_true", default=False)

    # ini option
    parser.addini(f"--{nCLI.APPIUM}", type='bool', help=f"Tells nRoBo to trigger via appium client")
    parser.addini(f"--{nCLI.CAP}", type='string', help="File name of appium capability file."
                                                       "nRoBo will search the given capability file "
                                                       "in appium directory under project root folder.")
    parser.addini(f"{nCLI.APP}", type="string",
                  help="Name of your app project under test")
    parser.addini(f"{nCLI.REPORT_TITLE}", type="string",
                  help="Defines HTML report title")
    parser.addini(f"{nCLI.URL}", type='string',
                  help="Link of application under test")
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
    parser.addini(f"--{nCLI.FULLPAGE_SCREENSHOT}", type='bool',
                  help="Take full page screenshot")


@pytest.fixture(scope='function')
def url(request):
    """Supply test URL given from nRoBo command line"""
    # Global fixture returning app url
    # Access pytest command line options
    update_pytest_life_cycle_log("url")

    return request.config.getoption(f"--{nCLI.URL}")


@pytest.fixture(scope='function')
def app(request):
    """Supply app name given from nRoBo command line"""

    update_pytest_life_cycle_log("app")

    # Global fixture returning app name
    # Access pytest command line options
    return request.config.getoption(f"--{nCLI.APP}")


@pytest.fixture(scope='function')
def username(request):
    """Supply username given from nRoBo command line"""

    update_pytest_life_cycle_log("username")

    # Global fixture returning admin username
    # Access pytest command line options
    return request.config.getoption(f"--{nCLI.USERNAME}")


@pytest.fixture(scope='function')
def password(request):
    """Supply password given from nRoBo command line"""

    update_pytest_life_cycle_log("password")
    # Global fixture returning admin password
    # Access pytest command line options
    return request.config.getoption(f"--{nCLI.PASSWORD}")


@pytest.fixture(autouse=True, scope='function')
def driver(request):
    """
    Instantiating driver for given browser.
    """

    update_pytest_life_cycle_log("driver")

    # Access pytest command line options
    from nrobo import EnvKeys, console
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

    if int(os.environ[EnvKeys.APPIUM]):

        """get appium driver with given capabilities"""
        from appium import webdriver as _webdriver
        from nrobo import NROBO_PATHS

        capabilities = get_appium_capabilities_from_file(request.config.getoption(f"--{nCLI.CAP}"))

        if capabilities[CAPABILITY.AUTOMATION_NAME] == AUTOMATION_NAMES.UI_AUTOMATION2:
            """Create uiautomator2 driver instance"""
            from appium.options.android import UiAutomator2Options

            options = UiAutomator2Options().load_capabilities(capabilities)

        elif capabilities[CAPABILITY.AUTOMATION_NAME] == AUTOMATION_NAMES.XCUITEST:
            from appium.options.ios import XCUITestOptions

            options = XCUITestOptions().load_capabilities(capabilities)

        _grid_url_missing = False

        if _grid_server_url is None:
            _grid_url_missing = True
            _grid_server_url = "http://localhost:4723"

        try:
            _driver = _webdriver.Remote(_grid_server_url, options=options)
        except Exception as e:
            if _grid_url_missing:
                console.rule(f"[{STYLE.HLRed}]\n\nAppium server url is missing![/]\n\n")
            else:
                console.rule(f"[{STYLE.HLRed}]\n\nIt seems like appium server is not running? "
                             f"\nor Is appium server url incorrect?"
                             f"\nPlease check!!![/]\n\n")

    elif browser == Browsers.CHROME:
        """if browser requested is chrome"""

        options = webdriver.ChromeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("useAutomationExtension", False)
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options = add_capabilities_from_file(options)

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

        # Anti Bot Detection logic by ZenRows
        # URL: https://www.zenrows.com/blog/selenium-avoid-bot-detection#how-anti-bots-work
        _driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

        # Initializing a list with two Useragents
        useragentarray = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
        ]

        for i in range(len(useragentarray)):
            # Setting user agent iteratively as Chrome 108 and 107
            _driver.execute_cdp_cmd("Network.setUserAgentOverride", {"userAgent": useragentarray[i]})
            print(_driver.execute_script("return navigator.userAgent;"))
            # _driver.get("https://www.httpbin.org/headers")

    elif browser == Browsers.CHROME_HEADLESS:
        """if browser requested is chrome"""

        options = webdriver.ChromeOptions()
        options.add_argument('--headless=new')
        options = add_capabilities_from_file(options)

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

    elif browser == Browsers.ANTI_BOT_CHROME:
        """if browser requested is anti_bot_chrome"""

        options = webdriver.ChromeOptions()
        options.add_argument('--headless=new')
        options = add_capabilities_from_file(options)

        # enable/disable chrome options from a file
        _browser_options = read_browser_config_options(
            request.config.getoption(f"--{nCLI.BROWSER_CONFIG}"))
        # apply chrome options
        [options.add_argument(_option) for _option in _browser_options]

        if _grid_server_url:
            """Get instance of remote webdriver"""
            from nrobo import console
            console.rule(f"[{STYLE.HLRed}]Anti-Bot Chrome is not supported by Grid Infrastructure![/]")
            sys.exit()
            # _driver = webdriver.Remote(_grid_server_url,
            #                            options=options)
        else:
            """Get instance of local chrom driver"""
            import undetected_chromedriver as uc
            _driver = uc.Chrome(use_subprocess=False, options=options)
            # _driver = webdriver.Chrome(options=options,
            #                            service=ChromeService(
            #                                ChromeDriverManager().install(),
            #                                log_output=_driver_log_path))

    elif browser == Browsers.SAFARI:
        """if browser requested is safari"""

        options = webdriver.SafariOptions()
        options.add_argument("ShowOverlayStatusBar=YES")
        options = add_capabilities_from_file(options)

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
        options = add_capabilities_from_file(options)

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
        options = add_capabilities_from_file(options)

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
                """Please note that the Internet Explorer (IE) 11 desktop application ended support 
                for certain operating systems on June 15, 2022. 
                Customers are encouraged to move to Microsoft Edge with IE mode.""")
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

    update_pytest_life_cycle_log("logger")

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

    update_pytest_life_cycle_log("pytest_report_header", "hook")

    from nrobo import EnvKeys
    return f"{os.environ[EnvKeys.APP]}" + " test summary".title()


# set up a hook to be able to check if a test has failed
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Make report with screenshot attached
    """

    update_pytest_life_cycle_log("pytest_runtest_makereport", "hook")

    outcome = yield
    report = outcome.get_result()

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
            screenshot_filename = f'{node_id}_{datetime.today().strftime("%Y-%m-%d_%H:%M")}' \
                                  f'_{Common.generate_random_numbers(1000, 9999)}.png' \
                .replace(CONST.FORWARD_SLASH, CONST.UNDERSCORE) \
                .replace(CONST.SCOPE_RESOLUTION_OPERATOR, CONST.UNDERSCORE) \
                .replace(CONST.COLON, CONST.EMPTY).replace('.py', CONST.EMPTY)

            # build screenshot relative path for html report and actual path for saving screenshot
            screenshot_filepath = NREPORT.REPORT_DIR + os.sep + \
                                  NREPORT.SCREENSHOTS_DIR + \
                                  os.sep + screenshot_filename
            screenshot_relative_path = NREPORT.SCREENSHOTS_DIR + os.sep + screenshot_filename

            # Handle fullpagescreenshot cli switch
            fullpagescreenshot = feature_request.config.getoption(f"--{nCLI.FULLPAGE_SCREENSHOT}")

            if fullpagescreenshot:
                driver.maximize_window()
                document_height = \
                    driver.execute_script(
                        'return Math.max( document.body.scrollHeight, document.body.offsetHeight, '
                        'document.documentElement.clientHeight, document.documentElement.scrollHeight, '
                        'document.documentElement.offsetHeight );')
                document_size = driver.get_window_size()
                driver.set_window_size(document_size['width'], document_height)
                driver.find_element(By.TAG_NAME, 'body').screenshot(screenshot_filepath)

            # Attach screenshot to allure report
            try:
                allure.attach(
                    # Not working. Still work in progress...
                    driver.get_screenshot_as_png() if not fullpagescreenshot else driver.find_element(By.TAG_NAME,
                                                                                                      'body').screenshot_as_png,
                    name='screenshot',
                    attachment_type=allure.attachment_type.PNG
                )

                # Attach screenshot to html report
                # Create and save screenshot at <screenshot_filepath>
                if not fullpagescreenshot:
                    driver.save_screenshot(screenshot_filepath)

                # get base64 screenshot
                # failure_screen_shot = driver.get_screenshot_as_base64()

                # attach screenshot with html report. Use relative path to report directory
                extras.append(pytest_html.extras.image(screenshot_relative_path))
                # add relative path to screenshot in the html report
                extras.append(pytest_html.extras.url(screenshot_relative_path))

            except Exception as e:
                extras = []

        # update the report.extras
        report.extras = extras


def pytest_configure(config):
    """
    Description
        configure pytest.
    """
    from nrobo.util.constants import CONST
    update_pytest_life_cycle_log("pytest_configure", "hook")

    os.environ[EnvKeys.TITLE] = str(config.getoption(f'--{nCLI.REPORT_TITLE}')).replace(CONST.UNDERSCORE, CONST.SPACE)
    os.environ[EnvKeys.APP] = str(config.getoption(f'--{nCLI.APP}')).replace(CONST.UNDERSCORE, CONST.SPACE)
    os.environ[EnvKeys.APPIUM] = "1" if str(config.getoption(f'--{nCLI.APPIUM}')) == "True" else "0"

    # add custom markers
    config.addinivalue_line("markers", "sanity: marks as sanity test")
    config.addinivalue_line("markers", "regression: mark as regression test")
    config.addinivalue_line("markers", "ui: mark as ui test")
    config.addinivalue_line("markers", "api: mark as api tests")
    config.addinivalue_line("markers", "nogui: mark as NOGUI tests")
    config.addinivalue_line("markers", "unit: mark as unit test")

    from nrobo import NROBO_PATHS
    if detect.production_machine() and not detect.developer_machine():
        markers = Common.read_yaml(NROBO_PATHS.EXEC_DIR / NROBO_PATHS.MARKERS_YAML)
    else:
        markers = Common.read_yaml(NROBO_PATHS.EXEC_DIR / NROBO_PATHS.NROBO / NROBO_PATHS.MARKERS_YAML)
    for marker, desc in markers.items():
        config.addinivalue_line("markers", f"{marker}: {desc}")


def pytest_metadata(metadata):
    """
    Description
        pytest metadata
    """

    update_pytest_life_cycle_log("pytest_metadata", "hook")

    # pop all the python environment table data
    # metadata.pop("Packages", None)
    # metadata.pop("Platform", None)
    # metadata.pop("Plugins", None)
    # metadata.pop("Python", None)


def pytest_runtest_setup(item):
    from nrobo.util.common import Common
    update_pytest_life_cycle_log("pytest_runtest_setup", "hook")
    from pprint import pprint
    from nrobo.util.common import Common
    try:
        callspec = item.callspec
    except AttributeError as ae:
        callspec = None

    try:
        callobj = item.callobj
    except AttributeError as ae:
        callobj = None

    try:
        fixtureinfo = item.fixtureinfo
    except AttributeError as ae:
        fixtureinfo = None

    update_pytest_life_cycle_log_with_value(f"Function properties:\n"
                                            f"name={item.name}\n"
                                            f"parent={item.parent}\n"
                                            f"config={item.config}\n"
                                            f"callspec={callspec}\n"
                                            f"callobj={callobj}\n"
                                            f"keywords={item.keywords}\n"
                                            f"session={item.session}\n"
                                            f"fixtureinfo={fixtureinfo}\n"
                                            f"originalname={item.originalname}\n"
                                            f"filepath={item.fspath}\n"
                                            f"docstring={item.__doc__}")

    pprint(item.__doc__)
    pprint(item.config)
    print(item.parent)
    pprint(item.name)
    pprint(item.fspath)
    pprint(item.session)
    mod = item.getparent(pytest.Module).obj
    print("Mod.dir")
    pprint(mod.__dir__)
    _class = item.getparent(pytest.Class).obj
    print(f"class where this test {item.name} belong to")
    pprint(_class)
    print(f"All attributes of test class")
    pprint(_class.__dir__(item.name))
    print(f"Get doc string")
    print(_class.__dir__(item.name).__doc__)
    print("Check if item has attribute hello")
    pprint(hasattr(mod, "hello"))
    print(f"node id")
    pprint(item.nodeid)
    print(f"Nodeid dir object")
    pprint(item.nodeid.__dir__)

    if isinstance(item, pytest.Function):
        pass

    # if isinstance(item, pytest.Function):
    #     if not item.fspath.relto(mydir):
    #         return
    #     mod = item.getparent(pytest.Module).obj
    #     if hasattr(mod, "hello"):
    #         print(f"mod.hello {mod.hello!r}")


def pytest_runtest_setup(item):
    # called for running each test in 'a' directory
    update_pytest_life_cycle_log("pytest_runtest_setup", "hook")
    print("setting up", item)


def pytest_html_report_title(report):
    from nrobo import EnvKeys, NROBO_CONST
    from nrobo.cli.cli_constants import NREPORT
    import os
    update_pytest_life_cycle_log("pytest_html_report_title", "hook")

    _suffix = NREPORT.DEFAULT_REPORT_TITLE
    _title_env = os.environ[EnvKeys.TITLE]
    if _title_env not in [_suffix] and _title_env:
        _title = os.environ[EnvKeys.TITLE]
    elif os.environ[EnvKeys.APP].lower() not in [NROBO_CONST.NROBO.lower()]:
        _title = f"{os.environ[EnvKeys.APP]} {_suffix}"
    else:
        _title = f"{_suffix}"

    report.title = _title


def pytest_html_results_summary(prefix, summary, postfix, session):
    """Called before adding the summary section to the report"""

    update_pytest_life_cycle_log("pytest_html_results_summary", "hook")


def pytest_html_results_table_header(cells):
    """Called after building results table header."""

    update_pytest_life_cycle_log("pytest_html_results_table_header", "hook")


def pytest_html_results_table_row(report, cells):
    """Called after building results table row."""

    update_pytest_life_cycle_log("pytest_html_results_table_row", "hook")


def pytest_html_results_table_html(report, data):
    """Called after building results table additional HTML."""

    update_pytest_life_cycle_log("pytest_html_results_table_html", "hook")


def pytest_html_duration_format(duration):
    """Called before using the default duration formatting."""

    update_pytest_life_cycle_log("pytest_html_duration_format", "hook")
