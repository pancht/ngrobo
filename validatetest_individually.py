from framework_tests.nrobo_args.test_nrobo_args_package import TestNroboArgsPackage
from framework_tests.test_package_presence import TestNRoboFrameworkPaths

t = TestNroboArgsPackage()
t.test_nrobo_cli_arg_url_switch()
# t.test_nrobo_cli_arg_color_switch_with_invalid_value()

from framework_tests.version.test_version_pkg import TestVersionPkg
t = TestVersionPkg()

t = TestNRoboFrameworkPaths()
t.test_framework_tests_gui_pypi_home_page_test_py_file_is_present()