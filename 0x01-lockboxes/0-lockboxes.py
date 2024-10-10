#!/usr/bin/env python3
""" Lock boxes problem """


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Parameters:
    boxes (list of lists): A list of n boxes, where boxes[i] represents the keys
                          in box i. Each box is numbered sequentially from 0 to n-1.

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


def test_canUnlockAll():
    """
    Test cases for the canUnlockAll function
    """
    # Test case 1: Simple sequential case
    boxes1 = [[1], [2], [3], [4], []]
    print(f"Test case 1: {boxes1}")
    result = canUnlockAll(boxes1)
    print(f"Expected: True, Got: {result}")
    assert result == True, "Test case 1 failed"

    # Test case 2: More complex case with multiple keys
    boxes2 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(f"\nTest case 2: {boxes2}")
    result = canUnlockAll(boxes2)
    print(f"Expected: False, Got: {result}")
    assert result == False, "Test case 2 failed"

    # Test case 3: Cannot open all boxes
    boxes3 = [[1, 3], [3, 0, 1], [2], [0]]
    print(f"\nTest case 3: {boxes3}")
    result = canUnlockAll(boxes3)
    print(f"Expected: False, Got: {result}")
    assert result == False, "Test case 3 failed"

    # Test case 4: Single box
    boxes4 = [[]]
    print(f"\nTest case 4: {boxes4}")
    result = canUnlockAll(boxes4)
    print(f"Expected: True, Got: {result}")
    assert result == True, "Test case 4 failed"

    print("\nAll test cases passed!")


if __name__ == "__main__":
    test_canUnlockAll()
