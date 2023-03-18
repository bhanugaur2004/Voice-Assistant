import googletrans
import speech_recognition
import gtts
# import playsound
import os

def transhien():
    recognizer = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("speak now")
        voice = recognizer.listen(source,0,8)
        text = recognizer.recognize_google(voice,language="hi")
        print(text)

    # print(googletrans.LANGUAGES)
    translator = googletrans.Translator()
    translation = translator.translate(text,dest="en")
    print(translation.text)
    converted_audio = gtts.gTTS(translation.text, lang="en")
    converted_audio.save("hello.mp3")
    # playsound.playsound("hello.mp3")
    music_dir = 'D:\\Jarvis Voice Assistant'
    songs = os.listdir(music_dir)
    # print(songs)
    os.startfile(os.path.join(music_dir, songs[7]))

# transhien()

def transenhi():
    recognizer = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("speak now")
        voice = recognizer.listen(source,0,8)
        text = recognizer.recognize_google(voice,language="en")
        print(text)

    # print(googletrans.LANGUAGES)
    translator = googletrans.Translator()
    translation = translator.translate(text,dest="hi")
    print(translation.text)
    converted_audio = gtts.gTTS(translation.text, lang="hi")
    converted_audio.save("hello.mp3")
    # playsound.playsound("hello.mp3")
    music_dir = 'D:\\Jarvis Voice Assistant'
    songs = os.listdir(music_dir)
    # print(songs)
    os.startfile(os.path.join(music_dir, songs[7]))

# transenhi()