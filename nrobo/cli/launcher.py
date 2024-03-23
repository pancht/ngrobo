"""
=====================CAUTION=======================
DO NOT DELETE THIS FILE SINCE IT IS PART OF NROBO
FRAMEWORK AND IT MAY CHANGE IN THE FUTURE UPGRADES
OF NROBO FRAMEWORK. THUS, TO BE ABLE TO SAFELY UPGRADE
TO LATEST NROBO VERSION, PLEASE DO NOT DELETE THIS
FILE OR ALTER ITS LOCATION OR ALTER ITS CONTENT!!!
===================================================

Launcher for nRoBo framework.

@author: Panchdev Singh Chauhan
@email: erpanchdev@gmail.com
"""
import os
import time

from nrobo import *
from nrobo.cli import *
from nrobo.cli.cli_constants import *
from nrobo.cli.install import *
from nrobo.cli.install import install_nrobo
from nrobo.cli.nglobals import *
from nrobo.util.platform import PLATFORMS

from nrobo.util.process import *
from nrobo.cli.nrobo_args import SHOW_ONLY_SWITCHES, BoolArgs
import nrobo.cli.detection as detect

global __REQUIREMENTS__


def launcher_command(exit_on_failure=True):
    """Prepares nrobo launcher command
       by parsing command line switches
       in order to trigger test suite launch.

       Returns [str], args: command list, actual args
    """

    # Need to import set_environment method here
    # to handle circular import of partially initialized module
    from nrobo import set_environment
    import argparse

    set_environment()

    # parse command line arguments
    from nrobo.cli.nrobo_args import nrobo_cli_parser
    args = nrobo_cli_parser(exit_on_failure=exit_on_failure)

    # process each nrobo cli arguments
    if args.install:
        # Install dependencies
        with console.status(f"[{STYLE.TASK}]Installing dependencies...\n"):
            install_nrobo(None)
            return None, None, None

    if args.VERSION:
        # show version
        from nrobo import __version__
        console.print(f"nrobo {__version__}\n")
        return None, None, None

    if args.suppress:
        # suppress upgrade prompt
        os.environ[EnvKeys.SUPPRESS_PROMPT] = '0'

    if args.version:
        result = terminal(['pytest', f"--version"], debug=True, text=True, capture_output=True)
        console.print(f"{result.stdout}")
        return None, None, None

    if args.npm and args.npm in PACKAGES.APPIUM:
        # command = ['sudo', 'npm', 'cache', 'clean', '-f']
        # terminal(command=command, debug=True)
        # command = ['sudo', 'npm', 'install', '-g', 'n']
        # terminal(command=command, debug=True)
        # command = ['sudo', 'n', 'stable']
        # terminal(command=command, debug=True)
        # --------------------------------------
        # Steps to upgrade node
        # 1. sudo npm cache clean -f
        # 2. sudo npm install -g n
        # 3. sudo n stable
        # --------------------------------------
        # Update node using brew
        # brew uninstall node
        # brew install node
        # Remove any file or dir that are being shown when run node -v command after uninstalling node
        command = ['sudo', nCLI.NPM, 'install', '-g', args.npm, '--unsafe-perm=true', '--allow-root']
        terminal(command=command, debug=True)

        exit(0)

    elif args.npm and args.npm not in PACKAGES.APPIUM:
        console.print(f"[{STYLE.HLRed}]{args.npm} package support is not in [{STYLE.HLOrange}]nRoBo[/].[/]"
                      f"\nSupported packages are [{STYLE.HLOrange}]{PACKAGES.APPIUM}[/].")
        exit(1)

    # build pytest launcher command
    command = ["pytest"]  # start with programme name
    command_builder_notes = []  # list for storing notes during cli switch processing
    override_defaults = []

    # process other switches
    with console.status(f"[{STYLE.TASK}]Parsing command-line-args...\n"):
        for key, value in args.__dict__.items():
            """break each arg into key, value pairs and process each key"""

            # handle hyphens in key names since argparser replaces hyphes with underscore
            # while parsing cli args
            # this, replace hyphen with dash if present_release in key
            key = key.replace('_', '-')

            if value:
                """if key has value, then only proceed with current key"""

                if type(value) is bool or isinstance(value, bool):
                    """if a bool key is found, only add key to the launcher command, not the value
                        and proceed with next key"""
                    if key == nCLI.FULLPAGE_SCREENSHOT or key == BoolArgs.PYARGS:
                        continue
                    elif key == nCLI.SUPPRESS:
                        os.environ[EnvKeys.SUPPRESS_PROMPT] = "1"
                    elif key in SHOW_ONLY_SWITCHES:
                        terminal(['pytest', f"--{key}"], debug=True)
                        return None, None, None
                    elif key == args.version:
                        terminal(['pytest', f"--{key}"], debug=True)
                        exit()
                    elif key == 'capture-no':
                        command.append('-s')
                        continue
                    elif key == 'extra-summary':
                        command.append('-r')
                        continue
                    else:
                        command.append(f"--{key}")
                        continue
                elif key not in nCLI.ARGS.keys():
                    """process special short keys(single letter keys) that does not have corresponding long key"""
                    if key == "c":
                        "process key==-c"
                        command.append(f"-{key}")
                        command.append(str(value))
                    else:
                        """simply add long keys to launcher command"""
                        if key == nCLI.TARGET or key == nCLI.FILES or key == BoolArgs.PYARGS:
                            continue  # DO NOT ADD TO PYTEST LAUNCHER

                        if f"--{key}" in nCLI.DEFAULT_ARGS:
                            override_defaults.append(f"--{key}")

                        command.append(f"--{key}")
                        command.append(str(value))
                elif key in nCLI.ARGS:
                    """process nrobo specific keys"""
                    if key in [nCLI.URL, nCLI.USERNAME, nCLI.PASSWORD, nCLI.BROWSER_CONFIG]:
                        if key == nCLI.URL:
                            os.environ[EnvKeys.URL] = value
                        elif key == nCLI.USERNAME:
                            os.environ[EnvKeys.USERNAME] = value
                        elif key == nCLI.PASSWORD:
                            os.environ[EnvKeys.PASSWORD] = value

                        # add keys to launcher command
                        command.append(f"--{key}")
                        command.append(str(value))
                        continue

                    if key == nCLI.BROWSER:
                        os.environ[EnvKeys.BROWSER] = value
                        raise_exception_if_browser_not_supported(os.environ[EnvKeys.BROWSER])
                        if args.fullpagescreenshot:
                            command.append(f"--{nCLI.BROWSER}")
                            command.append(str(Browsers.CHROME_HEADLESS))
                            if f"--{nCLI.FULLPAGE_SCREENSHOT}" not in command:
                                command.append(f"--{nCLI.FULLPAGE_SCREENSHOT}")
                            command_builder_notes.append(
                                f"[{STYLE.HLOrange}]\tOverride --browser switch value with {Browsers.CHROME_HEADLESS} because fullpagescreenshot switch is enabled...")
                        else:
                            command.append(f"--{key}")
                            command.append(str(value))
                        continue
                    elif key == nCLI.MARKER:
                        command.append(f"-m")
                        command.append(str(value))
                        continue
                    elif key == nCLI.KEY:
                        command.append(f"-k")
                        command.append(value)
                        continue
                    elif key == nCLI.INSTANCES:
                        command.append(f"-n")
                        command.append(str(value))
                    elif key == nCLI.RERUNS:
                        command.append(f"--{key}")
                        command.append(value)
                        continue
                    elif key == nCLI.REPORT:
                        if str(value).lower() not in [NREPORT.HTML, NREPORT.ALLURE]:
                            console.print(f"Incorrect report type! Valid report types are html | allure.")
                            exit(1)
                        if str(value).lower() in NREPORT.HTML:
                            command.append(f"--{NREPORT.HTML}")
                            command.append(f"{Path(NREPORT.REPORT_DIR) / args.target}")
                        elif str(value).lower() in NREPORT.ALLURE:
                            command.append(f"--{NREPORT.HTML}")
                            command.append(f"{Path(NREPORT.REPORT_DIR) / args.target}")
                            # command.append(f"--allure-no-capture")

                            # Doc: https://allurereport.org/docs/gettingstarted-installation/
                    else:
                        if key == nCLI.TARGET or key == nCLI.FILES:
                            continue  # DO NOT ADD TO PYTEST LAUNCHER

                        if key in [nCLI.APP, nCLI.REPORT_TITLE]:
                            command.append(f"--{key}")
                            command.append(str(value).replace(CONST.SPACE, CONST.UNDERSCORE))
                        else:
                            command.append(f"--{key}")
                            command.append(value)

    if not args.browser:
        """browser not provided"""

        if args.fullpagescreenshot:
            command.append(f"--{nCLI.BROWSER}")
            command.append(str(Browsers.CHROME_HEADLESS))
            command.append(f"--{nCLI.FULLPAGE_SCREENSHOT}")
            command_builder_notes.append(
                f"[{STYLE.HLOrange}]\t--browser switch was missing. Default browser {Browsers.CHROME_HEADLESS} is "
                f"selected because fullpagescreenshot switch is enabled...")
        else:
            command.append(f"--{nCLI.BROWSER}")
            command.append(f"{Browsers.CHROME}")
            command_builder_notes.append(
                f"[{STYLE.HLOrange}]\t--browser switch was missing. Default browser {Browsers.CHROME} is selected...")
    if not args.rootdir:
        command_builder_notes.append(
            f"[{STYLE.HLOrange}]\t--rootdir switch was missing. Default test path <current-dir> is selected...")

    if not args.alluredir:
        command.append(f"--alluredir")
        command.append(f"{NREPORT.ALLURE_REPORT_PATH}")

    if not args.pythonwarnings and args.browser == Browsers.ANTI_BOT_CHROME:
        # Suppress DeprecationWarning when running in undetected_chromedriver
        # Due to the following error:
        #  /Users/einsteinpanchdev/webdev/nrobo/venv/lib/python3.12/site-packages/undetected_chromedriver/__init__.py:363:
        #  DeprecationWarning: 'locale.getdefaultlocale' is deprecated and slated for removal in Python 3.15.
        #  Use setlocale(), getencoding() and getlocale() instead.
        command.append(f"-W")
        command.append(f"ignore::DeprecationWarning")

    # Add single parameter commands by default
    # That make sense.
    # command.append("-V") # This setting is not working. With this, tests are even not running at all.

    for k, v in nCLI.DEFAULT_ARGS.items():
        if k in override_defaults:
            continue  # skip adding k,v pair if it is already added by arg parse
        command = command + v

    # Process files
    if args.files:
        files = args.files
        [command.append(f) for f in files]

    # Process files
    if args.pyargs:
        command.append(f"--{BoolArgs.PYARGS}")
        files = args.pyargs
        [command.append(f) for f in files]

    if args.pyargs and args.files:
        # Error
        console.print(f"[{STYLE.HLRed}]--{BoolArgs.PYARGS} and --{nCLI.FILES} "
                      f"switch can not be used in combination![/]")
        exit(1)

    # select tests directory
    if not args.files:
        if args.appium:
            command.append(str(NROBO_PATHS.EXEC_DIR / NROBO_PATHS.TESTS / NROBO_PATHS.MOBILE))
        else:
            command.append(str(NROBO_PATHS.EXEC_DIR / NROBO_PATHS.TESTS / NROBO_PATHS.WEB))

    return command, args, command_builder_notes


def launch_nrobo():
    """Parse command-line-arguments"""

    command, args, command_builder_notes = launcher_command()

    if command is None and args is None and command_builder_notes is None:
        return

    with console.status(f"[{STYLE.TASK}]:smiley: Running tests. Press Ctrl+C to exit nRoBo.\n"):

        if detect.developer_machine():
            console.print(f"[{STYLE.INFO}]{command}")

        if args.report and args.report == NREPORT.ALLURE:  # test if needed allure report
            create_allure_report(command)
        else:
            create_simple_html_report(command)

        print_notes(command_builder_notes)


def create_allure_report(command: list) -> int:
    """prepares allure report based on pytest launcher <command>"""

    console.print(f"[{STYLE.HLGreen}]Running tests and preparing allure report")

    _ALLURE_DIR = '--alluredir'
    allure_results = (Path(os.environ[EnvKeys.EXEC_DIR]) / "results" / "allure-results")
    if _ALLURE_DIR in command:
        allure_results = command[command.index(_ALLURE_DIR) + 1]
    terminal(command + [_ALLURE_DIR, allure_results], debug=True, use_os_system_call=True)

    if _ALLURE_DIR in command:
        allure_generated_report = Path(allure_results) / "allure-report"
    else:
        allure_generated_report = allure_results.parent / "allure-report"

    console.print(f"[{STYLE.HLGreen}]Preparing allure report")

    terminal([NREPORT.ALLURE, "generate", "--name", "nRoBo TEST REPORT", "-o", allure_generated_report, "--clean",
              allure_results], use_os_system_call=True)

    terminal([NREPORT.ALLURE, "serve", allure_results], use_os_system_call=True)


def create_simple_html_report(command: list) -> int:
    """prepares simple html report based on pytest launcher command"""
    console.print(f"[{STYLE.HLGreen}]Running tests and preparing html report")

    return_code = terminal(command, debug=True, use_os_system_call=True)
    console.rule(
        f"[{STYLE.HLOrange}]Report is ready at file://{Path(os.environ[EnvKeys.EXEC_DIR]) / Path(NREPORT.REPORT_DIR) / NREPORT.HTML_REPORT_NAME}")

    return return_code


def print_notes(notes: list):
    """print notes"""

    if len(notes) == 1:
        console.print(f":warning:[{STYLE.HLOrange}] Note:")
    elif len(notes) >= 2:
        console.print(f":warning:[{STYLE.HLOrange}] Notes:")

    if notes:
        for note in notes:
            console.print(note)
