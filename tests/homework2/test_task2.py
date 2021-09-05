from homework2.task2 import major_and_minor_elem


def test_major_and_minor_elem():
    a = [1, 1, 2, 3, 1, 3,  1, 1]
    b = [3, 2, 3]
    c = [2, 2, 1, 1, 1, 2, 2]
    d = [5]
    e = ["aaa", "bbb", "aaa"]
    assert major_and_minor_elem(a) == (1, 2)
    assert major_and_minor_elem(b) == (3, 2)
    assert major_and_minor_elem(c) == (2, 1)
    assert major_and_minor_elem(d) == (5, 5)
    assert major_and_minor_elem(e) == ("aaa", "bbb")
