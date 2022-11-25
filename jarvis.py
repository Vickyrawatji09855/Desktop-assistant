import pyttsx3
import datetime


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishes():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    elif hour>=18 and hour<22:
        speak("Good Evening!")
    else:
        speak("Good Night!")

    speak("I am Jarvis Sir. Please tell me How may i help you")


if __name__ == "__main__":
    wishes()
    speak(" and sorry but Venom is a BC person")