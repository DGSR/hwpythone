from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    temp = 0
    if len(nums) <= k:
        return sum(nums)
    for i in range(0, len(nums)-k+1):
        if sum(nums[i:i+k]) > temp:
            temp = sum(nums[i:i+k])
    return temp
