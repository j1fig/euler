import sys
import cProfile


def collatz_length(n):
    """
    modified collatz sequence
    see https://en.wikipedia.org/wiki/Collatz_conjecture#As_a_parity_sequence
    """
    if n == 1:
        return 1
    if (n % 2) == 0:
        return 1 + collatz_length(n/2)
    else:
        return 2 + collatz_length((3*n + 1)/2)


def s_collatz_length(n, prev):
    if n == 1:
        return 1
    if n in prev:
        return prev[n]
    if (n % 2) == 0:
        return 1 + s_collatz_length(n/2, prev)
    else:
        return 2 + s_collatz_length((3*n + 1)/2, prev)


def bit_smarter(limit):
    """
    if its already computed, why not just look it up in the dict? duh!
    """
    c_lengths = {}

    for s in range(1, limit+1):
        c_lengths[s] = s_collatz_length(s, c_lengths)

    return max(c_lengths, key=lambda x: c_lengths[x])


def brute(limit):
    """
    takes about 32 secs
    """
    c_lengths = {s: collatz_length(s) for s in range(1, limit+1)}
    return max(c_lengths, key=lambda x: c_lengths[x])


if __name__ == "__main__":
    arg = int(sys.argv[1])

    def main():
        # print brute(arg)
        print bit_smarter(arg)

    cProfile.run('main()')
