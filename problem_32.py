#! /usr/bin/env python

from common import permutations



digits = '123456789'
perms = permutations(digits)
pandigital_products = []
for perm in perms:
    for x in range(1, 6):
        for eq in range(x+1, 7):
            multiplicand = int(''.join(perm[0:x]))
            multiplier = int(''.join(perm[x:eq]))
            product = int(''.join(perm[eq:]))

            if multiplicand * multiplier == product:
                print perm, multiplicand, "x", multiplier, "=", product
                pandigital_products.append(product)


print sum(set(pandigital_products))
