import sys
import cProfile
from math import sqrt


arg = int(sys.argv[1])


def _triangle_number(n):
    return sum(range(1, n+1))


def _divisors(n):
    divisors = set([1, n])
    for d in range(2, int(sqrt(n))+1):
        if (n % d) == 0:
            divisors.update([d, n/d])
    return divisors


def brute(div_target):
    """
    takes about 5 sec
    """
    n = 1
    while len(_divisors(_triangle_number(n))) < div_target:
        n += 1
    return _triangle_number(n)


def main():
    """
    Right now I just want to move on to the next level however it'd be
    interesting to implement using the prime factors as:

    Let d(n) be the number of divisors for the natural number, n.

    We begin by writing the number as a product of prime factors: n = paqbrc...
    then the number of divisors, d(n) = (a+1)(b+1)(c+1)...

    To prove this, we first consider numbers of the form, n = pa.
    The divisors are 1, p, p2, ..., pa; that is, d(pa)=a+1.

    Now consider n = paqb. The divisors would be:

    1   p   p2  ... pa
    q   pq  p2q ... paq
    q2  pq2 p2q2    ... paq2
    ... ... ... ... ...
    qb  pqb p2qb    ... paqb
    Hence we prove that the function, d(n), is multiplicative, and in this
    particular case, d(paqb)=(a+1)(b+1).
    It should be clear how this can be extended for any natural number which
    is written as a product of prime factors.

    The number of divisor function can be quickly demonstrated with the example
    we considered earlier: 48 = 24×31, therefore d(48)=5×2=10.
    """
    print brute(arg)


cProfile.run('main()')
