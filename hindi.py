import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


speak("Bhanu Acha Ladka h")