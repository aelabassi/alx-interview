#!/usr/bin/python3
""" Lock boxes problem """


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Parameters:
    boxes (list of lists): A list of n boxes, where boxes[i]
                          represents the keys
                          in box i. Each box is numbered
                          sequentially from 0 to n-1.

    Returns:
    bool: True if all boxes can be opened, False otherwise

    Requirements:
    - Boxes are numbered sequentially from 0 to n-1
    - Each box contains keys to other boxes
    - Box 0 is unlocked initially
    """
    n = len(boxes)
    if n == 0:
        return False

    # Keep track of which boxes we can unlock
    unlocked = {0}  # Box 0 is already unlocked
    keys_to_try = boxes[0][:]  # Make a copy of the keys from box 0

    while keys_to_try:
        key = keys_to_try.pop()

        # Check if this is a valid box number and we haven't unlocked it yet
        if 0 <= key < n and key not in unlocked:
            unlocked.add(key)
            # Add new keys from this box to our keys to try
            keys_to_try.extend(boxes[key])

    # Check if we can unlock all boxes
    return len(unlocked) == n


if __name__ == "__main__":
    canUnlockAll([[]])
