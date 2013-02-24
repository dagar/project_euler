#! /usr/bin/env python



def permutations(s):
    if len(s) <= 1:
        yield s
    else:
        for perm in permutations(s[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + s[0] + perm[i:]


all_perms = []

for p in permutations("1234567890"):
    #print p
    all_perms.append(p)

all_perms.sort()

print all_perms[1000000-1]
