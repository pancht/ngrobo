import os
import sys

from nrobo import EnvKeys

from nrobo import NROBO_PATHS


class TestLauncherFeature:

    def test_launcher_command_with_no_args(self):
        """Test app switch"""

        from nrobo.cli.launcher import launcher_command

        from nrobo.cli import main

        print(sys.argv)


