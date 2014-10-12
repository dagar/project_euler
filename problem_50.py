#! /usr/bin/env python3

from common import isprime

primes = [n for n in range(1000000) if isprime(n)]

longest_subset_length = 0
for p in primes[-1000:]:
    # subset starts at the first prime and grows
    min = 0
    max = min + 1
    current_sum = sum(primes[min:max+1])
    while min < max:
        if current_sum < p:
            # grow subset with larger primes 
            max += 1
            current_sum += primes[max]
        elif current_sum > p:
            # shrink subset by removing the lowest primes
            min += 1
            current_sum -= primes[min-1]
        else:
            # found the subset
            subset_len = len(primes[min:max+1])
    
            if subset_len > longest_subset_length:
                longest_subset_length = subset_len
                print("prime =", p, "number of terms =", subset_len)

            break


