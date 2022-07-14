import pyttsx3
import pyaudio
import speech_recognition
import datetime

MIKU = pyttsx3.init()
MIKU.setProperty('voice', 'com.apple.speech.synthesis.voice.kyoko')

def speak(audio):
    print("MIKU: " + audio)
    MIKU.say(audio)
    MIKU.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S %p")
    speak("It's " + str(Time))

def welcome():
    speak("Yahoo Megumin-chan")
    time()

def command():
    c = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        c.pause_threshold = 2 # time between 2ms different commands
        audio = c.listen(source)
    try:
        query = c.recognize_google(audio, language = 'en-US')
        print("Customer: " + query)
    except speech_recognition.UnknownValueError:
        print("Sorry I can't hear you! Try a gain!")
        query = str(input('Your order is: '))
    return query

welcome()

while True:
    query = command().lower()
    if "hello" in query:
        speak("Yahoo")
    elif "time" in query:
        time()
    elif "quit" in query:
        speak("Bye! Have a great time")
        break

