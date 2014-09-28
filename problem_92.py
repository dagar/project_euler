#! /usr/bin/env python


numberChainDict = {}

def numberChain(n):
    if n in numberChainDict:
        return numberChainDict[n]

    N = str(n)

    result = sum([int(digit)**2 for digit in N])
    numberChainDict[n] = result
    return result


numberChain89 = []

def main():
    count89 = 0
    for n in xrange(1, 10000000):
        N = n
        while True:
            N = numberChain(N)
            if N == 1:
                break
            elif N == 89:
                count89 = count89 + 1
                break

    print count89


if __name__ == "__main__":
    main()
