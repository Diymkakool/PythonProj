import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Импортируем Pillow для работы с изображениями
import time

def toggle_button():
    """Активируем или деактивируем кнопку в зависимости от состояния галочки."""
    if checkbox_var.get():
        button.config(state="normal")  # Активируем кнопку
    else:
        button.config(state="disabled")  # Деактивируем кнопку

def display_text():
    """Показать текст с задержкой после нажатия кнопки."""
    # Показываем временное сообщение
    label.config(text="Обрабатывается...")
    root.update()  # Обновляем интерфейс, чтобы сообщение сразу отобразилось
    time.sleep(2)  # Задержка на 2 секунды (ожидание)

    # Получаем текст и обновляем метку
    user_input = entry.get()
    if user_input.strip():  # Проверяем, что текст не пустой
        label.config(text=f"Вы ввели: {user_input}")
    else:
        label.config(text="Пожалуйста, введите текст.")
    messagebox.showinfo("Завершено", "Ваш текст обработан!")

# Функция для перетаскивания изображения
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

# Создаем главное окно
root = tk.Tk()
root.title("Текстовый ввод с изображением")
root.geometry("350x350")

# Загрузка изображения с использованием Pillow
image = Image.open("image.png")  # Загружаем изображение
image = image.resize((200, 200))  # Изменяем размер изображения
photo = ImageTk.PhotoImage(image)  # Конвертируем в формат для tkinter

# Добавляем метку с изображением
image_label = tk.Label(root, image=photo)
image_label.place(x=50, y=50)  # Устанавливаем начальную позицию изображения

# Привязываем события мыши для перетаскивания
image_label.bind("<ButtonPress-1>", on_press)  # Начало перетаскивания
image_label.bind("<B1-Motion>", on_motion)  # Движение мыши (перемещение)

# Добавляем метку
label = tk.Label(root, text="Введите текст ниже и поставьте галочку:", font=("Arial", 12))
label.pack(pady=10)

# Поле для ввода текста
entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)

# Переменная для галочки
checkbox_var = tk.BooleanVar(value=False)  # Изначально галочка не отмечена

# Добавляем чекбокс
checkbox = tk.Checkbutton(root, text="Я подтверждаю", font=("Arial", 12), variable=checkbox_var, command=toggle_button)
checkbox.pack(pady=10)

# Кнопка для отображения текста
button = tk.Button(root, text="Показать текст", font=("Arial", 14), command=display_text, state="disabled")
button.pack(pady=10)

# Запуск приложения
root.mainloop()
