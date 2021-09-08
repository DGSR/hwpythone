from typing import Any, List


def custom_range(iterable: Any, start: Any = None,
                 stop: Any = None, step: int = 1) -> List[Any]:
    """
    returns iterable object with set start and end (By default not)
    and iterated with given step (By default = 1)
    """
    res = list(iterable)
    if start not in res:
        start, stop = res[0], res[len]
    if stop not in res:
        start, stop = res[0], start
    return res[res.index(start):res.index(stop):step]
