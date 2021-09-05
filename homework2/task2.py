from typing import List, Tuple


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    """
    returns most and least commont elements in list
    """
    return max(inp, key=inp.count), min(inp, key=inp.count)
