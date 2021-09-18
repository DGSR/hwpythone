def is_armstrong(num: int) -> bool:
    """
    returns if given number is armstrong number
    """
    return sum([int(digit)**len(str(num)) for digit in str(num)]) == num
