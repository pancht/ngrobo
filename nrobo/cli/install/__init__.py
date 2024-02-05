import os

from nrobo.cli.cli_constansts import nCLI, PACKAGES

from nrobo.util.process import terminal
from nrobo.util.python import __PYTHON__, __PIP__

__REQUIREMENTS__ = "requirements.txt"


def install_dependencies(requirements_file=None):
    """
    Install requirements from <requirements_file>
    :return:
    """

    if requirements_file is None:
        requirements_file = __REQUIREMENTS__

    if os.path.exists(__REQUIREMENTS__):
        requirements_file = __REQUIREMENTS__
    elif os.path.exists(PACKAGES.NROBO + os.sep + PACKAGES.CLI + os.sep + nCLI.INSTALL + os.sep + __REQUIREMENTS__):
        requirements_file = PACKAGES.NROBO + os.sep + PACKAGES.CLI + os.sep + nCLI.INSTALL + os.sep + __REQUIREMENTS__

    terminal([__PIP__, nCLI.INSTALL, '-r', requirements_file])
