#!/usr/bin/python3
"""
Main file for testing
"""

makeChange = __import__('0-making_change').makeChange
from time_test import timer

@timer
def run_makeChange(coins, total):
    print(makeChange(coins, total))


print(makeChange([1, 2, 25], 37))
print(makeChange([1256, 54, 48, 16, 102], 1453))

# time performance test
run_makeChange([1, 2, 25], 37)
