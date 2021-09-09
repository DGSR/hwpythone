from homework2.task4 import cache


@cache
def func(a, b):
    return (a ** b) ** 2


def test_cache():
    some = 100, 200
    val_1 = func(*some)
    val_2 = func(*some)
    val_3 = func(*some)

    assert val_1 == val_2
    assert val_1 == val_3
