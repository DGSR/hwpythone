from homework4.task5 import fizzbuzz, get_value_for_fizzbuzz


def test_get_value_for_fizzbuzz():
    assert get_value_for_fizzbuzz(25) == "buzz"
    assert get_value_for_fizzbuzz(24) == "fizz"
    assert get_value_for_fizzbuzz(30) == "fizzbuzz"
    assert get_value_for_fizzbuzz(29) == "29"


def test_fizzbuzz():
    assert list(fizzbuzz(5)) == ['1', '2', 'fizz', '4', 'buzz']
    assert list(fizzbuzz(15))[10:] == ['11', 'fizz', '13', '14', 'fizzbuzz']
