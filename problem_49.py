#! /usr/bin/env python

from common import isprime, permutations

primes = []
for n in xrange(1000, 10000):
    if isprime(n):
        primes.append(n)

primelist = {}
for prime in primes:
    string_perms = set(permutations(str(prime)))
    perms = []
    for perm in string_perms:
        p = int(perm)
        if p > prime and isprime(p):
            perms.append(p)

    if len(perms) > 1:
        perms.sort()
        for perm_prime in perms:
            next_prime = perm_prime + perm_prime - prime
            if next_prime in perms:
                print prime, perm_prime, next_prime, "- all terms concatenated:", str(prime) + str(perm_prime) + str(next_prime)
