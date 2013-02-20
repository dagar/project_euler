#! /usr/bin/env python

def is_fifth_power_sum(n):
  sum = 0
  for digit in str(n):
    sum += int(digit) ** 5

  if (sum == n):
    print n
    return n
  else:
    return 0


sum = 0
for i in xrange(2, 299999):
  sum += is_fifth_power_sum(i)

print "Sum =", sum
