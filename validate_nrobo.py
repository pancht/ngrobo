import os
import subprocess
from pathlib import Path

from nrobo import set_environment, Environment, EnvKeys, console
from nrobo.cli.cli_constants import NREPORT
from nrobo.util.process import terminal


def run_unit_tests(debug=False) -> int:
    """run nrobo framework unit tests"""

    set_environment()
    validator_report = f"{NREPORT.REPORT_DIR}{os.sep}validator_nrobo_report.html"
    return terminal(
        ['pytest', 'nrobo_framework_tests', '--confcutdir', Path(os.environ[EnvKeys.EXEC_DIR]) / 'nrobo_framework_tests'
            , '--html', validator_report], debug=debug)

    # return terminal(['python', 'nrobo.py', '--report' 'html', '-n', '2', '--rootdir',
    #                  Path(os.environ[EnvKeys.EXEC_DIR]) / 'nrobo_framework_tests', '--confcutdir',
    #                  Path(os.environ[EnvKeys.EXEC_DIR]) / 'nrobo_framework_tests'])

    console.print(f"\t[{STYLE.HLGreen}]All tests passed.")
    console.rule(f"Review validator report at {validator_report}")

    return 0  # success


if __name__ == '__main__':
    run_unit_tests(debug=True)
