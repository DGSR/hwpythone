from fnmatch import fnmatch
from os import listdir
from pathlib import Path
from typing import Callable, Optional


def universal_file_counter(dir_path: Path, file_extension: str,
                           tokenizer: Optional[Callable] = None) -> int:
    """
    return number of lines or tokens
     in given path for files with given extension
    """
    file_pattern = "*." + file_extension
    file_list = [file for file in listdir(dir_path)
                 if fnmatch(file, file_pattern)]
    open_files = [open(dir_path/file, 'r') for file in file_list]
    counter = 0
    for file in open_files:
        for line in file:
            counter += len(tokenizer(line)) if tokenizer else 1
    [file.close() for file in open_files]
    return counter
