import sys
import cProfile


arg = int(sys.argv[1])


def bit_smarter(nth_prime):
    """
    0.08 sec for the 10001th.
    note to future: tried to dynamically update multple expansion limit with
                    generators but performance sucked...
    """
    primes = [2]
    multiples_set = set(range(2*2, 110000, 2))
    while len(primes) < nth_prime:
        for p in range(primes[-1]+1, 110000):
            if p not in multiples_set:
                primes.append(p)
                multiples_set.update(range(p*2, 110000, p))
    return primes[nth_prime-1]


def brute(nth_prime):
    """
    takes around 30 sec for the 10001th, not enough for my 2012 lenovo
    """
    prime_index = 0
    nextPrime = 2
    while prime_index < nth_prime:
        test_div = 2
        while nextPrime % test_div != 0:
            test_div += 1
        if test_div == nextPrime:
            prime_index += 1
            if prime_index == nth_prime:
                return nextPrime
        nextPrime += 1


def main():
    print bit_smarter(arg)


cProfile.run('main()')
