#!/usr/bin/env python

# written by Emily April 12, 2012

def factorial(n):
    fn = 1
    for i in range(n, 1, -1):
        fn *= i

    return fn

big_number = factorial(100)
big_string = str(big_number)

sum = 0
for puppy in big_string:
    sum += int(puppy)

print sum
