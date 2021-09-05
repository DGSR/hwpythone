import string
from typing import List


def open_bom_file(file_path: str) -> List[str]:
    """
    returns decoded contents with bom symbols replaced by unicode character
    """
    with open(file_path, "r", encoding='unicode_escape') as file:
        return file.read()


def has_unique_chars(word: str) -> bool:
    """
    checks if given word has all unique symbols
    """
    return len(set(word.lower())) == len(word.lower())


def get_longest_diverse_words(file_path: str) -> List[str]:
    """
    returns 10 largest words with unique letters only in given file
    """
    file = open_bom_file(file_path)
    unique_words = []
    words = set(file.split())
    while(len(words) > 0):
        longest = max(words)
        words.remove(longest)
        longest = longest.strip(string.punctuation)

        if not has_unique_chars(longest):
            continue
        else:
            unique_words.append(longest)
        if len(unique_words) > 10:
            unique_words.remove(min(unique_words, key=len))
    return unique_words


def get_rarest_char(file_path: str) -> str:
    """
    returns rarest symbol in file
    """
    file = open_bom_file(file_path)
    char_dict = {}
    for line in file:
        for char in line:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return min(char_dict, key=char_dict.get)


def count_punctuation_chars(file_path: str) -> int:
    """
    returns number of punctuatuin chars in given file
    """
    file = open_bom_file(file_path)
    counter = 0
    for line in file:
        for char in line:
            if char in string.punctuation:
                counter += 1
    return counter


def count_non_ascii_chars(file_path: str) -> int:
    """
    returns number of non ascii chars in given file
    """
    file = open_bom_file(file_path)
    counter = 0
    for line in file:
        for char in line:
            if not char.isascii():
                counter += 1
    return counter


def get_most_common_non_ascii_char(file_path: str) -> str:
    """
    returns most common non ascii char in given file, otherwise None
    """
    file = open_bom_file(file_path)
    char_dict = {}
    for line in file:
        for char in line:
            if char.isascii():
                continue
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    if char_dict:
        return max(char_dict, key=char_dict.get)
    else:
        return None
