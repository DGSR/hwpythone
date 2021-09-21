import pytest

from homework2.task4 import cache


@cache
def func(a, b):
    return (a ** b) ** 2


@pytest.mark.timeout(1)
def test_cache():
    result = 1000 ** 4000
    for test_case in [(1000, 2000)] * 10000:
        assert func(*test_case) == result
