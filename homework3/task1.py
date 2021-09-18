from typing import Callable


def cache(times: int) -> Callable:
    """
    parametrised decorator which returns function,
     that caches given calls
    """

    def wrapped(func: Callable):
        memory = {'calls': times, 'data': None}

        def inner(*args):
            if memory['data'] is None or memory['calls'] == 0:
                memory['data'] = func(*args)
            else:
                memory['calls'] -= 1
            return memory['data']
        return inner
    return wrapped
