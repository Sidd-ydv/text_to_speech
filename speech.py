import pyttsx3

while True:
    text_speech = pyttsx3.init()
    text = input("write to listen: ")
    if text == "Q":
        break
    text_speech.say(text)
    text_speech.runAndWait()
print("program has been ended")
