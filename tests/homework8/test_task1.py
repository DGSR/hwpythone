import pytest

from homework8.task1 import KeyValueStorage


def test_KeyValueStorage():
    p = KeyValueStorage('tests/homework8/task1.txt')
    assert p['last_name'] == 'top'
    assert p.name == 'kek'
    assert isinstance(p.power, int) is True
    with pytest.raises(ValueError):
        KeyValueStorage('tests/homework8/task1_err.txt')
