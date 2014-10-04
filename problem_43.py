#! /usr/bin/env python

from common import permutations, isprime

n = '0123456789'
perms = permutations(n)

primes = []
for p in range(1, 18):
    if isprime(p):
        primes.append(p)

def subStringDivisibility(n):
    for d in range(1, 8):
        if int(n[d:d+3]) % primes[d-1] != 0:
            return False

    return True


count = 0
sum = 0
for perm in perms:
    if subStringDivisibility(perm):
        count += 1
        sum += int(perm)

print "the sum of all 0 to 9 pandigital numbers with this property", sum
print "count", count
