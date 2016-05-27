import sys
import cProfile


arg = int(sys.argv[1])


def sieve_n_sum(limit):
    primes = [2]
    multiples_set = set(range(2*2, limit, 2))
    for p in range(primes[-1]+1, limit):
        if p not in multiples_set:
            primes.append(p)
            multiples_set.update(range(p*2, limit, p))
    return sum(primes)


def main():
    print sieve_n_sum(arg)


cProfile.run('main()')
