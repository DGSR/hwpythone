from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    """
    Function returns max and min values in file
    search and comparison is done line by line
    start values are those in first line of the file
    """
    with open(file_name, 'r') as f:
        maxN = int(f.readline().strip())
        minN = maxN
        for line in f:
            if int(line.strip()) > maxN:
                maxN = int(line.strip())
            elif int(line.strip()) < minN:
                minN = int(line.strip())
    return (maxN, minN)
