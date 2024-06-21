import pyttsx3
# Với macOS chip M thì sử dụng lệnh: pip install py3-tts
# Cho máy macOS chip M: pip install pyobjc==9.0.1

engine = pyttsx3.init()

newVoiceRate = 145
engine.setProperty('rate', newVoiceRate)
engine.setProperty('volume', 1.0)

def response(text:str) -> str:
    computer_text = "Sorry, I don't understand."
    if 'hello' in text:
        computer_text = "Hello."
    elif 'name' in text:
        computer_text = "My name's Harito."
    return computer_text
    # import time 
    # do st ...

 
def speak(text:str):
    engine.say(text)
    engine.runAndWait()
