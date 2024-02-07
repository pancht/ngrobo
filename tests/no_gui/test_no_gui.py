import pytest


class TestNoGUI():
    @pytest.mark.nogui
    @pytest.mark.skip
    def f2(self):
        raise ExceptionGroup(
            "Group message",
            [
                RuntimeError(),
            ],
        )

    @pytest.mark.nogui
    @pytest.mark.skip
    def test_exception_in_group(self):
        with pytest.raises(ExceptionGroup) as excinfo:
            self.f2()
        assert excinfo.group_contains(RuntimeError)
        assert not excinfo.group_contains(TypeError)

    def f(self):
        raise SystemExit(1)

    @pytest.mark.nogui
    @pytest.mark.skip
    def test_mytest(self):
        with pytest.raises(SystemExit):
            self.f()
