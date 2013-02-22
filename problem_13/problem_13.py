#! /usr/bin/env python


f = open("numbers")
numbers = []
for line in f.readlines():
  numbers.append(int(line))

total = sum(numbers)

print str(total)[0:10]
