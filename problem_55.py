#! /usr/bin/env python
"""
problem 55: A number that never forms a palindrome through the reverse and add process is called a Lychrel number.
How many Lychrel numbers are there below ten-thousand?
"""

from common import ispalindrome

def isLychrel(n):
    for i in range(50):
        n = n + int(str(n)[::-1])
        if ispalindrome(n):
            return True
    return False


not_lychrel_count = 0
for n in range(10000):
    if not isLychrel(n):
        not_lychrel_count += 1

print "There are", not_lychrel_count, "numbers < 10000 that aren't Lychrel"
