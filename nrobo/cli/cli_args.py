import argparse
import os

from nrobo import FRAMEWORK_PATHS
from nrobo.cli import install_dependencies, STYLE, __REQUIREMENTS__
from nrobo.cli.cli_constansts import nCLI as CLI, NREPORT
from rich.console import Console
from nrobo.cli.formatting import themes as th
from nrobo.cli.nglobals import *

global __APP_NAME__, __URL__,__PASSWORD__,__USERNAME__, __BROWSER__

from nrobo.util.process import terminal

console = Console(theme=th)


def parse_cli_args():
    """
    Parse command-line-arguments
    Doc: https://docs.python.org/3/library/argparse.html#example
    pytest cli: https://docs.pytest.org/en/6.2.x/reference.html#command-line-flags

    :return:
    """
    parser = argparse.ArgumentParser(
        prog="nrobo",
        description='Run tests through nrobo framework')
    parser.add_argument("-i", f"--{CLI.INSTALL}", action="store_true")
    parser.add_argument(f"--{CLI.APP}", help="Name of your test.yaml project")
    parser.add_argument(f"--{CLI.URL}", help="Link of application under test.yaml")
    parser.add_argument(f"--{CLI.USERNAME}", help="Username for login", default="")
    parser.add_argument(f"--{CLI.PASSWORD}", help="Password for login", default="")
    parser.add_argument("-n", f"--{CLI.INSTANCES}",
                        help="Number of parallel test.yaml instances. Default to 1 meaning sequential.",
                        default=1)
    parser.add_argument(f"--{CLI.RERUNS}", help="Number of reruns for a test.yaml if it fails", default=0)
    parser.add_argument(f"--{CLI.RERUNS_DELAY}", help="Rerun delay. Default=1")
    parser.add_argument(f"--{CLI.REPORT}",
                        help="Report target. Default HTML or Rich Allure report. Options are html | allure",
                        default="html")
    # parser.add_argument(f"--{CLI.TESTDIR}", help="Tests directory. Defaults to tests")
    parser.add_argument("-b", f"--{CLI.BROWSER}", help="""
    Target browser name. Default is chrome.
    Options could be:
        chrome | chrome_headless | 
        firefox | safari | edge.
        (Only chrome is supported at present.)
    """)
    parser.add_argument(f"--{CLI.BROWSER_CONFIG}", help="""
        Path of browser config file containing additional options which are needed to be applied
        in driver instantiation. Each line in file should contain one option only.
        For example: you want to appy, --start-maximized, chrome option for chrome driver.
        and the browser config file is 'chrome_config.txt', then
        the content of file should be as below:
        
        --start-maximized
        
        There will be no conversion taking place by nrobo!!!
        """)
    parser.add_argument("-k", f"--{CLI.KEY}", help="""
    Only run tests which match the given substring
                        expression. An expression is a python evaluatable
                        expression where all names are substring-matched
                        against test.yaml names and their parent classes.
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
    parser.add_argument(f"--{CLI.GRID}", help="""
            Remote webdriver grid url
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

    # Get parsed args
    args = parser.parse_args()

    if args.install:
        # Install dependencies
        with console.status(f"[{STYLE.TASK}]Installing dependencies...\n"):
            install_dependencies(FRAMEWORK_PATHS.REQUIREMENTS + __REQUIREMENTS__)
            exit(1)

    # build pytest command
    command = ["pytest"]

    # Rest of the options if present
    with console.status(f"[{STYLE.TASK}]Parsing command-line-args...\n"):
        for key, value in args.__dict__.items():
            # process pytest keys first

            # replace hyphen with dash if hyphen is present in key
            key = key.replace('_', '-')

            if value:
                if type(value) is bool:
                    command.append(f"--{key}")
                    continue  # proceed with next key
                elif key not in CLI.ARGS.keys():
                    """Check for all no nrobo cli keys. All pytest keys"""
                    # print(key)
                    if key == "c":
                        command.append(f"-{key}")
                        command.append(str(value))
                    else:
                        command.append(f"--{key}")
                        command.append(str(value))
                elif key in CLI.ARGS:
                    if key in [CLI.APP, CLI.URL, CLI.USERNAME, CLI.PASSWORD, CLI.BROWSER_CONFIG]:
                        if key == CLI.APP:
                            __APP_NAME__ = value
                        elif key == CLI.URL:
                            __URL__ = value
                        elif key == CLI.USERNAME:
                            __USERNAME__ = value
                        elif key == CLI.PASSWORD:
                            __PASSWORD__ = value

                        command.append(f"--{key}")
                        command.append(str(value))

                    if key == CLI.BROWSER:
                        __BROWSER__ = value
                        raise_exception_if_browser_not_supported(__BROWSER__)
                        command.append(f"--{key}")
                        command.append(str(value))
                    elif key == CLI.KEY:
                        command.append(f"-k")
                        command.append(value)
                    elif key == CLI.INSTANCES:
                        command.append(f"-n")
                        command.append(str(value))
                    elif key == CLI.RERUNS:
                        command.append(f"--{key}")
                        command.append(value)
                    elif key == CLI.REPORT:
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
    # print(__BROWSER__)
    # print(command)
    # exit(1)

    # Add single parameter commands by default
    # That make sense.
    # command.append("-V") # This setting is not working. With this, tests are even not running at all.
    for k, v in CLI.DEFAULT_ARGS.items():
        command = command + v

    with console.status(f"[{STYLE.TASK}]:smiley: Running tests...\n"):
        console.print(f"[{STYLE.INFO}]{command}")
        terminal(command)

        if args.report and args.report == NREPORT.ALLURE:
            # https://allurereport.org/docs/gettingstarted-installation/
            terminal([NREPORT.ALLURE, f"serve", NREPORT.ALLURE_REPORT_PATH])

    with console.status(f"[{STYLE.TASK}]Test report is ready! Please analyze results...\n"):
        pass
