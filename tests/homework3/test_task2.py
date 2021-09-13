import pytest

from homework3.task2 import sum_slow_calculation


@pytest.mark.timeout(60)
def test_sum_slow_calculation():
    assert sum_slow_calculation(500) == 1024259
