import string

from homework2.task5 import custom_range


def test_custom_range():
    assert custom_range(string.ascii_lowercase, 'g') == [
                                                        'a', 'b', 'c',
                                                        'd', 'e', 'f'
                                                        ]
    assert custom_range(string.ascii_lowercase, 'g', 'p') == [
                                                'g', 'h', 'i', 'j', 'k',
                                                'l', 'm', 'n', 'o'
                                                ]
    assert custom_range(string.ascii_lowercase, 'p', 'g', -2) == [
                                          'p', 'n', 'l', 'j', 'h']
    assert custom_range([
                        'H', 'e', 'l', 'o', 'd',
                        'a', 'r', 'k', 'n', 's',
                        'm', 'y', 'f', 'i'
                        ], 'e', 'y') == [
                                            'e', 'l', 'o', 'd', 'a',
                                            'r', 'k', 'n', 's', 'm'
                                            ]
