#! /usr/bin/env python3

from common import factors, isprime

primes = [n for n in range(1000000) if isprime(n)]

def distinct_prime_factor_count(n):
    f = factors(n) - set([1, n])

    prime_factors = set([])
    for p in f:
        if isprime(p):
            prime_factors.add(p)

    return len(prime_factors)


numbers = []
for n in range(1, 1000000):
    nDistinctPrimes = distinct_prime_factor_count(n)
    if nDistinctPrimes == 4:
        if len(numbers) > 0 and n - 1 != numbers[-1]:
            numbers = []

        numbers.append(n)

        if len(numbers) == 4:
            print("The first 4 are", numbers)
            exit(0)

