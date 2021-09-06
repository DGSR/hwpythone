from typing import List


def check_zeros(nums: List[int]) -> int:
    """
    all ellements which are 0 are returned in list expression
    function returns length of that list expression
    """
    return len([i for i in nums if i == 0])


def check_sum_of_four(*nums: List[int]) -> int:
    """
    function receives any number of lists
    and returns number of combinations i + j + k + l + ...
    where sum of any element in list is zero
    A[i] + B[j] + C[k] + D[l] + ... = 0
    """
    res = 1
    for i in nums:
        res *= check_zeros(i)
    return res
