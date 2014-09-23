#! /usr/bin/env python

from common import isprime

MAX_A=1
MAX_B=41

def makef(a, b):
    def f(n):
        return n**n + a*n + b

    return f

def prime_run(f):
    primes = []
    for n in range(1, 100):
        fn = f(n)
        if ((fn > 0 and isprime(fn)) or (f(-n) > 0 and isprime(f(-n)))):
            #print n, fn, isprime(fn)
            primes.append(n)
        else:
            return primes

ab = {}
for a in xrange(-MAX_A, MAX_A+1):
    for b in xrange(-MAX_B, MAX_B+1):
        f = makef(a, b)
        pr = prime_run(f)
        if (len(pr) > 0):
            print a, b, len(pr), pr
            ab[len(pr)] = a, b

l = max(ab.keys())

print "Max length", l
print "a, b = ", ab[l]
print ab[l][0] * ab[l][1]
