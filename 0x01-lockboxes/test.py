#!/usr/bin/env python3

from collections import deque


# Solution 1: BFS with Queue
def canUnlockAll_bfs(boxes):
    """
    Solves the lockboxes problem using Breadth-First Search with a queue.
    Time Complexity: O(N + K) where N is number of boxes, K is total number of keys
    Space Complexity: O(N)
    """
    n = len(boxes)
    if n == 0:
        return False

    queue = deque([0])  # Start with box 0
    unlocked = {0}

    while queue:
        current_box = queue.popleft()

        # Try all keys in the current box
        for key in boxes[current_box]:
            if key < n and key not in unlocked:
                unlocked.add(key)
                queue.append(key)

    return len(unlocked) == n


# Solution 2: DFS with Recursion
def canUnlockAll_dfs(boxes):
    """
    Solves the lockboxes problem using Depth-First Search with recursion.
    Time Complexity: O(N + K)
    Space Complexity: O(N) - Due to recursion stack
    """

    def dfs(box, unlocked):
        for key in boxes[box]:
            if key < len(boxes) and key not in unlocked:
                unlocked.add(key)
                dfs(key, unlocked)

    if not boxes:
        return False

    unlocked = set([0])
    dfs(0, unlocked)
    return len(unlocked) == len(boxes)


# Solution 3: Graph Theory with Adjacency List
def canUnlockAll_graph(boxes):
    """
    Solves the lockboxes problem using graph theory concepts.
    Treats boxes as nodes and keys as directed edges.
    Time Complexity: O(N + K)
    Space Complexity: O(N + K)
    """
    n = len(boxes)
    if n == 0:
        return False

    # Create adjacency list representation
    graph = {i: set(boxes[i]) for i in range(n)}

    # DFS to traverse the graph
    visited = set()

    def traverse(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor < n and neighbor not in visited:
                traverse(neighbor)

    traverse(0)
    return len(visited) == n


# Benchmark function to compare approaches
def benchmark_solutions():
    import time

    test_cases = [
        [[1], [2], [3], [4], []],  # Simple linear case
        [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]],  # Complex case
        [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]  # Not all reachable
    ]

    solutions = [
        ("BFS with Queue", canUnlockAll_bfs),
        ("DFS with Recursion", canUnlockAll_dfs),
        ("Graph Theory", canUnlockAll_graph)
    ]

    for name, func in solutions:
        print(f"\nTesting {name}:")
        start_time = time.time()

        for i, test_case in enumerate(test_cases, 1):
            result = func(test_case)
            print(f"Test case {i}: {'Passed' if result == (i < 3) else 'Failed'}")

        end_time = time.time()
        print(f"Time taken: {(end_time - start_time) * 1000:.2f} ms")


if __name__ == "__main__":
    benchmark_solutions()
