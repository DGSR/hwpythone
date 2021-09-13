from unittest.mock import patch

from homework3.task1 import cache


@cache(times=2)
def f():
    return input('? ')


def test_cache():
    with patch('builtins.input', return_value="1"):
        assert f() == '1'
    assert f() == '1'
    assert f() == '1'
    with patch('builtins.input', return_value="2"):
        assert f() == '2'
