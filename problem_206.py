#! /usr/bin/env python


string = "1_2_3_4_5_6_7_8_9_0"

def squareHasTheForm(n):
    n2 = n ** 2

    if n2 % 10 != 0:
        return False

    N = str(n2)

    if len(N) != len(string):
        return False

    if N[0] != 1:
        return False

    if N[-1] != 0:
        return False

    print n

    if N[0:-1:2] == string[0:-1:2]:
        return True


# find the correct length

starting_value = 1000000000
for x in xrange(starting_value, 10 * starting_value):
    if len(str(x**2)) == len(string):
        starting_value = x
        print "starting value", x
        break

for x in xrange(starting_value, starting_value * 10):
    if squareHasTheForm(x):
        print x

