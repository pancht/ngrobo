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
import argparse
import os

from nrobo import *
from nrobo.cli import *
from nrobo.cli.cli_constansts import *
from nrobo.cli.install import *
from nrobo.cli.nglobals import *

from nrobo.util.process import *
from nrobo.cli.tools import *

global __REQUIREMENTS__


def parse_cli_args():
    """
    Parse command-line-arguments

    :return:
    """

    # Need to import set_environment method here
    # to handle circular import of partially initialized module
    from nrobo import set_environment
    set_environment()

    # Define nrobo command line argument parser
    parser = argparse.ArgumentParser(
        prog="nrobo",
        description='Run tests through nrobo framework')
    parser.add_argument("-i", f"--{nCLI.INSTALL}", help="Install nRoBo requirements and framework on host system",
                        action="store_true")
    parser.add_argument(f"--{nCLI.APP}", help="Name of application under test. Name should not include special chars "
                                              "and should only having alphanumeric values.")
    parser.add_argument(f"--{nCLI.URL}", help="Application url under test.")
    parser.add_argument(f"--{nCLI.USERNAME}", help="Username for login.", default="")
    parser.add_argument(f"--{nCLI.PASSWORD}", help="Password for login.", default="")
    parser.add_argument("-n", f"--{nCLI.INSTANCES}",
                        help="Number of parallel tests to reduce test-run-time. Default value is 1. Meaning single test at a time in sequence.",
                        default=1)
    parser.add_argument(f"--{nCLI.RERUNS}",
                        help=f"Retries to rerun the failed tests n times specified by --{nCLI.RERUNS} switch.",
                        default=0)
    parser.add_argument(f"--{nCLI.RERUNS_DELAY}",
                        help="Delay time in second(s) before a rerun for a failed test. Default is 1 second.",
                        default=1)
    parser.add_argument(f"--{nCLI.REPORT}",
                        help="Defines type of test report. Two types are supported, Simple HTML or Rich Allure report. Options are <html> | <allure>. Default is <html>",
                        default="html")
    parser.add_argument("-b", f"--{nCLI.BROWSER}", help="""
    Target browser. Default is chrome.
    Options could be:
        {} | {} | 
        {} | {} | {} | {}
    """.format(Browsers.CHROME, Browsers.CHROME_HEADLESS,
               Browsers.FIREFOX, Browsers.FIREFOX_HEADLESS,
               Browsers.SAFARI, Browsers.EDGE))
    parser.add_argument(f"--{nCLI.BROWSER_CONFIG}", help="""
        Path of browser-config-file containing additional options that is/are needed to be applied
        before browser instantiation. Each line in file should contain one option only.
        For example: You want to apply, --start-maximized, chrome switch for chrome browser.
        and if the browser-config-file is names as 'chrome_config.txt', then
        the content of file would be as following:

        --start-maximized

        There will be no conversion taking place by nRoBo! The browser switches will be applied to the browser instance.
        """)
    parser.add_argument("-k", f"--{nCLI.KEY}", help="""
    Only run tests that match the given substring
                        expression. An expression is a python resolvable
                        expression where all names are substring-matched
                        against test names and their parent classes.
                        
                        Example: -k 'test_method or test_other' matches all
                        test.yaml functions and classes whose name contains
                        'test_method' or 'test_other', while -k 'not
                        test_method' matches those that don't contain
                        'test_method' in their names. -k 'not test_method
                        and not test_other' will eliminate the matches.
                        Additionally keywords are matched to classes and
                        functions containing extra names in their
                        'extra_keyword_matches' set, as well as functions
                        which have names assigned directly to them. The
                        matching is case-insensitive.
    """)
    # parser.add_argument("--alluredir", help="""
    #     Path to the directory where Allure Pytest will save the test results.
    #     """)
    parser.add_argument(f"--{nCLI.GRID}", help="""
            Remote Grid server url. Tests will be running on the machine when Grid server is running pointed by Grid url.
            """)
    parser.add_argument("-m", "--marker", help="""
    Only run tests matching given mark expression.
                        For example: -m 'mark1 and not mark2'
    """)
    parser.add_argument("--markers", help="""
    Show markers (builtin, plugin and per-project ones).
    """)
    parser.add_argument("-x", "--exitfirst", help="""
    exit instantly on first error or failed test.yaml.
    """)
    parser.add_argument("--fixtures", help="""
    show available fixtures, sorted by plugin appearance
                        (fixtures with leading '_' are only shown with '-v')
                        """)
    parser.add_argument("--funcargs", help="""
        show available fixtures, sorted by plugin appearance
                            (fixtures with leading '_' are only shown with '-v')
                            """)
    parser.add_argument("--fixtures-per-test.yaml", help="show fixtures per test.yaml")
    parser.add_argument("--pdb", help="""
    start the interactive Python debugger on errors or
                        KeyboardInterrupt.
                        """)
    parser.add_argument("--pdbcls", help="""
    --pdbcls=modulename:classname
                        start a custom interactive Python debugger on
                        errors. For example:
                        --pdbcls=IPython.terminal.debugger:TerminalPdb
                        """)
    parser.add_argument("--trace", help="Immediately break when running each test.yaml.")
    parser.add_argument("--capture", help="""
    --capture=method      per-test.yaml capturing method: one of fd|sys|no|tee-sys.
    """)
    parser.add_argument("-s", help="shortcut for --capture=no.")
    parser.add_argument("--runxfail", help="""
    report the results of xfail tests as if they were
                        not marked
                        """)
    parser.add_argument("-lf", "--last-failed", help="""
    rerun only the tests that failed at the last run (or
                        all if none failed)
                        """)
    parser.add_argument("--ff", "--failed-first", help="""
    run all tests, but run the last failures first.
                        This may re-order tests and thus lead to repeated
                        fixture setup/teardown.
                        """)
    parser.add_argument("--nf", "--new-first", help="""
    run tests from new files first, then the rest of the
                        tests sorted by file mtime
                        """)
    parser.add_argument("--cache-show", help="""
        --cache-show=[CACHESHOW]
                        show cache contents, don't perform collection or
                        tests. Optional argument: glob (default: '*').
                            """)
    parser.add_argument("--cache-clear", help="""
        remove all cache contents at start of test run.
                            """, action="store_true")
    parser.add_argument("--lfnf", help="""
        --lfnf={all,none}, --last-failed-no-failures={all,none}
                        which tests to run with no previously (known)
                        failures.
                            """)
    parser.add_argument("--sw", "--stepwise", help="""
        exit on test failure and continue from last failing
                        test next time
                            """)
    parser.add_argument("--sw-skip", "--stepwise-skip", help="""
        ignore the first failing test but stop on the next
                        failing test
                            """)
    parser.add_argument("--durations", help="""
        --durations=N         show N slowest setup/test durations (N=0 for all).
                            """)
    parser.add_argument("--durations-min", help="""
        Minimal duration in seconds for inclusion in slowest
                        list. Default 0.005
                            """)
    parser.add_argument("-v", "--verbose", help="""
        increase verbosity.
                            """)
    parser.add_argument("--no-header", help="""
        disable header
                            """)
    parser.add_argument("--no-summary", help="""
        disable summary
        """)
    parser.add_argument("-q", "--quiet", help="""
        decrease verbosity.
                            """, action="store_true")
    parser.add_argument("--verbosity", help="""
        --verbosity=VERBOSE   
        set verbosity. Default is 0.
                            """)
    parser.add_argument("-r", help="""
        -r chars              show extra test summary info as specified by chars:
                        (f)ailed, (E)rror, (s)kipped, (x)failed, (X)passed,
                        (p)assed, (P)assed with output, (a)ll except passed
                        (p/P), or (A)ll. (w)arnings are enabled by default
                        (see --disable-warnings), 'N' can be used to reset
                        the list. (default: 'fE').
                            """)
    parser.add_argument("--disable-warnings", "--disable-pytest-warnings", help="""
            disable warnings summary
            """)
    parser.add_argument("-l", "--showlocals", help="""
            show locals in tracebacks (disabled by default).
            """)
    parser.add_argument("--tb", help="""
            --tb=style.            traceback print mode
                        (auto/long/short/line/native/no).
            """)
    parser.add_argument("--show-capture", help="""
           --show-capture={no,stdout,stderr,log,all}.
                        Controls how captured stdout/stderr/log is shown on
                        failed tests. Default is 'all'.
            """)
    parser.add_argument("--full-trace", help="""
            don't cut any tracebacks (default is to cut).
            """)
    parser.add_argument("--color", help="""
            --color=color. color terminal output (yes/no/auto).
            """)
    parser.add_argument("--code-highlight", help="""
            --code-highlight={yes,no}.
                        Whether code should be highlighted (only if --color
                        is also enabled)
            """)
    parser.add_argument("--pastebin", help="""
            --pastebin=mode.      send failed|all info to bpaste.net pastebin service.
            """)
    parser.add_argument("--junit-xml", help="""
            --junit-xml=path.      create junit-xml style report file at given path.
            """)
    parser.add_argument("--junit-prefix", help="""
            --junit-prefix=str. prepend prefix to classnames in junit-xml output
            """)
    parser.add_argument("-W", "--pythonwarnings", help="""
            -W PYTHONWARNINGS, --pythonwarnings=PYTHONWARNINGS
                        set which warnings to report, see -W option of
                        python itself.
            """)
    parser.add_argument("--maxfail", help="""
            --maxfail=num. exit after first num failures or errors.
            """)
    parser.add_argument("--strict-config", help="""
            any warnings encountered while parsing the `pytest`
                        section of the configuration file raise errors.
            """)
    parser.add_argument("--strict-markers", help="""
            markers not registered in the `markers` section of
                        the configuration file raise errors.
            """)
    parser.add_argument("--strict", help="""
            (deprecated) alias to --strict-markers.
            """)
    parser.add_argument("-c", help="""
            -c file. load configuration from `file` instead of trying to
                        locate one of the implicit configuration files.
            """)
    parser.add_argument("--continue-on-collection-errors", help="""
            --continue-on-collection-errors.
                        Force test execution even if collection errors
                        occur.
            """)
    parser.add_argument("--rootdir", help="""
            --rootdir=ROOTDIR. Define root directory for tests. Can be relative
                        path: 'root_dir', './root_dir',
                        'root_dir/another_dir/'; absolute path:
                        '/home/user/root_dir'; path with variables:
                        '$HOME/root_dir'.
            """)
    parser.add_argument("--co", "--collect-only", help="""
            only collect tests, don't execute them.
            """, action="store_true")
    parser.add_argument("--pyargs", help="""
            try to interpret all arguments as python packages.
            """)
    parser.add_argument("--ignore", help="""
            --ignore=path. ignore path during collection (multi-allowed).
            """)
    parser.add_argument("--ignore-glob", help="""
            --ignore-glob=path. ignore path pattern during collection (multi-
                        allowed).
            """)
    parser.add_argument("--deselect", help="""
            --deselect=nodeid_prefix. deselect item (via node id prefix) during collection
                        (multi-allowed).
            """)
    parser.add_argument("--confcutdir", help="""
            --confcutdir=dir. only load conftest.py's relative to specified dir.
            """)
    parser.add_argument("--noconftest", help="""
            Don't load any conftest.py files.
            """)
    parser.add_argument("--keep-duplicates", help="""
            Keep duplicate tests.
            """)
    parser.add_argument("--collect-in-virtualenv", help="""
                    Don't ignore tests in a local virtualenv directory
                    """)
    parser.add_argument("--import-mode", help="""
                    --import-mode={prepend,append,importlib}. prepend/append to sys.path when importing test
                    """)
    parser.add_argument("--doctest-modules", help="""
                    run doctests in all .py modules
                    """)
    parser.add_argument("--doctest-report", help="""
                    --doctest-report={none,cdiff,ndiff,udiff,only_first_failure}. 
                    choose another output format for diffs on doctest
                        failure
                    """)
    parser.add_argument("--doctest-glob", help="""
                    --doctest-glob=pat. doctests file matching pattern, default: test*.txt
                    """)
    parser.add_argument("--doctest-ignore-import-errors", help="""
                    ignore doctest ImportErrors
                    """)
    parser.add_argument("--doctest-continue-on-failure", help="""
                    for a given doctest, continue to run after the first
                        failure
                    """)
    parser.add_argument("--basetemp", help="""
                    --basetemp=dir. base temporary directory for this test run.(warning:
                        this directory is removed if it exists)
                    """)
    parser.add_argument("-V", "--version", help="""
                    display pytest version and information about
                        plugins.When given twice, also display information
                        about plugins.
                    """)
    # parser.add_argument("-h", "--help", help="""
    #                 show help message and configuration info
    #                 """)
    parser.add_argument("-p", help="""
                    -p name               early-load given plugin module name or entry point
                        (multi-allowed).
                        To avoid loading of plugins, use the `no:` prefix,
                        e.g. `no:doctest`.
                    """)
    parser.add_argument("--trace-config", help="""
                    trace considerations of conftest.py files.
                    """)
    parser.add_argument("--debug", help="""
                    store internal tracing debug information in
                        'pytestdebug.log'.
                    """)
    parser.add_argument("-o", "--override-ini", help="""
                    -o OVERRIDE_INI, --override-ini=OVERRIDE_INI
                        override ini option with "option=value" style, e.g.
                        `-o xfail_strict=True -o cache_dir=cache`.
                    """)
    parser.add_argument("--assert", help="""
                    --assert=MODE         Control assertion debugging tools.
                        'plain' performs no assertion debugging.
                        'rewrite' (the default) rewrites assert statements
                        in test modules on import to provide assert
                        expression information.
                    """)
    parser.add_argument("--setup-only", help="""
                    only setup fixtures, do not execute tests.
                    """)
    parser.add_argument("--setup-show", help="""
                    show setup of fixtures while executing tests.
                    """)
    parser.add_argument("--setup-plan", help="""
                    show what fixtures and tests would be executed but
                        don't execute anything.
                    """)
    parser.add_argument("--log-level", help="""
                    --log-level=LEVEL     level of messages to catch/display.
                        Not set by default, so it depends on the root/parent
                        log handler's effective level, where it is "WARNING"
                        by default.
                    """)
    parser.add_argument("--log-format", help="""
                    --log-format=LOG_FORMAT
                        log format as used by the logging module.
                    """)
    parser.add_argument("--log-date-format", help="""
                    --log-date-format=LOG_DATE_FORMAT
                        log date format as used by the logging module.
                    """)
    parser.add_argument("--log-cli-level", help="""
                    --log-cli-level=LOG_CLI_LEVEL
                        cli logging level.
                    """)
    parser.add_argument("--log-cli-format", help="""
                    --log-cli-format=LOG_CLI_FORMAT
                        log format as used by the logging module.
                    """)
    parser.add_argument("--log-cli-date-format", help="""
                    --log-cli-date-format=LOG_CLI_DATE_FORMAT
                        log date format as used by the logging module.
                    """)
    parser.add_argument("--log-file", help="""
                    --log-file=LOG_FILE   path to a file when logging will be written to.
                    """)
    parser.add_argument("--log-file-level", help="""
                    --log-file-level=LOG_FILE_LEVEL
                        log file logging level.
                    """)
    parser.add_argument("--log-file-format", help="""
                    --log-file-format=LOG_FILE_FORMAT
                        log format as used by the logging module.
                    """)
    parser.add_argument("--log-file-date-format", help="""
                    --log-file-date-format=LOG_FILE_DATE_FORMAT
                        log date format as used by the logging module.
                    """)
    parser.add_argument("--log-auto-indent", help="""
                    --log-auto-indent=LOG_AUTO_INDENT
                        Auto-indent multiline messages passed to the logging
                        module. Accepts true|on, false|off or an integer.
                    """)

    # parse command line arguments
    args = parser.parse_args()

    # process each nrobo cli arguments
    if args.install:
        # Install dependencies
        with console.status(f"[{STYLE.TASK}]Installing dependencies...\n"):
            # install_nrobo(None)
            exit(1)

    # build pytest launcher command
    command = ["pytest"]  # start with programme name
    command_builder_notes = []  # list for storing notes during cli switch processing

    # process other switches
    with console.status(f"[{STYLE.TASK}]Parsing command-line-args...\n"):
        for key, value in args.__dict__.items():
            """break each arg into key, value pairs and process each key"""

            # handle hyphens in key names since argparser replaces hyphes with underscore
            # while parsing cli args
            # this, replace hyphen with dash if present in key
            key = key.replace('_', '-')

            if value:
                """if key has value, then only proceed with current key"""
                if type(value) is bool:
                    """if a bool key is found, only add key to the launcher command, not the value
                        and proceed with next key"""
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
                        command.append(f"--{key}")
                        command.append(str(value))
                elif key in nCLI.ARGS:
                    """process nrobo specific keys"""
                    if key in [nCLI.APP, nCLI.URL, nCLI.USERNAME, nCLI.PASSWORD, nCLI.BROWSER_CONFIG]:
                        if key == nCLI.APP:
                            os.environ[EnvKeys.APP] = value
                        elif key == nCLI.URL:
                            os.environ[EnvKeys.URL] = value
                        elif key == nCLI.USERNAME:
                            os.environ[EnvKeys.USERNAME] = value
                        elif key == nCLI.PASSWORD:
                            os.environ[EnvKeys.PASSWORD] = value

                        # add keys to launcher command
                        command.append(f"--{key}")
                        command.append(str(value))

                    if key == nCLI.BROWSER:
                        os.environ[EnvKeys.BROWSER] = value
                        raise_exception_if_browser_not_supported(os.environ[EnvKeys.BROWSER])
                        command.append(f"--{key}")
                        command.append(str(value))
                    elif key == nCLI.KEY:
                        command.append(f"-k")
                        command.append(value)
                    elif key == nCLI.INSTANCES:
                        command.append(f"-n")
                        command.append(str(value))
                    elif key == nCLI.RERUNS:
                        command.append(f"--{key}")
                        command.append(value)
                    elif key == nCLI.REPORT:
                        if str(value).lower() not in [NREPORT.HTML, NREPORT.ALLURE]:
                            console.print(f"Incorrect report type! Valid report types are html | allure.")
                            exit(1)
                        if str(value).lower() in NREPORT.HTML:
                            command.append(f"--{NREPORT.HTML}")
                            command.append(f"{NREPORT.HTML_REPORT_PATH}")
                        elif str(value).lower() in NREPORT.ALLURE:
                            command.append(f"--{NREPORT.HTML}")
                            command.append(f"{NREPORT.HTML_REPORT_PATH}")
                            command.append(f"--alluredir")
                            command.append(f"{NREPORT.ALLURE_REPORT_PATH}")
                            # command.append(f"--allure-no-capture")

                            # Doc: https://allurereport.org/docs/gettingstarted-installation/
                    else:
                        command.append(f"--{key}")
                        command.append(value)

    # Debug code line
    # print(command)
    # exit(1)

    if not args.browser:
        """browser not provided"""
        command.append(f"--{nCLI.BROWSER}")
        command.append(f"{Browsers.CHROME}")
        command_builder_notes.append(
            f"[{STYLE.HLOrange}]\t--browser switch was missing. Default browser {Browsers.CHROME} is selected...")
    if not args.rootdir:
        command_builder_notes.append(
            f"[{STYLE.HLOrange}]\t--rootdir switch was missing. Default test path <current-dir> is selected...")

    # Add single parameter commands by default
    # That make sense.
    # command.append("-V") # This setting is not working. With this, tests are even not running at all.
    for k, v in nCLI.DEFAULT_ARGS.items():
        command = command + v

    with console.status(f"[{STYLE.TASK}]:smiley: Running tests...\n"):
        if os.environ[EnvKeys.ENVIRONMENT] in [Environment.DEVELOPMENT]:
            console.print(f"[{STYLE.INFO}]{command}")
        terminal(command)

        if args.report and args.report == NREPORT.ALLURE:
            terminal([NREPORT.ALLURE, f"serve", NREPORT.ALLURE_REPORT_PATH])

    with console.status(f"[{STYLE.TASK}]Test report is ready! Please analyze results...\n"):
        if len(command_builder_notes) == 1:
            console.print(f"[{STYLE.HLOrange}]Note:")
        elif len(command_builder_notes) >= 2:
            console.print(f"[{STYLE.HLOrange}]Notes:")

        if command_builder_notes:
            for note in command_builder_notes:
                console.print(note)
