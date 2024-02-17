from framework_tests.nrobo_args.test_nrobo_args_package import TestNroboArgsPackage

t = TestNroboArgsPackage()
t.test_nrobo_cli_arg_i_switch()
t.test_nrobo_cli_arg_i_long_switch()

from framework_tests.version.test_version_pkg import TestVersionPkg
t = TestVersionPkg()

t.test_arithmetic_operations_on_Version_class()
