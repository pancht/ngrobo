"""
=====================CAUTION=======================
DO NOT DELETE THIS FILE SINCE IT IS PART OF NROBO
FRAMEWORK AND IT MAY CHANGE IN THE FUTURE UPGRADES
OF NROBO FRAMEWORK. THUS, TO BE ABLE TO SAFELY UPGRADE
TO LATEST NROBO VERSION, PLEASE DO NOT DELETE THIS
FILE OR ALTER ITS LOCATION OR ALTER ITS CONTENT!!!
===================================================

Unit tests for validating upgrade process.

@author: Panchdev Singh Chauhan
@email: erpanchdev@gmail.com
"""

from nrobo import console, NroboConst


class TestUpgradePkg:
    """Test upgrade package."""
    def test_get_host_version_method(self):
        """Validate nrobo.cli.upgrade.get_host_version() method"""

        from nrobo.cli.upgrade import get_host_version  # pylint: disable=C0415
        from nrobo import __version__  # pylint: disable=C0415

        assert __version__ == get_host_version()

    def test_get_pypi_index_method(self):
        """Validate nrobo.cli.upgrade.get_pypi_index() method"""

        from nrobo.cli.upgrade import get_pypi_index  # pylint: disable=C0415

        package = NroboConst.NROBO
        import subprocess  # pylint: disable=C0415

        result = subprocess.run(  # pylint: disable=W1510
            ["pip", "index", "versions", package], text=True, capture_output=True
        )

        import re  # pylint: disable=C0415

        match = re.search(package + r" \(([\d]+[.][\d]+[.][\d]+)\)", result.stdout)

        # Test return type AnyStr
        assert match.group(1) == get_pypi_index(package)

        package = "xyzabc"
        result = subprocess.run(  # pylint: disable=W1510
            ["pip", "index", "versions", package], text=True, capture_output=True
        )
        match = re.search(package + r" \(([\d]+[.][\d]+[.][\d]+)\)", result.stdout)

        assert get_pypi_index(package) is None

    def test_update_available_method(self):
        """Validate nrobo.cli.upgrade.update_available() method"""

        from nrobo.cli.upgrade import update_available, get_pypi_index  # pylint: disable=C0415
        from nrobo.util.version import Version  # pylint: disable=C0415

        with console.status("Test if update not available"):

            # scenario-1: Update not available
            package = NroboConst.NROBO
            from nrobo import __version__  # pylint: disable=C0415

            if Version(__version__) < Version(get_pypi_index(package)):
                assert update_available()
            else:
                assert not update_available()
