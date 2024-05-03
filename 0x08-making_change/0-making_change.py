#!/usr/bin/python3
"""
Module for making change with fewest oins
"""

def makeChange(coins, total):
    """
    Deterimine the fewest number of coins needed to meet a given total
    """
    if total <= 0:
        return 0

    else:
        coin = sorted(coins)
        coin.reverse()
        counter = 0
        for i in coin:
            while(total >= i):
                counter += 1
                total -= i
        if total == 0:
            return counter
        return -1

