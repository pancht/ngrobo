"""Test launcher functionalities module."""
import sys


class TestLauncherFeature:  # pylint: disable=R0903
    """Test launcher feature."""
    def test_launcher_command_with_no_args(self):
        """Test app switch"""

        print(sys.argv)
