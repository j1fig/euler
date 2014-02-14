import sys
import cProfile

from collections import deque

arg = int(sys.argv[1])


def findHighestFactorPrimeEratosthenes(limit):
    highestPrime = 2
    allPrimes = []
    while highestPrime < limit:
        nextLimit = highestPrime**2
        primes = set([i for i in range(highestPrime,nextLimit)])
        print 'Current prime candidates: ' + str(primes)
        highestPrime = max(primes)
        for prime in primes:
            primeMultiple = prime + prime
            while primeMultiple < highestPrime:
                if primeMultiple in primes:
                    primes.remove(primeMultiple)
                primeMultiple = prime + prime
        highestPrime = max(primes)
        print 'Found primes: ' + str(primes)
        allPrimes += list(primes)
    return allPrimes

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
    print 'Calculating prime numbers Eratosthenes until ' + str(arg) + '...'
    primes = findHighestFactorPrimeEratosthenes(arg)
    print '...done!'


cProfile.run('main()')

