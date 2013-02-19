#! /usr/bin/env python

import csv


def alphabetical_value(name):
  ret = 0
  for letter in name.lower():
    ret += ord(letter) - 96

  return ret

f = csv.reader(open('names.txt'))
names = f.next()
names.sort()

total_name_scores = 0
for i, name in enumerate(names):
  #print name[i], i+1, alphabetical_value(name), alphabetical_value(name) * i+1
  print i+1, name, alphabetical_value(name), (alphabetical_value(name) * (i+1))
  total_name_scores += (i+1) * alphabetical_value(name)

print total_name_scores
