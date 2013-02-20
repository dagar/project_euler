#!/usr/bin/env python

from common import ispalindrome

def main():
    palindromes = {}

    for i in range(1000):
        for j in range(1000):
            pal = i * j
            if ispalindrome(pal):
                palindromes[pal] = str(i) + "x" + str(j)

    print max(palindromes.keys()), palindromes[max(palindromes.keys())]


main()
