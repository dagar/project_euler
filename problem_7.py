#!/usr/bin/env python

from common import isprime
from math import log

def main(n):

    primes = []

    for x in xrange(2, 2*int(n*log(n))):
        if isprime(x):
            primes.append(x)

        if len(primes) == n:
            print primes
            return primes[-1]

print main(10001)
