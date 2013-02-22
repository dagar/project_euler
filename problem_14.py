#! /usr/bin/env python

def collatz_sequence(n):
  ret = []
  while True:
    if n % 2:
      # odd
      n = 3 * n + 1

    else:
      #even
      n = n / 2

    #print n
    ret.append(n)
    if (n == 1):
      return set(ret)


longest_chain = 0
longest_n = 0
for x in xrange(2, 1000000):
  l = len(collatz_sequence(x))
  if l > longest_chain:
    longest_chain = l
    longest_n = x

print longest_n, longest_chain
