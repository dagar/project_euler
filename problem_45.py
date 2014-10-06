#! /usr/bin/env python
"""
problem 45: T285 = P165 = H143 = 40755.
the next triangle number that is also pentagonal and hexagonal
"""

def triangle(n):
    " Tn=n(n+1)/2 "
    return int(0.5 * n * (n + 1))

def pentagonal(n):
    " Pn=n(3n-1)/2 "
    return int(0.5 * n * (3 * n - 1))

def hexagonal(n):
    " Hn=n(2n-1) "
    return n * (2 * n - 1)


# generate large list of triangle numbers
triangle_numbers = []
for number in xrange(100, 100000):
    triangle_numbers.append(triangle(number))

# generate sets of pentagonal and hexagonal numbers
pentagonal_numbers = set()
hexagonal_numbers = set()
for number in xrange(100, 1000000):
    pentagonal_numbers.add(pentagonal(number))
    hexagonal_numbers.add(hexagonal(number))

# find triangle numbers that are also pentagonal and hexagonal numbers
for Tn in triangle_numbers:
    if Tn in pentagonal_numbers and Tn in hexagonal_numbers:
        print Tn
