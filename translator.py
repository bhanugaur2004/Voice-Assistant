import googletrans
import speech_recognition
import gtts
# import playsound
import os

input_lang = "en"
output_lang = "hi"

recognizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print("speak now")
    voice = recognizer.listen(source,0,8)
    text = recognizer.recognize_google(voice,language=input_lang)
    print(text)

# print(googletrans.LANGUAGES)
translator = googletrans.Translator()
translation = translator.translate(text,dest=output_lang)
print(translation.text)
converted_audio = gtts.gTTS(translation.text, lang=output_lang)
converted_audio.save("hello.mp3")
# playsound.playsound("hello.mp3")
music_dir = 'D:\\Jarvis Voice Assistant'
songs = os.listdir(music_dir)
# print(songs)
os.startfile(os.path.join(music_dir, songs[2]))




# elif 'play music' in query:
#             music_dir = 'D:\\Songs'
#             songs = os.listdir(music_dir)
#             print(songs)
#             speak("Playing the song")
#             os.startfile(os.path.join(music_dir, songs[5]))