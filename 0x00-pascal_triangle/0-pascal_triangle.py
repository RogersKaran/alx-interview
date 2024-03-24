#!/usr/bin/python3
"""
    A module to return Pascal's triangle
"""

def pascal_triangle(n):
    """
    func: pascal_triangle
       returns a list of lists of integers
       representing the Pascal's triangle of n
    args:
      (int: n): The number of triangle rows (> 0>
    returns:
      <list <of lists>>
    """

    if type(n) is not int and n < 0:
        return ([])
    rows = []
    for i in range(n):
        row.append([])
        row[i].append(1)
        if (i > 0):
            for j in range(1, i):
                rows[i].append(lists[i - 1][j - 1] + row[i -1][j])
            row[i].append(1)
            
    return (row)
