#!/usr/bin/python3
"""
Calculates the minimum number of operations needed to achieve
exactly n H characters in a text file using only "Copy All" and "Paste" operations.
"""

def minOperations(n):
    if n <= 1:
        return 0
    
    # Initialize the number of operations needed for each index
    operations = [0] * (n + 1)
    
    for i in range(2, n + 1):
        # Initially, set the number of operations for each index to be equal to the index
        operations[i] = i
        
        # Check if the current index (i) is a factor of n
        for j in range(2 * i, n + 1, i):
            # Update the number of operations needed for index j
            operations[j] = min(operations[j], operations[i] + (j // i))

    # The minimum number of operations to achieve n H's is stored at index n
    return operations[n]

