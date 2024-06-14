import pyttsx3
# Với macOS chip M thì sử dụng lệnh: pip install py3-tts
# Cho máy macOS chip M: pip install pyobjc==9.0.1

engine = pyttsx3.init()

def response(text:str):
    computer_text = "Sorry, I don't understand.\n"
    if 'hello' in text:
        computer_text = "Hello.\n"
    elif 'name' in text:
        computer_text = "My name's Harito.\n"
    return computer_text
    # import time 
    # do st ...

 
def speak(text:str):
    engine.say(text)
    engine.runAndWait()
