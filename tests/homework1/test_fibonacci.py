from homework1.fib import check_fibonacci


def test_check_fibonacci():
    assert check_fibonacci([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233,
                            377, 610, 987, 1597, 2584, 4181, 6765])
    assert check_fibonacci([1, 2, 3])
    assert check_fibonacci([1, 1, 2])
    assert not check_fibonacci([1, 1, 3])
    assert not check_fibonacci([0, 1, 2])
    assert check_fibonacci([0, 1])
    assert check_fibonacci([1, 1])
    assert not check_fibonacci([1, 3])
    assert check_fibonacci([1])
    assert check_fibonacci([0])
    assert not check_fibonacci([4])
    assert not check_fibonacci([])
