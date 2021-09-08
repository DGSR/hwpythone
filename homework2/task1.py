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
    words = set(file.split())
    words = [i.strip(string.punctuation) for i in words if has_unique_chars(i)]
    words.sort()
    return sorted(words, reverse=True, key=len)[:10]


def get_rarest_char(file_path: str) -> str:
    """
    returns rarest symbol in file
    """
    file = open_bom_file(file_path)
    char_dict = {}
    chars_in_file = [c for x in file for c in x]
    for char in chars_in_file:
        char_dict[char] = char_dict.get(char, 0) + 1
    return min(char_dict, key=char_dict.get)


def count_punctuation_chars(file_path: str) -> int:
    """
    returns number of punctuatuin chars in given file
    """
    file = open_bom_file(file_path)
    return len([chr for x in file for chr in x if chr in string.punctuation])


def count_non_ascii_chars(file_path: str) -> int:
    """
    returns number of non ascii chars in given file
    """
    file = open_bom_file(file_path)
    return len([chr for x in file for chr in x if not chr.isascii()])


def get_most_common_non_ascii_char(file_path: str) -> str:
    """
    returns most common non ascii char in given file, otherwise None
    """
    file = open_bom_file(file_path)
    char_dict = {}
    chars_in_file = [chr for x in file for chr in x if not chr.isascii()]
    for chr in chars_in_file:
        char_dict[chr] = char_dict.get(chr, 0) + 1
    return max(char_dict, key=char_dict.get) if char_dict else None