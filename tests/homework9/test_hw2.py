import pytest

from homework9.hw2 import suppresor_class, suppresor_generator


def test_suppresor():
    with suppresor_class(IndexError):
        [][2]
    with suppresor_generator(ZeroDivisionError):
        1/0

    with pytest.raises(ZeroDivisionError):
        with suppresor_class(IndexError):
            1/0

    with pytest.raises(IndexError):
        with suppresor_generator(ZeroDivisionError):
            [][2]
