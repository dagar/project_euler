#! /usr/bin/env python3

from decimal import *

def ispandigital(N):
    if len(N) != 9:
        return False
    for c in range(1, 10):
        if c not in N:
            return False
    return True


fn = Decimal(1)
f1 = Decimal(1)
f2 = Decimal(1)
getcontext().prec = 999999999999999999
for x in range(2, 1000000):
    fn = f1 + f2
    f2, f1 = f1, fn

    ft = fn.as_tuple()[1]
    first_nine = ft[:9]
    last_nine = ft[-9:]
    if ispandigital(first_nine) and ispandigital(last_nine):
        print("k =", x+1, "length =", len(str(fn)))
        break

