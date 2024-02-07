import os

from nrobo.cli.cli_constansts import nCLI, PACKAGES

from nrobo.util.process import terminal
from nrobo.util.python import __PYTHON__, __PIP__

__REQUIREMENTS__ = "requirements.txt"


def install_nrobo(requirements_file=None):
    """
    Install nrobo

    :return:
    """

    from nrobo.cli.tools import console

    console.rule("Welcome to NROBO install")
    with console.status(f"Installing requirements"):
        if requirements_file is None:
            requirements_file = __REQUIREMENTS__

        if os.path.exists(__REQUIREMENTS__):
            requirements_file = __REQUIREMENTS__
        elif os.path.exists(PACKAGES.NROBO + os.sep + PACKAGES.CLI + os.sep + nCLI.INSTALL + os.sep + __REQUIREMENTS__):
            requirements_file = PACKAGES.NROBO + os.sep + PACKAGES.CLI + os.sep + nCLI.INSTALL + os.sep + __REQUIREMENTS__

        terminal([__PIP__, nCLI.INSTALL, '-r', requirements_file])

    with console.status(f"Installing framework"):
        # create framework folders on host system

        # Copy framework to current directory

        # Copy conftest.py to current directory

        #

        pass

