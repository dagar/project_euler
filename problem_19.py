#! /usr/bin/env python


import datetime

total_sundays = 0
for year in range(1901, 2001):
  for month in range(1, 12+1):
    d = datetime.date(year,month,1)
    if d.weekday() == 6:
        print d
        total_sundays = total_sundays + 1



print total_sundays
