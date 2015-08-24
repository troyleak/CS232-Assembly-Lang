###########################################
# Assignment 2 is similar, so I'm lumping it into one file. I'll break them down
# later, I'm sure.
userInput = 0
while True:
    try:
        userInput = int(input("Enter something: "))
    except ValueError:
        print "Not an integer!"
        continue
    else:
        print "Integer found!"
        break

while True:
    # Creates a list with decimal values representing hex values
    # Need to create a function to convert 10-15 to A-F
    finalList = []
    finalList.append(integer%16)
    print "Appending " + str(integer%16) + " to finalList"
    integer = (integer/16)
    print str(integer)
    if (integer/16)==0:
        print "Exiting loop"
        break
