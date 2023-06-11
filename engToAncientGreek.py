english_text = input("Enter the English text to be converted to Ancient Greek: ")

# Define a dictionary with the character mapping
greek_map = {
    'a': 'α',
    'b': 'β',
    'c': 'ψ',
    'd': 'δ',
    'e': 'ε',
    'f': 'φ',
    'g': 'γ',
    'h': 'η',
    'i': 'ι',
    'j': 'ξ',
    'k': 'κ',
    'l': 'λ',
    'm': 'μ',
    'n': 'ν',
    'o': 'ο',
    'p': 'π',
    'q': 'θ',
    'r': 'ρ',
    's': 'σ',
    't': 'τ',
    'u': 'υ',
    'v': 'ω',
    'w': 'ω',
    'x': 'χ',
    'y': 'υ',
    'z': 'ζ',
    ' ': ' '
}

# Convert the English text to Ancient Greek using the character mapping
greek_text = ''
for char in english_text:
    if char.lower() in greek_map:
        greek_text += greek_map[char.lower()]
    else:
        greek_text += char

# Print the result
print("The Ancient Greek equivalent is: ", greek_text)
