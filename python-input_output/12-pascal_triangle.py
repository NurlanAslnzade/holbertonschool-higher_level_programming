#!/usr/bin/python3
"""Pascal Triangle"""


def pascal_triangle(n):
    """pascal_triangle"""
    if n <= 0:
        return []
    triangle = []
    for i in range(n):
        a = [1]
        if i >= 1:
            b = triangle[i-1]
            for k in range(1, i):
                a.append(b[k] + b[k-1])
            a.append(1)
        triangle.append(a)
    return triangle
