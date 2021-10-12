from homework9.hw1 import merge_sorted_files


def test_merge_sorted_files(tmpdir):
    temp_file1 = tmpdir.mkdir('tmp').join('file1.txt')
    temp_file2 = tmpdir.join('tmp/file2.txt')
    temp_file1.write('\n'.join(['1', '3', '5']))
    temp_file2.write('\n'.join(['2', '4', '6']))
    assert list(merge_sorted_files([temp_file1, temp_file2]))
