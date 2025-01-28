import tkinter as tk
from tkinter import messagebox

def on_click(button_text):
    if button_text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Ошибка", "Некорректное выражение!")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

# Создаем окно
root = tk.Tk()
root.title("Калькулятор")

# Поле ввода
entry = tk.Entry(root, width=20, font=("Arial", 18), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Кнопки
buttons = [
    "3", "3", "3", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

row = 1
col = 0

for button_text in buttons:
    button = tk.Button(
        root, text=button_text, font=("Arial", 18), width=4, height=2,
        command=lambda text=button_text: on_click(text)
    )
    button.grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Запуск приложения
root.mainloop()
