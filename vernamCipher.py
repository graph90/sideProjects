def encrypt(text, key):
    # Initializing cipherText
    cipherText,cipher  = "", []
    # which stores the sum of corresponding no.'s |  of plainText and key.
    for i in range(len(key)):
        cipher.append(ord(text[i]) - ord('A') + ord(key[i])-ord('A'))
    # If the sum is greater than 25 |  subtract 26 from it |  and store that resulting value
    for i in range(len(key)):
        if cipher[i] > 25:
            cipher[i] = cipher[i] - 26
    # Converting the no.'s into integers | Convert these integers to corresponding |  characters and add them up to cipherText
    for i in range(len(key)):
        x = cipher[i] + ord('A')
        cipherText += chr(x)
    return cipherText

def decrypt(s, key):
    plainText,plain  = "", []
    # Running for loop for each character | subtracting and storing in the array
    for i in range(len(key)):
        plain.append(ord(s[i]) - ord('A') - (ord(key[i]) - ord('A')))
    # If the difference is less than 0 | add 26 and store it in the array.
    for i in range(len(key)):
        if (plain[i] < 0):
            plain[i] = plain[i] + 26
    # Converting int to corresponding char | add them up to plainText
    for i in range(len(key)):
        x = plain[i] + ord('A')
        plainText += chr(x)
    # Returning plainText
    return plainText

plainText = "Hello"
key = "MONEY"
encryptedText = encrypt(plainText.upper(), key.upper())
print("Cipher Text - " + encryptedText)
print("Message - " + decrypt(encryptedText, key.upper()))
 