import os
import platform

from nrobo import EnvKeys


class PLATFORMS:
    """
    This class holds possible platform names.
    """
    LINUX = "Linux"
    DARWIN = "Darwin"
    MACOS = DARWIN
    JAVA = "Java"
    WINDOWS = "Windows"


os.environ[EnvKeys.HOST_PLATFORM] = platform.system()
