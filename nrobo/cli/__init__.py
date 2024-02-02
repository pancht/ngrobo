"""
install command line utility of nrobo-copy framework.
"""
from nrobo.util.process import run_command
from nrobo.util.python import verify_set_python_command
from nrobo.util.constants import CONST
from nrobo.util.commands.ncommands import clear_screen, remove_files_recursively

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


def greet_the_guest():
    greet_msg = 'Namastey Wolrd!. Thank you for choosing, NROBO.'.format(CONST.NEWLINE)
    formatted_heart_string = CONST.HEART_RED * (len(greet_msg)//2)

    print('\n{}\n{}\n{}'.format(formatted_heart_string, greet_msg, formatted_heart_string))
    print('\nWe are still in the process of refactoring next gen nrobo.'
          '\nStay tuned!\n')

def main():
    """
    Entry point of nrobo command-line-utility.

    :return:
    """
    clear_screen()
    verify_set_python_command()
    greet_the_guest()
    remove_files_recursively("dist")





