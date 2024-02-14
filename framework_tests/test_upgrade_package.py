import os
import re
from pathlib import Path

from nrobo import console


class TestUpgradePkg():

    def test_get_host_version_method(self):
        """Validate nrobo.cli.upgrade.get_host_version() method"""

        from nrobo.cli.upgrade import get_host_version
        from nrobo import __version__

        assert __version__ == get_host_version()

    def test_get_pypi_index_method(self):
        """Validate nrobo.cli.upgrade.get_pypi_index() method"""

        from nrobo.cli.upgrade import get_pypi_index
        package = "nrobo"
        import subprocess
        result = subprocess.run(['pip', 'index', 'versions', package], text=True, capture_output=True)

        import re
        match = re.search(package + r" \(([\d]+4[.][\d]+[.][\d]+)\)", result.stdout)

        # Test return type AnyStr
        assert match.group(1) == get_pypi_index(package)

        package = "xyzabc"
        result = subprocess.run(['pip', 'index', 'versions', package], text=True, capture_output=True)
        match = re.search(package + r" \(([\d]+4[.][\d]+[.][\d]+)\)", result.stdout)
        assert None == get_pypi_index(package)

    def test_update_available_method(self):
        """Validate nrobo.cli.upgrade.update_available() method"""

        from nrobo.cli.upgrade import update_available, get_pypi_index, get_host_version

        with console.status("Test if update not available"):

            # scenario-1: Update not available
            package = "nrobo"
            from nrobo import __version__
            if __version__ == get_pypi_index(package):
                assert update_available() == False
            else:
                assert update_available() == True
