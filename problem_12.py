#!/usr/bin/env python

from common import factors

def triangle_number(n):
    return sum(xrange(n+1))

for n in xrange(2, 100000):
    tn = triangle_number(n)
    ln = len(factors(tn))
    #print n, tn, ln
    if ln > 100:
        print "Over 100 factors ", n, tn, ln
    if ln > 500:
        print "Over 500 factors ", n, tn, ln
        break
