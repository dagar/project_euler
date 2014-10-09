#! /usr/bin/env python
"""
problem 62: Find the smallest cube for which exactly five permutations of its digits are cube.
"""

cubes = []
for n in range(100000):
    cubes.append(n**3)

cube_sorted = {}
for cube in cubes:
    C = [c for c in str(cube)]
    C.sort()
    key = "".join(C)
    if not key in cube_sorted:
        cube_sorted[key] = set([cube])
    else:
        cube_sorted[key].add(cube)

    if len(cube_sorted[key]) >= 5:
        print "Min cube with exactly five permutations:", min(cube_sorted[key]), cube_sorted[key]
        break
