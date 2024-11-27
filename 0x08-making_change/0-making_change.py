#!/usr/bin/python3
"""Make change problem."""


def makeChange(coins, total):
    """Make change.
    Args:
        coins: list of the values of
        the coins in your possession (int)
        total: total amount of money
        to make change for (int)
    Returns:
        The minimum number of coins
        needed to make the change"""
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    change = 0
    for coin in coins:
        change += total // coin
        total = total % coin
    if total != 0:
        return -1
    return change
