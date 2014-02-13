import sys

arg = int(sys.argv[1])

def generateNDigitLimitNumber(digits,isHighest):
    number = '1'
    numberToAppend = '0'
    if isHighest:
        number = '9'
        numberToAppend = '9'
    digit = 0
    while digit < (digits-1):
        number += numberToAppend
        digit += 1
    return number


def calculatePalindromes(startPalindromeHalf,digits):
    palindrome = int(startPalindromeHalf + startPalindromeHalf[::-1])
    palindromes = [palindrome]
    firstHalf = startPalindromeHalf
    firstHalfInt = int(startPalindromeHalf)
    while len(firstHalf) <= digits:
        firstHalfInt += 1
        firstHalf = str(firstHalfInt)
        palindrome = int(firstHalf + firstHalf[::-1])
        palindromes += [palindrome]
    palindromes.pop()
    return palindromes

def generatePalindromes(digits):
    startHalf = generateNDigitLimitNumber(digits,False);
    return calculatePalindromes(startHalf, digits)

def calculateHighestBiProductInSequence(sequence,digits):
    highestFactor = int(generateNDigitLimitNumber(digits,True))
    firstFactor = highestFactor
    for number in sequence[::-1]:
        while len(str(firstFactor))==digits:
            if number%firstFactor == 0:
                secondFactor = number/firstFactor
                if (len(str(secondFactor))==digits):
                    print 'First factor is ' + str(firstFactor)
                    print 'Second factor is ' + str(secondFactor)
                    return number
            firstFactor -= 1
        firstFactor = highestFactor
                

print 'Calculating palindrome number with ' + str(arg) + ' digits...'
palindromes = generatePalindromes(arg)
print palindromes
print '...done!'

print 'Calculating highest palindrome number with a product of two ' + str(arg) + ' digit numbers...'
highestPalindrome = calculateHighestBiProductInSequence(palindromes,arg)
print highestPalindrome
print '...done!'


