import sys

def calculateMultiples(factor,limit):
    multiples = [factor]
    currentMultiple = factor
    while currentMultiple<(limit - factor):
        currentMultiple = currentMultiple + factor
        multiples += [currentMultiple]
    return multiples


limit = int(sys.argv[1])

print 'Calculating multiples of 3 under ' + str(limit) + '...'
multiplesOfThree = calculateMultiples(3,limit)
print multiplesOfThree
print '...done!'

print 'Calculating multiples of 5 under ' + str(limit) + '...'
multiplesOfFive = calculateMultiples(5,limit)
print multiplesOfFive
print '...done!'

print 'Removing duplicate entries...'
for multiple in multiplesOfThree:
    if multiple in multiplesOfFive:
        multiplesOfFive.pop(multiplesOfFive.index(multiple))
print multiplesOfFive
print '...done!'

multipleSum = sum(multiplesOfThree) + sum(multiplesOfFive)

print 'Sum of multiples is ' + str(multipleSum)
