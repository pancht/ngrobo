import os

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

    terminal([__PIP__, 'install', '-r', requirements_file])
