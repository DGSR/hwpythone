from homework11.hw1 import SimplifiedEnum


class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")


class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS")


def test_SimplifiedEnum():
    assert ColorsEnum.RED == "RED"
    assert SizesEnum.XL == "XL"
