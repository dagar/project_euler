#! /usr/bin/env python

from common import isprime

def rotate_number(n):
    original_number = str(n)
    N = ""
    for c in original_number[1:]:
        N += c 
    N += original_number[0]
    return N


def isCircularPrime(n):
    
    all_rotations = [] 
    all_rotations.append(n)
    for i in xrange(len(str(n))-1):
        all_rotations.append(rotate_number(all_rotations[i]))

    for num in all_rotations:
        if not isprime(int(num)):
            return False

    return True


count = 0
max = 1000000
for n in xrange(2, max+1):
    if isCircularPrime(n):
        count += 1
        print n


print "There are", count, "circular primes below", max

