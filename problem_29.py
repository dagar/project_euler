#! /usr/bin/env python

terms = []
for a in xrange(2, 100+1):
  for b in xrange(2, 100+1):
    terms.append(a**b)

print len(set(terms))
