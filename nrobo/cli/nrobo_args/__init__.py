"""
=====================CAUTION=======================
DO NOT DELETE THIS FILE SINCE IT IS PART OF NROBO
FRAMEWORK AND IT MAY CHANGE IN THE FUTURE UPGRADES
OF NROBO FRAMEWORK. THUS, TO BE ABLE TO SAFELY UPGRADE
TO LATEST NROBO VERSION, PLEASE DO NOT DELETE THIS
FILE OR ALTER ITS LOCATION OR ALTER ITS CONTENT!!!
===================================================

Definitions of nRoBo command line arguments.


@author: Panchdev Singh Chauhan
@email: erpanchdev@gmail.com
"""

# Define nrobo command line argument parser
import argparse

from nrobo.cli.cli_constants import nCLI, NREPORT
from nrobo.cli.nglobals import Browsers


class BoolArgs:
    PYARGS = "pyargs"


BOOL_SWITCHES = [
    f"--{nCLI.INSTALL}",
    f"--{nCLI.VERSION}",
    f"--{nCLI.SUPPRESS}",
    "--markers",
    "--exitfirst",
    "--fixtures",
    "--funcargs",
    "--fixtures-per-test",
    "--pdb",
    "--trace",
    "-s",
    "--runxfail",
    "--last-failed",
    "--failed-first",
    "--ff",
    "--nf",
    "--new-first",
    "--cache-clear",
    "--sw",
    "--stepwise",
    "--sw-skip",
    "--stepwise-skip",
    "--verbose",
    "--no-header",
    "--no-summary",
    "--quiet",
    "--disable-warnings",
    "--disable-pytest-warnings",
    "--showlocals",
    "--full-trace",
    "--strict-config",
    "--strict-markers",
    "--strict",
    "--continue-on-collection-errors",
    "--co",
    "--collect-only",
    f"--{BoolArgs.PYARGS}",
    "--noconftest",
    "--keep-duplicates",
    "--collect-in-virtualenv",
    "--doctest-modules",
    "--doctest-ignore-import-errors",
    "--doctest-continue-on-failure",
    "--version",
    "--trace-config",
    "--debug",
    "--override-ini",
    "--setup-only",
    "--setup-show",
    "--setup-plan",
]

SHOW_ONLY_SWITCHES = [
    "markers",
    "fixtures",
    "funcargs",
    "fixtures-per-test",
    "collect-only",
    "version",
    "setup-plan",
    "co"
]


def nrobo_cli_parser(exit_on_failure=True):
    """Define nRoBo command line arguments

       and return args."""

    parser = argparse.ArgumentParser(
        prog="nrobo",
        description='CLI Switches of nRoBo Test Automation framework', exit_on_error=exit_on_failure)
    # Add NPM command line support
    parser.add_argument(f"--{nCLI.NPM}", help=f"Executed given npm command."
                                                         f"\n Usage:"
                                                         f"\n       --npm <package>"
                                                         f"\n "
                                                         f"\n  Example:"
                                                         f"\n       nrobo --npm appium"
                                                         f"\n Will install appium dependency as global package")
    parser.add_argument(f"--{nCLI.APPIUM}", help=f"Tells nRoBo to trigger via appium client",
                        action="store_true", default=False)
    parser.add_argument(f"--{nCLI.CAP}", help="File name of appium capability file."
                                              "nRoBo will search the given capability file "
                                              "in appium directory under project root folder.")

    # Add nrobo command line args
    parser.add_argument("-i", f"--{nCLI.INSTALL}", help="Install nRoBo requirements and framework on host system",
                        action="store_true")
    parser.add_argument(f"--{nCLI.APP}", help="Name of application under test. Name should not include special chars "
                                              "and should only having alphanumeric values.", default="nRoBo")
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
    parser.add_argument(f"--{nCLI.REPORT_TITLE}",
                        help="Defines HTML Report title.",
                        default=f"{NREPORT.DEFAULT_REPORT_TITLE}")
    parser.add_argument(f"--{nCLI.TARGET}",
                        help="Report name", default=f"{NREPORT.HTML_REPORT_NAME}")
    parser.add_argument(f"--{nCLI.VERSION}",
                        help="Shows nRoBo version", action="store_true")
    parser.add_argument(f"--{nCLI.SUPPRESS}",
                        help="Suppresses upgrade prompt on each test run", action="store_true", default=False)
    parser.add_argument(f"--{nCLI.FULLPAGE_SCREENSHOT}",
                        help="Take full page screenshot", action="store_true", default=False)
    parser.add_argument("-b", f"--{nCLI.BROWSER}", help="""
        Target browser. Default is chrome.
        Options could be:
            {} | {} | {} |
            {} | {} | {} | {}
        """.format(Browsers.CHROME, Browsers.CHROME_HEADLESS, Browsers.ANTI_BOT_CHROME,
                   Browsers.FIREFOX, Browsers.FIREFOX_HEADLESS,
                   Browsers.SAFARI, Browsers.EDGE))
    parser.add_argument(f"--{nCLI.FILES}",
                        help="Input files", nargs='+')
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
    parser.add_argument("--alluredir", help="""
        Path to the directory where Allure Pytest will save the test results.
        """)
    parser.add_argument(f"--{nCLI.GRID}", help="""
                Remote Grid server url. Tests will be running on the machine when Grid server is running pointed by Grid url.
                """)
    parser.add_argument("-m", "--marker", help="""
        Only run tests matching given mark expression.
        For example: -m 'mark1 and not mark2'
        Following ready to use markers are registered by nRoBo framework: sanity, regression, ui, api, nogui, and unit.
        
        Usage:
        @pytest.mark.regression
        def test_method1(self, driver, logger):
            ...
            
        @pytest.mark.ui
        def test_method1(self, driver, logger):
            ...
                       
        Then,
        
        To only run regression tests, following switch can be used: 
        nrobo --marker regression OR nrobo -m regression     
        """)
    parser.add_argument("--markers", help="""
        Show markers (builtin, plugin and per-project ones).
        """, action="store_true")
    parser.add_argument("-x", "--exitfirst", help="""
        exit instantly on first error or failed test.yaml.
        """, action="store_true")
    parser.add_argument("--fixtures", help="""
        show available fixtures, sorted by plugin appearance
                            (fixtures with leading '_' are only shown with '-v')
                            """, action="store_true")
    parser.add_argument("--funcargs", help="""
            show available fixtures, sorted by plugin appearance
                                (fixtures with leading '_' are only shown with '-v')
                                """, action="store_true")
    parser.add_argument("--fixtures-per-test", help="show fixtures per test.yaml", action="store_true")
    parser.add_argument("--pdb", help="""
        start the interactive Python debugger on errors or
                            KeyboardInterrupt.
                            """, action="store_true")
    parser.add_argument("--pdbcls", help="""
        --pdbcls=modulename:classname
                            start a custom interactive Python debugger on
                            errors. For example:
                            --pdbcls=IPython.terminal.debugger:TerminalPdb
                            """)
    parser.add_argument("--trace", help="Immediately break when running each test.yaml.", action="store_true")
    parser.add_argument("--capture", help="""
        --capture=method      per-test.yaml capturing method: one of fd|sys|no|tee-sys.
        """)
    parser.add_argument("-s", f"--capture-no", help="shortcut for --capture=no.", action="store_true")
    parser.add_argument("--runxfail", help="""
        report the results of xfail tests as if they were
                            not marked
                            """, action="store_true")
    parser.add_argument("-lf", "--last-failed", help="""
        rerun only the tests that failed at the last run (or
                            all if none failed)
                            """, action="store_true")
    parser.add_argument("--ff", "--failed-first", help="""
        run all tests, but run the last failures first.
                            This may re-order tests and thus lead to repeated
                            fixture setup/teardown.
                            """, action="store_true")
    parser.add_argument("--nf", "--new-first", help="""
        run tests from new files first, then the rest of the
                            tests sorted by file mtime
                            """, action="store_true")
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
                                """, action="store_true")
    parser.add_argument("--sw-skip", "--stepwise-skip", help="""
            ignore the first failing test but stop on the next
                            failing test
                                """, action="store_true")
    parser.add_argument("--durations", help="""
            --durations=N         show N slowest setup/test durations (N=0 for all).
                                """)
    parser.add_argument("--durations-min", help="""
            Minimal duration in seconds for inclusion in slowest
                            list. Default 0.005
                                """, default='0.005')
    parser.add_argument("-v", "--verbose", help="""
            increase verbosity.
                                """, action="store_true")
    parser.add_argument("--no-header", help="""
            disable header
                                """, action="store_true")
    parser.add_argument("--no-summary", help="""
            disable summary
            """, action="store_true")
    parser.add_argument("-q", "--quiet", help="""
            decrease verbosity.
                                """, action="store_true")
    parser.add_argument("--verbosity", help="""
            --verbosity=VERBOSE   
            set verbosity. Default is 0.
                                """, default='0')
    parser.add_argument("-r", "--extra-summary", help="""
            -r chars              show extra test summary info as specified by chars:
                            (f)ailed, (E)rror, (s)kipped, (x)failed, (X)passed,
                            (p)assed, (P)assed with output, (a)ll except passed
                            (p/P), or (A)ll. (w)arnings are enabled by default
                            (see --disable-warnings), 'N' can be used to reset
                            the list. (default: 'fE').
                                """)
    parser.add_argument("--disable-warnings", "--disable-pytest-warnings", help="""
                disable warnings summary
                """, action="store_true")
    parser.add_argument("-l", "--showlocals", help="""
                show locals in tracebacks (disabled by default).
                """, action="store_true")
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
                """, action="store_true")
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
                """, action="store_true")
    parser.add_argument("--strict-markers", help="""
                markers not registered in the `markers` section of
                            the configuration file raise errors.
                """, action="store_true")
    parser.add_argument("--strict", help="""
                (deprecated) alias to --strict-markers.
                """, action="store_true")
    parser.add_argument("-c", "--configuration", help="""
                -c file. load configuration from `file` instead of trying to
                            locate one of the implicit configuration files.
                """)
    parser.add_argument("--continue-on-collection-errors", help="""
                --continue-on-collection-errors.
                            Force test execution even if collection errors
                            occur.
                """, action="store_true")
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
    parser.add_argument(f"--{BoolArgs.PYARGS}", nargs='+', help="""
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
                """, action="store_true")
    parser.add_argument("--keep-duplicates", help="""
                Keep duplicate tests.
                """, action="store_true")
    parser.add_argument("--collect-in-virtualenv", help="""
                        Don't ignore tests in a local virtualenv directory
                        """, action="store_true")
    parser.add_argument("--import-mode", help="""
                        --import-mode={prepend,append,importlib}. prepend/append to sys.path when importing test
                        """)
    parser.add_argument("--doctest-modules", help="""
                        run doctests in all .py modules
                        """, action="store_true")
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
                        """, action="store_true")
    parser.add_argument("--doctest-continue-on-failure", help="""
                        for a given doctest, continue to run after the first
                            failure
                        """, action="store_true")
    parser.add_argument("--basetemp", help="""
                        --basetemp=dir. base temporary directory for this test run.(warning:
                            this directory is removed if it exists)
                        """)
    parser.add_argument("-V", "--version", help="""
                        display pytest version and information about
                            plugins.When given twice, also display information
                            about plugins.
                        """, action="store_true")
    # parser.add_argument("-h", "--help", help="""
    #                 show help message and configuration info
    #                 """)
    parser.add_argument("-p", "--plugin-module", help="""
                        -p name               early-load given plugin module name or entry point
                            (multi-allowed).
                            To avoid loading of plugins, use the `no:` prefix,
                            e.g. `no:doctest`.
                        """)
    parser.add_argument("--trace-config", help="""
                        trace considerations of conftest.py files.
                        """, action="store_true")
    parser.add_argument("--debug", help="""
                        store internal tracing debug information in
                            'pytestdebug.log'.
                        """, action="store_true")
    parser.add_argument("-o", "--override-ini", help="""
                        -o OVERRIDE_INI, --override-ini=OVERRIDE_INI
                            override ini option with "option=value" style, e.g.
                            `-o xfail_strict=True -o cache_dir=cache`.
                        """, action="store_true")
    parser.add_argument("--assert", help="""
                        --assert=MODE         Control assertion debugging tools.
                            'plain' performs no assertion debugging.
                            'rewrite' (the default) rewrites assert statements
                            in test modules on import to provide assert
                            expression information.
                        """)
    parser.add_argument("--setup-only", help="""
                        only setup fixtures, do not execute tests.
                        """, action="store_true")
    parser.add_argument("--setup-show", help="""
                        show setup of fixtures while executing tests.
                        """, action="store_true")
    parser.add_argument("--setup-plan", help="""
                        show what fixtures and tests would be executed but
                            don't execute anything.
                        """, action="store_true")
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

    return parser.parse_args()
