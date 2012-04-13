#!/usr/bin/env python


def triangle_number(n):
    return sum(xrange(n+1))

def factor(n):
    return [i for i in xrange(1, n+1) if (n % i == 0)]


for n in range(9999):
    tn = triangle_number(n)
    ln = len(factor(tn))
    #print n, tn, ln
    if ln > 500:
        print "Over 500 factors ", tn
