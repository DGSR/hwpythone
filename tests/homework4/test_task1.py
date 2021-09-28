import pytest

from homework4.task1 import read_magic_number


def test_read_magic_number_positive(tmpdir):
    temp_file = tmpdir.mkdir('tmp').join('tmp1.txt')
    temp_file.write('2.5')
    temp_file1 = tmpdir.join('tmp/tmp2.txt')
    temp_file1.write('3')
    assert read_magic_number(temp_file) is True
    assert read_magic_number(temp_file1) is False


def test_read_magic_number_negative(tmpdir):
    temp_file = tmpdir.mkdir('tmp').join('tmp1.txt')
    temp_file.write('hey')
    with pytest.raises(ValueError):
        read_magic_number(temp_file)
    with pytest.raises(ValueError):
        read_magic_number('nonexisting_file.txt')
