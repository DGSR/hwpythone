from homework2.task3 import combinations


def test_combinations():
    assert combinations([1, 2], [3, 4]) == [(1, 3), (1, 4), (2, 3), (2, 4)]
    assert combinations([2, 4], [3, 5], [6, 9]) == [(2, 3, 6), (2, 3, 9),
                                                    (2, 5, 6), (2, 5, 9),
                                                    (4, 3, 6), (4, 3, 9),
                                                    (4, 5, 6), (4, 5, 9)]
