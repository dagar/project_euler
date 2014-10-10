#! /usr/bin/env python3
"""
problem 53: How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are greater than one-million?
"""
from math import factorial


def choose(n, r):
    if r > n:
        return 0
    return int(factorial(n) / (factorial(r) * factorial(n-r)))


def main():
    greater_one_million = 0
    for n in range(1, 100 + 1):
        for r in range(1, n + 1):
            if choose(n, r) > 1000000:
                greater_one_million += 1

    print("There are", greater_one_million, "values > 1000000")

if __name__ == "__main__":
    main()