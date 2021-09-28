import functools


def save_original_info(orig_func):
    """parameterized decorator, which saves info about initial function"""
    def wrapper(func):
        def substitute(*args, **kwargs):
            return func(*args, **kwargs)
        substitute.__original_func = orig_func
        substitute.__name__ = orig_func.__name__
        substitute.__doc__ = orig_func.__doc__
        return substitute
    return wrapper


def print_result(func):
    @save_original_info(func)
    def wrapper(*args, **kwargs):
        """Function-wrapper which print result of an original function"""
        result = func(*args, **kwargs)
        print(result)
        return result

    return wrapper


@print_result
def custom_sum(*args):
    """This function can sum any objects which have __add___"""
    return functools.reduce(lambda x, y: x + y, args)
