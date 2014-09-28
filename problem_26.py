#! /usr/bin/env python

from decimal import Decimal 



for d in range(2, 20):
  n = Decimal(1.0/d)
  print "1 /", d, str(n)[2:]

