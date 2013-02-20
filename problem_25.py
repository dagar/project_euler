#! /usr/bin/env python

from common import fib

for n in xrange(4000, 5001):
  fibn = fib(n)
  #print n, fibn, len(str(fibn))
  if (len(str(fibn)) == 1000):
    print n, fibn, len(str(fibn))
