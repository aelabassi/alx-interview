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


# Test cases
def test_canUnlockAll():
    # Test case 1: All boxes can be opened
    boxes1 = [[1], [2], [3], [4], []]
    assert canUnlockAll(boxes1) == True, "Test case 1 failed"

    # Test case 2: Not all boxes can be opened
    boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    assert canUnlockAll(boxes2) == True, "Test case 2 failed"

    # Test case 3: Some boxes can't be reached
    boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    assert canUnlockAll(boxes3) == False, "Test case 3 failed"

    print("All test cases passed!")


# Run the tests
if __name__ == "__main__":
    test_canUnlockAll()
