from unittest.mock import patch

import pytest

from homework3.task1 import cache


@cache(times=2)
def f():
    return input('? ')


@cache(times=99999)
def f1(a, b):
    return (a ** b) ** 2


@pytest.mark.timeout(1)
def test_cache_heavy():
    result = 1000 ** 4000
    for test_case in [(1000, 2000)] * 10**5:
        assert f1(*test_case) == result


@pytest.mark.timeout(1)
def test_cache_light():
    res = 2 ** 6
    res0 = 3 ** 8
    for test_case in [(2, 3)] * 10**5:
        assert f1(*test_case) == res
    for test_case in [(3, 4)] * 10**5:
        assert f1(*test_case) == res0


def test_cache_input():
    with patch('builtins.input', return_value='1'):
        assert f() == '1'
    assert f() == '1'
    assert f() == '1'
    with patch('builtins.input', return_value='2'):
        assert f() == '2'
