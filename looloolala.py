import tkinter as tk
import random

root = tk.Tk()
root.title("Guess the Number")
root.geometry("300x300")

random_num = random.randint(1, 100)

def guess():
    try:
        user_guess = int(entry.get())
        if user_guess < random_num:
            label.config(text="Random number > guessed")
        elif user_guess > random_num:
            label.config(text="Random number < guessed")
        else:
            label.config(text="You guessed it!")
    except ValueError:
        label.config(text="enter a number!!!!!!!!")


label = tk.Label(root, text="Guess the number", font=("Arial", 15))
label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)

button = tk.Button(root, text="Try", font=("Arial", 15), command=guess)
button.pack(pady=10)

root.mainloop()