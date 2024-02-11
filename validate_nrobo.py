import subprocess
from nrobo import set_environment, Environment, EnvKeys
from nrobo.util.process import terminal


def run_unit_tests() -> int:
    """run nrobo framework unit tests"""
    set_environment()
    # pytest nrobo_framework_tests --noconftest --confcutdir nrobo_framework_tests
    return terminal(
        ['pytest', 'nrobo_framework_tests', '--noconftest', '--noconftest', 'nrobo_framework_tests', '-n', '10'])


if __name__ == '__main__':
    run_unit_tests()
