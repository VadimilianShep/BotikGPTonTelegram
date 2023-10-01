import tkinter as tk
from tkinter import messagebox
import math

# Функция для сложения двух чисел
def add():

    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
    result = a + b
    messagebox.showinfo("Результат", f"Результат: {result}")
    except ValueError:
    messagebox.showerror("Ошибка", "Проверьте введенные значения!")

# Функция для вычитания двух чисел
def subtract():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
    result = a - b
    messagebox.showinfo("Результат", f"Результат: {result}")
    except ValueError:
        messagebox.showerror("Ошибка", "Проверьте введенные значения!")

# Функция для умножения двух чисел
def multiply():
try:
a = float(entry_a.get())
b = float(entry_b.get())
result = a * b
messagebox.showinfo("Результат", f"Результат: {result}")
except ValueError:
messagebox.showerror("Ошибка", "Проверьте введенные значения!")

# Функция для деления двух чисел
def divide():
try:
a = float(entry_a.get())
b = float(entry_b.get())
if b != 0:
result = a / b
messagebox.showinfo("Результат", f"Результат: {result}")
else:
messagebox.showerror("Ошибка", "Деление на ноль!")
except ValueError:
messagebox.showerror("Ошибка", "Проверьте введенные значения!")

# Функция для вычисления квадратного корня числа
def square_root():
try:
a = float(entry_a.get())
if a >= 0:
result = math.sqrt(a)
messagebox.showinfo("Результат", f"Результат: {result}")
else:
messagebox.showerror("Ошибка", "Квадратный корень из отрицательного числа!")
except ValueError:
messagebox.showerror("Ошибка", "Проверьте введенные значения!")

# Создание графического интерфейса
window = tk.Tk()
window.title("Математический пакет")

# Поле ввода числа a
label_a = tk.Label(window, text="Число a:")
label_a.grid(row=0, column=0, sticky="e")
entry_a = tk.Entry(window)
entry_a.grid(row=0, column=1)

# Поле ввода числа b
label_b = tk.Label(window, text="Число b:")
label_b.grid(row=1, column=0, sticky="e")
entry_b = tk.Entry(window)
entry_b.grid(row=1, column=1)

# Кнопка сложения
button_add = tk.Button(window, text="Сложить", command=add)
button_add.grid(row=2, column=0)

# Кнопка вычитания
button_subtract = tk.Button(window, text="Вычесть", command=subtract)
button_subtract.grid(row=2, column=1)

# Кнопка умножения
button_multiply = tk.Button(window, text="Умножить", command=multiply)
button_multiply.grid(row=3, column=0)

# Кнопка деления
button_divide = tk.Button(window, text="Разделить", command=divide)
button_divide.grid(row=3, column=1)

# Кнопка вычисления квадратного корня
button_sqrt = tk.Button(window, text="Квадратный корень", command=square_root)
button_sqrt.grid(row=4, column=0, columnspan=2, pady=10)

# Запуск главного цикла графического интерфейса
window.mainloop()