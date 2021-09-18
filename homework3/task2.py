import hashlib
import random
import struct
import time
from concurrent.futures import ThreadPoolExecutor
from constant.constants import MAX_WORKERS


def slow_calculate(value: int) -> int:
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack('<' + 'B' * len(data), data))


def sum_slow_calculation(num: int) -> int:
    """
    asynchronously returns sum of numbers from 0 to given number
    """
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        return sum(executor.map(slow_calculate, range(num)))
