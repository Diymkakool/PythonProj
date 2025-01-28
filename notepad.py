import tkinter as tk
from tkinter import filedialog, messagebox

def save_file():
    """Сохранить текст в файл."""
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")]
    )
    if file_path:
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(text_area.get("1.0", tk.END))  # Сохраняем весь текст из текстового поля
            messagebox.showinfo("Сохранение", "Файл успешно сохранён!")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось сохранить файл: {e}")

def open_file():
    """Открыть текстовый файл."""
    file_path = filedialog.askopenfilename(
        filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")]
    )
    if file_path:
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
                text_area.delete("1.0", tk.END)  # Очищаем текущее содержимое
                text_area.insert("1.0", content)  # Загружаем содержимое из файла
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось открыть файл: {e}")

def clear_text():
    """Очистить текстовое поле."""
    text_area.delete("1.0", tk.END)

# Создание главного окна
root = tk.Tk()
root.title("Блокнот")
root.geometry("600x400")

# Текстовое поле для ввода текста
text_area = tk.Text(root, font=("Arial", 14), wrap="word")
text_area.pack(expand=True, fill="both", padx=5, pady=5)

# Меню
menu_bar = tk.Menu(root)

# Подменю "Файл"
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Открыть", command=open_file)
file_menu.add_command(label="Сохранить", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Очистить", command=clear_text)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=root.quit)

menu_bar.add_cascade(label="Файл", menu=file_menu)

# Добавление меню в главное окно
root.config(menu=menu_bar)

# Запуск приложения
root.mainloop()
