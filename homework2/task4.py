from typing import Callable


def cache(func: Callable) -> Callable:
    """
    returns function, which caches all calls
    """
    memory = {}

    def wrapped(*args):
        if args not in memory:
            memory[args] = func(*args)
        return memory[args]
    return wrapped
