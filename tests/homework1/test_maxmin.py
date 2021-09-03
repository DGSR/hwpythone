from homework1.maxmin import find_maximum_and_minimum as find_max_min
from homework1.maxmin import max_min


def test_find_max_min():
    assert find_max_min(".\\tests\\homework1\\2.txt") == (15, 1)
    assert find_max_min(".\\tests\\homework1\\3.txt") == (10000, 1096)


def test_max_min():
    a = ["1", "2", "6", "7", "8", "9", "10", "0"]
    b = ["101", "110", "111"]
    assert max_min(a) == (10, 0)
    assert max_min(b) == (111, 101)
