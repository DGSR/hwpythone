from typing import List


def tic_tac_toe_checker(board: List[List]) -> str:
    """
    return result of checking tic-tac-toe board
    """
    victory_conditions = [[(0, 0), (0, 1), (0, 2)],
                          [(1, 0), (1, 1), (1, 2)],
                          [(2, 0), (2, 1), (2, 2)],
                          [(0, 0), (1, 0), (2, 0)],
                          [(0, 1), (1, 1), (2, 1)],
                          [(0, 2), (1, 2), (2, 2)],
                          [(0, 0), (1, 1), (2, 2)],
                          [(0, 2), (1, 1), (2, 0)]]
    for row in victory_conditions:
        board_elems = [board[elem[0]][elem[1]] for elem in row]
        if board_elems.count(board_elems[0]) == 3:
            return f'{board_elems[0]} wins!'
    return 'unfinished' if any('-' in row for row in board) else 'draw'
