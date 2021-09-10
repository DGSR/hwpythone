def is_armstrong(number: int) -> bool:
    """
    returns if given number is armstrong number
    """
    num = str(number)
    return sum([int(digit)**len(num) for digit in num]) == number
