def check_power_of_2(number: int) -> bool:
    """
    Bytewise check if given number is power of two
    """
    return not (bool(number & (number - 1)))
