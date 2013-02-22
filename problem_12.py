#!/usr/bin/env python

from common import factor

def triangle_number(n):
    return sum(xrange(n+1))

x=1
for n in xrange(x, x+10):
    tn = triangle_number(n)
    ln = len(factor(tn))
    print n, tn, ln
    if ln > 100:
        print "Over 100 factors ", n, tn, ln
    if ln > 500:
        print "Over 500 factors ", tn
        break
