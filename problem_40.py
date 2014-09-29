#! /usr/bin/env python

d = "."
for n in xrange(1, 1000000+1):
    d += str(n)

product = 1
for n in xrange(7):
    product = product * int(d[10**n])

print product
