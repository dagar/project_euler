from functools import reduce
def isprime(n):
  '''check if integer n is a prime'''
  # range starts with 2 and only needs to go up the squareroot of n
  if n <= 1:
      return False

  for x in range(2, int(n**0.5) + 1):
    if (n % x == 0):
      return False

  return True


def ispalindrome(n):
    pal = str(n)
    for i, v in enumerate(pal):
        if v != pal[len(pal) - i - 1]:
            return False

    return True


def fib(n):
    fn = f1 = f2 = 1
    for x in range(2, n):
        fn = f1 + f2
        f2, f1 = f1, fn
    return fn


def factors(n):
    #return [i for i in xrange(1, int(n**0.5)+1) if (n % i == 0)]
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


def proper_divisor_sum(n):
    d = factors(n)
    d.remove(n)
    return sum(d)


def permutations(word):
    if len(word) == 1:
        return set([word])
    
    perms = permutations(word[1:])
    char = word[0]
    result = set([])
    for perm in perms:
        for i in range(len(perm) + 1):
            result.add(perm[:i] + char + perm[i:])
            
    return result
