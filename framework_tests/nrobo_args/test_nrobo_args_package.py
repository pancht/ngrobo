import argparse
import sys
from collections import OrderedDict
from pathlib import Path

import pytest

from nrobo import terminal
from nrobo.cli.cli_constants import NREPORT
from nrobo.cli.nrobo_args import BOOL_SWITCHES
from nrobo.exceptions import BrowserNotSupported


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
            if _copy[idx] == key:
                _copy[idx + 1] = value
                return ['pytest'] + _copy

    def _match_key_value_pairs(self, src: [str], dest: [str]):
        """Match key-value pairs with src in dest list.

           If found match, True else return false.

           If any wrong outcome, please check if there is any pair key that is stored in BOOL_SWITCHES as bool key?"""

        len_src = len(src)
        len_dest = len(dest)
        if not len_src == len_dest:
            return False

        pair_key_match = False

        _idx_src = 0
        while _idx_src < len_src:
            for _idx_dest in range(len_dest):
                # search key from src in dest
                if src[_idx_src] == dest[_idx_dest]:
                    # key matches
                    if src[_idx_src] == "pytest":
                        break
                    elif src[_idx_src] in BOOL_SWITCHES:
                        break
                    else:
                        if src[_idx_src + 1] == dest[_idx_dest + 1]:
                            # matching value found
                            # thus, update index in src
                            pair_key_match = True
                            break
                        else:
                            return False  # value did not match

            if pair_key_match:
                _idx_src += 2
                pair_key_match = not pair_key_match
            else:
                _idx_src +=1

        return True  # All switches matched

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
        sys.argv = command.copy()

        expected_command = command + self.DEFAULT_NROBO_ARGS
        actual_command, args, notes = launcher_command()

        assert set(actual_command) == set(expected_command)

    def test_nrobo_cli_arg_i_switch(self):
        """Validate nRoBo cli -i switch"""

        SWITCH = '-i'
        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        command.remove(SWITCH)
        expected_command = command + self.DEFAULT_NROBO_ARGS
        actual_command, args, notes = launcher_command()

        assert actual_command is None

    def test_nrobo_cli_arg_i_long_switch(self):
        """Validate nRoBo cli -i long switch: --install"""

        from nrobo.cli.launcher import launcher_command
        SWITCH = "--install"
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        command.remove(SWITCH)
        expected_command = command + self.DEFAULT_NROBO_ARGS
        actual_command, args, notes = launcher_command()

        assert actual_command is None

    def test_nrobo_cli_arg_app_switch(self):
        """Validate nRoBo cli --app switch: --app APP"""

        from nrobo.cli.launcher import launcher_command
        SWITCH = '--app'
        APP = 'APPLE.COM'
        command = ['pytest', SWITCH, APP]
        sys.argv = command.copy()

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
        sys.argv = command.copy()

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
        sys.argv = command.copy()

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
        sys.argv = command.copy()

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
        sys.argv = command.copy()

        expected_command = command + self.DEFAULT_NROBO_ARGS
        actual_command, args, notes = launcher_command()

        assert set(actual_command) == set(expected_command)

    def test_nrobo_cli_arg_n_switch_without_value(self):
        """Validate nRoBo cli -n switch"""

        from nrobo.cli.launcher import launcher_command
        SWITCH = '-n'
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

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
        sys.argv = command.copy()

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
        sys.argv = command.copy()

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
        sys.argv = command.copy()

        expected_command = command + self.DEFAULT_NROBO_ARGS
        actual_command, args, notes = launcher_command()

        assert set(actual_command) == set(expected_command)

    def test_nrobo_cli_arg_reruns_switch_without_value(self):
        """Validate nRoBo cli --reruns switch: --reruns """

        SWITCH = '--reruns'
        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

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
        sys.argv = command.copy()

        expected_command = command + self.DEFAULT_NROBO_ARGS
        actual_command, args, notes = launcher_command()

        assert set(actual_command) == set(expected_command)

    def test_nrobo_cli_arg_reruns_delay_switch_without_value(self):
        """Validate nRoBo cli --reruns-delay switch: --reruns """

        SWITCH = '--reruns-delay'
        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        try:
            launcher_command(exit_on_failure=False)
        except argparse.ArgumentError as e:
            return

        assert False  # If expected exception did not raise

    def test_nrobo_cli_arg_report_switch_with_allure_option(self):
        """Validate nRoBo cli --report switch: --report allure"""

        SWITCH = '--report'
        VALUE = 'allure'
        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH, VALUE]
        sys.argv = command.copy()

        command.remove(SWITCH)
        command.remove(VALUE)
        command.append(f"--{NREPORT.HTML}")
        command.append(f"{Path(NREPORT.REPORT_DIR) / NREPORT.HTML_REPORT_NAME}")
        command.append('--alluredir')
        command.append(f"{NREPORT.ALLURE_REPORT_PATH}")
        expected_command = command + self.DEFAULT_NROBO_ARGS
        actual_command, args, notes = launcher_command()

        assert set(actual_command) == set(expected_command)

    def test_nrobo_cli_arg_report_switch_without_value(self):
        """Validate nRoBo cli --report switch without value: --report """

        SWITCH = '--report'
        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        try:
            launcher_command(exit_on_failure=False)
        except argparse.ArgumentError as e:
            return

        assert False  # If expected exception did not raise

    def test_nrobo_cli_arg_target_switch(self):
        """Validate nRoBo cli --target switch: --target TARGET"""

        SWITCH = '--target'
        VALUE = 'test-report.html'
        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH, VALUE]
        sys.argv = command.copy()

        command.remove(SWITCH)
        command.remove(VALUE)

        _copy_of_command = self._replace_and_get_default_key_value(f"--html", f"{Path(NREPORT.REPORT_DIR) / VALUE}")
        expected_command = command + _copy_of_command
        actual_command, args, notes = launcher_command()

        assert set(actual_command) == set(expected_command)

    def test_nrobo_cli_arg_target_switch_without_value(self):
        """Validate nRoBo cli --target switch without value: --target TARGET """

        SWITCH = '--target'
        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        try:
            launcher_command(exit_on_failure=False)
        except argparse.ArgumentError as e:
            return

        assert False  # If expected exception did not raise

    def test_nrobo_cli_arg_VERSION_switch(self):
        """Validate nRoBo cli --VERSION switch: --VERSION"""

        SWITCH = '--VERSION'
        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        actual_command, args, notes = launcher_command()

        assert actual_command is None

    def test_nrobo_cli_arg_suppress_switch(self):
        """Validate nRoBo cli --suppress switch: --suppress"""

        SWITCH = '--suppress'
        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        command.remove(SWITCH)

        expected_command = command + self.DEFAULT_NROBO_ARGS
        actual_command, args, notes = launcher_command()

        assert set(actual_command) == set(expected_command)

    def test_nrobo_cli_arg_browsers_switch_with_value_chrome(self):
        """Validate nRoBo cli --browser switch: --browser chrome"""

        SWITCH = '--browser'
        VALUE = 'chrome'
        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH, VALUE]
        sys.argv = command.copy()

        command.remove(SWITCH)
        command.remove(VALUE)

        expected_command = command + self.DEFAULT_NROBO_ARGS
        actual_command, args, notes = launcher_command()

        assert set(actual_command) == set(expected_command)

    def test_nrobo_cli_arg_browsers_switch_with_value_chrome_headless(self):
        """Validate nRoBo cli --browser switch: --browser chrome_headless"""

        PYTEST = "PYTEST"
        SWITCH = '--browser'
        VALUE = 'chrome_headless'

        from nrobo.cli.launcher import launcher_command
        command = [PYTEST, SWITCH, VALUE]
        sys.argv = command.copy()

        _copy_of_default_args = self._replace_and_get_default_key_value(SWITCH, VALUE)
        expected_command = _copy_of_default_args
        actual_command, args, notes = launcher_command()

        assert self._match_key_value_pairs(expected_command, actual_command)

    def test_nrobo_cli_arg_browsers_switch_with_value_firefox(self):
        """Validate nRoBo cli --browser switch: --browser firefox"""

        PYTEST = "PYTEST"
        SWITCH = '--browser'
        VALUE = 'firefox'

        from nrobo.cli.launcher import launcher_command
        command = [PYTEST, SWITCH, VALUE]
        sys.argv = command.copy()

        _copy_of_default_args = self._replace_and_get_default_key_value(SWITCH, VALUE)
        expected_command = _copy_of_default_args
        actual_command, args, notes = launcher_command()

        assert self._match_key_value_pairs(expected_command, actual_command)

    def test_nrobo_cli_arg_browsers_switch_with_value_firefox_headless(self):
        """Validate nRoBo cli --browser switch: --browser firefox_headless"""

        PYTEST = "PYTEST"
        SWITCH = '--browser'
        VALUE = 'firefox_headless'

        from nrobo.cli.launcher import launcher_command
        command = [PYTEST, SWITCH, VALUE]
        sys.argv = command.copy()

        _copy_of_default_args = self._replace_and_get_default_key_value(SWITCH, VALUE)
        expected_command = _copy_of_default_args
        actual_command, args, notes = launcher_command()

        assert self._match_key_value_pairs(expected_command, actual_command)

    def test_nrobo_cli_arg_browsers_switch_with_value_safari(self):
        """Validate nRoBo cli --browser switch: --browser safari"""

        PYTEST = "PYTEST"
        SWITCH = '--browser'
        VALUE = 'safari'

        from nrobo.cli.launcher import launcher_command
        command = [PYTEST, SWITCH, VALUE]
        sys.argv = command.copy()

        _copy_of_default_args = self._replace_and_get_default_key_value(SWITCH, VALUE)
        expected_command = _copy_of_default_args
        actual_command, args, notes = launcher_command()

        assert self._match_key_value_pairs(expected_command, actual_command)

    def test_nrobo_cli_arg_browsers_switch_with_value_edge(self):
        """Validate nRoBo cli --browser switch: --browser edge"""

        PYTEST = "PYTEST"
        SWITCH = '--browser'
        VALUE = 'edge'

        from nrobo.cli.launcher import launcher_command
        command = [PYTEST, SWITCH, VALUE]
        sys.argv = command.copy()

        _copy_of_default_args = self._replace_and_get_default_key_value(SWITCH, VALUE)
        expected_command = _copy_of_default_args
        actual_command, args, notes = launcher_command()

        assert self._match_key_value_pairs(expected_command, actual_command)

    def test_nrobo_cli_arg_browsers_switch_with_value_of_not_supported_browser(self):
        """Validate nRoBo cli --browser switch: --browser xxx"""

        PYTEST = "PYTEST"
        SWITCH = '--browser'
        VALUE = 'xxx'

        from nrobo.cli.launcher import launcher_command
        command = [PYTEST, SWITCH, VALUE]
        sys.argv = command.copy()

        _copy_of_default_args = self._replace_and_get_default_key_value(SWITCH, VALUE)
        expected_command = _copy_of_default_args
        try:
            actual_command, args, notes = launcher_command()
        except BrowserNotSupported as e:
            return True

        return False

    def test_nrobo_cli_arg_browser_switch_without_value(self):
        """Validate nRoBo cli --browser switch without value: --browser """

        SWITCH = '--browser'
        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        try:
            launcher_command(exit_on_failure=False)
        except argparse.ArgumentError as e:
            return

        assert False  # If expected exception did not raise

    def test_nrobo_cli_arg_browser_config_switch(self):
        """Validate nRoBo cli --browser-config switch: --browser BROWSER-CONFIG"""

        SWITCH = '--browser-config'
        VALUE = 'xyz'
        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH, VALUE]
        sys.argv = command.copy()

        expected_command = command + self.DEFAULT_NROBO_ARGS
        actual_command, args, notes = launcher_command()

        assert set(actual_command) == set(expected_command)

    def test_nrobo_cli_arg_browser_config_switch_without_value(self):
        """Validate nRoBo cli --browser-config switch without value: --browser """

        SWITCH = '--browser-config'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        try:
            launcher_command(exit_on_failure=False)
        except argparse.ArgumentError as e:
            return

        assert False  # If expected exception did not raise

    def test_nrobo_cli_arg_key_switch(self):
        """Validate nRoBo cli --key switch: --key KEY"""

        SWITCH = '--key'
        VALUE = '1'
        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH, VALUE]
        sys.argv = command.copy()

        command[1] = '-k'
        expected_command = command + self.DEFAULT_NROBO_ARGS
        actual_command, args, notes = launcher_command()

        assert self._match_key_value_pairs(expected_command, actual_command)

    def test_nrobo_cli_arg_key_switch_without_value(self):
        """Validate nRoBo cli --key switch without value: --key """

        SWITCH = '--key'
        VALUE = '1'
        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        try:
            launcher_command(exit_on_failure=False)
        except argparse.ArgumentError as e:
            return

        assert False  # If expected exception did not raise

    def test_nrobo_cli_arg_grid_switch(self):
        """Validate nRoBo cli --grid switch: --grid GRID"""

        SWITCH = '--grid'
        VALUE = 'https://apple.com'
        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH, VALUE]
        sys.argv = command.copy()

        expected_command = command + self.DEFAULT_NROBO_ARGS
        actual_command, args, notes = launcher_command()

        assert self._match_key_value_pairs(expected_command, actual_command)

    def test_nrobo_cli_arg_grid_switch_without_value(self):
        """Validate nRoBo cli --grid switch without value: --grid """

        SWITCH = '--grid'
        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        try:
            launcher_command(exit_on_failure=False)
        except argparse.ArgumentError as e:
            return

        assert False  # If expected exception did not raise

    def test_nrobo_cli_arg_marker_switch(self):
        """Validate nRoBo cli --marker switch: --marker MARKER"""

        SWITCH = '--marker'
        VALUE = 'test'
        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH, VALUE]
        sys.argv = command.copy()

        expected_command = command + self.DEFAULT_NROBO_ARGS
        actual_command, args, notes = launcher_command()

        assert self._match_key_value_pairs(expected_command, actual_command)

    def test_nrobo_cli_arg_marker_switch_without_value(self):
        """Validate nRoBo cli --marker switch: --marker """

        SWITCH = '--marker'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        try:
            launcher_command(exit_on_failure=False)
        except argparse.ArgumentError as e:
            return

        assert False  # If expected exception did not raise

    def test_nrobo_cli_arg_markers_switch(self):
        """Validate nRoBo cli --markers switch: --markers MARKERS"""

        SWITCH = '--markers'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        expected_command = command + self.DEFAULT_NROBO_ARGS
        actual_command, args, notes = launcher_command()

        assert actual_command is None

    def test_nrobo_cli_arg_exitfirst_switch(self):
        """Validate nRoBo cli --exitfirst switch: --exitfirst """

        SWITCH = '--exitfirst'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        expected_command = command + self.DEFAULT_NROBO_ARGS
        actual_command, args, notes = launcher_command()

        assert self._match_key_value_pairs(expected_command, actual_command)

    def test_nrobo_cli_arg_fixtures_switch(self):
        """Validate nRoBo cli --fixtures switch: --fixtures """

        SWITCH = '--fixtures'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        expected_command = command + self.DEFAULT_NROBO_ARGS
        actual_command, args, notes = launcher_command()

        assert actual_command is None

    def test_nrobo_cli_arg_funcargs_switch(self):
        """Validate nRoBo cli --funcargs switch: --funcargs """

        SWITCH = '--funcargs'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        expected_command = command + self.DEFAULT_NROBO_ARGS
        actual_command, args, notes = launcher_command()

        assert actual_command is None

    def test_nrobo_cli_arg_fixtures_per_test_switch(self):
        """Validate nRoBo cli --fixtures-per-test switch: --fixtures-per-test """

        SWITCH = '--fixtures-per-test'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        expected_command = command + self.DEFAULT_NROBO_ARGS
        actual_command, args, notes = launcher_command()

        assert actual_command is None

    def test_nrobo_cli_arg_pdb_switch(self):
        """Validate nRoBo cli --pdb switch: --pdb """

        SWITCH = '--pdb'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        expected_command = command + self.DEFAULT_NROBO_ARGS
        actual_command, args, notes = launcher_command()

        assert self._match_key_value_pairs(expected_command, actual_command)

    def test_nrobo_cli_arg_pdbcls_switch(self):
        """Validate nRoBo cli --pdbcls switch: --pdbcls modulename:classname"""

        SWITCH = '--pdbcls'
        VALUE = 'modulename:classname'
        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH, VALUE]
        sys.argv = command.copy()

        expected_command = command + self.DEFAULT_NROBO_ARGS
        actual_command, args, notes = launcher_command()

        assert self._match_key_value_pairs(expected_command, actual_command)

    def test_nrobo_cli_arg_pdbcls_switch_without_value(self):
        """Validate nRoBo cli --pdbcls switch without value: --pdbcls """

        SWITCH = '--pdbcls'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        try:
            launcher_command(exit_on_failure=False)
        except argparse.ArgumentError as e:
            return

        assert False  # If expected exception did not raise

    def test_nrobo_cli_arg_trace_switch(self):
        """Validate nRoBo cli --trace switch: --trace """

        SWITCH = '--trace'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        expected_command = command + self.DEFAULT_NROBO_ARGS
        actual_command, args, notes = launcher_command()

        assert self._match_key_value_pairs(expected_command, actual_command)

    def test_nrobo_cli_arg_capture_switch(self):
        """Validate nRoBo cli --capture switch: --capture method"""

        SWITCH = '--capture'
        VALUE = 'method'
        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH, VALUE]
        sys.argv = command.copy()

        expected_command = command + self.DEFAULT_NROBO_ARGS
        actual_command, args, notes = launcher_command()

        assert self._match_key_value_pairs(expected_command, actual_command)

    def test_nrobo_cli_arg_capture_switch_without_value(self):
        """Validate nRoBo cli --capture switch without value: --capture method"""

        SWITCH = '--capture'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        try:
            launcher_command(exit_on_failure=False)
        except argparse.ArgumentError as e:
            return

        assert False  # If expected exception did not raise

    def test_nrobo_cli_arg_capture_no_switch(self):
        """Validate nRoBo cli --capture-no switch: --capture-no """

        SWITCH = '--capture-no'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        command[1] = '-s'
        expected_command = command + self.DEFAULT_NROBO_ARGS
        actual_command, args, notes = launcher_command()

        assert self._match_key_value_pairs(expected_command, actual_command)

