import sys
import cProfile


def brute(arg):
    return reduce(lambda x, y: x + int(y), str(2**arg), 0)


if __name__ == "__main__":
    arg = int(sys.argv[1])

    def main():
        print brute(arg)

    cProfile.run('main()')
