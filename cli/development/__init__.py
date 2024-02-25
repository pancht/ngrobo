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

from nrobo import *
from nrobo.util.common import Common
from cli.build import ENV_CLI_SWITCH


def set_switch_environment(env: str, debug=False):
    """sets the environment"""

    if env not in [ENV_CLI_SWITCH.TEST, ENV_CLI_SWITCH.PROD]:
        print(f"Wrong environment provided=> {env}. Valid options are {ENV_CLI_SWITCH.PROD} | {ENV_CLI_SWITCH.TEST}")
        exit()

    # set the environment
    set_environment()

    file_content = ""

    file_content = Common.read_file_as_string(
        NROBO_PATHS.EXEC_DIR / Path(NROBO_CONST.NROBO) / Path(NROBO_PATHS.INIT_PY)
    )

    # update environment to production_machine
    # pattern for finding version setting
    PATTERN = ""

    # Replacement text
    if env == ENV_CLI_SWITCH.TEST:
        PATTERN = "(os.environ\[EnvKeys.ENVIRONMENT\][ ]*=[ ]*Environment.PRODUCTION)"
        REPLACEMENT_TEXT = "os.environ[EnvKeys.ENVIRONMENT]" + " = Environment.DEVELOPMENT"
    elif env == ENV_CLI_SWITCH.PROD:
        PATTERN = "(os.environ\[EnvKeys.ENVIRONMENT\][ ]*=[ ]*Environment.DEVELOPMENT)"
        REPLACEMENT_TEXT = "os.environ[EnvKeys.ENVIRONMENT]" + " = Environment.PRODUCTION"
    else:
        print(f"Wrong environment provided=> {env}. Valid options are {ENV_CLI_SWITCH.PROD} | {ENV_CLI_SWITCH.TEST}")
        exit()

    PATTERN_REGULAR_EXPRESSION = PATTERN

    # Update version number in README file
    file_content = re.sub(PATTERN_REGULAR_EXPRESSION, REPLACEMENT_TEXT, file_content, count=1)

    # Write file_content
    Common.write_text_to_file(
        NROBO_PATHS.EXEC_DIR / Path(NROBO_CONST.NROBO) / Path(NROBO_PATHS.INIT_PY),
        file_content
    )
