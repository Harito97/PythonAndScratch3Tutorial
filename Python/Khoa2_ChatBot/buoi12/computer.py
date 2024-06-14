import pyttsx3
engine = pyttsx3.init()

def response(text):
    computer_text = "Sorry, I don't understand.\n"
    if 'hello' in text:
        computer_text = "Hello.\n"
    elif 'name' in text:
        computer_text = "My name's Harito.\n"
    return computer_text
    # import time 
    # do st ...

 
def speak(text):
    engine.say(text)
    engine.runAndWait()
