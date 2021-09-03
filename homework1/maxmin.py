from typing import List, Tuple


def max_min(nums: List[str]) -> Tuple[int, int]:
    """
    Function converts list of strings to int
    and returns max and min values
    """
    nums = [int(x) for x in nums]
    return (max(nums), min(nums))


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    """
    Function returns max and min values in file
    """
    with open(file_name, 'r') as file:
        contents = file.read().split()
        return max_min(contents)
