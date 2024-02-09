import os

from nrobo.util.common import Common
from nrobo import *


def set_switch_environment(env: str):
    """sets the environment"""

    # test environment
    if env not in ['test', 'prod']:
        print(f"Wrong environment provided=> {env}. Valid options are prod | test")
        exit()

    # set the environment
    set_environment()

    file_content = ""

    file_content = Common.read_file_as_string(
        Path(os.environ[EnvKeys.EXEC_DIR]) / Path(NROBO_CONST.NROBO) / Path(NROBO_PATHS.INIT_PY)
    )

    # update environment to production
    # pattern for finding version setting
    PATTERN = "[^ ](os.environ[\[]EnvKeys.ENVIRONMENT[\][ ]*=[ ]*Environment.(DEVELOPMENT|PRODUCTION))"
    PATTERN_REGULAR_EXPRESSION = PATTERN

    # Replacement text
    if env == 'test':
        REPLACEMENT_TEXT = "\nos.environ[EnvKeys.ENVIRONMENT]" + " = Environment.DEVELOPMENT"
    elif env == 'prod':
        REPLACEMENT_TEXT = "\nos.environ[EnvKeys.ENVIRONMENT]" + " = Environment.PRODUCTION"
    else:
        print(f"Wrong environment provided=> {env}. Valid options are prod | test")
        exit()

    # Update version number in README file
    file_content = re.sub(PATTERN_REGULAR_EXPRESSION, REPLACEMENT_TEXT, file_content, count=1)

    # Write file_content
    Common.write_text_to_file(
        Path(os.environ[EnvKeys.EXEC_DIR]) / Path(NROBO_CONST.NROBO) / Path(NROBO_PATHS.INIT_PY),
        file_content
    )
