import openai
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import time
import googletrans
import speech_recognition
import gtts
import playsound


recognizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print("speak now")
    voice = recognizer.listen(source,0,8)
    text = recognizer.recognize_google(voice,language="hi")
    print(text)
# print(googletrans.LANGUAGES)
    translator = googletrans.Translator()
    translation = translator.translate(text,dest="en")
# print(translation.text)
    a = translation.text
    print(a)
    converted_audio = gtts.gTTS(translation.text, lang="en")
# converted_audio.save("chatgpt.mp3")
# playsound.playsound("hello.mp3")
# music_dir = 'D:\\Jarvis Voice Assistant'
# songs = os.listdir(music_dir)
# print(songs)
# os.startfile(os.path.join(music_dir, songs[7]))

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


openai.api_key="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"

model_engine = "text-davinci-003"
prompt = a

completion = openai.Completion.create(
    engine = model_engine,
    prompt = prompt,
    max_tokens = 1024,
    n =1,
    stop = None,
    temperature = 0.5,
)

response = completion.choices[0].text
print(response)
# speak(response)

# print(googletrans.LANGUAGES)
translator = googletrans.Translator()
translation = translator.translate(response,dest="hi")
print(translation.text)
converted_audio = gtts.gTTS(translation.text, lang="hi")
converted_audio.save("chatgpt.mp3")
# playsound.playsound("hello.mp3")
music_dir = 'D:\\Jarvis Voice Assistant'
songs = os.listdir(music_dir)
# print(songs)
os.startfile(os.path.join(music_dir, songs[4]))


