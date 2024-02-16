"""
=====================CAUTION=======================
DO NOT DELETE THIS FILE SINCE IT IS PART OF NROBO
FRAMEWORK AND IT MAY CHANGE IN THE FUTURE UPGRADES
OF NROBO FRAMEWORK. THUS, TO BE ABLE TO SAFELY UPGRADE
TO LATEST NROBO VERSION, PLEASE DO NOT DELETE THIS
FILE OR ALTER ITS LOCATION OR ALTER ITS CONTENT!!!
===================================================

validator.py script is for running nRoBo unit tests
on developer machine.

@author: Panchdev Singh Chauhan
@email: erpanchdev@gmail.com
"""

import os
import subprocess
import sys

from nrobo import set_environment, Environment, EnvKeys, STYLE
from nrobo.cli.nglobals import Browsers
from nrobo.util.process import terminal
from nrobo.cli.cli_constants import nCLI


def run_unit_tests(debug=False) -> int:
    """run nrobo framework unit tests"""

    from pathlib import Path
    # set environment path
    set_environment()

    # pytest nrobo_framework_tests --noconftest --confcutdir nrobo_framework_tests
    target = "results-unittests/nrobo_unit_tests_run_report.html"
    unit_tests_dir = 'framework_tests'
    conftest_dir = Path(os.environ[EnvKeys.EXEC_DIR]) / unit_tests_dir
    print(sys.path)
    return_code_unit_test_run = terminal(
        ['pytest', '--confcutdir', str(conftest_dir),
         '--html', target, unit_tests_dir, '-n', '20',
         '--rootdir', str(conftest_dir)],
        debug=debug
    )

    from nrobo import console
    if return_code_unit_test_run == 0:
        console.rule(f"[{STYLE.HLGreen}][{STYLE.ITALIC}]Unit tests[/] [{STYLE.BOLD}]PASSED[/].")
    else:
        console.rule(f"[{STYLE.HLRed}]Exit. [Reason] One or more unit tests [{STYLE.BOLD}]failed[/]! Please fix them to proceed.", style=f"{STYLE.HLRed}")
        return return_code_unit_test_run

    return_code_web_test_run = terminal(['python', 'nrobo.py', '--browser', Browsers.CHROME_HEADLESS, '-n', '20'],
                                        debug=debug)
    if return_code_unit_test_run == 0:
        console.rule(f"[{STYLE.HLGreen}][{STYLE.ITALIC}]Web tests[/] [{STYLE.BOLD}]PASSED[/].")
    else:
        console.rule(f"[{STYLE.HLRed}]Exit. [Reason] One or more web tests [{STYLE.BOLD}]failed[/]! Please fix them to proceed.",  style=f"{STYLE.HLRed}")
        return_code_web_test_run

    console.rule(f"\n\n[{STYLE.HLGreen}][{STYLE.ITALIC}]Unit tests[/] and [{STYLE.ITALIC}]Web tests[/] [{STYLE.BOLD}]PASSED[/].")
    return 0  # A SUCCESS


if __name__ == '__main__':
    run_unit_tests(debug=True)
