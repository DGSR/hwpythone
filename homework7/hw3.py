from typing import List

from constant.tic_tac_toe_victory_conditions import VICTORY_CONDITIONS


def tic_tac_toe_checker(board: List[List]) -> str:
    """
    return result of checking tic-tac-toe board
    """
    for row in VICTORY_CONDITIONS:
        board_elems = [board[elem[0]][elem[1]] for elem in row]
        if board_elems.count(board_elems[0]) == 3:
            return f'{board_elems[0]} wins!'
    return 'unfinished' if any('-' in row for row in board) else 'draw'
