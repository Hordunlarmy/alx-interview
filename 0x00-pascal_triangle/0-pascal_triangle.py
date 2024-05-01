#!/usr/bin/env python3
from typing import List


def pascal_triangle(n: int) -> List[List[int]]:
    """
    Generate Pascal's Triangle up to the nth row.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    # print(f"Initial triangle with one row: {triangle}")

    for i in range(1, n):
        # print(f"\nfor i={i} in range(1, n)[n={n}]")
        row = [1]
        # print(f"Starting new row: {row}")

        for j in range(len(triangle[i - 1]) - 1):
            # print(
            #     f"for j={j} in range( "
            #     f"len(triangle[i - 1]) - 1)[{len(triangle[i - 1]) - 1}]")
            sum_elements = triangle[i - 1][j] + triangle[i - 1][j + 1]
            # print(
            #     f"sum_elements = "
            #     f"triangle[i={i} - 1][j={j}][{triangle[i - 1][j]}] + "
            #     f"triangle[i={i} - 1][j={j} + 1][{triangle[i - 1][j + 1]}]")
            row.append(sum_elements)
            # print(
            #     f"Appending sum of {triangle[i - 1][j]} + "
            #     f"{triangle[i - 1][j + 1]} = {sum_elements} to row {i + 1}")

        row.append(1)
        # print(f"Ending row {i + 1} with final '1': {row}")

        triangle.append(row)
        # print(f"Triangle after adding row {i + 1}: {triangle}")

    return triangle
