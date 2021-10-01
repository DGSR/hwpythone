from re import sub


def backspace_compare(first: str, second: str) -> bool:
    """
    return if given strings are equal after deleting # sign and a symbol before
    """
    pattern = r'((\w)?#)+'
    return sub(pattern, '', first) == sub(pattern, '', second)
