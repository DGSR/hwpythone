from functools import partial
from typing import Callable


def get_calls_counter(self: Callable) -> int:
    """
    return variable calls in target function
    """
    return self.calls


def reset_calls_counter(self: Callable) -> int:
    """
    return variable calls in target function and set it to 0
    """
    res = self.calls
    self.calls = 0
    return res


def instances_counter(cls):
    """
    class decorator to count number of created instances
    adds 2 methods get_created_instances and reset_instances_counter
    to get number and to reset the counter
    """
    def __init__(self, *args, **kwargs):
        __init__.calls += 1
        super(cls, self).__init__(*args, **kwargs)
    __init__.calls = 0
    cls.__init__ = __init__
    cls.get_created_instances = partial(get_calls_counter, __init__)
    cls.reset_instances_counter = partial(reset_calls_counter, __init__)
    return cls
