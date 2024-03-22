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


