from nrobo.util.version import Version


class TestVersionPkg():

    def test_version_class_properties(self):
        """Validate Version class property @major"""

        major = 2024
        minor = 6
        patch = 1

        version = Version(f"{major}.{minor}.{patch}")

        assert version.major == major
        assert version.minor == minor
        assert version.patch == patch
        assert version.major_next == major + 1
        assert version.major_prev == major - 1
        assert version.patch_next == patch + 1
        assert version.patch_prev == patch - 1
        assert version.version == f"{major}.{minor}.{patch}"
        assert version.version_next == f"{major}.{minor}.{patch+1}"
        assert version.version_prev == f"{major}.{minor}.{patch-1}"
        assert version.major_incremented() == f"{major+1}.{minor}.{patch}"
        assert version.major_decremented() == f"{major-1}.{minor}.{patch}"
        assert version.minor_incremented() == f"{major}.{minor+1}.{patch}"
        assert version.minor_decremented() == f"{major}.{minor-1}.{patch}"
        assert version.patch_incremented() == f"{major}.{minor}.{patch+1}"
        assert version.patch_decremented() == f"{major}.{minor}.{patch-1}"
        assert version.version_incremented() == f"{major}.{minor}.{patch+1}"
        assert version.version_decremented() == f"{major}.{minor}.{patch-1}"
