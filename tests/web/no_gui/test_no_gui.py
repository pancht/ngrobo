import pytest


class TestNoGUI():
    def f2(self):
        """Verify no gui test f2"""
        raise ExceptionGroup(
            "Group message",
            [
                RuntimeError(),
            ],
        )

    @pytest.mark.nogui
    # @pytest.mark.skip
    def test_exception_in_group(self):
        """Verify no gui test execution in group"""
        with pytest.raises(ExceptionGroup) as excinfo:
            self.f2()
        assert excinfo.group_contains(RuntimeError)
        assert not excinfo.group_contains(TypeError)

    def f(self):
        raise SystemExit(1)

    @pytest.mark.nogui
    # @pytest.mark.skip
    def test_raise_exception_system_exit(self):
        """Verify no gui test mytest"""
        with pytest.raises(SystemExit):
            self.f()


