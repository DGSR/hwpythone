from typing import Callable


def cache(func: Callable) -> Callable:
    """
    returns call of function first time
    after first time returns cached call
    """
    memory = {}

    def wrapped(*args):
        if args not in memory:
            memory[args] = func(*args)
        return memory[args]
    return wrapped
