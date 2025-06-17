import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia

r = sr.Recognizer()

def speak(command):
    engine = pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Change index to select different voice
    engine.setProperty('rate', 150)  # Speed of speech
    engine.say(command)
    engine.runAndWait()

def commands():
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Listening... Ask Now!")
            audioin = r.listen(source)
            my_text = r.recognize_google(audioin)
            my_text = my_text.lower()
            print("You said:", my_text)
    except Exception as e:
        print("Error in capturing the audio:", str(e))


speak("Hello there! I am your AI assistant built by Somnath Mukherjee. How can I help you today?")
