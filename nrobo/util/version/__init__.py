
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
        return f"{self._major_next}.{self._minor}.{self._patch}"

    def major_decremented(self) -> str:
        return f"{self._major_prev}.{self._minor}.{self._patch}"

    def minor_incremented(self) -> str:
        return f"{self._major}.{self._minor_next}.{self._patch}"

    def minor_decremented(self) -> str:
        return f"{self._major}.{self._minor_prev}.{self._patch}"

    def patch_incremented(self) -> str:
        return f"{self._major}.{self._minor}.{self._patch_next}"

    def patch_decremented(self) -> str:
        return f"{self._major}.{self._minor}.{self._patch_prev}"

    def version_incremented(self) -> str:
        return f"{self._major}.{self._minor}.{self._patch_next}"

    def version_decremented(self) -> str:
        return f"{self._major}.{self._minor}.{self._patch_prev}"

    def _version_parts(self):
        patten = r"(([\d]*)[.]([\d]*)[.]([\d]*))"
        import re
        m = re.match(patten, self._version)
        _version = m.group(1)
        _major = m.group(2)
        _minor = m.group(3)
        _patch = m.group(4)

        return [_major, _minor, _patch]
