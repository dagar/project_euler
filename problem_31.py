#! /usr/bin/env python

TWOPOUNDS = 200
p = [1, 2, 5, 10, 20, 50, 100, 200]
n = [0, 0, 0, 0, 0, 0, 0, 0]

total_count = 0


for P8 in range(TWOPOUNDS/p[7] + 1):
    for P7 in range(TWOPOUNDS/p[6] + 1):
        for P6 in range(TWOPOUNDS/p[5] + 1):
            for P5 in range(TWOPOUNDS/p[4] + 1):
                for P4 in range(TWOPOUNDS/p[3] + 1):
                    for P3 in range(TWOPOUNDS/p[2] + 1):
                        for P2 in range(TWOPOUNDS/p[1] + 1):
                            for P1 in range(TWOPOUNDS - P2*p[1] - P3*p[2] - P4*p[3] - P5*p[4] - P6*p[5] - P7*p[6] + 1):
                                n = [P1, P2, P3, P4, P5, P6, P7, P8]
                                #print n
                                if TWOPOUNDS == sum([a * b for a, b in zip(p, n)]):
                                    total_count += 1
                                    #print n


print "Total:", total_count
