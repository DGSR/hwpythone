from string import ascii_lowercase
from typing import List


def custom_range(start: str = None, stop: str = None, step: int = 1,
                 string: str = ascii_lowercase) -> List[str]:
    """
    returns iterable object with set start and end (By default not)
    and iterated with given step (By default = 1)
    if iterable is not given then ascii lowercase is used
    """
    res = list(string)
    if start not in res:
        return res[::step]
    if stop not in res:
        start, stop = res[0], start
    return res[res.index(start):res.index(stop):step]
