from collections.abc import Iterable
from typing import Any


def find_occurrences(tree: dict, element: Any, count: int = 0) -> int:
    """
    returns number of occurences of element in dict and its nested structures
    """
    is_iterable = isinstance(tree, Iterable) and not isinstance(tree, str)
    if isinstance(tree, dict):
        count += sum([find_occurrences(val, element, count)
                      for val in tree.values()])
    elif is_iterable:
        count += sum([find_occurrences(val, element, count) for val in tree])
    else:
        count += 1 if tree == element else 0
    return count
