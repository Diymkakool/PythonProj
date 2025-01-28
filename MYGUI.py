import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Импортируем Pillow для работы с изображениями
import time

root = tk.Tk()
root.title("skibidi tolet")
root.geometry("600x500")

def toggle_button():
    if checkbox_var.get():
        button.config(state="normal")  # Активируем кнопку
    else:
        button.config(state="disabled")  # Деактивируем кнопку

def display_text():
    # Показываем временное сообщение
    label.config(text="Обрабатывается...")
    root.update()  # Обновляем интерфейс, чтобы сообщение сразу отобразилось
    time.sleep(2)  # Задержка на 2 секунды (ожидание)

    # Получаем текст и обновляем метку
    user_input = entry.get()
    if user_input.strip():  # Проверяем, что текст не пустой
        label.config(text=f"Вы ввели: {user_input}")
    else:
        messagebox.showinfo("Пожалуйста, введите текст.", "Пожалуйста, введите текст.")
        label.config(text="Enter text")

def on_press(event):
    """Сохраняем начальную позицию мыши при нажатии на картинку."""
    global start_x, start_y  # Объявляем переменные как глобальные
    start_x = event.x
    start_y = event.y

def on_motion(event):
    """Перемещаем картинку в зависимости от движения мыши."""
    global start_x, start_y  # Объявляем переменные как глобальные
    dx = event.x - start_x
    dy = event.y - start_y
    new_x = image_label.winfo_x() + dx
    new_y = image_label.winfo_y() + dy
    image_label.place(x=new_x, y=new_y)  # Перемещаем изображение

    # Обновляем начальные координаты
    start_x = event.x
    start_y = event.y
    
label = tk.Label(root, text="I will predict your number", font=("Comic Sans MS", 14))
label.pack(pady=10)

label = tk.Label(root, text="Enter text below", font=("Arial", 14))
label.pack(pady=15)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)

button = tk.Button(root, text="Enter text", font=("Arial", 14), command=display_text, state="disabled")
button.pack(pady=10)

checkbox_var = tk.BooleanVar(value=False)  # Изначально галочка не отмечена

image = Image.open("image.png")  # Загружаем изображение
image = image.resize((32, 72))  # Изменяем размер изображения (200x200)
photo = ImageTk.PhotoImage(image)  # Конвертируем в формат, поддерживаемый tkinter

image_label = tk.Label(root, image=photo)
image_label.pack(pady=1)

image_label.bind("<ButtonPress-1>", on_press)  # Начало перетаскивания
image_label.bind("<B1-Motion>", on_motion)  # Движение мыши (перемещение)

# Добавляем чекбокс
checkbox = tk.Checkbutton(root, text="I agree to the Terms and Conditions", font=("Arial", 12), variable=checkbox_var, command=toggle_button)
checkbox.pack(pady=10)


root.mainloop()