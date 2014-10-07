#! /usr/bin/env python
"""
problem 38: largest 1 to 9 pandigital 9-digit number that can be formed 
as the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""

def ispandigital(n):
    N = str(n)
    if len(N) != 9:
        return False
    for c in '123456789':
        if c not in N:
            return False

    return True


def concatenated_product(number, n):
    product = ""
    for i in range(1, n + 1):
        product += str(number * i)

    return int(product)


largest_concatenated_product = 0
for number in range(100000):
    for n in range(1, 10):
        cp = concatenated_product(number, n)
        if ispandigital(cp):
            if cp > largest_concatenated_product:
                largest_concatenated_product = cp
                print "new largest: product of", number, "and", tuple(i for i in range(1, n+1)), "=", cp

