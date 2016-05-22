import sys
import cProfile

arg = int(sys.argv[1])


def _generate_next_prime(last_prime):
    nextPrime = last_prime + 1
    while True:
        testNumber = 2
        while nextPrime % testNumber != 0:
            testNumber += 1
        if testNumber == nextPrime:
            yield nextPrime
        nextPrime += 1


def find_prime_factors(primes, number, result=[]):
    found_factor = False
    for factor in primes:
        if number % factor == 0:
            found_factor = True
    gen = _generate_next_prime(primes[-1])
    while not found_factor:
        factor = gen.next()
        primes.append(factor)

        if number % factor == 0:
            found_factor = True
    number = number/factor
    result.append(factor)
    if number == 1:
        return result
    return find_prime_factors(primes, number, result)


def main():
    prime_factors = find_prime_factors([2, 3], arg)
    print prime_factors

cProfile.run('main()')
