#! /usr/bin/env python

from common import isprime, permutations


def isPandigital(n):
    number = ""
    for i in range(1, n+1):
        number += str(i)

    perms = permutations(number)

    primes = []
    for perm in perms:
        if isprime(int(perm)):
            primes.append(int(perm))
    return primes

for n in range(4, 9):
    primes = isPandigital(n)
    print primes
    largest = 0
    for i in primes:
        if i > largest:
            largest = i

    print "largest =", largest
