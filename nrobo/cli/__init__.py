"""
install command line utility of nrobo-copy framework.
"""
from nrobo.util.process import run_command
from nrobo.util.python import verify_set_python_command

# refer to global defined in nrobo.util.process
global __PYTHON__


def install_requirements(requirements_file):
    """
    Install requirements from requirements.txt
    :return:
    """
    try:
        run_command(__PYTHON__ + " install -r {}".format(requirements_file))
    except Exception as e:
        print(e)


def main():
    """
    Entry point of nrobo command-line-utility.

    :return:
    """
    print('[italic red]Namastey Wolrd! _/\\_')
    verify_set_python_command()
