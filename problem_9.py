#!/usr/bin/env python

for c in xrange(1000, 0, -1):
    for b in xrange(1000-c, 0, -1):
        a = 1000 - c - b
        #print a, b, c
        if (a*a + b*b == c*c):
            if (a < b < c):
                print "a", "b", "c", "abc"
                print a, b, c, a*b*c

