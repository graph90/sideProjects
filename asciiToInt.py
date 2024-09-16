def main():
    print ("This program converts a sequence of ASCII codes into a string of text.")
    inString = input("Please enter the ASCII-encoded message: ")
    message = ""
    for numStr in inString.split():
        codeNum = int(numStr)
        message = message + chr(codeNum)

    print ("The decoded message is:", message)

main()
