def sign_replacement(string: str, sign: str = '#') -> str:
    """
    return string where each given sign and a symbol before is deleted
    """
    res = ''
    for i in string:
        if i == sign:
            res = res[:-1]
        else:
            res += i
    return res


def backspace_compare(first: str, second: str) -> bool:
    """
    return if given strings are equal after deleting # sign and a symbol before
    """
    return sign_replacement(first) == sign_replacement(second)
