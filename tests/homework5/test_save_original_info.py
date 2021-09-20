from homework5.save_original_info import custom_sum


def test_save_original_info(capsys):
    custom_sum(1, 2, 3, 4)
    without_print = custom_sum.__original_func
    captured = capsys.readouterr()
    assert captured.out == str(without_print(1, 2, 3, 4))+'\n'
    assert custom_sum.__doc__ == 'This function can sum '\
                                 'any objects which have __add___'
    assert custom_sum.__name__ == 'custom_sum'
