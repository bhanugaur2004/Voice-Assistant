import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os
from tkinter import *
from PIL import ImageTk, Image
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


root = Tk()
root.title("Debuggers")
root.geometry("900x450+200+200")
root.resizable(False, False)
root.configure(bg="#3e8187")


# icon
image_icon = PhotoImage(file="speaker logo.png")
root.iconphoto(False, image_icon)

# Top Frame
Top_frame = Frame(root, bg="#154c79", width=900, height=100)
Top_frame.place(x=0, y=0)


Label(Top_frame, text="Voice Translator", font="arial 36 bold",
      bg="#154c79", fg="white").place(x=300, y=20)


################
Top_frame = Frame(root, bg="#2e2e2d", width=250, height=500)
Top_frame.place(x=0, y=100)

btn = Button(root, text="Hindi", width=10, font="arial 14 bold", bg="#39c790")
btn.place(x=300, y=160)

btn = Button(root, text="English", width=10,
             font="arial 14 bold", bg="#39c790")
btn.place(x=530, y=160)

img = Image.open("R.png")
img = img.resize((50, 50), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)

label = Label(root, image=img, bg="#3e8187")
label.pack()
label.place(x=450, y=150)

btn = Button(root, text="Speak", width=10, font="arial 14 bold", bg="#39c790", command=transhien)
btn.place(x=740, y=160)

btn = Button(root, text="Hindi", width=10, font="arial 14 bold", bg="#39c790")
btn.place(x=300, y=250)
btn = Button(root, text="English", width=10,
             font="arial 14 bold", bg="#39c790")
btn.place(x=530, y=250)
img1 = Image.open("a.png")
img1 = img1.resize((50, 50), Image.ANTIALIAS)
img1 = ImageTk.PhotoImage(img1)
label1 = Label(root, image=img1, bg="#3e8187")
label1.pack()
label1.place(x=450, y=250)

btn1 = Button(root, text="Speak", width=10, font="arial 14 bold", bg="#39c790",command=transenhi)
btn1.place(x=740, y=250)


root.mainloop()
