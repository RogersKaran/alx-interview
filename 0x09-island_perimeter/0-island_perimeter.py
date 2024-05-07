#!/usr/bin/python3
"""
Create a function def island_perimeter(grid): that returns the perimeter
of the island described in a certain grid
"""


def island_perimeter(grid):
    """
    intialize the perimeter at zero
    """
    perimeter = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                perimeter += 4
                # Check if the cell is an edge cell
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2

    return perimeter

# Update the import statement
island_perimeter = __import__('0-island_perimeter').island_perimeter

