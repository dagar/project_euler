#! /usr/bin/env python

from common import isprime

def truncate_left(number):
    N = str(number)
    return int(N[1:])

def truncate_right(number):
    N = str(number)
    return int(N[:-1])

def truncatable_prime(n, truncate_fn):
    N = str(n)
    original_n = N
    while True:
        if isprime(int(N)):
            if len(N) == 1:
                return True
            else:
                N = str(truncate_fn(N))
        else:
            return False

prime_list = []
for n in xrange(10, 1000000):
    if truncatable_prime(n, truncate_left):
        prime_list.append(n)

# final sum of primes
sum = 0
for n in prime_list:
    if truncatable_prime(n, truncate_right):
        sum += n
        print n, "is a truncatable prime (left and right)"

print "sum of all truncatable primes is", sum
