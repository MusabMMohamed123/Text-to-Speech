from tkinter import *
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 140)
engine.setProperty('volume', 1.0)


root = Tk()
root.geometry("640x480")
root.configure(bg="white")
root.title("Musab's Project - Text to Speak")

background_image = PhotoImage(file="img_1.png")
bg_label = Label(root, image=background_image).pack()

Label(root, text = "Text to Speech", font = "Perpetua 20 bold", fg = "black", bg = "white").pack()
Label(root, text = "Enter Text",  font = "Perpetua 15 bold", fg = "black", bg= "white").place(x=15, y=60)

Msg = StringVar()
entry_field = Entry(root, fg = "Black", font="Calibri 18 bold", textvariable=Msg, width=50, bg= "white")
entry_field.place(x=15, y=100)

def Text_to_speech():
    Message = entry_field.get()
    engine.say(Message)
    engine.runAndWait()

def Exit():
    root.destroy()

def Clear():
    Msg.set("")

Button(root, text="PLAY", font="Calibri 15 bold", command= Text_to_speech, width=4,).place(x=15, y=140)

Button(root, font="Calibri 15 bold", text= "EXIT", width=4, command= Exit,).place(x=547, y=140)

Button(root, font="Calibri 15 bold", text="CLEAR", width=6, command= Clear).place(x= 257, y=140)


root.mainloop()



