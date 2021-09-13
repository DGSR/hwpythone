import time
import struct
import random
import hashlib
from concurrent.futures import ThreadPoolExecutor


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack('<' + 'B' * len(data), data))


def sum_slow_calculation(num):
    """
    asynchronously returns sum of numbers from 0 to given number
    """
    with ThreadPoolExecutor(max_workers=25) as executor:
        return sum([res for res in executor.map(slow_calculate, range(num))])
