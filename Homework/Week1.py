## -----------------------------------
# Part 1: Binary to Decimal converter

print "Part 1: "

def stringChecker(x):
    # return false if x isn't 16 bits or contains anything other than 1 or 0
    print len(x)
    if ((len(x)) != 16) or ( not( set([1,0]) and set(x))):
        print "not a valid 16-bit binary string"
        return False
    else:
        return True

def binToDecimal(binString):
    # Validate input
    if stringChecker(binString) == True:
        # init final value to be returned
        finalValue = 0
        exponent = 15
        # loop over each element of the binary string, if it's a 1, use WPN to
        # derive its value and add it to finalValue
        for n in binString:
            # Summation of Weighted Positional Notation addition of parts
            # n is string containing either 0 or 1
            # exponent iterates down
            if int(n)==0:
                continue
            if int(n)==1:
                finalValue = finalValue + (2**(exponent))
            exponent = exponent - 1
        return finalValue


print binToDecimal(raw_input('Please input any 16-bit binary number: '))

## ----------------------------------
# PART 2 - Decimal Hexadecimal converter


print "Part 2"

def letterAdder(tempList):
    for i in tempList:
        if i in hexDict.keys():
            z = tempList.index(i)
            y = hexDict[i]
            backwardsList.insert(z,y)
            backwardsList.remove(i)
            # list is still backwards at this point.

userInput = 0

while True:
    # Gets user input and validates it is an integer
    # Technically not required but a good idea nonetheless
    try:
        userInput = int(input("Enter an integer: "))
    except ValueError:
        print "Not a valid integer!"
        continue
    else:
        break

backwardsList = []
hexDict = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}


while True:
    backwardsList.append(userInput%16)
    # print "The remainder of " + str(userInput) + " / 16 = " + str(userInput%16)
    userInput = (userInput/16)
    # print "Now we're working with " + str(userInput)
    if (userInput/16)==0:
        backwardsList.append(userInput%16)
        # print (str(backwardsList)) + " are the numbers we're working with"
        # print "Now we need to convert 10 - 15 to A - F"
        break



letterAdder(backwardsList)

finalList = []

for i in reversed(backwardsList):
    finalList.append(i)

print "Hexadecimal value for that integer is :"
for i in finalList:
    print i,
