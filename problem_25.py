#! /usr/bin/env python

from math import sqrt

def fib(n):
  return int((1/sqrt(5)) * ((((1 + sqrt(5))/2)**n) - (((1 - sqrt(5))/2)**n)))


for n in xrange(1500, 100000):
  fibn = fib(n)
  if (len(str(fibn)) > 10):
    print n, fibn, len(str(fibn))
