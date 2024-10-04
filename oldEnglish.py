modern_to_old_english = {
    "hello": "hāl",
    "world": "weoruld",
    "friend": "freond",
    "good": "gōd",
    "day": "dæg",
    "morning": "morgen",
    "night": "niht",
    "love": "lufu",
    "king": "cyning",
    "queen": "cwēn"
}

def translate_to_old_english(sentence):
    words = sentence.lower().split()
    
    translated_sentence = []
    for word in words:
        if word in modern_to_old_english:
            translated_sentence.append(modern_to_old_english[word])
        else:
            translated_sentence.append(word)
    
    return ' '.join(translated_sentence)

if __name__ == "__main__":
    sentence = input("Enter a sentence to translate to Old English: ")
    translated = translate_to_old_english(sentence)
    print("Old English Translation:", translated)
