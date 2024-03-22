#!/usr/bin/python3

from collections import deque

def canUnlockAll(boxes):
    """
    Determine if all the boxes can be opened.

    Args:
        boxes (list): A list of lists where each inner list represents a box and contains keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    visited = set()
    queue = deque([0])  # Start with the first box
    
    while queue:
        current_box = queue.popleft()
        visited.add(current_box)
        
        for key in boxes[current_box]:
            if key < n and key not in visited:
                queue.append(key)
    
    return len(visited) == n

if __name__ == "__main__":
    # Test cases
    boxes1 = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes1))  # Output: True

    boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes2))  # Output: True

    boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes3))  # Output: False
