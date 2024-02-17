from framework_tests.nrobo_args.test_nrobo_args_package import TestNroboArgsPackage

t = TestNroboArgsPackage()
t.test_nrobo_cli_arg_junit_xml_switch()

from framework_tests.version.test_version_pkg import TestVersionPkg
t = TestVersionPkg()

t.test_version_class_properties()
