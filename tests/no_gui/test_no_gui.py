import pytest


class TestNoGUI():
    def f2(self):
        raise ExceptionGroup(
            "Group message",
            [
                RuntimeError(),
            ],
        )

    def test_exception_in_group(self):
        with pytest.raises(ExceptionGroup) as excinfo:
            self.f2()
        assert excinfo.group_contains(RuntimeError)
        assert not excinfo.group_contains(TypeError)

    def f(self):
        raise SystemExit(1)

    def test_mytest(self):
        with pytest.raises(SystemExit):
            self.f()
