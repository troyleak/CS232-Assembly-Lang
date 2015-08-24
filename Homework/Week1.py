def stringChecker(x):
    # return false if x isn't 16 bits or contains anything other than 1 or 0
    print len(x)
    if ((len(x)) != 16) or ( not( set([1,0]) and set(x))):
        print "not a valid string"
        return False
    else:
        print "valid string"
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
            print "checking index " + str(exponent) + " for a 1"
            if int(n)==0:
                print "index " + str(exponent) + " is " + n + ", doing nothing"
            if int(n)==1:
                print "adding " + str(2**(exponent)) + " at index " + str(exponent)
                finalValue = finalValue + (2**(exponent))
            exponent = exponent - 1
        return finalValue


print binToDecimal(raw_input('Please input any 16-bit binary number: '))
