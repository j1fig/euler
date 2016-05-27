import sys
import cProfile

arg = int(sys.argv[1])


def brute(number):
    """
    works just fine...
    """
    interval = range(1, number+1)
    sum_squares = sum([n**2 for n in interval])
    square_of_sum = sum(interval)**2
    return square_of_sum - sum_squares


def main():
    print brute(arg)


cProfile.run('main()')
