from tkinter import *
import googletrans
import textblob
from tkinter import ttk, messagebox

mainWindow = Tk()
mainWindow.geometry("880x300")

def translate_it():
    translate_text.delete(1.0, END)
    try:
        for key, value in languages.items():
            if(value == original_combo.get()):
                from_language_key = key
        
        for key, value in languages.items():
            if(value == translated_combo.get()):
                to_language_key = key
        
        words = textblob.TextBlob(original_text.get(1.0, END))
        words = words.translate(from_lang = from_language_key, to = to_language_key)
        translate_text.insert(1.0, words)
    except Exception as e:
        messagebox.showerror("Translator", e)

def clear():
    original_text.delete(1.0, END)
    translate_text.delete(1.0, END)

languages = googletrans.LANGUAGES
language_list = list(languages.values())

original_text = Text(mainWindow, height= 10, width=40)
original_text.grid(row=0, column=0, pady=20, padx=10)

translate_button = Button(mainWindow,text="Translate!", font=("Helvetica", 24), command="translate_it")
translate_button.grid(row=0, column=1, padx=10)

translate_text = Text(mainWindow,height=10,width=40)
translate_text.grid(row=0, column=2, pady=20,padx=10)

original_combo = ttk.Combobox(mainWindow, width=50, values=language_list)
original_combo.current(20)
original_combo.grid(row=1,column=0)

translated_combo = ttk.Combobox(mainWindow, width=50, values=language_list)
translated_combo.current(26)
translated_combo.grid(row=1, column=2)


clear_button = Button(mainWindow, text="Clear", command=clear)
clear_button.grid(row=2, column=1)

mainWindow.mainloop()