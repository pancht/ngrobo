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

        from nrobo.cli.upgrade import update_available, get_pypi_index

        with console.status("Test if update not available"):

            # scenario-1: Update not available
            package = "nrobo"
            from nrobo import __version__
            if __version__ == get_pypi_index(package):
                assert update_available() == False

        with console.status("Test if update available"):

            # scenario-1: Update not available
            package = "nrobo"
            from nrobo import __version__
            if __version__ == get_pypi_index(package):
                """update not available. already covered above"""
                backup_version = __version__
                del __version__
                new_version = '2024.0.1'
                _update_upgrade_init_py(new_version)
                from nrobo import __version__
                assert update_available() == True
                # _update_upgrade_init_py(backup_version)



def _update_upgrade_init_py(version=None):
    """update version info"""
    if version is None:
        return

    from nrobo.util.common import Common
    from nrobo import EnvKeys, NROBO_PATHS, NROBO_CONST
    root = os.environ[EnvKeys.EXEC_DIR]
    file_content = Common.read_file_as_string(Path(root) / NROBO_CONST.NROBO / NROBO_PATHS.INIT_PY)
    # pattern for finding version setting
    PATTERN_PREFIX = "version = "
    PATTERN_REGULAR_EXPRESSION = PATTERN_PREFIX + r'("[\d.]+")'

    # Replacement text
    REPLACEMENT_TEXT = PATTERN_PREFIX + "\'" + version + "\'"

    # Update version number in README file
    file_content = re.sub(PATTERN_REGULAR_EXPRESSION, REPLACEMENT_TEXT, file_content, count=1)

    # Write file_content
    Common.write_text_to_file(Path(root) / NROBO_CONST.NROBO / NROBO_PATHS.INIT_PY, file_content)