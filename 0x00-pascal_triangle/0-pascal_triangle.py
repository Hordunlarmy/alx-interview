#!/usr/bin/env python3


def pascal_triangle(n):
    """ Generate Pascal's Triangle up to the nth row """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(len(triangle[i - 1]) - 1):
            sum_elements = triangle[i - 1][j] + triangle[i - 1][j + 1]
            row.append(sum_elements)
        row.append(1)
        triangle.append(row)

    return triangle
