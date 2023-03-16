import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os

root = Tk()
root.title("Speech Recognition")
root.geometry("900x450+200+200")
root.resizable(False,False)
root.configure(bg="#7EA8E4")



#icon
image_icon=PhotoImage(file="speaker logo.png")
root.iconphoto(False,image_icon)

# Top Frame
Top_frame = Frame(root,bg="white", width=900, height=100)
Top_frame.place(x=0,y=0)

Logo = PhotoImage(file="speaker logo.png")
Label(Top_frame,image=Logo, bg="white").place(x=10,y=5)

Label(Top_frame,text="SPEECH TO TEXT", font="arial 36 bold", bg="white", fg="black").place(x=100,y=20)


################
text_area=Text(root,font="Roboto 20", bg="#FFF2F2", relief=GROOVE,wrap=WORD)
text_area.place(x=10,y=150,width=500,height=250)

Label(root,text="VOICE",font="arial 15 bold", bg="#7EA8E4", fg="Black").place(x=570,y=160)
Label(root,text="SPEED",font="arial 15 bold", bg="#7EA8E4", fg="black").place(x=750,y=160)


gender_combobox = Combobox(root,values=['Male', 'Female'],font="arial 14", state="r", width=10)
gender_combobox.place(x=550,y=200)
gender_combobox.set("Male")


speed_combobox = Combobox(root,values=['Fast', 'Normal', 'Slow'],font="arial 14", state="r", width=10)
speed_combobox.place(x=730,y=200)
speed_combobox.set("Normal")

image_icon=PhotoImage(file='speak.png')
btn=Button(root,text="SPEAK", width=130, font="arial 14 bold", bg="#39c790", image=image_icon, compound=LEFT)
btn.place(x=650,y=280)



root.mainloop()
