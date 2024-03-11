from collections import deque

def canUnlockAll(boxes):
    if not boxes:
        return False

    n = len(boxes)
    visited = set()
    # Start with the first box
    queue = deque([0])

    while queue:
        current_box = queue.popleft()
        visited.add(current_box)

        for key in boxes[current_box]:
            if key < n and key not in visited:
                queue.append(key)

    return len(visited) == n
