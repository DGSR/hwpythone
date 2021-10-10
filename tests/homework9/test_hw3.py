from homework9.hw3 import universal_file_counter


def test_universal_file_counter(tmpdir):
    tmpdir.mkdir('tmp')
    temp_file1 = tmpdir.join('file1.txt')
    temp_file2 = tmpdir.join('file2.txt')
    temp_file1.write('\n'.join(['1', '3', '5']))
    temp_file2.write('\n'.join(['2', '4', '6']))

    assert universal_file_counter(tmpdir, 'txt') == 6
    assert universal_file_counter(tmpdir, 'txt', str.split) == 6
