def read_magic_number(path: str) -> bool:
    """
    reads first line of file, if it is in [1, 3) returns True
    otherwise False
    any error is raised as ValueError
    """
    try:
        with open(path, "r", encoding="utf-8") as file:
            temp = file.readline()
        return 1.0 <= float(temp) < 3.0
    except (ValueError, FileNotFoundError):
        raise ValueError("file not found or first line value is wrong")
