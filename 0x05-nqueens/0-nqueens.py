#!/usr/bin/python3
"""N queens solution finder module."""

import sys

solutions = []  # The list of possible solutions to the N queens problem.
n = 0  # The size of the chessboard.
pos = None  # The list of possible positions on the chessboard.


def get_input() -> int:
    """Retrieves and validates this program's argument.

    Returns:
        int: The size of the chessboard.
    """
    global n
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    return n


def is_attacking(pos0: list, pos1: list) -> bool:
    """Checks if two queens are attacking each other.

    Args:
        pos0 (list): The first queen's position.
        pos1 (list): The second queen's position.

    Returns:
        bool: True if attacking, otherwise False.
    """
    return (
        pos0[0] == pos1[0]
        or pos0[1] == pos1[1]
        or abs(pos0[0] - pos1[0]) == abs(pos0[1] - pos1[1])
    )


def group_exists(group: list) -> bool:
    """Checks if a group exists in the list of solutions.

    Args:
        group (list): A group of possible positions.

    Returns:
        bool: True if it exists, otherwise False.
    """
    global solutions
    for stn in solutions:
        matches = sum(
            1 for stn_pos, grp_pos in zip(stn, group) if stn_pos == grp_pos
        )
        if matches == n:
            return True
    return False


def build_solution(row: int, group: list) -> None:
    """Builds a solution for the n queens problem.

    Args:
        row (int): The current row in the chessboard.
        group (list): The group of valid positions.
    """
    global solutions, n
    if row == n:
        if not group_exists(group):
            solutions.append(group.copy())
        return

    for col in range(n):
        idx = row * n + col
        if not any(is_attacking(pos[idx], g) for g in group):
            group.append(pos[idx])
            build_solution(row + 1, group)
            group.pop()


def get_solutions() -> None:
    """Finds all solutions for the N queens problem."""
    global pos, n
    pos = [[i // n, i % n] for i in range(n**2)]
    build_solution(0, [])


if __name__ == "__main__":
    n = get_input()
    get_solutions()
    for solution in solutions:
        print(solution)
