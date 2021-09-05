from itertools import product
from typing import Any, List


def combinations(*args: List[Any]) -> List[List]:
    """
    returns product of arguments
    """
    return list(product(*args))
