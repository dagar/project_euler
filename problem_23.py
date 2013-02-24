#! /usr/bin/env python

from common import proper_divisor_sum

MAX_NUM = 28123


abundant = set()
for n in range(2, MAX_NUM+1):

    d = proper_divisor_sum(n)
    if (d > n):
        abundant.add(n)

abundant_sums = set()
for i in abundant:
    for j in abundant:
        abundant_sums.add(i+j)

not_abundant_sum = set()
for n in range(MAX_NUM+1):
    if n not in abundant_sums:
        not_abundant_sum.add(n)


print sum(not_abundant_sum)
