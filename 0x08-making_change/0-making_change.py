#!/usr/bin/python3
"""
Module for making change with fewest oins
"""

def makeChange(coins, total):
    """
    Deterimine the fewest number of coins needed to meet a given total
    """
    if total < 1:
        return 0

    # Initialize a list to store the minimum number of ccins
    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0

    # Iterate through each coin value
    for coin in coins:
        # Update min_coins for eacch possible total
        for i in range(coin, total + 1):
            min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)

    # If the total amount cannot be met by any number of coins, return -1
    if min_coins[total] == float('inf'):
        return -1

    return min_coins[total]
