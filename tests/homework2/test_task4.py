from homework2.task4 import cache


def func(a, b):
    return (a ** b) ** 2


def test_cache():
    cache_func = cache(func)
    some = 100, 200
    val_1 = cache_func(*some)
    val_2 = cache_func(*some)
    val_3 = cache_func(2, 3)
    assert val_1 == val_2
    assert val_3 == 64
