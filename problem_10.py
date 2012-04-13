#!/usr/bin/env python

from common import isprime


def main():

    sum = 0
    for n in xrange(2, 2000000+1):
        if isprime(n):
            sum += n

    print sum



main()
