#! /usr/bin/env python3

from common import isprime

primes = [n for n in range(1000000) if isprime(n)]


max_subset_length = 0
for min, p1 in enumerate(primes):
    for max, p2 in enumerate(primes[min:]):
        subset = primes[min:max]
        prime_sum = sum(subset)

        if prime_sum < 1000000 and isprime(prime_sum):
            if len(subset) > max_subset_length:
                max_subset_length = len(subset)
                print(prime_sum, max_subset_length, p1, p2)

