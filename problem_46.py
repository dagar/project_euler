#! /usr/bin/env python

from common import isprime
import math

MAX = 10000

primes = []
for n in xrange(MAX):
    if isprime(n):
        primes.append(n)

def prime_and_twice_sqaure(n):
    for p in primes:
        if n <= p:
            return False
        for x in xrange(int(math.sqrt((n-p)/2)) + 1):
            if n == p + 2 * x**2:
                #print n, "=", p, "+ 2 x", x, "^2"
                return True

    return False

odd_composites = []
for n in xrange(1, MAX):
    i = 2*n + 1
    if i not in primes:
        odd_composites.append(i)


for c in odd_composites:
    if not prime_and_twice_sqaure(c):
        print "odd composite that cannot be written as the sum of a prime and twice a square:", c
