#! /usr/bin/env python3
"""
problem 56: max digit sum a^b a, b < 100
"""

import math

def digit_sum(n):
    sum = 0
    while n != 0:
        sum += n % 10
        n = n // 10

    return sum

max_sum = 0
for a in range(100):
    for b in range(100):
        pow = a**b
        sum = digit_sum(pow)
        if sum > max_sum:
            max_sum = sum
            print("%d^%d, digitsum = %d" % (a, b, sum))
