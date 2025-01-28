import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

root = tk.Tk()
root.title("best program award of 2025")
root.geometry("300x300")

def display_text(): # display the definition of what you just typed
    global unlockentry
    user_input = entry.get()
    if user_input == ("quarter"):
        label.config(text="4")
    if user_input == ("half"):
        label.config(text="0.5")
    if user_input == ("fortnight"):
        entry.destroy()
        button.destroy()
        label.config(text="Enter code")
        unlockentry = tk.Entry(root, font=("Arial", 14))
        unlockentry.pack(pady=20)
        unlock = tk.Button(root, text="Unlock", font=("Arial", 14), command=unlocker)
        unlock.pack(pady=20)

def unlocker(): # secret unlock
    unlock_input = unlockentry.get()
    if unlock_input == "491hh3jjs":
        label.config(text="Unlocked!")
        os.startfile('D:/PythonProj/secret.jpg')
    else:
        label.config(text="Incorrect!")

label = tk.Label(root, text="How many parts are in a...", font=("Comic Sans MS", 16))
label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)

button = tk.Button(root, text="Enter text", font=("Arial", 14), command=display_text)
button.pack(pady=10)

root.mainloop()