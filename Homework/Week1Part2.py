def letterAdder(tempList):
    for i in tempList:
        if i in hexDict.keys():
            # print "Replacing " + str(i) + " with " + hexDict[i]
            z = tempList.index(i)
            y = hexDict[i]
            backwardsList.insert(z,y)
            backwardsList.remove(i)
            # list is still backwards at this point.

userInput = 0

while True:
    try:
        userInput = int(input("Enter an integer: "))
    except ValueError:
        print "Not an integer!"
        continue
    else:
        # print "That is a valid integer"
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
