from typing import Any, List


def custom_range(iterable: Any, start: Any = None,
                 stop: Any = None, step: int = 1) -> List[Any]:
    """
    returns iterable object with set start and end (By default not)
    and iterated with given step (By default = 1)
    """
    res = list(iterable)
    if start is None and stop is None:
        return res[::step]
    elif start is not None and stop is None:
        return res[:res.index(start):step]
    else:
        return res[res.index(start):res.index(stop):step]
