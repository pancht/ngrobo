import os

from nrobo.util.process import terminal
from nrobo.util.platform import __HOST_PLATFORM__, PLATFORMS
from nrobo.util.python import verify_set_python_install_pip_command, __PYTHON__
from nrobo_cli.check import check
from nrobo_cli.build import build, __CUR_ENV__, ENVIRONMENT
from nrobo.util.constants import CONST

global __CUR_ENV__


def publish(target):
    """
    Check and publish package

    :return:
    """
    check()

    global __CUR_ENV__

    if str(target).lower() == ENVIRONMENT.TEST:
        __CUR_ENV__ = "testpypi"
    elif str(target).lower() == ENVIRONMENT.PROD:
        __CUR_ENV__ = "pypi"
    else:
        print("Invalid target environment <{}>. Options: test | prod".format(target))
        exit(1)

    command = ""
    if __HOST_PLATFORM__ in [PLATFORMS.DARWIN, PLATFORMS.LINUX, PLATFORMS.MACOS]:
        command = ["twine", "upload", "--repository", __CUR_ENV__,
                   "dist" + os.sep + "*"]
    elif __HOST_PLATFORM__ in [PLATFORMS.WINDOWS]:
        command = ["twine", "upload", "--repository", __CUR_ENV__,
                  CONST.DOT + os.sep + "dist" + os.sep + "*.*"]

    print(command)

    # Run command
    terminal(command)
