# pylint: disable=R0401
"""
=====================CAUTION=======================
DO NOT DELETE THIS FILE SINCE IT IS PART OF NROBO
FRAMEWORK AND IT MAY CHANGE IN THE FUTURE UPGRADES
OF NROBO FRAMEWORK. THUS, TO BE ABLE TO SAFELY UPGRADE
TO LATEST NROBO VERSION, PLEASE DO NOT DELETE THIS
FILE OR ALTER ITS LOCATION OR ALTER ITS CONTENT!!!
===================================================

No definitions yet!

@author: Panchdev Singh Chauhan
@email: erpanchdev@gmail.com
"""
import sys

from nrobo import *
from nrobo.util.common import Common
from cli.build import EnvCliSwitch


def set_switch_environment(env: str, debug=False):  # pylint: disable=W0613
    """sets the environment"""

    if env not in [EnvCliSwitch.TEST, EnvCliSwitch.PROD]:
        print(
            f"Wrong environment provided=> {env}. "
            f"Valid options are {EnvCliSwitch.PROD} | {EnvCliSwitch.TEST}"
        )
        sys.exit()

    # set the environment
    set_environment()

    file_content = ""

    file_content = Common.read_file_as_string(
        NroboPaths.EXEC_DIR / Path(NroboConst.NROBO) / Path(NroboPaths.INIT_PY)
    )

    # update environment to production_machine
    # pattern for finding version setting
    pattern = ""

    # Replacement text
    if env == EnvCliSwitch.TEST:
        pattern = "(os.environ\[EnvKeys.ENVIRONMENT\][ ]*=[ ]*Environment.PRODUCTION)"  # pylint: disable=W1401
        replacement_text = (
            "os.environ[EnvKeys.ENVIRONMENT]" + " = Environment.DEVELOPMENT"
        )
    elif env == EnvCliSwitch.PROD:
        pattern = "(os.environ\[EnvKeys.ENVIRONMENT\][ ]*=[ ]*Environment.DEVELOPMENT)"  # pylint: disable=W1401
        replacement_text = (
            "os.environ[EnvKeys.ENVIRONMENT]" + " = Environment.PRODUCTION"
        )
    else:
        print(
            f"Wrong environment provided=> {env}. "
            f"Valid options are {EnvCliSwitch.PROD} | {EnvCliSwitch.TEST}"
        )
        sys.exit()

    pattern_regular_expression = pattern

    # Update version number in README file
    file_content = re.sub(
        pattern_regular_expression, replacement_text, file_content, count=1
    )

    # Write file_content
    Common.write_text_to_file(
        NroboPaths.EXEC_DIR / Path(NroboConst.NROBO) / Path(NroboPaths.INIT_PY),
        file_content,
    )
