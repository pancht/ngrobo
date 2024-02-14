import os
import subprocess
import sys

from nrobo import set_environment, Environment, EnvKeys
from nrobo.util.process import terminal


def run_unit_tests(debug=False) -> int:
    """run nrobo framework unit tests"""

    from pathlib import Path
    set_environment()
    # pytest nrobo_framework_tests --noconftest --confcutdir nrobo_framework_tests
    target = "results-unittests/nrobo_unit_tests_run_report.html"
    unit_tests_dir = 'framework_tests'
    conftest_dir = Path(os.environ[EnvKeys.EXEC_DIR]) / unit_tests_dir
    print(sys.path)
    return terminal(
        ['pytest', unit_tests_dir, '--confcutdir', str(conftest_dir), '--html', target], debug=debug)


if __name__ == '__main__':
    run_unit_tests(debug=True)
