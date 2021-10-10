from pathlib import Path
from typing import Iterator, List, Union


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    """
    read integer in files and merge lists into one
    return iterator
    """
    open_files = [open(file, 'r') for file in file_list]
    file_ints = [open_file.read().splitlines() for open_file in open_files]
    [file.close() for file in open_files]
    return (int(num) for elements in zip(*file_ints) for num in elements)
