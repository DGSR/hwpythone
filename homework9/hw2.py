from contextlib import contextmanager


class suppresor_class(object):
    """
    class context manager that supresses given error
    """
    def __init__(self, error):
        self.error = error

    def __enter__(self):
        pass

    def __exit__(self, type_error, value, traceback):
        return True if type_error == self.error else None


@contextmanager
def suppresor_generator(error):
    """
    generator context manager that supresses given error
    """
    try:
        yield
    except error:
        return 0
