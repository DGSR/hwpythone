from homework1.fib import check_fibonacci


def test_check_fibonacci():
    a = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233,
         377, 610, 987, 1597, 2584, 4181, 6765]
    b = [1, 2, 3]
    c = [1, 1, 2]
    d = [1, 1, 3]
    e = [0, 1, 2]
    f = [0, 1]
    g = [1, 1]
    h = [1, 3]
    i = [1]
    j = [0]
    k = [4]
    m = []
    assert check_fibonacci(a) is True
    assert check_fibonacci(b) is True
    assert check_fibonacci(c) is True
    assert check_fibonacci(d) is False
    assert check_fibonacci(e) is False
    assert check_fibonacci(f) is True
    assert check_fibonacci(g) is True
    assert check_fibonacci(h) is False
    assert check_fibonacci(i) is True
    assert check_fibonacci(j) is True
    assert check_fibonacci(k) is False
    assert check_fibonacci(m) is False
