#!/usr/bin/env python3
""" Lock boxes problem """


def canUnlockAll(boxes):
    """
    Determines if all boxes in a list of locked boxes can be opened.

    Args:
        boxes (list of lists): A list of lists where
                              each inner list contains keys.
                              Keys are positive integers.
                              A key with the same number
                              as a box opens that box.
                              The first box boxes[0] is unlocked.
                              There can be keys that do not have boxes.

    Returns:
        bool: True if all boxes can be opened, else False

    Example:
        >>> boxes = [[1], [2], [3], [4], []]
        >>> canUnlockAll(boxes)
        True
        >>> boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
        >>> canUnlockAll(boxes)
        True
        >>> boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
        >>> canUnlockAll(boxes)
        False
    """
    n = len(boxes)
    if n == 0:
        return False

    unlocked = set([0])  # First box is always unlocked
    keys = set(boxes[0])  # Keys from the first box

    while keys:
        new_key = keys.pop()

        # Check if the key opens a valid, new box
        if (isinstance(new_key, int) and 0 <= new_key < n and
                new_key not in unlocked):
            unlocked.add(new_key)
            # Add new keys from the newly opened box
            for key in boxes[new_key]:
                if isinstance(key, int) and key >= 0:
                    keys.add(key)

    return len(unlocked) == n
