from homework2.task5 import custom_range


def test_custom_range():
    assert custom_range('g') == [
                                'a', 'b', 'c',
                                'd', 'e', 'f'
                                ]
    assert custom_range('g', 'p') == [
                                     'g', 'h', 'i', 'j', 'k',
                                     'l', 'm', 'n', 'o'
                                     ]
    assert custom_range('p', 'g', -2) == [
                                          'p', 'n', 'l', 'j', 'h']
    assert custom_range('e', 'y', string=[
                        'H', 'e', 'l', 'o', 'd',
                        'a', 'r', 'k', 'n', 's',
                        'm', 'y', 'f', 'i'
                        ]) == [
                                            'e', 'l', 'o', 'd', 'a',
                                            'r', 'k', 'n', 's', 'm'
                                            ]
