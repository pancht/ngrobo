import argparse

from nrobo import FRAMEWORK_PATHS
from nrobo.cli import install_dependencies, STYLE, __REQUIREMENTS__
from nrobo.cli.cli_constansts import nCLI as CLI, REPORT_TYPES
from rich.console import Console
from nrobo.cli.formatting import themes as th

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
    parser.add_argument("-a", f"--{CLI.APP}", help="Name of your test.yaml project")
    parser.add_argument("-l", f"--{CLI.LINK}", help="Link of application under test.yaml")
    parser.add_argument("-u", f"--{CLI.USERNAME}", help="Username for login", default="")
    parser.add_argument("-p", f"--{CLI.PASSWORD}", help="Password for login", default="")
    parser.add_argument("-n", f"--{CLI.INSTANCES}",
                        help="Number of parallel test.yaml instances. Default to 1 meaning sequential.",
                        default=1)
    parser.add_argument("-r", f"--{CLI.RERUN}", help="Number of reruns for a test.yaml if it fails", default=0)
    parser.add_argument(f"--{CLI.REPORT}",
                        help="Report target. Default HTML or Rich Allure report. Options are html | allure",
                        default="html")
    # parser.add_argument(f"--{CLI.TESTDIR}", help="Tests directory. Defaults to tests")
    parser.add_argument("-b", f"--{CLI.BROWSER}", help="""
    Target browser name. Default is chrome.
    Options could be:
        chrome | firefox | safari | edge.
        (Only chrome is supported at present.)
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
    parser.add_argument("-m", "--marker", help="""
    Only run tests matching given mark expression.
                        For example: -m 'mark1 and not mark2'
    """)
    # parser.add_argument("--markers", help="""
    # Show markers (builtin, plugin and per-project ones).
    # """)
    # parser.add_argument("-x", "--exitfirst", help="""
    # exit instantly on first error or failed test.yaml.
    # """)
    # parser.add_argument("--fixtures", help="""
    # show available fixtures, sorted by plugin appearance
    #                     (fixtures with leading '_' are only shown with '-v')
    #                     """)
    # parser.add_argument("--funcargs", help="""
    #     show available fixtures, sorted by plugin appearance
    #                         (fixtures with leading '_' are only shown with '-v')
    #                         """)
    # parser.add_argument("--fixtures-per-test.yaml", help="show fixtures per test.yaml")
    # parser.add_argument("--pdb", help="""
    # start the interactive Python debugger on errors or
    #                     KeyboardInterrupt.
    #                     """)
    # parser.add_argument("--pdbcls", help="""
    # --pdbcls=modulename:classname
    #                     start a custom interactive Python debugger on
    #                     errors. For example:
    #                     --pdbcls=IPython.terminal.debugger:TerminalPdb
    #                     """)
    # parser.add_argument("--trace", help="Immediately break when running each test.yaml.")
    # parser.add_argument("--capture", help="""
    # --capture=method      per-test.yaml capturing method: one of fd|sys|no|tee-sys.
    # """)
    # parser.add_argument("-s", help="shortcut for --capture=no.")
    # parser.add_argument("--runxfail", help="""
    # report the results of xfail tests as if they were
    #                     not marked
    #                     """)
    # parser.add_argument("-lf", "--last-failed", help="""
    # rerun only the tests that failed at the last run (or
    #                     all if none failed)
    #                     """)
    # parser.add_argument("--ff", "--failed-first", help="""
    # run all tests, but run the last failures first.
    #                     This may re-order tests and thus lead to repeated
    #                     fixture setup/teardown.
    #                     """)
    # parser.add_argument("--nf", "--new-first", help="""
    # run tests from new files first, then the rest of the
    #                     tests sorted by file mtime
    #                     """)

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
            if value:
                if key not in CLI.ARGS.keys():
                    command.append(key)
                    command.append(str(value))
                elif key == CLI.KEY:
                    command.append("-k")
                    command.append(str(args.key))
                elif key == CLI.INSTANCES:
                    command.append("-n")
                    command.append(str(value))
                elif key == CLI.REPORT:
                    if value == REPORT_TYPES.HTML:
                        command.append(f"--{REPORT_TYPES.HTML}")
                        command.append(f"{REPORT_TYPES.HTML_REPORT_PATH}")
                    elif key == REPORT_TYPES.ALLURE:
                        console.print(f"Allure support is still in pipeline. Please come again later!")
                        exit(1)
                    else:
                        console.print(f"Incorrect report type! Valid report types are html | allure.")
                        exit(1)

    with console.status(f"[{STYLE.TASK}]:smiley: Running tests...\n"):
        console.print(f"[{STYLE.INFO}]{command}")
        terminal(command)

    with console.status(f"[{STYLE.TASK}]Test report is ready! Please analyze results...\n"):
        pass
