import platform


class PLATFORMS:
    """
    This class holds possible platform names.
    """
    LINUX = "Linux"
    DARWIN = "Darwin"
    MACOS = DARWIN
    JAVA = "Java"
    WINDOWS = "Windows"


__HOST_PLATFORM__ = platform.system()
