import math

sum_of_all = 0
for n in xrange(3, 10000000):
    N = str(n)
    length = len(N)

    factorial_sum = sum([math.factorial(int(c)) for c in N])
    if n == factorial_sum:
        sum_of_all = sum_of_all + n
        print n


print "Sum of all numbers which are equal to the sum of the factorial of their digits is", sum_of_all
