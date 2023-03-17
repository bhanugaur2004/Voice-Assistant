import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os

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


Label(Top_frame,text="Admin Panel", font="arial 36 bold", bg="#154c79", fg="white").place(x=300,y=20)


################
Top_frame = Frame(root,bg="#2e2e2d", width=250, height=500)
Top_frame.place(x=0,y=100)


Label(root,text="Education",font="arial 24 bold", bg="#3e8187", fg="Black").place(x=350,y=160)
btn=Button(root,text="Open", width=10, font="arial 14 bold", bg="#39c790")
btn.place(x=600,y=160)
Label(root,text="Medical",font="arial 24 bold", bg="#3e8187", fg="black").place(x=350,y=230)
btn=Button(root,text="Open", width=10, font="arial 14 bold", bg="#39c790")
btn.place(x=600,y=230)
Label(root,text="Translator",font="arial 24 bold", bg="#3e8187", fg="black").place(x=350,y=300)
btn=Button(root,text="Open", width=10, font="arial 14 bold", bg="#39c790")
btn.place(x=600,y=300)






root.mainloop()
