#!/usr/bin/python3
""""Prime Game"""


def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def play_game(n):
    """
    Simulate a single game with a set of numbers from 1 to n.
    Returns True if Maria wins, False if Ben wins.
    """
    # Create a set of available numbers
    available = set(range(1, n + 1))

    # Track current player (True for Maria, False for Ben)
    maria_turn = True

    while True:
        # Find available prime numbers
        primes = [p for p in available if is_prime(p)]

        # If no primes left, current player loses
        if not primes:
            return not maria_turn

        # Choose the smallest prime
        chosen_prime = min(primes)

        # Remove chosen prime and its multiples
        to_remove = {p for p in available if p % chosen_prime == 0}
        available -= to_remove

        # Switch turns
        maria_turn = not maria_turn


def isWinner(x, nums):
    """
    Determine the overall winner across x rounds.

    Args:
    x (int): Number of rounds
    nums (list): List of n values for each round

    Returns:
    str or None: Name of the winner or None if undetermined
    """
    # Validate inputs
    if x != len(nums):
        return None

    # Track wins for Maria and Ben
    maria_wins = 0
    ben_wins = 0

    # Play each round
    for n in nums:
        if play_game(n):
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
