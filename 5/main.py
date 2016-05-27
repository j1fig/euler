import sys
import cProfile
import operator

arg = int(sys.argv[1])


def brute(number):
    """
    works fine until 16-17
    """
    smallest_int = 1
    while True:
        all_div = True
        for d in range(1, number+1):
            if (smallest_int % d != 0):
                smallest_int += 1
                all_div = False
                break
        if all_div:
            print 'Result: \t', smallest_int
            return smallest_int


def is_common(f, multiples):
    return [f in m for m in multiples]


def generate_multiples(factors, limit):
    return [range(f, limit+1, f) for f in factors]


def bit_smarter(number):
    factors = range(2, number+1)
    common_denominator = reduce(operator.mul, factors)

    factor_multiples = generate_multiples(factors, common_denominator)

    for f in factor_multiples[-1]:
        if all(is_common(f, factor_multiples)):
            return f


def gcd(a, b):
    """
    calculates the greatest common denominator of two numbers
    """
    if b == 0:
        return a
    r = a % b
    return gcd(b, r)


def lcd(a, b):
    return (a/gcd(a, b))*b


def multi_lcd(factors):
    return reduce(lcd, factors)


def moderately_smart(number):
    """
    meh, instantaneous!
    """
    factors = range(1, number+1)
    return multi_lcd(factors)


def main():
    print moderately_smart(arg)


cProfile.run('main()')
