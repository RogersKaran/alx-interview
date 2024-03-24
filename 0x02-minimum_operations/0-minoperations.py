#!/usr/bin/python3

"""
Calculates the minimum number of operations needed to achieve
exactly n H characters in a text file using only "Copy All" and "Paste" operations.
"""

def minOperations(n):
    """
        function: 
            Calculates the fewest number of operations needed to give a result of exactly
            n H characters in a file
        args: n: Number of characters to be displayed
        return: number of min operations
    """

    now = 1
    start = 0
    counter = 0
    while now < n:
        reminder = n - now
        if (reminder % now == 0):
            start = now
            now += start
            counter += 2
        else:
            now += start
            counter += 1
    return counter
