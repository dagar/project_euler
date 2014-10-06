#! /usr/bin/env python

triangle_numbers = []
def triangle_number(n):
    return (0.5 * n * (n + 1))

alphabet='"ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def word_sum(word):
    sum = 0
    for c in word:
        sum += alphabet.index(c)

    return sum

# build list of triangle numbers
for n in range(1000):
    triangle_numbers.append(triangle_number(n))

# read word file
with open('p042_words.txt') as f:
    wordstmp = f.read()

words = wordstmp.split(",")

triangle_word_count = 0
for word in words:
    if word_sum(word) in triangle_numbers:
        triangle_word_count += 1
        #print word


print "There are", triangle_word_count, "triangle words"
