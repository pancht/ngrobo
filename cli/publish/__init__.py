from cli.build import ENV_CLI_SWITCH
from cli.check import check
from nrobo import *
from nrobo.util.constants import CONST
from nrobo.util.platform import PLATFORMS
from nrobo.util.process import terminal

global __CUR_ENV__


def publish(target, *, debug: bool = False, override: bool = False):
    """
    Check and publish package

    :return:
    """
    check()

    global __CUR_ENV__

    if str(target).lower() == ENV_CLI_SWITCH.TEST:
        __CUR_ENV__ = "testpypi"
    elif str(target).lower() == ENV_CLI_SWITCH.PROD:
        __CUR_ENV__ = "pypi"
    else:
        print("Invalid target environment <{}>. Options: test | prod".format(target))
        exit(1)

    with console.status(f"Publish on pypi..."):
        command = ""
        if os.environ[EnvKeys.HOST_PLATFORM] in [PLATFORMS.DARWIN, PLATFORMS.LINUX, PLATFORMS.MACOS]:
            command = ["twine", "upload", "--repository", __CUR_ENV__,
                       "dist" + os.sep + "*"]
        elif os.environ[EnvKeys.HOST_PLATFORM] in [PLATFORMS.WINDOWS]:
            command = ["twine", "upload", "--repository", __CUR_ENV__,
                       CONST.DOT + os.sep + "dist" + os.sep + "*.*"]

        # add --skip-existing switch
        if override:
            command.append("--skip-existing")

        # Run command
        console_output = terminal(command, text=True, capture_output=True)

        if errors_in_console(r'(HTTPError:)', console_output.stdout):
            print(console_output.stdout)
            exit(1)
        else:
            from cli.build import get_version_from_yaml_version_files, write_new_version_to_nrobo_init_py_file
            build_version = get_version_from_yaml_version_files(target)
            write_new_version_to_nrobo_init_py_file(build_version)

            console.print(f"nRoBo {get_version_from_yaml_version_files(target)} is published successfully.")


def errors_in_console(pattern: str, string: str) -> bool:
    """return True if pattern is found in string else false."""
    import re
    return re.search(pattern, string)
