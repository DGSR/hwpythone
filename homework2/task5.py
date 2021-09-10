from string import ascii_lowercase
from typing import List


def custom_range(iterable: str = ascii_lowercase, start: str = None,
                 stop: str = None, step: int = 1) -> List[str]:
    """
    returns iterable object with set start and end (By default not)
    and iterated with given step (By default = 1)
    """
    res = list(iterable)
    if start not in res:
        return res[::step]
    if stop not in res:
        start, stop = res[0], start
    return res[res.index(start):res.index(stop):step]
