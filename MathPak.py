import tkinter as tk
from tkinter import messagebox
import math

# ������� ��� �������� ���� �����
def add():

    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
    result = a + b
    messagebox.showinfo("���������", f"���������: {result}")
    except ValueError:
    messagebox.showerror("������", "��������� ��������� ��������!")

# ������� ��� ��������� ���� �����
def subtract():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
    result = a - b
    messagebox.showinfo("���������", f"���������: {result}")
    except ValueError:
        messagebox.showerror("������", "��������� ��������� ��������!")

# ������� ��� ��������� ���� �����
def multiply():
try:
a = float(entry_a.get())
b = float(entry_b.get())
result = a * b
messagebox.showinfo("���������", f"���������: {result}")
except ValueError:
messagebox.showerror("������", "��������� ��������� ��������!")

# ������� ��� ������� ���� �����
def divide():
try:
a = float(entry_a.get())
b = float(entry_b.get())
if b != 0:
result = a / b
messagebox.showinfo("���������", f"���������: {result}")
else:
messagebox.showerror("������", "������� �� ����!")
except ValueError:
messagebox.showerror("������", "��������� ��������� ��������!")

# ������� ��� ���������� ����������� ����� �����
def square_root():
try:
a = float(entry_a.get())
if a >= 0:
result = math.sqrt(a)
messagebox.showinfo("���������", f"���������: {result}")
else:
messagebox.showerror("������", "���������� ������ �� �������������� �����!")
except ValueError:
messagebox.showerror("������", "��������� ��������� ��������!")

# �������� ������������ ����������
window = tk.Tk()
window.title("�������������� �����")

# ���� ����� ����� a
label_a = tk.Label(window, text="����� a:")
label_a.grid(row=0, column=0, sticky="e")
entry_a = tk.Entry(window)
entry_a.grid(row=0, column=1)

# ���� ����� ����� b
label_b = tk.Label(window, text="����� b:")
label_b.grid(row=1, column=0, sticky="e")
entry_b = tk.Entry(window)
entry_b.grid(row=1, column=1)

# ������ ��������
button_add = tk.Button(window, text="�������", command=add)
button_add.grid(row=2, column=0)

# ������ ���������
button_subtract = tk.Button(window, text="�������", command=subtract)
button_subtract.grid(row=2, column=1)

# ������ ���������
button_multiply = tk.Button(window, text="��������", command=multiply)
button_multiply.grid(row=3, column=0)

# ������ �������
button_divide = tk.Button(window, text="���������", command=divide)
button_divide.grid(row=3, column=1)

# ������ ���������� ����������� �����
button_sqrt = tk.Button(window, text="���������� ������", command=square_root)
button_sqrt.grid(row=4, column=0, columnspan=2, pady=10)

# ������ �������� ����� ������������ ����������
window.mainloop()