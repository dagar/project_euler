#! /usr/bin/env python

from common import permutations

def check_all_multiples(multiples, perms):
    for m in multiples:
        if m not in perms:
            return False

    return True

for n in xrange(1, 1000000):
    multiples = []
    for i in [2, 3, 4, 5, 6]:
        multiples.append(str(i * n))

    perms = permutations(str(n))

    if check_all_multiples(multiples, perms):
        print n, multiples
