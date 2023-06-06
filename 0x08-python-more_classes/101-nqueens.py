#!/usr/bin/python3
"""N-queens puzzle"""
import sys


def init_board(n):
    """Initialize an `n`x`n` sized chessboard with 0's."""
    board = []
    [board.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in board]
    return (board)


def board_deepcopy(board):
    """deepcopy of a chess"""
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return (board)


def get_solution(board):
    """solved chessboard."""
    result = []
    for var in range(len(board)):
        for char in range(len(board)):
            if board[var][char] == "Q":
                result.append([var, char])
                break
    return (result)


def xout(board, row, col):
    """X out spots on a chess"""

    for char in range(col + 1, len(board)):
        board[row][char] = "x"

    for char in range(col - 1, -1, -1):
        board[row][char] = "x"

    for var in range(row + 1, len(board)):
        board[var][col] = "x"

    for var in range(row - 1, -1, -1):
        board[var][col] = "x"

    char = col + 1
    for var in range(row + 1, len(board)):
        if char >= len(board):
            break
        board[var][char] = "x"
        char += 1

    char = col - 1
    for var in range(row - 1, -1, -1):
        if char < 0:
            break
        board[var][char]
        char -= 1

    char = col + 1
    for var in range(row - 1, -1, -1):
        if char >= len(board):
            break
        board[var][char] = "x"
        char += 1

    char = col - 1
    for var in range(row + 1, len(board)):
        if char < 0:
            break
        board[var][char] = "x"
        char -= 1


def recursive_solve(board, row, queens, results):
    """Recursive N-queens puzzle"""
    if queens == len(board):
        results.append(get_solution(board))
        return (results)

    for char in range(len(board)):
        if board[row][char] == " ":
            tmp_board = board_deepcopy(board)
            tmp_board[row][char] = "Q"
            xout(tmp_board, row, char)
            results = recursive_solve(tmp_board, row + 1, queens + 1, results)

    return results


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    results = recursive_solve(board, 0, 0, [])
    for res in results:
        print(res)
