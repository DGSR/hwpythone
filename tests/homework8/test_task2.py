from homework8.task2 import TableData


def test_TableData():
    presidents = TableData('tests/homework8/example.sqlite', 'presidents')
    assert len(presidents) == 3
    assert presidents['Yeltsin'] == ('Yeltsin', 999, 'Russia')
    assert ('Yeltsin' in presidents) is True
    assert [president['name'] for president in presidents] == [
                                    'Yeltsin', 'Trump', 'Big Man Tyrone']
