#/usr/bin/env python

from common import ispalindrome

sum = 0
for n in xrange(1, 1000000):
    if ispalindrome(n) and ispalindrome(str(bin(n))[2:]):
        print n, bin(n)
        sum = sum + n

print "sum = ", sum
