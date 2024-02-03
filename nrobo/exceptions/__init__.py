from nrobo.util.platform import __HOST_PLATFORM__


class MissingCommandImplementation(Exception):
    """
    This exception raise when <command> implementation missing for <host-platform>
    """

    # constructor
    def __init__(self, command):
        self.value = f'Command <{command}> for host platform <{__HOST_PLATFORM__}>'

    def __str__(self):
        return repr(self.value)
