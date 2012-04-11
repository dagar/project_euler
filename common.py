def isprime(n):
  '''check if integer n is a prime'''
  # range starts with 2 and only needs to go up the squareroot of n
  for x in xrange(2, int(n**0.5) + 1):
    if (n % x == 0):
      return False
  return True


def ispalindrome(n):
    pal = str(n)
    for i, v in enumerate(pal):
        if v != pal[len(pal) - i - 1]:
            return False

    return True

