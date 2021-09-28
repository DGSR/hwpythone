from constant.constants import DEFAULT_ENCODING


def read_magic_number(path: str, lower_bound: int = 1.0,
                      upper_bound: int = 3.0) -> bool:
    """
    reads first line of file, if it is in between lower and upper bounds
     (upper bound excluded)
     returns True otherwise False
    any error is raised as ValueError
    """
    try:
        with open(path, 'r', encoding=DEFAULT_ENCODING) as file:
            temp = file.readline()
        return lower_bound <= float(temp) < upper_bound
    except (ValueError, FileNotFoundError):
        raise ValueError('file not found or first line value is wrong')
