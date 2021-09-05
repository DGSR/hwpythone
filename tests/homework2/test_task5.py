import string

from homework2.task5 import custom_range


def test_custom_range():
    a = ["H", "e", "l", "o", "d", "a", "r", "k", "n", "s", "m", "y", "f", "i"]
    res0 = ['a', 'b', 'c', 'd', 'e', 'f']
    res1 = ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
    res2 = ['p', 'n', 'l', 'j', 'h']
    res3 = ["e", "l", "o", "d", "a", "r", "k", "n", "s", "m"]
    assert custom_range(string.ascii_lowercase, 'g') == res0
    assert custom_range(string.ascii_lowercase, 'g', 'p') == res1
    assert custom_range(string.ascii_lowercase, 'p', 'g', -2) == res2
    assert custom_range(a, 'e', 'y') == res3
