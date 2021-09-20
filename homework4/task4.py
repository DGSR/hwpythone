from typing import List


def fizzbuzz(number: int) -> List[str]:
    """
    returns list of n fizzbuzz numbers, starting with 1

    >>> fizzbuzz(5)
    ["1", "2", "fizz", "4", "buzz"]
    >>> fizzbuzz(15)[5:]
    ["fizz", "7", "8", "fizz", "buzz", "11", "fizz", "13", "14", "fizzbuzz"]
    """
    res = []
    for num in range(1, number+1):
        temp = ""

        if num % 3 == 0:
            temp += "fizz"
        if num % 5 == 0:
            temp += "buzz"

        res.append(temp or str(num))
    return res
