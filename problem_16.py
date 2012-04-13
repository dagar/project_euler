#!/usr/bin/env python

# written by Emily April 12, 2012

big_number = 2**1000
big_string = str(big_number)

sum = 0
for puppy in big_string:
    sum += int(puppy)

print sum
