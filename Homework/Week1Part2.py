###########################################
# Assignment 2 is similar, so I'm lumping it into one file. I'll break them down
# later, I'm sure.

def letterAdder(tempList):
    for i in tempList:
        if i in hexDict.keys():
            print "Replacing " + str(i) + " with " + hexDict[i]
            z = tempList.index(i)
            y = hexDict[i]
            finalList.insert(z,y)
            finalList.remove(i)
            print finalList

userInput = 0

while True:
    try:
        userInput = int(input("Enter an integer: "))
    except ValueError:
        print "Not an integer!"
        continue
    else:
        print "That is a valid integer"
        break

finalList = []
hexDict = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}


while True:
    finalList.append(userInput%16)
    print "Appending " + str(userInput%16) + " to finalList"
    userInput = (userInput/16)
    print str(userInput)
    if (userInput/16)==0:
        finalList.append(userInput%16)
        print (str(finalList)) + " are the numbers we're working with"
        print "Now we need to convert 10 - 15 to A - F"
        break



letterAdder(finalList)
