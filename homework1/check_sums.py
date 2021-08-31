from typing import List


def check_zeros(x):
    """
    all ellements which are 0 are returned in list expression
    function returns length of that list expression
    """
    return len([i for i in x if i == 0])


def check_sum_of_four(a: List[int], b: List[int],
                      c: List[int], d: List[int]) -> int:
    return check_zeros(a) * check_zeros(b) * check_zeros(c) * check_zeros(d)
