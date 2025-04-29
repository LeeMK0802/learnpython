from tkinter import *
import pyshorteners

mainWindow = Tk()
mainWindow.geometry("500x500")

def shorten():
    if shorty.get():
        shorty.delete(0, END)

    if my_entry.get():
        url = pyshorteners.Shortener().tinyurl.short(my_entry.get())
        shorty.insert(END, url)

        print(pyshorteners.Shortener().tinyurl.expand(url))

my_label = Label(mainWindow, text="Enter link to shorten", font=('Helvatica',34))
my_label.pack(pady=20)

my_entry = Entry(mainWindow, font=("Helvatica", 24))
my_entry.pack(pady=20)

my_button = Button(mainWindow, command= shorten,text="Shortened Link", font=("Helvetica", 14))
my_button.pack(pady=20)

shorty_label = Label(mainWindow, text="Shortened Link", font=("Helvertica", 14))
shorty_label.pack(pady=50)

shorty = Entry(mainWindow, font=("Helvetica", 22), justify=CENTER, width=30, bd=0, bg="systembuttonface")
shorty.pack(pady=10)

mainWindow.mainloop()