#! /usr/bin/env python

import math

def pentagonal_number(n):
    return int(n * (3 * n - 1) * 0.5)

pentagonal_numbers = []
for n in range(1, 10000):
    pentagonal_numbers.append(pentagonal_number(n))

pentagonal_set = set(pentagonal_numbers)

# find pair of pentagonal numbers, sum and difference both pentagonal, and minimize D = abs(Pk - Pj). What is D?
for j in range(10000):
    for k in range(j, 10000-1):
        Pj = pentagonal_numbers[j]
        Pk = pentagonal_numbers[k]

        if Pj + Pk in pentagonal_set:
            if Pk - Pj in pentagonal_set:
                print "Pj =", Pj, "Pk =", Pk, "D =", int(math.fabs(Pj-Pk))
