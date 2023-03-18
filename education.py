import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Debuggers")
root.geometry("900x450+200+200")
root.resizable(False,False)
root.configure(bg="#3e8187")



#icon
image_icon=PhotoImage(file="speaker logo.png")
root.iconphoto(False,image_icon)

# Top Frame
Top_frame = Frame(root,bg="#154c79", width=900, height=100)
Top_frame.place(x=0,y=0)


Label(Top_frame,text="Education", font="arial 36 bold", bg="#154c79", fg="white").place(x=350,y=20)


################
Top_frame = Frame(root,bg="#2e2e2d", width=250, height=500)
Top_frame.place(x=0,y=100)

btn=Button(root,text="Speak", width=10, font="arial 14 bold", bg="#39c790")
btn.place(x=400,y=160)
btn2=Button(root,text="Standard", width=10, font="arial 14 bold", bg="#39c790")
btn2.place(x=650,y=160)
btn3=Button(root,text="Sleep", width=10, font="arial 14 bold", bg="#39c790")
btn3.place(x=400,y=280)
btn4=Button(root,text="Exit", width=10, font="arial 14 bold", bg="#39c790")
btn4.pack()
btn4.place(x=650,y=280)


root.mainloop()
