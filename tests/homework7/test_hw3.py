from homework7.hw3 import tic_tac_toe_checker


board1 = [['-', '-', 'o'],
          ['-', 'x', 'o'],
          ['x', 'o', 'x']]
board2 = [['-', '-', 'o'],
          ['-', 'o', 'o'],
          ['x', 'x', 'x']]
board3 = [['o', 'x', 'o'],
          ['o', 'x', 'o'],
          ['x', 'o', 'x']]


def test_tic_tac_toe_checker():
    assert tic_tac_toe_checker(board1) == 'unfinished'
    assert tic_tac_toe_checker(board2) == 'x wins!'
    assert tic_tac_toe_checker(board3) == 'draw'
