import sys

def fibonacciSum(previous,current):
    return previous+current 

def fibonacciSequence(limit):
    sequence = [1, 2]
    while sequence[-1] < limit:
        sequence += [fibonacciSum(sequence[-2],sequence[-1])]
    sequence.pop()
    return sequence

def trimOddNumbers(sequence):
    evenSequence = []
    for number in sequence:
        if number%2 == 0:
            evenSequence += [number]
    return evenSequence


limit = int(sys.argv[1])

print 'Calculating fibonacci sequence under ' + str(limit) + '...'
fibSequence = fibonacciSequence(limit)
print fibSequence
print '...done!'

print 'Trimming odd numbers from fibonacci sequence...'
evenSequence = trimOddNumbers(fibSequence)
print evenSequence
print '...done!'

print 'Sum of even numbers is ' + str(sum(evenSequence))

