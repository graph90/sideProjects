def main():
    print "This program converts a sequence of ASCII codes into a string of text."
    print

    # get the message to encode
    inString = raw_input("Please enter the ASCII-encoded message: ")

    # loop through each substring and build Unicode message
    message = ""
    for numStr in inString.split():
        codeNum = int(numStr) # convert digits to a number
        message = message + chr(codeNum) # concatentate character to message

    print "The decoded message is:", message

main()