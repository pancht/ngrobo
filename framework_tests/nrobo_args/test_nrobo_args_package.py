import argparse
import sys
from collections import OrderedDict
from pathlib import Path

import pytest

from nrobo import terminal
from nrobo.cli import launcher_command
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
                _idx_src += 1

        return True  # All switches matched

    def _assert_command(self, command):
        """Add default args to give <command>,

           prepare the nrobo launcher command,

           and assert if expected and actual commands are same."""

        expected_command = command + self.DEFAULT_NROBO_ARGS
        actual_command, args, notes = launcher_command()

        assert self._match_key_value_pairs(expected_command, actual_command)

    def _assert_exception(self):
        """Assert if preparing command resulted in exception,

           catch the exception for assertion,

           and assert."""
        try:
            launcher_command(exit_on_failure=False)
        except argparse.ArgumentError as e:
            return

        assert False  # If expected exception did not raise

    def _assert_command_replace_default_values(self, switch, new_value):
        """Replace the default key, value pair with given <switch> <value> pair,

           prepare the nrobo launcher command,

           and assert if expected and actual commands are same."""

        _copy_of_default_args = self._replace_and_get_default_key_value(switch, new_value)
        expected_command = _copy_of_default_args
        actual_command, args, notes = launcher_command()
        print(f"{expected_command} \n\n{actual_command}")
        assert self._match_key_value_pairs(expected_command, actual_command)

    def _assert_command_is_None(self):
        """assert if sys command results in None value"""

        actual_command, args, notes = launcher_command()

        assert actual_command is None

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

        command = ['pytest']
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_i_switch(self):
        """Validate nRoBo cli -i switch"""

        SWITCH = '-i'

        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        command.remove(SWITCH)

        self._assert_command_is_None()

    def test_nrobo_cli_arg_i_long_switch(self):
        """Validate nRoBo cli -i long switch: --install"""

        SWITCH = "--install"
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        command.remove(SWITCH)

        self._assert_command_is_None()

    def test_nrobo_cli_arg_app_switch(self):
        """Validate nRoBo cli --app switch: --app APP"""

        SWITCH = '--app'
        APP = 'APPLE.COM'
        command = ['pytest', SWITCH, APP]
        sys.argv = command.copy()

        command.remove(SWITCH)
        command.remove(APP)

        self._assert_command(command)

    def test_nrobo_cli_arg_url_switch(self):
        """Validate nRoBo cli --url switch: --url URL"""

        SWITCH = '--url'
        URL = 'HTTPS://APPLE.COM'
        command = ['pytest', SWITCH, URL]
        sys.argv = command.copy()

        command.remove(SWITCH)
        command.remove(URL)

        self._assert_command(command)

    def test_nrobo_cli_arg_username_switch(self):
        """Validate nRoBo cli --username switch: --username USERNAME"""

        SWITCH = '--username'
        USERNAME = 'USERNAME'
        command = ['pytest', SWITCH, USERNAME]
        sys.argv = command.copy()

        command.remove(SWITCH)
        command.remove(USERNAME)

        self._assert_command(command)

    def test_nrobo_cli_arg_password_switch(self):
        """Validate nRoBo cli --password switch: --password PASSWORD"""

        from nrobo.cli.launcher import launcher_command
        SWITCH = '--password'
        VALUE = 'PASSWORD'
        command = ['pytest', SWITCH, VALUE]
        sys.argv = command.copy()

        command.remove(SWITCH)
        command.remove(VALUE)

        self._assert_command(command)

    def test_nrobo_cli_arg_n_switch(self):
        """Validate nRoBo cli -n switch"""

        SWITCH = '-n'
        VALUE = '-30'

        command = ['pytest', SWITCH, VALUE]
        sys.argv = command.copy()

        self._assert_command_replace_default_values(SWITCH, VALUE)

    def test_nrobo_cli_arg_n_switch_without_value(self):
        """Validate nRoBo cli -n switch"""

        SWITCH = '-n'
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_exception()

    def test_nrobo_cli_arg_n_long_switch(self):
        """Validate nRoBo cli -n long switch: --instances"""

        SWITCH = '--instances'
        VALUE = '-20'
        command = ['pytest', SWITCH, VALUE]
        sys.argv = command.copy()

        SWITCH = '-n'
        command[1] = '-n'

        self._assert_command_replace_default_values(SWITCH, VALUE)

    def test_nrobo_cli_arg_n_long_switch_without_value(self):
        """Validate nRoBo cli -n long switch: --instances without value"""

        SWITCH = '--instances'

        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_exception()

    def test_nrobo_cli_arg_reruns_switch(self):
        """Validate nRoBo cli --reruns switch: --reruns RERUNS"""

        SWITCH = '--reruns'
        VALUE = '3'

        command = ['pytest', SWITCH, VALUE]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_reruns_switch_without_value(self):
        """Validate nRoBo cli --reruns switch: --reruns """

        SWITCH = '--reruns'

        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_exception()

    def test_nrobo_cli_arg_reruns_delay_switch(self):
        """Validate nRoBo cli --reruns-delay switch: --reruns-delay RERUNS-DELAY"""

        SWITCH = '--reruns-delay'
        VALUE = '3'

        command = ['pytest', SWITCH, VALUE]
        sys.argv = command.copy()

        self._assert_command_replace_default_values(SWITCH, VALUE)

    def test_nrobo_cli_arg_reruns_delay_switch_without_value(self):
        """Validate nRoBo cli --reruns-delay switch: --reruns """

        SWITCH = '--reruns-delay'

        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_exception()

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

        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_exception()

    def test_nrobo_cli_arg_target_switch(self):
        """Validate nRoBo cli --target switch: --target TARGET"""

        SWITCH = '--target'
        VALUE = 'test-report.html'

        command = ['pytest', SWITCH, VALUE]
        sys.argv = command.copy()

        command.remove(SWITCH)
        command.remove(VALUE)

        self._assert_command_replace_default_values(f"--html", f"{Path(NREPORT.REPORT_DIR) / VALUE}")

    def test_nrobo_cli_arg_target_switch_without_value(self):
        """Validate nRoBo cli --target switch without value: --target TARGET """

        SWITCH = '--target'

        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_exception()

    def test_nrobo_cli_arg_VERSION_switch(self):
        """Validate nRoBo cli --VERSION switch: --VERSION"""

        SWITCH = '--VERSION'

        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_command_is_None()

    def test_nrobo_cli_arg_suppress_switch(self):
        """Validate nRoBo cli --suppress switch: --suppress"""

        SWITCH = '--suppress'
        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        command.remove(SWITCH)

        self._assert_command(command)

    def test_nrobo_cli_arg_browsers_switch_with_value_chrome(self):
        """Validate nRoBo cli --browser switch: --browser chrome"""

        SWITCH = '--browser'
        VALUE = 'chrome'

        command = ['pytest', SWITCH, VALUE]
        sys.argv = command.copy()

        command.remove(SWITCH)
        command.remove(VALUE)

        self._assert_command(command)

    def test_nrobo_cli_arg_browsers_switch_with_value_chrome_headless(self):
        """Validate nRoBo cli --browser switch: --browser chrome_headless"""

        PYTEST = "PYTEST"
        SWITCH = '--browser'
        VALUE = 'chrome_headless'

        from nrobo.cli.launcher import launcher_command
        command = [PYTEST, SWITCH, VALUE]
        sys.argv = command.copy()

        self._assert_command_replace_default_values(SWITCH, VALUE)

    def test_nrobo_cli_arg_browsers_switch_with_value_firefox(self):
        """Validate nRoBo cli --browser switch: --browser firefox"""

        PYTEST = "PYTEST"
        SWITCH = '--browser'
        VALUE = 'firefox'

        command = [PYTEST, SWITCH, VALUE]
        sys.argv = command.copy()

        self._assert_command_replace_default_values(SWITCH, VALUE)

    def test_nrobo_cli_arg_browsers_switch_with_value_firefox_headless(self):
        """Validate nRoBo cli --browser switch: --browser firefox_headless"""

        PYTEST = "PYTEST"
        SWITCH = '--browser'
        VALUE = 'firefox_headless'

        command = [PYTEST, SWITCH, VALUE]
        sys.argv = command.copy()

        self._assert_command_replace_default_values(SWITCH, VALUE)

    def test_nrobo_cli_arg_browsers_switch_with_value_safari(self):
        """Validate nRoBo cli --browser switch: --browser safari"""

        PYTEST = "PYTEST"
        SWITCH = '--browser'
        VALUE = 'safari'

        command = [PYTEST, SWITCH, VALUE]
        sys.argv = command.copy()

        self._assert_command_replace_default_values(SWITCH, VALUE)

    def test_nrobo_cli_arg_browsers_switch_with_value_edge(self):
        """Validate nRoBo cli --browser switch: --browser edge"""

        PYTEST = "PYTEST"
        SWITCH = '--browser'
        VALUE = 'edge'

        command = [PYTEST, SWITCH, VALUE]
        sys.argv = command.copy()

        self._assert_command_replace_default_values(SWITCH, VALUE)

    def test_nrobo_cli_arg_browsers_switch_with_value_of_not_supported_browser(self):
        """Validate nRoBo cli --browser switch: --browser xxx"""

        PYTEST = "PYTEST"
        SWITCH = '--browser'
        VALUE = 'xxx'

        command = [PYTEST, SWITCH, VALUE]
        sys.argv = command.copy()

        try:
            launcher_command()
        except BrowserNotSupported as e:
            assert True
            return

        assert False

    def test_nrobo_cli_arg_browser_switch_without_value(self):
        """Validate nRoBo cli --browser switch without value: --browser """

        SWITCH = '--browser'

        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_exception()

    def test_nrobo_cli_arg_browser_config_switch(self):
        """Validate nRoBo cli --browser-config switch: --browser BROWSER-CONFIG"""

        SWITCH = '--browser-config'
        VALUE = 'xyz'

        command = ['pytest', SWITCH, VALUE]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_browser_config_switch_without_value(self):
        """Validate nRoBo cli --browser-config switch without value: --browser """

        SWITCH = '--browser-config'

        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_exception()

    def test_nrobo_cli_arg_key_switch(self):
        """Validate nRoBo cli --key switch: --key KEY"""

        SWITCH = '--key'
        VALUE = '1'

        command = ['pytest', SWITCH, VALUE]
        sys.argv = command.copy()

        command[1] = '-k'

        self._assert_command(command)

    def test_nrobo_cli_arg_key_switch_without_value(self):
        """Validate nRoBo cli --key switch without value: --key """

        SWITCH = '--key'

        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_exception()

    def test_nrobo_cli_arg_grid_switch(self):
        """Validate nRoBo cli --grid switch: --grid GRID"""

        SWITCH = '--grid'
        VALUE = 'https://apple.com'

        command = ['pytest', SWITCH, VALUE]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_grid_switch_without_value(self):
        """Validate nRoBo cli --grid switch without value: --grid """

        SWITCH = '--grid'

        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_exception()

    def test_nrobo_cli_arg_marker_switch(self):
        """Validate nRoBo cli --marker switch: --marker MARKER"""

        SWITCH = '--marker'
        VALUE = 'test'

        command = ['pytest', SWITCH, VALUE]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_marker_switch_without_value(self):
        """Validate nRoBo cli --marker switch: --marker """

        SWITCH = '--marker'

        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_exception()

    def test_nrobo_cli_arg_markers_switch(self):
        """Validate nRoBo cli --markers switch: --markers MARKERS"""

        SWITCH = '--markers'

        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_command_is_None()

    def test_nrobo_cli_arg_exitfirst_switch(self):
        """Validate nRoBo cli --exitfirst switch: --exitfirst """

        SWITCH = '--exitfirst'

        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_fixtures_switch(self):
        """Validate nRoBo cli --fixtures switch: --fixtures """

        SWITCH = '--fixtures'

        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_command_is_None()

    def test_nrobo_cli_arg_funcargs_switch(self):
        """Validate nRoBo cli --funcargs switch: --funcargs """

        SWITCH = '--funcargs'

        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_command_is_None()

    def test_nrobo_cli_arg_fixtures_per_test_switch(self):
        """Validate nRoBo cli --fixtures-per-test switch: --fixtures-per-test """

        SWITCH = '--fixtures-per-test'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_command_is_None()

    def test_nrobo_cli_arg_pdb_switch(self):
        """Validate nRoBo cli --pdb switch: --pdb """

        SWITCH = '--pdb'

        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_pdbcls_switch(self):
        """Validate nRoBo cli --pdbcls switch: --pdbcls modulename:classname"""

        SWITCH = '--pdbcls'
        VALUE = 'modulename:classname'

        command = ['pytest', SWITCH, VALUE]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_pdbcls_switch_without_value(self):
        """Validate nRoBo cli --pdbcls switch without value: --pdbcls """

        SWITCH = '--pdbcls'

        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_exception()

    def test_nrobo_cli_arg_trace_switch(self):
        """Validate nRoBo cli --trace switch: --trace """

        SWITCH = '--trace'

        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_capture_switch(self):
        """Validate nRoBo cli --capture switch: --capture method"""

        SWITCH = '--capture'
        VALUE = 'method'

        command = ['pytest', SWITCH, VALUE]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_capture_switch_without_value(self):
        """Validate nRoBo cli --capture switch without value: --capture method"""

        SWITCH = '--capture'

        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_exception()

    def test_nrobo_cli_arg_capture_no_switch(self):
        """Validate nRoBo cli --capture-no switch: --capture-no """

        SWITCH = '--capture-no'

        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        command[1] = '-s'

        self._assert_command(command)

    def test_nrobo_cli_arg_runxfail_switch(self):
        """Validate nRoBo cli --runxfail switch: --runxfail """

        SWITCH = '--runxfail'

        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_last_failed_switch(self):
        """Validate nRoBo cli --last-failed switch: --last-failed """

        SWITCH = '--last-failed'

        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_failed_first_switch(self):
        """Validate nRoBo cli --failed-first switch: --failed-first """

        SWITCH = '--failed-first'

        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_new_first_switch(self):
        """Validate nRoBo cli --new-first switch: --new-first """

        SWITCH = '--new-first'

        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_cache_show_switch(self):
        """Validate nRoBo cli --cache-show switch: --cache-show [CACHESHOW]"""

        SWITCH = '--cache-show'
        VALUE = 'method'

        command = ['pytest', SWITCH, VALUE]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_cache_show_switch_without_value(self):
        """Validate nRoBo cli --cache-show switch without: --cache-show [CACHESHOW]"""

        SWITCH = '--cache-show'

        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_exception()

    def test_nrobo_cli_arg_cache_clear_switch(self):
        """Validate nRoBo cli --cache-clear switch: --cache-clear"""

        SWITCH = '--cache-clear'

        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_lfnf_switch(self):
        """Validate nRoBo cli --lfnf switch: --lfnf [{all,none}]"""

        SWITCH = '--lfnf'
        VALUE = '{all,none}'

        command = ['pytest', SWITCH, VALUE]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_lfnf_switch_without_value(self):
        """Validate nRoBo cli --lfnf switch without: --lfnf [{all,none}]"""

        SWITCH = '--lfnf'

        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_exception()

    def test_nrobo_cli_arg_sw_switch(self):
        """Validate nRoBo cli --sw switch: --sw"""

        SWITCH = '--sw'

        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_stepwise_switch(self):
        """Validate nRoBo cli --stepwise switch: --stepwise"""

        SWITCH = '--stepwise'

        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_sw_skip_switch(self):
        """Validate nRoBo cli --sw-skip switch: --sw-skip"""

        SWITCH = '--sw-skip'

        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_stepwise_skip_switch(self):
        """Validate nRoBo cli --stepwise-skip switch: --stepwise-skip"""

        SWITCH = '--stepwise-skip'

        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_durations_switch(self):
        """Validate nRoBo cli --durations switch: --durations N"""

        SWITCH = '--durations'
        VALUE = '0.4445'

        command = ['pytest', SWITCH, VALUE]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_durations_min_switch(self):
        """Validate nRoBo cli --durations-min switch: --durations-min N"""

        SWITCH = '--durations-min'
        VALUE = '0.006'

        command = ['pytest', SWITCH, VALUE]
        sys.argv = command.copy()

        self._assert_command_replace_default_values(SWITCH, VALUE)

    def test_nrobo_cli_arg_durations_min_switch_without_value(self):
        """Validate nRoBo cli --durations-min switch without value: --durations-min N"""

        SWITCH = '--durations-min'

        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_exception()

    def test_nrobo_cli_arg_verbose_switch(self):
        """Validate nRoBo cli --verbose switch: --verbose """

        SWITCH = '--verbose'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_no_header_switch(self):
        """Validate nRoBo cli --no-header switch: --no-header """

        SWITCH = '--no-header'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_no_summary_switch(self):
        """Validate nRoBo cli --no-summary switch: --no-summary """

        SWITCH = '--no-summary'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_quiet_switch(self):
        """Validate nRoBo cli --quiet switch: --quiet """

        SWITCH = '--quiet'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_verbosity_switch(self):
        """Validate nRoBo cli --verbosity switch: --verbosity N"""

        SWITCH = '--verbosity'
        VALUE = '1'
        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH, VALUE]
        sys.argv = command.copy()

        self._assert_command_replace_default_values(SWITCH, VALUE)

    def test_nrobo_cli_arg_verbosity_switch_without_value(self):
        """Validate nRoBo cli --verbosity switch without: --verbosity N"""

        SWITCH = '--verbosity'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_exception()

    def test_nrobo_cli_arg_extra_summary_switch(self):
        """Validate nRoBo cli --extra-summary switch: --extra-summary CHARS-CODES"""

        SWITCH = '--extra-summary'
        VALUE = 'CHAR-CODES'
        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH, VALUE]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_extra_summary_switch_without_value(self):
        """Validate nRoBo cli --extra-summary switch without value: --extra-summary CHARS-CODES"""

        SWITCH = '--extra-summary'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_exception()

    def test_nrobo_cli_arg_disable_warning_switch(self):
        """Validate nRoBo cli --disable-warnings switch: --disable-warnings """

        SWITCH = '--disable-warnings'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_showlocals_switch(self):
        """Validate nRoBo cli --showlocals switch: --showlocals """

        SWITCH = '--showlocals'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_tb_switch(self):
        """Validate nRoBo cli --tb switch: --tb STYLE"""

        SWITCH = '--tb'
        VALUE = 'STYLE'
        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH, VALUE]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_tb_switch_without_value(self):
        """Validate nRoBo cli --tb switch without value: --tb STYLE"""

        SWITCH = '--tb'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_exception()

    def test_nrobo_cli_arg_show_capture_switch(self):
        """Validate nRoBo cli --show-capture switch: --show-capture STYLE"""

        SWITCH = '--show-capture'
        VALUE = 'STYLE'
        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH, VALUE]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_show_capture_switch_without_value(self):
        """Validate nRoBo cli --show-capture switch without value: --show-capture STYLE"""

        SWITCH = '--show-capture'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_exception()

    def test_nrobo_cli_arg_full_trace_switch(self):
        """Validate nRoBo cli --full-trace switch: --full-trace """

        SWITCH = '--full-trace'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_color_switch_with_value_auto(self):
        """Validate nRoBo cli --color switch: --color auto"""

        SWITCH = '--color'
        VALUE = 'auto'
        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH, VALUE]
        sys.argv = command.copy()

        self._assert_command_replace_default_values(SWITCH, VALUE)

    def test_nrobo_cli_arg_color_switch_with_value_yes(self):
        """Validate nRoBo cli --color switch: --color yes"""

        SWITCH = '--color'
        VALUE = 'yes'
        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH, VALUE]
        sys.argv = command.copy()

        self._assert_command_replace_default_values(SWITCH, VALUE)

    def test_nrobo_cli_arg_color_switch_with_value_no(self):
        """Validate nRoBo cli --color switch: --color yes"""

        SWITCH = '--color'
        VALUE = 'no'
        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH, VALUE]
        sys.argv = command.copy()

        self._assert_command_replace_default_values(SWITCH, VALUE)

    def test_nrobo_cli_arg_color_switch_with_invalid_value(self):
        """Validate nRoBo cli --color switch: --color xxx"""

        SWITCH = '--color'
        VALUE = 'xxx'
        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH, VALUE]
        sys.argv = command.copy()

        self._assert_command_replace_default_values(SWITCH, VALUE)

    def test_nrobo_cli_arg_color_switch_without_value(self):
        """Validate nRoBo cli --color switch without value: --color """

        SWITCH = '--color'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_exception()

    def test_nrobo_cli_arg_code_highlight_switch_with_value_yes(self):
        """Validate nRoBo cli --code-highlight switch: --code-highlight yes"""

        SWITCH = '--code-highlight'
        VALUE = 'yes'
        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH, VALUE]
        sys.argv = command.copy()

        self._assert_command_replace_default_values(SWITCH, VALUE)

    def test_nrobo_cli_arg_code_highlight_switch_with_value_no(self):
        """Validate nRoBo cli --code-highlight switch: --code-highlight no"""

        SWITCH = '--code-highlight'
        VALUE = 'no'
        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH, VALUE]
        sys.argv = command.copy()

        self._assert_command_replace_default_values(SWITCH, VALUE)

    def test_nrobo_cli_arg_code_highlight_switch_with_invalid_value(self):
        """Validate nRoBo cli --code-highlight switch with invalid value: --code-highlight xxx"""

        SWITCH = '--code-highlight'
        VALUE = 'xxx'
        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH, VALUE]
        sys.argv = command.copy()

        self._assert_command_replace_default_values(SWITCH, VALUE)

    def test_nrobo_cli_arg_code_highlight_switch_without_value(self):
        """Validate nRoBo cli --code-highlight switch without value: --code-highlight """

        SWITCH = '--code-highlight'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_exception()

    def test_nrobo_cli_arg_pastebin_switch(self):
        """Validate nRoBo cli --pastebin switch: --pastebin mode"""

        SWITCH = '--pastebin'
        VALUE = 'mode'
        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH, VALUE]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_pastebin_switch_without_value(self):
        """Validate nRoBo cli --pastebin switch without value: --pastebin """

        SWITCH = '--pastebin'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_exception()

    def test_nrobo_cli_arg_junit_xml_switch(self):
        """Validate nRoBo cli --junit-xml switch: --junit-xml filepath"""

        SWITCH = '--junit-xml'
        VALUE = 'filepath'
        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH, VALUE]
        sys.argv = command.copy()

        self._assert_command_replace_default_values(SWITCH, VALUE)

    def test_nrobo_cli_arg_junit_xml_switch_without_value(self):
        """Validate nRoBo cli --junit-xml switch without value: --junit-xml filepath"""

        SWITCH = '--junit-xml'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_exception()

    def test_nrobo_cli_arg_junit_prefix_switch(self):
        """Validate nRoBo cli --junit-prefix switch: --junit-prefix prefix"""

        SWITCH = '--junit-prefix'
        VALUE = 'prefix'
        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH, VALUE]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_junit_prefix_switch_without_value(self):
        """Validate nRoBo cli --junit-prefix switch: --junit-prefix prefix"""

        SWITCH = '--junit-prefix'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_exception()

    def test_nrobo_cli_arg_pythonwarnings_switch(self):
        """Validate nRoBo cli --pythonwarnings switch: --pythonwarnings [pythonwarnings]]"""

        SWITCH = '--pythonwarnings'
        VALUE = 'pythonwarnings'
        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH, VALUE]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_pythonwarnings_switch_without_value(self):
        """Validate nRoBo cli --pythonwarnings switch without value: --pythonwarnings [pythonwarnings]]"""

        SWITCH = '--pythonwarnings'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_exception()

    def test_nrobo_cli_arg_maxfail_switch(self):
        """Validate nRoBo cli --maxfail switch: --maxfail [num]]"""

        SWITCH = '--maxfail'
        VALUE = 'num'
        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH, VALUE]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_maxfail_switch_without_value(self):
        """Validate nRoBo cli --maxfail switch without value: --maxfail [num]]"""

        SWITCH = '--maxfail'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_exception()

    def test_nrobo_cli_arg_strict_config_switch(self):
        """Validate nRoBo cli --strict-config switch without value: --strict-config """

        SWITCH = '--strict-config'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_strict_markers_switch(self):
        """Validate nRoBo cli --strict-markers switch without value: --strict-markers """

        SWITCH = '--strict-markers'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_strict_switch(self):
        """Validate nRoBo cli --strict switch: --strict """

        SWITCH = '--strict'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_configuration_switch(self):
        """Validate nRoBo cli --configuration switch: --configuration file"""

        SWITCH = '--configuration'
        VALUE = 'file'
        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH, VALUE]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_configuration_switch_without_value(self):
        """Validate nRoBo cli --configuration switch without value: --configuration file"""

        SWITCH = '--configuration'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_exception()

    def test_nrobo_cli_arg_continue_on_collection_errors_switch(self):
        """Validate nRoBo cli --continue-on-collection-errors switch: --continue-on-collection-errors"""

        SWITCH = '--continue-on-collection-errors'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_rootdir_switch(self):
        """Validate nRoBo cli --rootdir switch: --rootdir file"""

        SWITCH = '--rootdir'
        VALUE = 'file'
        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH, VALUE]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_rootdir_switch_without_value(self):
        """Validate nRoBo cli --rootdir switch without value: --rootdir file"""

        SWITCH = '--rootdir'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

    def test_nrobo_cli_arg_co_switch(self):
        """Validate nRoBo cli --co switch: --co """

        SWITCH = '--co'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_command_is_None()

    def test_nrobo_cli_arg_collect_only_switch(self):
        """Validate nRoBo cli --collect-only switch: --co """

        SWITCH = '--collect-only'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_command_is_None()

    def test_nrobo_cli_arg_pyargs_switch(self):
        """Validate nRoBo cli --pyargs switch: --co """

        SWITCH = '--pyargs'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_ignore_switch(self):
        """Validate nRoBo cli --ignore switch: --ignore path"""

        SWITCH = '--ignore'
        VALUE = 'path'
        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH, VALUE]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_ignore_switch_without_value(self):
        """Validate nRoBo cli --ignore switch without value: --ignore path"""

        SWITCH = '--ignore'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_exception()

    def test_nrobo_cli_arg_ignore_glob_switch(self):
        """Validate nRoBo cli --ignore-glob switch: --ignore-glob path"""

        SWITCH = '--ignore-glob'
        VALUE = 'path'
        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH, VALUE]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_ignore_glob_switch_without_value(self):
        """Validate nRoBo cli --ignore-glob switch: --ignore-glob path"""

        SWITCH = '--ignore-glob'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_exception()

    def test_nrobo_cli_arg_deselect_switch(self):
        """Validate nRoBo cli --deselect switch: --deselect nodeid"""

        SWITCH = '--deselect'
        VALUE = 'nodeid'
        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH, VALUE]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_deselect_switch_without_value(self):
        """Validate nRoBo cli --deselect switch without value: --deselect nodeid"""

        SWITCH = '--deselect'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_exception()

    def test_nrobo_cli_arg_confcutdir_switch(self):
        """Validate nRoBo cli --confcutdir switch: --confcutdir path"""

        SWITCH = '--confcutdir'
        VALUE = 'path'
        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH, VALUE]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_confcutdir_switch_without_value(self):
        """Validate nRoBo cli --confcutdir switch: --confcutdir path"""

        SWITCH = '--confcutdir'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_exception()

    def test_nrobo_cli_arg_noconftest_switch(self):
        """Validate nRoBo cli --noconftest switch: --noconftest """

        SWITCH = '--noconftest'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_keep_duplicates_switch(self):
        """Validate nRoBo cli --keep-duplicates switch: --keep-duplicates """

        SWITCH = '--keep-duplicates'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_collect_in_virtualenv_switch(self):
        """Validate nRoBo cli --collect-in-virtualenv switch: --collect-in-virtualenv """

        SWITCH = '--collect-in-virtualenv'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_import_mode_switch(self):
        """Validate nRoBo cli --import-mode switch: --import-mode mode"""

        SWITCH = '--import-mode'
        VALUE = '{prepend,append,importlib}'
        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH, VALUE]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_import_mode_switch_without_value(self):
        """Validate nRoBo cli --import-mode switch: --import-mode mode"""

        SWITCH = '--import-mode'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_exception()

    def test_nrobo_cli_arg_doctest_modules_switch(self):
        """Validate nRoBo cli --doctest-modules switch: --doctest-modules """

        SWITCH = '--doctest-modules'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_doctest_report_switch(self):
        """Validate nRoBo cli --doctest-report switch: --doctest-report ['{none,cdiff,ndiff,udiff,only_first_failure}']"""

        SWITCH = '--doctest-report'
        VALUE = '{none,cdiff,ndiff,udiff,only_first_failure}'
        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH, VALUE]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_doctest_report_switch_without_value(self):
        """Validate nRoBo cli --doctest-report switch without value: --doctest-report ['{none,cdiff,ndiff,udiff,only_first_failure}']"""

        SWITCH = '--doctest-report'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_exception()

    def test_nrobo_cli_arg_doctest_glob_switch(self):
        """Validate nRoBo cli --doctest-glob switch: --doctest-glob pat"""

        SWITCH = '--doctest-glob'
        VALUE = 'pat'
        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH, VALUE]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_doctest_glob_switch_without_value(self):
        """Validate nRoBo cli --doctest-glob switch without value: --doctest-glob pat"""

        SWITCH = '--doctest-glob'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_exception()

    def test_nrobo_cli_arg_doctest_ignore_import_errors_switch(self):
        """Validate nRoBo cli --doctest-ignore-import-errors switch: --doctest-ignore-import-errors """

        SWITCH = '--doctest-ignore-import-errors'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_doctest_continue_on_failure_switch(self):
        """Validate nRoBo cli --doctest-continue-on-failure switch: --doctest-continue-on-failure """

        SWITCH = '--doctest-continue-on-failure'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_doctest_continue_on_failure_switch(self):
        """Validate nRoBo cli --doctest-continue-on-failure switch: --doctest-continue-on-failure """

        SWITCH = '--doctest-continue-on-failure'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_basetemp_switch(self):
        """Validate nRoBo cli --basetemp switch: --basetemp dir"""

        SWITCH = '--basetemp'
        VALUE = 'dir'
        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH, VALUE]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_basetemp_switch_without_value(self):
        """Validate nRoBo cli --basetemp switch without value: --basetemp dir"""

        SWITCH = '--basetemp'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_exception()

    def test_nrobo_cli_arg_version_switch(self):
        """Validate nRoBo cli --version switch: --version """

        SWITCH = '--version'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_command_is_None()

    def test_nrobo_cli_arg_plugin_module_switch(self):
        """Validate nRoBo cli --plugin-module switch: --plugin-module name"""

        SWITCH = '--plugin-module'
        VALUE = 'name'
        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH, VALUE]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_plugin_module_switch_without_value(self):
        """Validate nRoBo cli --plugin-module switch: --plugin-module name"""

        SWITCH = '--plugin-module'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_exception()

    def test_nrobo_cli_arg_trace_config_switch(self):
        """Validate nRoBo cli --trace-config switch: --trace-config """

        SWITCH = '--trace-config'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_debug_switch(self):
        """Validate nRoBo cli --debug switch: --debug """

        SWITCH = '--debug'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_override_ini_switch(self):
        """Validate nRoBo cli --override-ini switch: --override-ini """

        SWITCH = '--override-ini'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_assert_switch(self):
        """Validate nRoBo cli --assert switch: --assert mode"""

        SWITCH = '--assert'
        VALUE = 'plain | rewrite'
        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH, VALUE]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_assert_switch_without_value(self):
        """Validate nRoBo cli --assert switch without value: --assert mode"""

        SWITCH = '--assert'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_exception()

    def test_nrobo_cli_arg_setup_only_switch(self):
        """Validate nRoBo cli --setup-only switch: --setup-only """

        SWITCH = '--setup-only'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_setup_show_switch(self):
        """Validate nRoBo cli --setup-show switch: --setup-show """

        SWITCH = '--setup-show'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_setup_plan_switch(self):
        """Validate nRoBo cli --setup-plan switch: --setup-plan """

        SWITCH = '--setup-plan'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_command_is_None()

    def test_nrobo_cli_arg_log_level_switch(self):
        """Validate nRoBo cli --log-level switch: --log-level mode"""

        SWITCH = '--log-level'
        VALUE = 'LEVEL'
        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH, VALUE]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_log_level_switch_without_value(self):
        """Validate nRoBo cli --log-level switch: --log-level mode"""

        SWITCH = '--log-level'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_exception()

    def test_nrobo_cli_arg_log_format_switch(self):
        """Validate nRoBo cli --log-format switch: --log-format LOG_FORMAT"""

        SWITCH = '--log-format'
        VALUE = 'LOG_FORMAT'
        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH, VALUE]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_log_format_switch_without_value(self):
        """Validate nRoBo cli --log-format switch: --log-format LOG_FORMAT"""

        SWITCH = '--log-format'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_exception()

    def test_nrobo_cli_arg_log_date_format_switch(self):
        """Validate nRoBo cli --log-date-format switch: --log-date-format LOG_DATE_FORMAT"""

        SWITCH = '--log-date-format'
        VALUE = 'LOG_DATE_FORMAT'
        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH, VALUE]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_log_date_format_switch_without_value(self):
        """Validate nRoBo cli --log-date-format switch: --log-date-format LOG_DATE_FORMAT"""

        SWITCH = '--log-date-format'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_exception()

    def test_nrobo_cli_arg_log_cli_level_switch(self):
        """Validate nRoBo cli --log-cli-level switch: --log-cli-level LOG_CLI_LEVEL"""

        SWITCH = '--log-cli-level'
        VALUE = 'LOG_CLI_LEVEL'
        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH, VALUE]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_log_cli_level_switch_without_value(self):
        """Validate nRoBo cli --log-cli-level switch: --log-cli-level LOG_CLI_LEVEL"""

        SWITCH = '--log-cli-level'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_exception()

    def test_nrobo_cli_arg_log_cli_format_switch(self):
        """Validate nRoBo cli --log-cli-format switch: --log-cli-format LOG_CLI_FORMAT"""

        SWITCH = '--log-cli-format'
        VALUE = 'LOG_CLI_FORMAT'
        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH, VALUE]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_log_cli_format_switch_without_value(self):
        """Validate nRoBo cli --log-cli-format switch: --log-cli-format LOG_CLI_FORMAT"""

        SWITCH = '--log-cli-format'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_exception()

    def test_nrobo_cli_arg_log_cli_date_format_switch(self):
        """Validate nRoBo cli --log-cli-date-format switch: --log-cli-date-format LOG_CLI_DATE_FORMAT"""

        SWITCH = '--log-cli-date-format'
        VALUE = 'LOG_CLI_DATE_FORMAT'
        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH, VALUE]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_log_cli_date_format_switch_without_value(self):
        """Validate nRoBo cli --log-cli-date-format switch: --log-cli-date-format LOG_CLI_DATE_FORMAT"""

        SWITCH = '--log-cli-date-format'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_exception()

    def test_nrobo_cli_arg_log_file_switch(self):
        """Validate nRoBo cli --log-file switch: --log-file LOG_FILE"""

        SWITCH = '--log-file'
        VALUE = 'LOG_FILE'
        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH, VALUE]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_log_file_switch_without_value(self):
        """Validate nRoBo cli --log-file switch: --log-file LOG_FILE"""

        SWITCH = '--log-file'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_exception()

    def test_nrobo_cli_arg_log_file_level_switch(self):
        """Validate nRoBo cli --log-file-level switch: --log-file-level LOG_FILE_LEVEL"""

        SWITCH = '--log-file-level'
        VALUE = 'LOG_FILE_LEVEL'
        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH, VALUE]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_log_file_level_switch_without_value(self):
        """Validate nRoBo cli --log-file-level switch: --log-file-level LOG_FILE_LEVEL"""

        SWITCH = '--log-file-level'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_exception()

    def test_nrobo_cli_arg_log_file_format_switch(self):
        """Validate nRoBo cli --log-file-format switch: --log-file-format LOG_FILE_FORMATE"""

        SWITCH = '--log-file-format'
        VALUE = 'LOG_FILE_FORMATE'
        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH, VALUE]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_log_file_format_switch_without_value(self):
        """Validate nRoBo cli --log-file-format switch: --log-file-format LOG_FILE_FORMATE"""

        SWITCH = '--log-file-format'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_exception()

    def test_nrobo_cli_arg_log_file_date_format_switch(self):
        """Validate nRoBo cli --log-file-date-format switch: --log-file-date-format LOG_FILE_DATE_FORMAT"""

        SWITCH = '--log-file-date-format'
        VALUE = 'LOG_FILE_FORMATE'
        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH, VALUE]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_log_file_date_format_switch_without_value(self):
        """Validate nRoBo cli --log-file-date-format switch without value: --log-file-date-format LOG_FILE_DATE_FORMAT"""

        SWITCH = '--log-file-date-format'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_exception()

    def test_nrobo_cli_arg_log_auto_indent_switch(self):
        """Validate nRoBo cli --log-auto-indent switch: --log-auto-indent LOG-AUTO-INDENT"""

        SWITCH = '--log-auto-indent'
        VALUE = 'LOG-AUTO-INDENT'
        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH, VALUE]
        sys.argv = command.copy()

        self._assert_command(command)

    def test_nrobo_cli_arg_log_auto_indent_switch_without_value(self):
        """Validate nRoBo cli --log-auto-indent switch without value: --log-auto-indent LOG-AUTO-INDENT"""

        SWITCH = '--log-auto-indent'

        from nrobo.cli.launcher import launcher_command
        command = ['pytest', SWITCH]
        sys.argv = command.copy()

        self._assert_exception()









