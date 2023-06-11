import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Set the voice properties
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # change the index to use a different voice

# Read the text file
with open('input.txt', 'r') as file:
    text = file.read().replace('\n', '')

# Convert text to speech and save as an audio file
engine.save_to_file(text, 'output.mp3')
engine.runAndWait()
