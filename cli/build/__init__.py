import os
import platform
import re
import time
import subprocess

import validate_nrobo
from nrobo.util.commands.ncommands import clear_screen
from nrobo.util.commands.ncommands import remove_files_recursively, terminal, terminal_nogui
from nrobo.util.common import Common
from nrobo.util.constants import CONST
from nrobo import Python
from nrobo.util.platform import PLATFORMS
from nrobo import *
from cli.development import *
from nrobo import console, STYLE
from nrobo.cli.cli_constants import NREPORT

__DIST_DIR__ = "dist"
__VERSIONS_DIR__ = "versions" + os.sep
__CUR_ENV__ = ""


class ENVIRONMENT:
    TEST = "test"
    PROD = "prod"


def get_version_from_yaml_version_files(target):
    # Grab version number from version yaml files in version/ directory
    return Common.read_yaml(__VERSIONS_DIR__ + target + ".yaml")['version']


def get_incremented_version(version, *, override: bool = False):
    """
    Increment version by 1

    :param override:
    :param version:
    :return:
    """
    if override:
        return version

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


def get_decremented_version(version, *, override: bool = False):
    """
    Decrement version by 1

    :param override:
    :param version:
    :return:
    """
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


def write_new_version_in_test_version_file(new_version: str):
    for _env in ['test', 'prod']:
        version_file = __VERSIONS_DIR__ + _env + ".yaml"
        content = Common.read_yaml(version_file)
        content['version'] = '' + new_version + ''
        Common.write_yaml(version_file, content)


def write_new_version_to_pyproject_toml_file(new_version):
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


def write_new_version_to_nrobo_init_py_file(new_version):
    nrobo_init_py_file = Path(os.environ[EnvKeys.EXEC_DIR]) / NROBO_CONST.NROBO / NROBO_PATHS.INIT_PY

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


def update_version_pyproject_toml_file(target, *, override: bool = False) -> int:
    """
    Update version in pyproject.toml

    :param override:
    :param target:
    :return:
    """
    global __CUR_ENV__

    if target == ENVIRONMENT.TEST:
        __CUR_ENV__ = ENVIRONMENT.TEST.lower()

    elif target == ENVIRONMENT.PROD:
        __CUR_ENV__ = ENVIRONMENT.PROD.lower()

    # get version
    version = get_version_from_yaml_version_files(__CUR_ENV__)

    # Increment version
    version = get_incremented_version(version, override=override)

    # update version in pyproject.toml and nrobo/__init__.py files
    write_new_version_in_test_version_file(version)

    # update version in pyproject.toml file
    write_new_version_to_pyproject_toml_file(version)

    return 0


def execute_unittests(debug=False):
    return_code = 1

    return_code = validate_nrobo.run_unit_tests()
    if not return_code == NROBO_CONST.SUCCESS:
        from cli import set_switch_environment
        console.print(
            f"[{STYLE.HLRed}]One or more validator tests have failed. Please fix failing tests and retry building packages.")
        set_switch_environment('test', debug)
        console.print(
            f"[{STYLE.HLRed}]Build process failed!!!")
        exit(1)


def copy_conftest_file():
    import shutil
    try:
        shutil.copyfile(
            f"{Path(os.environ[EnvKeys.EXEC_DIR]) / NROBO_PATHS.CONFTEST_PY}",
            f"{Path(os.environ[EnvKeys.EXEC_DIR]) / NROBO_CONST.NROBO / NROBO_PATHS.CONFTEST_PY}")
    except Exception as e:
        raise e


def delete_dist_folder():
    if os.environ[EnvKeys.HOST_PLATFORM] in [PLATFORMS.DARWIN, PLATFORMS.LINUX, PLATFORMS.MACOS]:
        try:
            remove_files_recursively(__DIST_DIR__)
        except Exception as e:
            print(e)
    elif os.environ[EnvKeys.HOST_PLATFORM] in [PLATFORMS.WINDOWS]:
        terminal(["del", "/q", "/S", __DIST_DIR__ + os.sep + "*.*"])


def run_build_command():
    terminal([os.environ[EnvKeys.PYTHON], "-m", "pip", "install", "build"])
    terminal([os.environ[EnvKeys.PYTHON], "-m", "pip", "install", "--upgrade", "build"])
    terminal([os.environ[EnvKeys.PYTHON], "-m", "build"])


def delete_conftest_after_build():
    conftest = f"{Path(os.environ[EnvKeys.EXEC_DIR]) / NROBO_CONST.NROBO / NROBO_PATHS.CONFTEST_PY}"
    terminal(["rm", "-f", conftest])


def build(target='test', *, override: bool = False, debug: bool = False) -> int:
    """
    Bundle package for <target> environment.

    :param debug:
    :param override:
    :param target: Either be 'test' | 'prod'
    :return: 0 if packing succeeds else 1
    """
    # Always correct version in version yaml files first
    from nrobo.cli.upgrade import get_pypi_index
    write_new_version_in_test_version_file(get_pypi_index(NROBO_CONST.NROBO))
    write_new_version_to_nrobo_init_py_file(get_pypi_index(NROBO_CONST.NROBO))

    # run_nrobo_validator_tests
    console.rule(f"[{STYLE.HLOrange}]Packaging nRoBo...")
    with console.status(f"[{STYLE.TASK}]Validating framework\n"):
        from cli import set_switch_environment
        set_switch_environment('prod', debug)  # update ENVIRONMENT=PRODUCTION in nrobo/__INIT__.py

        console.rule(f"[{STYLE.HLOrange}]Running unit tests")
        execute_unittests(debug)  # run unit tests

    with console.status(f"[{STYLE.TASK}]Switching environment to PRODUCTION for testing only\n"):
        set_switch_environment('prod', debug)  # update ENVIRONMENT=PRODUCTION in nrobo/__INIT__.py
        console.print(f"\t[{STYLE.HLOrange}]Environment set to PRODUCTION")

    with console.status(f"[{STYLE.TASK}]Update version in pyproject.toml\n"):
        if update_version_pyproject_toml_file(target, override=override) > 0: return 1  # # update toml version
        console.print(f"\t[{STYLE.HLOrange}]version updated in toml")

    with console.status(f"[{STYLE.TASK}]Update version in nrobo/__init__.py\n"):
        write_new_version_to_nrobo_init_py_file(get_version_from_yaml_version_files('prod'))  # update toml version
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
        # Reset ENVIRONMENT=DEVELOPMENT in nrobo/__INIT__.py
        set_switch_environment('test', debug)
        console.print(f"\t[{STYLE.HLOrange}]Environment reset.")

    with console.status(f"[{STYLE.TASK}]Correct version in nrobo/__init__.py file\n"):
        from nrobo.cli.upgrade import get_pypi_index
        write_new_version_to_nrobo_init_py_file(get_incremented_version(get_pypi_index(NROBO_CONST.NROBO)))
        console.print(f"\t[{STYLE.HLOrange}]Corrected.")

    with console.status(f"[{STYLE.TASK}]Packages are ready. Please run check.\n"):
        # Reset ENVIRONMENT=DEVELOPMENT in nrobo/__INIT__.py
        console.rule(f"[{STYLE.WARNING}]Now run check on packages.")
