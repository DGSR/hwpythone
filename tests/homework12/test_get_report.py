import datetime

from homework12.get_report import get_done_homework


def test_get_done_homework():
    assert get_done_homework('sqlite:///tests/homework12/main.db') == [
        (datetime.datetime(2021, 10, 22, 14, 51, 16), 'Ivanov', 'Heisenberg'),
        (datetime.datetime(2021, 10, 22, 14, 51, 16), 'Smith', 'Heisenberg')]
