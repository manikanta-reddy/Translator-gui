from googletrans import Translator
import pyttsx3
import tkinter as tk

root = tk.Tk()
root.geometry("800x400")
root.title("Translator by manikanta")
en = tk.StringVar()


def trans():
    global speech
    x = en.get()
    translator = Translator()
    trans = translator.translate(x)
    speech = trans.text
    T.insert("end", speech)


def speak():
    engine = pyttsx3.init()
    engine.say(speech)
    engine.runAndWait()


label = tk.Label(root, text="Enter Text:").grid(row=0, column=0)
entry = tk.Entry(root, textvariable=en).grid(row=0, column=1, ipady=20, ipadx=150)
tb = tk.Button(root, text="Translate", fg="black", command=trans).grid(row=1, column=0, padx=10, pady=10)
sb = tk.Button(root, text="Speak", fg="black", command=speak).grid(row=1, column=1, padx=10, pady=10)
T = tk.Text(root, height=30, width=30)
T.grid(row=2, column=0, padx=10, pady=10)
root.mainloop()
