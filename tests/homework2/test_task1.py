from homework2.task1 import (count_non_ascii_chars, count_punctuation_chars,
                             get_longest_diverse_words,
                             get_most_common_non_ascii_char, get_rarest_char,
                             has_unique_chars)


def test_has_unique_chars():
    assert has_unique_chars("hello") is False
    assert has_unique_chars("Dead") is False
    assert has_unique_chars("abduction") is True


def test_get_longest_diverse_words():
    res0 = ['»unsichtbare', 'verständlich', 'kalyptischen', 'Schlagworte',
            'Schilderung', 'Märchenwald', 'Moralischen',
            'Landstriche', 'Furchtlosen', 'Beschwörung']
    res1 = ['sich', 'nicht', 'machen', 'hinter',
            'hier«', 'gefaßt', 'chen',
            'ausführen', 'auch', 'Pfade']
    res2 = ['string', 'sniper', 'phone', 'keyboard',
            'fortune', 'false', 'absurdity',
            'absent', 'abjection', 'abduction']
    assert get_longest_diverse_words("tests/homework2/data.txt") == res0
    assert get_longest_diverse_words("tests/homework2/data1.txt") == res1
    assert get_longest_diverse_words("tests/homework2/data2.txt") == res2


def test_get_rarest_char():
    assert get_rarest_char("tests/homework2/data.txt") == "›"
    assert get_rarest_char("tests/homework2/data1.txt") == "S"
    assert get_rarest_char("tests/homework2/data2.txt") == "v"


def test_count_punctuation_chars():
    assert count_punctuation_chars("tests/homework2/data.txt") == 5305
    assert count_punctuation_chars("tests/homework2/data1.txt") == 7
    assert count_punctuation_chars("tests/homework2/data2.txt") == 0


def test_count_non_ascii_chars():
    assert count_non_ascii_chars("tests/homework2/data.txt") == 2972
    assert count_non_ascii_chars("tests/homework2/data1.txt") == 9
    assert count_non_ascii_chars("tests/homework2/data2.txt") == 0


def test_get_most_common_non_ascii_char():
    assert get_most_common_non_ascii_char("tests/homework2/data.txt") == "ä"
    assert get_most_common_non_ascii_char("tests/homework2/data1.txt") == "ü"
    assert get_most_common_non_ascii_char("tests/homework2/data2.txt") is None
