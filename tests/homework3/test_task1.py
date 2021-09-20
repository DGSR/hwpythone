import pytest
from unittest.mock import patch

from homework3.task1 import cache


@cache(times=2)
def f():
    return input('? ')


@cache(times=9999)
def f1(a, b):
    return (a ** b) ** 2


@pytest.mark.timeout(1)
def test_cache_heavy():
    result = 1000 ** 4000
    for test_case in [(1000, 2000)] * 10000:
        assert f1(*test_case) == result


def test_cache_light():
    result = 2 ** 6
    for test_case in [(2, 3)] * 10000:
        assert f1(*test_case) == result


def test_cache_input():
    with patch('builtins.input', return_value="1"):
        assert f() == '1'
    assert f() == '1'
    assert f() == '1'
    with patch('builtins.input', return_value="2"):
        assert f() == '2'
