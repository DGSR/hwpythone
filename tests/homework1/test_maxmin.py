import os.path as oss
from homework1.maxmin import find_maximum_and_minimum as find_max_min


def test_find_max_min():
    our_dir = oss.dirname(__file__)
    assert find_max_min(oss.join(our_dir, "2.txt")) == (15, 1)
    assert find_max_min(oss.join(our_dir, "3.txt")) == (10000, 1096)
