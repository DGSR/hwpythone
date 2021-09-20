from typing import Generator


def get_value_for_fizzbuzz(val: int) -> str:
    """
    returns value for fizzbuzz generator using mod 15 and dictionary
    """
    dict = {1: val, 2: val, 3: "fizz", 4: val, 5: "buzz",
            6: "fizz", 7: val, 8: val, 9: "fizz", 10: "buzz",
            11: val, 12: "fizz", 13: val, 14: val, 0: "fizzbuzz"}
    return str(dict[val % 15])


def fizzbuzz(number: int) -> Generator[str, str, str]:
    """
    returns generator of n fizzbuzz numbers, starting with 1 without if
    """
    for num in range(1, number+1):
        yield get_value_for_fizzbuzz(num)
