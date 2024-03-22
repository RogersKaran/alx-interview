#!/usr/bin/python3
"""Script will unlock list of list"""

def canUnlockAll(boxes):
    """
    Determine if all the boxes can be opened.

    Args:
        boxes (list): A list of lists where each inner list represents a box and contains keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """

    keys = [0]
    for key in keys:
        for boxKey in boxes[key]:
            if boxKey not in keys and boxKey < len(boxes):
                keys.append(boxKey)
    if len(keys) == len(boxes):
        return True
    return False
