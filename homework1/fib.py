from typing import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    if len(data) == 0:
        return False
    temp = 0
    temp1 = 1
    while temp < data[0]:
        temp, temp1 = temp1, temp + temp1
    if len(data) > 1:
        if data[0] == 1 and data[1] != 1:
            temp, temp1 = temp1, temp + temp1
    for i in data:
        if temp != i:
            return False
        temp, temp1 = temp1, temp + temp1
    return True
