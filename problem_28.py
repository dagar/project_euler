#! /usr/bin/env python

def create_spiral(n):
    spiral = [[0 for x in xrange(n)] for x in xrange(n)] 

    r = n / 2 
    c = r

    direction = 1
    value = 1
    moves = 1
    spiral[r][c] = 1
    for i in range(n):
        for m in range(moves):
            if m == n - 1:
                return spiral
            c = c + direction
            value = value + 1
            spiral[r][c] = value

        for m in range(moves):
            r = r + direction
            value = value + 1
            spiral[r][c] = value

        moves = moves + 1
        direction = direction * -1

def sum_diagonals(spiral):
    n = len(spiral[0])

    sum = 0
    for i in range(n):
        sum = sum + spiral[i][i] + spiral[i][n-i-1]

    sum = sum - 1
    return sum


spiral = create_spiral(1001)
print "Diagonal sum =", sum_diagonals(spiral)
