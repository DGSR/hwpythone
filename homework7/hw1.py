from collections.abc import Iterable
from typing import Any


def is_iterable(arg: Any) -> bool:
    """
    return True if argument is iterable but not string
    """
    return isinstance(arg, Iterable) and not isinstance(arg, str)


def find_occurrences(tree: dict, element: Any) -> int:
    """
    returns number of occurences of element in dict and its nested structures
    """
    count = 0
    if isinstance(tree, dict):
        count += sum([find_occurrences(val, element) for val in tree.values()])
    elif is_iterable(tree):
        count += sum([find_occurrences(val, element) for val in tree])
    else:
        count += 1 if tree == element else 0
    return count
