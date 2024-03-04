from framework_tests.nrobo_args.test_nrobo_args_package import TestNroboArgsPackage

t = TestNroboArgsPackage()
t.test_nrobo_cli_arg_pyargs_switch()
t.test_nrobo_cli_arg_color_switch_with_invalid_value()

from framework_tests.version.test_version_pkg import TestVersionPkg
t = TestVersionPkg()

t.test_arithmetic_operations_on_Version_class()
