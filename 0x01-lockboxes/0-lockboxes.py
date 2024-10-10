#!/usr/bin/env python3
""" Lock boxes problem """


def canUnlockAll(boxes):
    """
    Solves the lockboxes problem using Depth-First Search with recursion.
    Time Complexity: O(N + K)
    Space Complexity: O(N) - Due to recursion stack
    Args:
        boxes: List of lists containing keys to other boxes
    Returns:
        bool: True if all boxes can be opened, False otherwise
    """

    def dfs(box, unlocked):
        for key in boxes[box]:
            if key < len(boxes) and key not in unlocked:
                unlocked.add(key)
                dfs(key, unlocked)

    if not boxes:
        return False

    unlocked = {0}
    dfs(0, unlocked)
    return len(unlocked) == len(boxes)
