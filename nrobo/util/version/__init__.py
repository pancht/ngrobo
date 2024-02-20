"""
=====================CAUTION=======================
DO NOT DELETE THIS FILE SINCE IT IS PART OF NROBO
FRAMEWORK AND IT MAY CHANGE IN THE FUTURE UPGRADES
OF NROBO FRAMEWORK. THUS, TO BE ABLE TO SAFELY UPGRADE
TO LATEST NROBO VERSION, PLEASE DO NOT DELETE THIS
FILE OR ALTER ITS LOCATION OR ALTER ITS CONTENT!!!
===================================================

Version class handles version operations smoothly.


@author: Panchdev Singh Chauhan
@email: erpanchdev@gmail.com
"""
from nrobo.exceptions import NRoBoIncorrectVersion, NRoBoInvalidOperation


class Version:
    def __init__(self, version):
        self._version = version
        self._major = int(self._version_parts()[0])
        self._minor = int(self._version_parts()[1])
        self._patch = int(self._version_parts()[2])
        self._major_next = self._major + 1
        self._major_prev = self._major - 1
        self._minor_next = self._minor + 1
        self._minor_prev = self._minor - 1
        self._patch_next = self._patch + 1
        self._patch_prev = self._patch - 1
        self._version_next = f"{self._major}.{self._minor}.{self._patch_next}"
        self._version_prev = f"{self._major}.{self._minor}.{self._patch_prev}"

    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, version):
        self._version = version

    @property
    def version_next(self):
        return self._version_next

    @version_next.setter
    def version_next(self, version_next):
        self._version_next = version_next

    @property
    def version_prev(self):
        return self._version_prev

    @version_prev.setter
    def version_prev(self, version_prev):
        self._version_prev = version_prev

    @property
    def major(self):
        return self._major

    @major.setter
    def major(self, major):
        self._major = major

    @property
    def major_next(self):
        return self._major_next

    @major_next.setter
    def major_next(self, major_next):
        self._major_next = major_next

    @property
    def major_prev(self):
        return self._major_prev

    @major_prev.setter
    def major_prev(self, major_prev):
        self._major_prev = major_prev

    @property
    def minor(self):
        return self._minor

    @minor.setter
    def minor(self, minor):
        self._minor = minor

    @property
    def minor_next(self):
        return self._minor_next

    @minor_next.setter
    def minor_next(self, minor_next):
        self._minor_next = minor_next

    @property
    def minor_prev(self):
        return self._minor_prev

    @minor_prev.setter
    def minor_prev(self, minor_prev):
        self._minor_prev = minor_prev

    @property
    def patch(self):
        return self._patch

    @patch.setter
    def patch(self, patch):
        self._patch = patch

    @property
    def patch_next(self):
        return self._patch_next

    @patch_next.setter
    def patch_next(self, patch_next):
        self._patch_next = patch_next

    @property
    def patch_prev(self):
        return self._patch_prev

    @patch_prev.setter
    def patch_prev(self, patch_prev):
        self._patch_prev = patch_prev

    def major_incremented(self) -> str:
        return f"{self._major_next}.0.0"

    def major_decremented(self) -> str:
        return f"{self._major_prev}.0.0"

    def minor_incremented(self) -> str:
        return f"{self._major}.{self._minor_next}.0"

    def minor_decremented(self) -> str:
        return f"{self._major}.{self._minor_prev}.0"

    def patch_incremented(self) -> str:
        return f"{self._major}.{self._minor}.{self._patch_next}"

    def patch_decremented(self) -> str:
        return f"{self._major}.{self._minor}.{self._patch_prev}"

    def version_incremented(self) -> str:
        return f"{self._major}.{self._minor}.{self._patch_next}"

    def version_decremented(self) -> str:
        return f"{self._major}.{self._minor}.{self._patch_prev}"

    @staticmethod
    def first_major_release(release_version):
        _release_version = Version(release_version)
        return f"{_release_version._major}.0.0"

    @staticmethod
    def first_minor_release(release_version):
        _release_version = Version(release_version)
        return f"{_release_version._major}.{_release_version._minor}.{0}"

    @staticmethod
    def present_is_a_major_release(present_release: str, previous_release: str) -> bool:
        """Returns True if present release is a major release.

        :param present_release:
        :param previous_release:
        :return: """
        _present_release = Version(present_release)
        _previous_release = Version(previous_release)

        if _present_release.major > _previous_release.major:
            return True

        return False

    @staticmethod
    def present_is_a_minor_release(present_release: str, previous_release: str) -> bool:
        """Returns True if present release is a minor release.

        :param present_release:
        :param previous_release:
        :return: """
        _present_release = Version(present_release)
        _previous_release = Version(previous_release)

        if _present_release.minor > _previous_release.minor:
            return True

        return False

    @staticmethod
    def present_is_a_patch_release(present_release: str, previous_release: str) -> bool:
        """Returns True if present release is a patch release.

        :param present_release:
        :param previous_release:
        :return: """
        _present_release = Version(present_release)
        _previous_release = Version(previous_release)

        if _present_release.patch > _previous_release.patch:
            return True

        return False

    def _version_parts(self):
        patten = r"(([\d]*)[.]([\d]*)[.]([\d]*))"
        import re
        m = re.match(patten, self._version)

        if not m:
            # incorrect version
            raise NRoBoIncorrectVersion(self._version)

        _version = m.group(1)
        _major = m.group(2)
        _minor = m.group(3)
        _patch = m.group(4)

        return [_major, _minor, _patch]

    def __lt__(self, other):
        if not isinstance(other, Version):
            raise NRoBoInvalidOperation("<", type(other))

        if self.major < other.major:
            return True

        if self.minor < other.minor:
            return True

        if self.patch < other.patch:
            return True

        return False

    def __eq__(self, other):
        if not isinstance(other, Version):
            raise NRoBoInvalidOperation("=", type(other))

        if self.major == other.major \
                and self.minor == other.minor \
                and self.patch == other.patch:
            return True

        return False

    def __gt__(self, other):
        if not isinstance(other, Version):
            raise NRoBoInvalidOperation(">", type(other))

        if self.major > other.major:
            return True

        if self.minor > other.minor:
            return True

        if self.patch > other.patch:
            return True

        return False

    def __add__(self, other):
        if not isinstance(other, int) \
                and not isinstance(other, float):
            raise NRoBoInvalidOperation("+", type(other))

        if isinstance(other, float):
            other = int(float)

        return Version(f"{self.major}.{self.minor}.{self.patch + other}")

    def __sub__(self, other):
        if not isinstance(other, int) \
                and not isinstance(other, float):
            raise NRoBoInvalidOperation("-", type(other))

        if isinstance(other, float):
            other = int(float)

        return Version(f"{self.major}.{self.minor}.{self.patch - other}")

    def __le__(self, other):
        if not isinstance(other, Version):
            raise NRoBoInvalidOperation("<=", type(other))

        if self.__lt__(other):
            return True

        if self.__eq__(other):
            return True

        return False

    def __ge__(self, other):
        if not isinstance(other, Version):
            raise NRoBoInvalidOperation(">=", type(other))

        if self.__gt__(other):
            return True

        if self.__eq__(other):
            return True

        return False
