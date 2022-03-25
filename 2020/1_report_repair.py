# --- Day 1: Report Repair ---
# https://adventofcode.com/2020/day/1

from itertools import combinations
from math import prod


def findsum(values, target, n):
    """generates combinations of values to n places, checking if they
    sum to target, and returning the product if they do"""

    combolist = combinations(values, n)
    for combo in combolist:
        if sum(combo) == 2020:
            return prod(combo)


filename = "1.txt"
with open(filename, "r") as f:
    values = [int(x) for x in f.read().splitlines()]

print(findsum(values, 2020, 2))
print(findsum(values, 2020, 3))
