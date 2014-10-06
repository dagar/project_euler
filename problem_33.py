#! /usr/bin/env python
"""
problem 33: cancelling fractions
"""

# for single slash (/) always means true (non-truncating) division
from __future__ import division

for numerator in range(10, 100):
    for denominator in range(numerator, 100):
        if numerator % 10 and denominator % 10:
            N = str(numerator)
            D = str(denominator)
            reducedN = reducedD = 1
            if N[0] in D:
                reducedN = int(N[1])
                reducedD = int(D.replace(N[0], '', 1))

            if N[1] in D:
                reducedN = int(N[0])
                reducedD = int(D.replace(N[1], '',  1))

            fraction = numerator / denominator
            reducedFraction = reducedN / reducedD
            if fraction == reducedFraction and reducedN != reducedD:
                print numerator, "/", denominator, reducedN, "/", reducedD

