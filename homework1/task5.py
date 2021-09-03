from typing import List


def find_maximal_subarray_sum(nums: List[int], window: int) -> int:
    """
    given list and window
    function returns max sum of elements in subarray less or equal than window
    """
    res = 0
    while(nums):
        if sum(nums[-window:]) > res:
            res = sum(nums[-window:])
        nums.pop()
    return res
