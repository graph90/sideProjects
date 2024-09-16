import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
with open('input.txt', 'r') as file:
    text = file.read().replace('\n', '')

engine.save_to_file(text, 'output.mp3')
engine.runAndWait()
