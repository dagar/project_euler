#! /usr/bin/env python

names = { 1 : "ONE",
          2 : "TWO",
          3 : "THREE",
          4 : "FOUR",
          5 : "FIVE",
          6 : "SIX",
          7 : "SEVEN",
          8 : "EIGHT",
          9 : "NINE",
          10 : "TEN",
          11 : "ELEVEN",
          12 : "TWELVE",
          13 : "THIRTEEN",
          14 : "FOURTEEN",
          15 : "FIFTEEN",
          16 : "SIXTEEN",
          17 : "SEVENTEEN",
          18 : "EIGHTEEN",
          19 : "NINETEEN",
          20 : "TWENTY",
          30 : "THIRTY",
          40 : "FORTY", 
          50 : "FIFTY",
          60 : "SIXTY",
          70 : "SEVENTY",
          80 : "EIGHTY",
          90 : "NINETY",
          100 : "HUNDRED"}


def printNum(n):
  num = str(n)

  if (n == 0):
    return ""

  if len(num) == 1:
    return names[int(num[-1])]
  elif (len(num) == 2):
    if (n < 21):
      return names[int(num[-2:])]
    else:
      if (int(num[-1]) == 0):
        return names[int(num[-2])*10]
      else:
        return names[int(num[-2])*10] + names[int(num[-1])]
  elif (len(num) == 3):
    if num[-2:] == "00":
      return names[int(num[-3])] + names[100] + printNum(int(num[-2:]))
    else:
      return names[int(num[-3])] + names[100] + "and" + printNum(int(num[-2:]))

  elif (len(num) == 4):
    return "ONE" + "THOUSAND"


total_length = 0
for n in range(1, 1000+1):
  total_length += len(printNum(n))
  print printNum(n)

print total_length
