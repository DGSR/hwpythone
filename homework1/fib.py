from typing import Sequence


def check_fibonacci(sequence: Sequence[int]) -> bool:
    """
    Function checks if sequence is a Fibonacci sequence
    First, function reaches to first value
    then checks if values are the same as generated
    Special checks for size of sequence and 1, 1
    """
    if len(sequence) == 0:
        return False

    temp = 0
    temp1 = 1
    while temp < sequence[0]:
        temp, temp1 = temp1, temp + temp1

    if temp == 1 and [temp, temp1] != sequence[:2]:
        temp, temp1 = temp1, temp + temp1

    for i in sequence:
        if temp != i:
            return False
        temp, temp1 = temp1, temp + temp1
    return True
