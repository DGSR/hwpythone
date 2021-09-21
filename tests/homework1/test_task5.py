from homework1.task5 import find_maximal_subarray_sum as find_max


def test_find_max():
    a = [1, 3, -1, -3, 5, 3, 6, 7]
    b = [1, 2]
    c = [10, 2, 3]
    d = [1, 1, 10, 1, 1, 8, 9, 7]
    assert find_max(a, 3) == 16
    assert find_max(b, 3) == 3
    assert find_max(c, 3) == 15
    assert find_max(d, 3) == 24
