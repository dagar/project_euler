#! /usr/bin/env python

"""
problem 39: maximize the number of integer perimeters of a right angle triangle for p <= 1000
"""

import math

max_solution_count = 0
max_solution_perimeter = 0
for p in range(1000+1):
    solution_count = 0
    for h in range(1, p):
        for a in range(1, p - h):
            b = p - h - a
            if h**2 == a**2 + b**2:
                print p, "h^2 = a^2 + b^2", h, a, b
                solution_count += 1

    if solution_count > max_solution_count:
        max_solution_count = solution_count
        max_solution_perimeter = p


print "max number of solutions is", max_solution_count, "for perimeter =", max_solution_perimeter
