#!/usr/bin/env pythong

from common import isprime

def prime_factors(n):
  ret = []
  for x in xrange(1, int(n**0.5) + 1):
    if (n % x == 0):
      if isprime(x):
        print ret
        ret.append(x)

  return ret

print prime_factors(13195)
print prime_factors(600851475143)
