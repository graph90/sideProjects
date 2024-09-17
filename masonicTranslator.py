def masonic_translator(text):
    masonic_symbols = {
        "G": "George Washington",
        "S&C": "Strength & Courage",
        "G. W.": "George Washington",
        "T.B.": "Three Brothers",
        "JW": "Junior Warden",
        "SW": "Senior Warden",
        "WM": "Worshipful Master"
    }

    deciphered_text = ""
    words = text.split()

    for word in words:
        if word.upper() in masonic_symbols:
            deciphered_text += masonic_symbols[word.upper()] + " "
        else:
            deciphered_text += word + " "

    return deciphered_text.strip()

input_msg = "WM S&C T.B. JW G. W."
deciphered_msg = masonic_translator(input_msg)
print("Deciphered Message:", deciphered_msg)
