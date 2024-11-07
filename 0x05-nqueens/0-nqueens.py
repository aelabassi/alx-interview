#!/usr/bin/python3
""" N queens problem """
import sys
from typing import List


def isSafe(board: List[List[int]], row: int, col: int) -> bool:
    """ Check if a queen can be placed on board[row][col]
    Args:
        board (List[List[int]]): chessboard
        row (int): row index
        col (int): column index
    Returns:
        bool: True if queen can be placed, False otherwise
    """
    for i in range(col):
        if board[row][i]:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j]:
            return False
    return True


def solveNQUtil(board: List[List[int]], col: int) -> bool:
    """ Solve N queens problem
    Args:
        board (List[List[int]]): chessboard
        col (int): column index
    Returns:
        bool: True if queens can be placed, False otherwise
    """
    if col == len(board):
        print([[i, board[i].index(1)] for i in range(len(board))])
        return True
    res = False
    for i in range(len(board)):
        if isSafe(board, i, col):
            board[i][col] = 1
            res = solveNQUtil(board, col + 1) or res
            board[i][col] = 0
    return res


def nqueens(n: int) -> bool:
    """ N queens problem
    Args:
        n (int): number of queens
    Returns:
        bool: True if queens can be placed, False otherwise
    """
    if n < 4:
        print("N must be at least 4")
        return False
    board = [[0 for i in range(n)] for j in range(n)]
    if not solveNQUtil(board, 0):
        return False
    return True


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    n = int(sys.argv[1])
    nqueens(n)
