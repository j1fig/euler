import sys
import cProfile

from collections import deque

arg = int(sys.argv[1])


def findHighestFactorPrimeEratosthenes(limit):
    prime = 2
    while prime < limit:
        nextLimit = prime**2
              
    return prime

def findPrimesRaw(limit):
    primes = [2]
    nextPrime = 3
    while nextPrime < limit:
        testNumber = 2
        while nextPrime%testNumber != 0:
            testNumber += 1
        if testNumber == nextPrime:
            primes += [nextPrime]
        nextPrime += 1
    return primes
                


def main():
    #print 'Calculating prime numbers raw until ' + str(arg) + '...'
    #primes = findPrimesRaw(arg)
    #print '...done!'

    print 'Calculating prime numbers Eratosthenes until ' + str(arg) + '...'
    primes = findHighestFactorPrimeEratosthenes(arg)
    print '...done!'


cProfile.run('main()')

