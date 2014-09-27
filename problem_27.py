#! /usr/bin/env python

from common import isprime
import math

def prime_run(a, b):
    for n in xrange(100):
        p = math.pow(n, 2) + a*n + b
        if p > 0 and isprime(p):
            continue
        else:
            return n


largest = 1
final_a = 1
final_b = 1

MAX = 1000
for a in xrange(-MAX, MAX + 1):
    for b in xrange(-MAX, MAX + 1):
        N = prime_run(a, b)
        if N > largest:
            final_a = a
            final_b = b
            largest = N

print "a, b, N", final_a, final_b, largest

print "a * b", final_a * final_b
