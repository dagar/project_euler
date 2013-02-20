#! /usr/bin/env python

sum = 0
for n in xrange(1, 1000+1):
  sum += n**n

print sum
print str(sum)[-10:]
