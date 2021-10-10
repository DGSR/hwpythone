from homework9.hw2 import suppresor_class, suppresor_generator


def test_suppresor():
    with suppresor_class(IndexError):
        [][2]
    with suppresor_generator(ZeroDivisionError):
        1/0
