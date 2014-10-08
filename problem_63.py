#! /usr/bin/env python
"""
problem 63: How many n-digit positive integers exist which are also an nth power?
"""

count = 0
for n in range(1, 10000):
    for x in range(1, 50):
        result = str(n ** x)
        if len(result) == x:
            count += 1
            print n, x, result

print count
