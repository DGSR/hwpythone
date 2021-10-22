from __future__ import annotations

from contextlib import contextmanager
from types import TracebackType


class suppresor_class(object):
    """
    class context manager that supresses given error
    """
    def __init__(self, error: Exception):
        self.error = error

    def __enter__(self):
        pass

    def __exit__(self, type_error: type[BaseException],
                 value: BaseException, traceback: TracebackType):
        return True if type_error == self.error else None


@contextmanager
def suppresor_generator(error: BaseException):
    """
    generator context manager that supresses given error
    """
    try:
        yield
    except error:
        return 0
