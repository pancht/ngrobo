import argparse
import sys
from collections import OrderedDict

import pytest

from nrobo import terminal


class TestNroboArgsPackage():
    """Tests for nrobo.cli.nrobo_args package"""

    DEFAULT_NROBO_ARGS = ['-n', '1', '--reruns-delay', '1', '--html', 'results/report.html', '--durations-min',
                                       '0.005',
                                       '--verbosity', '0', '--browser', 'chrome', '--cache-clear', '--color', 'yes',
                                       '-r', 'fE', '--code-highlight', 'yes', '--junit-xml', 'results/junit-report.xml']

    def _replace_and_get_default_key_value(self, key, value) -> [str]:
        """Replace key-value if given <key> is found in default nRoBo args

           Returns [str]: [args]"""

        _copy = self.DEFAULT_NROBO_ARGS.copy()

        for idx in range(len(_copy)):
            print(_copy[idx])
            if _copy[idx] == key:
                _copy[idx+1] = value
                return _copy

    def test_show_only_pytest_switches(self):
        """Validate that all show only pytest switches are present in the list"""

        expected_show_only_switches = [
            "markers",
            "fixtures",
            "funcargs",
            "fixtures-per-test",
            "collect-only",
            "version",
            "setup-plan",
            "co"
        ]

        from nrobo.cli.nrobo_args import SHOW_ONLY_SWITCHES
        actual_show_only_switches = SHOW_ONLY_SWITCHES

        # test if all expected switches are present
        for switch in expected_show_only_switches:
            assert switch in actual_show_only_switches

    def test_nrobo_cli_args_with_no_arg(self):
        """Validate nRoBO cli args with no arg"""

        from nrobo.cli.launcher import launcher_command
        command = ['pytest']
        sys.argv = command

        expected_command = command + self.DEFAULT_NROBO_ARGS
        actual_command, args, notes = launcher_command()

        assert set(actual_command) == set(expected_command)

    def test_nrobo_cli_arg_i_switch(self):
        """Validate nRoBo cli -i switch"""

        SWITCH = '-i'
        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command

        command.remove(SWITCH)
        expected_command = command + self.DEFAULT_NROBO_ARGS
        actual_command, args, notes = launcher_command()

        assert set(actual_command) == set(expected_command)

    def test_nrobo_cli_arg_i_long_switch(self):
        """Validate nRoBo cli -i long switch: --install"""

        from nrobo.cli.launcher import launcher_command
        SWITCH = "--install"
        command = ['pytest', SWITCH]
        sys.argv = command

        command.remove(SWITCH)
        expected_command = command + self.DEFAULT_NROBO_ARGS
        actual_command, args, notes = launcher_command()

        assert (set(actual_command) == set(expected_command))

    def test_nrobo_cli_arg_app_switch(self):
        """Validate nRoBo cli --app switch: --app APP"""

        from nrobo.cli.launcher import launcher_command
        SWITCH = '--app'
        APP = 'APPLE.COM'
        command = ['pytest', SWITCH, APP]
        sys.argv = command

        command.remove(SWITCH)
        command.remove(APP)
        expected_command = command + self.DEFAULT_NROBO_ARGS
        actual_command, args, notes = launcher_command()

        assert set(actual_command) == set(expected_command)

    def test_nrobo_cli_arg_url_switch(self):
        """Validate nRoBo cli --url switch: --url URL"""

        from nrobo.cli.launcher import launcher_command
        SWITCH = '--url'
        URL = 'HTTPS://APPLE.COM'
        command = ['pytest', SWITCH, URL]
        sys.argv = command

        command.remove(SWITCH)
        command.remove(URL)
        expected_command = command + self.DEFAULT_NROBO_ARGS
        actual_command, args, notes = launcher_command()

        assert set(actual_command) == set(expected_command)

    def test_nrobo_cli_arg_username_switch(self):
        """Validate nRoBo cli --username switch: --username USERNAME"""

        from nrobo.cli.launcher import launcher_command
        SWITCH = '--username'
        USERNAME = 'USERNAME'
        command = ['pytest', SWITCH, USERNAME]
        sys.argv = command

        command.remove(SWITCH)
        command.remove(USERNAME)
        expected_command = command + self.DEFAULT_NROBO_ARGS
        actual_command, args, notes = launcher_command()

        assert set(actual_command) == set(expected_command)

    def test_nrobo_cli_arg_password_switch(self):
        """Validate nRoBo cli --password switch: --password PASSWORD"""

        from nrobo.cli.launcher import launcher_command
        SWITCH = '--password'
        VALUE = 'PASSWORD'
        command = ['pytest', SWITCH, VALUE]
        sys.argv = command

        command.remove(SWITCH)
        command.remove(VALUE)
        expected_command = command + self.DEFAULT_NROBO_ARGS
        actual_command, args, notes = launcher_command()

        assert set(actual_command) == set(expected_command)

    def test_nrobo_cli_arg_n_switch(self):
        """Validate nRoBo cli -n switch"""

        SWITCH = '-n'
        VALUE = '-30'
        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH, VALUE]
        sys.argv = command

        expected_command = command + self.DEFAULT_NROBO_ARGS
        actual_command, args, notes = launcher_command()

        assert set(actual_command) == set(expected_command)

    def test_nrobo_cli_arg_n_switch_without_value(self):
        """Validate nRoBo cli -n switch"""

        from nrobo.cli.launcher import launcher_command
        SWITCH = '-n'
        command = ['pytest', SWITCH]
        sys.argv = command

        try:
            launcher_command(exit_on_failure=False)
        except argparse.ArgumentError as e:
            return

        assert False  # If expected exception did not raise

    def test_nrobo_cli_arg_n_long_switch(self):
        """Validate nRoBo cli -n long switch: --instances"""

        from nrobo.cli.launcher import launcher_command
        SWITCH = '--instances'
        VALUE = '-20'
        command = ['pytest', SWITCH, VALUE]
        sys.argv = command

        command[1] = '-n'
        expected_command = command + self.DEFAULT_NROBO_ARGS
        actual_command, args, notes = launcher_command()

        assert set(actual_command) == set(expected_command)

    def test_nrobo_cli_arg_n_long_switch_without_value(self):
        """Validate nRoBo cli -n long switch: --instances without value"""

        SWITCH = '--instances'
        REPLACE_SWITCH = '-n'
        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command

        try:
            launcher_command(exit_on_failure=False)
        except argparse.ArgumentError as e:
            return

        assert False  # If expected exception did not raise

    def test_nrobo_cli_arg_reruns_switch(self):
        """Validate nRoBo cli --reruns switch: --reruns RERUNS"""

        SWITCH = '--reruns'
        VALUE = '3'
        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH, VALUE]
        sys.argv = command

        expected_command = command + self.DEFAULT_NROBO_ARGS
        actual_command, args, notes = launcher_command()

        assert set(actual_command) == set(expected_command)

    def test_nrobo_cli_arg_reruns_switch_without_value(self):
        """Validate nRoBo cli --reruns switch: --reruns """

        SWITCH = '--reruns'
        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command

        try:
            launcher_command(exit_on_failure=False)
        except argparse.ArgumentError as e:
            return

        assert False  # If expected exception did not raise

    def test_nrobo_cli_arg_reruns_delay_switch(self):
        """Validate nRoBo cli --reruns-delay switch: --reruns-delay RERUNS-DELAY"""

        SWITCH = '--reruns-delay'
        VALUE = '3'
        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH, VALUE]
        sys.argv = command

        expected_command = command + self.DEFAULT_NROBO_ARGS
        actual_command, args, notes = launcher_command()

        assert set(actual_command) == set(expected_command)

    def test_nrobo_cli_arg_reruns_delay_switch_without_value(self):
        """Validate nRoBo cli --reruns-delay switch: --reruns """

        SWITCH = '--reruns-delay'
        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command

        try:
            launcher_command(exit_on_failure=False)
        except argparse.ArgumentError as e:
            return

        assert False  # If expected exception did not raise
