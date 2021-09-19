from homework4.task3 import my_precious_logger


def test_my_precious_logger(capsys):
    my_precious_logger("OK")
    captured = capsys.readouterr()
    assert captured.out == "OK\n"

    my_precious_logger("error: file not found")
    captured = capsys.readouterr()
    assert captured.err == "error: file not found\n"
