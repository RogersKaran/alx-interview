#!/usr/bin/python3
"""
    A module to return pascal triangle
"""

def pascal_triangle(n):
    """
    Args:
      n (int): The number of triangle rows
    Returns:
      List having lists of integers that rep the Pascal's triangle
    """

    lists = []
    if n =0:
    return lists
    for i in range(n):
        lists.append([])
        lists[i].append(1)
        if (i > 0):
            for j in range(1, i):
                lists[i].append(lists[i - 1][j - 1] + lists[i -1][j])
            lists[i].append(1)
    return lists
