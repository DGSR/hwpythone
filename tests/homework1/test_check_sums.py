from homework1.check_sums import check_sum_of_four


def test_check_sums():
    a = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]
    b = [0, 1]
    c = [0] * 10
    d = [1, 2, 6, 7, 8, 9, 10, 0]
    e = [100, 0, 50]
    b1 = [1, 1]
    d2 = [0, 0]
    assert check_sum_of_four(a, b, c, d) == 10
    assert check_sum_of_four(a, b1, c, d) == 0
    assert check_sum_of_four(a, b, c, d2) == 20
    assert check_sum_of_four(a, b, c, d, e) == 10
