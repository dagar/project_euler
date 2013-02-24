#! /usr/bin/env python

import common

def proper_divisor_sum(n):
    d = common.factors(n)
    d.remove(n)
    return sum(d)

proper_divisors = {}
amicable_numbers = set()
for n in range(2, 10000):
    d = proper_divisor_sum(n)
    proper_divisors[n] = d

    if (proper_divisors.has_key(d) and (proper_divisors[d] == n)):
        if (n != d):
            print "Found amicable pair", n, d
            amicable_numbers.add(n)
            amicable_numbers.add(d)


#print proper_divisors
#print amicable_numbers

print sum(amicable_numbers)
