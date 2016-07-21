import sys
import cProfile


base_str = [
    '',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
    'ten',
    'eleven',
    'twelve',
    'thirteen',
    'fourteen',
    'fifteen',
    'sixteen',
    'seventeen',
    'eighteen',
    'nineteen',
    'twenty'
]

decimal_order = {
    1: [None,
        None,
        'twenty',
        'thirty',
        'forty',
        'fifty',
        'sixty',
        'seventy',
        'eighty',
        'ninety'],
    2: 'hundred',
    3: 'thousand'
}


def letters_for(n):
    letters = ''
    n_str = str(n)
    first_two_digits = int(n_str[-2:])
    if first_two_digits <= 20:
        letters = base_str[first_two_digits]
    else:
        first = int(n_str[-1])
        second = int(n_str[-2])
        first_str = ''
        if first:
            first_str = base_str[first]
        letters = ''.join([decimal_order[1][second], first_str])

    for i, c in enumerate(n_str[-3::-1]):
        number = int(c)
        if first_two_digits == 0:
            letters = ''.join([base_str[number],
                               decimal_order[i+2]])
        elif number != 0:
            letters = ''.join([base_str[number],
                               decimal_order[i+2],
                               'and',
                               letters])
    return letters


def brute(arg):
    if arg <= 20:
        return len(''.join(base_str[1:arg+1]))
    letters = ''.join(base_str[1:])

    for n in range(20, arg):
        letters = ''.join([letters, letters_for(n+1)])

    print letters
    return len(letters)

if __name__ == "__main__":
    arg = int(sys.argv[1])

    def main():
        print brute(arg)

    cProfile.run('main()')
