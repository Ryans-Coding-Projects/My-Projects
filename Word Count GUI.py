#This program is used to find the word count in a text

from tkinter import * #Import required libraries
from tkinter import Tk

window = Tk() #Create an instance of tkinter

window.geometry("700x350")
window.title("Word Count")


def update(event):
    label.config(text = "Total Characters: " + str(len(text.get("1.0", "end-1c"))))

text = Text(window, width=50, height = 10, font =("Calibri, 14"))
text.pack()

label = Label(window, text = "", justify=CENTER, font = ("Calibri, 11"))
label.pack()

text.bind("<KeyPress>", update)
text.bind("<KeyRelease>", update)

window.mainloop()
