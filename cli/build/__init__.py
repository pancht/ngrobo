"""
=====================CAUTION=======================
DO NOT DELETE THIS FILE SINCE IT IS PART OF NROBO
FRAMEWORK AND IT MAY CHANGE IN THE FUTURE UPGRADES
OF NROBO FRAMEWORK. THUS, TO BE ABLE TO SAFELY UPGRADE
TO LATEST NROBO VERSION, PLEASE DO NOT DELETE THIS
FILE OR ALTER ITS LOCATION OR ALTER ITS CONTENT!!!
===================================================

This module has actions pertaining to nRoBo build
process.

@author: Panchdev Singh Chauhan
@email: erpanchdev@gmail.com
"""

import validatenrobo
from nrobo import *
from nrobo import console, STYLE
from nrobo.util.commands.ncommands import remove_files_recursively
from nrobo.util.common import Common
from nrobo.util.constants import EXT
from nrobo.util.platform import PLATFORMS

__DIST_DIR__ = "dist"
__VERSIONS_DIR__ = "versions" + os.sep
__CUR_ENV__ = ""


class ENV_CLI_SWITCH:
    TEST = "test"
    PROD = "prod"


def get_version_from_yaml_version_files(target) -> str:
    """Get and return version form respective target environment yaml file."""

    # Grab version number from version yaml files in version/ directory
    return Common.read_yaml(__VERSIONS_DIR__ + target + EXT.YAML, fail_on_failure=False)['version']


def increment_version(version) -> str:
    """
    Increment <version> by 1 and return it."""

    # regular expression to verify version
    # major.minor.nightly-build
    regx = re.compile(r'([\d]+).[\d]+.[\d]+.*')

    if regx.match(version) is None:
        print("Version file corrupted! Correct it, please!")
        exit(1)
    else:
        # increment version
        res = re.findall(r'[\d]+', version)
        res[2] = str(int(res[2]) + 1)

        return CONST.DOT.join(res)


def decrement_version(version) -> str:
    """
    Decrement version by 1 and return it."""

    # regular expression to verify version
    # major.minor.nightly-build
    regx = re.compile(r'([\d]+).[\d]+.[\d]+.*')

    if regx.match(version) is None:
        print("Version file corrupted! Correct it, please!")
        exit(1)
    else:
        # increment version
        res = re.findall(r'[\d]+', version)
        res[2] = str(int(res[2]) - 1)

        return CONST.DOT.join(res)


def write_new_version_in_test_version_file(new_version: str) -> None:
    """Update version in version files with given <new_version>"""

    for _env in [ENV_CLI_SWITCH.TEST, ENV_CLI_SWITCH.PROD]:
        version_file = __VERSIONS_DIR__ + _env + EXT.YAML
        content = Common.read_yaml(version_file, fail_on_failure=False)
        content['version'] = '' + new_version + ''
        Common.write_yaml(version_file, content)


def write_new_version_to_pyproject_toml_file(new_version) -> None:
    """Update pyproject.toml file with given <new_version>"""

    PYPROJECT_TOML_FILE = "pyproject.toml"

    # Read file content as string
    file_content = str(Common.read_file_as_string(PYPROJECT_TOML_FILE))

    # pattern for finding version setting
    PATTERN_PREFIX = "version = "
    PATTERN_REGULAR_EXPRESSION = PATTERN_PREFIX + r'("[\d.]+")'

    # Replacement text
    REPLACEMENT_TEXT = PATTERN_PREFIX + "\"" + new_version + "\""

    # Update version number in README file
    file_content = re.sub(PATTERN_REGULAR_EXPRESSION, REPLACEMENT_TEXT, file_content, count=1)

    # Write file_content
    Common.write_text_to_file(PYPROJECT_TOML_FILE, file_content)


def write_new_version_to_nrobo_init_py_file(new_version) -> None:
    """Update nrobo.__init__.py with give <new_version>"""

    nrobo_init_py_file = NROBO_PATHS.EXEC_DIR / NROBO_CONST.NROBO / NROBO_PATHS.INIT_PY

    # Read file content as string
    file_content = str(Common.read_file_as_string(nrobo_init_py_file))

    # pattern for finding version setting
    PATTERN_PREFIX = "__version__ = "
    PATTERN_REGULAR_EXPRESSION = PATTERN_PREFIX + r"('[\d.]+')"

    # Replacement text
    REPLACEMENT_TEXT = PATTERN_PREFIX + "\'" + new_version + "\'"

    # Update version number in README file
    file_content = re.sub(PATTERN_REGULAR_EXPRESSION, REPLACEMENT_TEXT, file_content, count=1)

    # Write file_content
    Common.write_text_to_file(nrobo_init_py_file, file_content)


def update_version_pyproject_toml_file(target, override=False) -> int:
    """Update version in pyproject.toml

        Returns 0 if success."""

    global __CUR_ENV__

    if target == ENV_CLI_SWITCH.TEST:
        __CUR_ENV__ = ENV_CLI_SWITCH.TEST.lower()

    elif target == ENV_CLI_SWITCH.PROD:
        __CUR_ENV__ = ENV_CLI_SWITCH.PROD.lower()

    # get version
    version = get_version_from_yaml_version_files(__CUR_ENV__)

    # Increment version
    # version = increment_version(version)

    # update version in pyproject.toml and nrobo/__init__.py files
    write_new_version_in_test_version_file(version)

    # update version in pyproject.toml file
    write_new_version_to_pyproject_toml_file(version)

    return 0


def execute_unittests(debug=False) -> None:
    """Executes unit tests for nRoBo framework validation.

        If any errors during execution, exit nRoBo."""

    return_code = 1

    return_code = validatenrobo.run_unit_tests()

    if not return_code == NROBO_CONST.SUCCESS:
        from cli import set_switch_environment
        console.print(
            f"[{STYLE.HLRed}]One or more validator tests have failed. Please fix failing tests and retry building packages.")
        set_switch_environment(ENV_CLI_SWITCH.TEST, debug)
        console.print(
            f"[{STYLE.HLRed}]Build process failed!!!")
        exit(1)


def copy_conftest_file() -> None:
    """Copies conftest-host.py file from nrobo.framework package to nrobo package."""

    import shutil
    try:
        shutil.copyfile(
            f"{NROBO_PATHS.EXEC_DIR / NROBO_PATHS.CONFTEST_PY}",
            f"{NROBO_PATHS.EXEC_DIR / NROBO_CONST.NROBO / NROBO_PATHS.CONFTEST_PY}")
    except Exception as e:
        raise e


def delete_dist_folder() -> None:
    """Deletes dist folder for vacating space for fresh packages."""

    if os.environ[EnvKeys.HOST_PLATFORM] in [PLATFORMS.DARWIN, PLATFORMS.LINUX, PLATFORMS.MACOS]:
        try:
            remove_files_recursively(__DIST_DIR__)
        except Exception as e:
            print(e)
    elif os.environ[EnvKeys.HOST_PLATFORM] in [PLATFORMS.WINDOWS]:
        terminal(["del", "/q", "/S", __DIST_DIR__ + os.sep + "*.*"])


def run_build_command() -> None:
    """Run build utility."""

    terminal([os.environ[EnvKeys.PYTHON], "-m", "pip", "install", "build"])
    terminal([os.environ[EnvKeys.PYTHON], "-m", "pip", "install", "--upgrade", "build"])
    terminal([os.environ[EnvKeys.PYTHON], "-m", "build"])


def delete_conftest_after_build() -> None:
    """Delete conftest.py file from nrobo package after build process finishes."""

    conftest = f"{NROBO_PATHS.EXEC_DIR / NROBO_CONST.NROBO / NROBO_PATHS.CONFTEST_PY}"
    terminal(["rm", "-f", conftest])


def build(target=ENV_CLI_SWITCH.TEST, *, debug=False, override=False, build_version=None) -> int:
    """Bundle package for <target> environment.

    :param debug: enable/disable debug mode.
    :param target: Either be 'test' | 'prod'
    :return: 0 if packing succeeds else 1"""

    # Always correct version in version yaml files first
    from nrobo.cli.upgrade import get_pypi_index
    from nrobo.util.version import Version
    from cli import BUILD_VERSION

    pypi_version = Version(get_pypi_index(NROBO_CONST.NROBO))

    if build_version == BUILD_VERSION.MAJOR:
        new_version = pypi_version.major_incremented()
    elif build_version == BUILD_VERSION.MINOR:
        new_version = pypi_version.minor_incremented()
    elif build_version is None:
        new_version = pypi_version.patch_incremented()
    else:
        new_version = pypi_version.patch_incremented()

    write_new_version_in_test_version_file(new_version)
    write_new_version_to_nrobo_init_py_file(new_version)

    # run_nrobo_validator_tests
    console.rule(f"[{STYLE.HLOrange}]Packaging nRoBo...")
    with console.status(f"[{STYLE.TASK}]Validating framework\n"):
        # update ENV_CLI_SWITCH=PRODUCTION in nrobo/__INIT__.py
        from cli import set_switch_environment
        set_switch_environment(ENV_CLI_SWITCH.PROD, debug)

        console.rule(f"[{STYLE.HLOrange}]Running unit tests")
        execute_unittests(debug)  # run unit tests

    with console.status(f"[{STYLE.TASK}]Switching environment to PRODUCTION for testing only\n"):
        # update ENV_CLI_SWITCH=PRODUCTION in nrobo/__INIT__.py
        set_switch_environment(ENV_CLI_SWITCH.PROD, debug)
        console.print(f"\t[{STYLE.HLOrange}]Environment set to PRODUCTION")

    with console.status(f"[{STYLE.TASK}]Update version in pyproject.toml\n"):
        if update_version_pyproject_toml_file(target, override=override) > 0: return 1  # # update toml version
        console.print(f"\t[{STYLE.HLOrange}]version updated in toml")

    with console.status(f"[{STYLE.TASK}]Update version in nrobo/__init__.py\n"):
        # update toml version
        write_new_version_to_nrobo_init_py_file(get_version_from_yaml_version_files(ENV_CLI_SWITCH.PROD))
        console.print(f"\t[{STYLE.HLOrange}]version updated in toml")

    with console.status(f"[{STYLE.TASK}]Copy conftest.py file under nrobo directory for shipping\n"):
        # copy conftest.py to nrobo directory for shipping
        # Find the directory we executed the script from:
        copy_conftest_file()
        console.print(f"\t[{STYLE.HLOrange}]Conftest.py copied under nrobo directory for packing.")

    with console.status(f"[{STYLE.TASK}]Deleting {__DIST_DIR__}\n"):
        delete_dist_folder()

    with console.status(f"[{STYLE.TASK}]Building packages\n"):
        run_build_command()
        console.print(f"\t[{STYLE.HLOrange}]Packaging completed.")

    with console.status(f"[{STYLE.TASK}]Deleting conftest.py from the nrobo directory after packaging is complete\n"):
        console.print(f"\t[{STYLE.HLOrange}]conftest.py removed from nrobo directory.")
        delete_conftest_after_build()

    with console.status(f"[{STYLE.TASK}]Reset environment back to DEVELOPMENT\n"):
        # Reset ENV_CLI_SWITCH=DEVELOPMENT in nrobo/__INIT__.py
        set_switch_environment(ENV_CLI_SWITCH.TEST, debug)
        console.print(f"\t[{STYLE.HLOrange}]Environment reset.")

    with console.status(f"[{STYLE.TASK}]Correct version in nrobo/__init__.py file\n"):
        import nrobo.cli.detection as detect
        write_new_version_to_nrobo_init_py_file(detect.build_version_from_version_files())
        console.print(f"\t[{STYLE.HLOrange}]Corrected.")

    with console.status(f"[{STYLE.TASK}]Packages are ready. Please run check.\n"):
        # Reset ENV_CLI_SWITCH=DEVELOPMENT in nrobo/__INIT__.py
        console.rule(f"[{STYLE.WARNING}]Now run check on packages.")
        import nrobo.cli.detection as detect
        console.rule(f"Package version: {detect.build_version_from_version_files()} created.")
