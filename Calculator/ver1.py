# Minh  Lớp 8 - Sài Gòn 
# bắt đầu học buổi 4 (23/02/2024)

# from tkinter import Button
import tkinter as tk
wd = tk.Tk()
wd.title('Casio Calculator')

# define e 
e = tk.Entry(width=40, borderwidth=10, font='Arial 18', justify=tk.RIGHT)  # tạo đối tượng hộp nhập văn bản
e.grid()    # gắn đối tượng lên cửa sổ

# define command function
def button_click(number):
    e.insert(tk.END, number)

def addition():
    global num1
    num1 = int(e.get())
    e.delete(0, tk.END)
    # e.insert(tk.END, '+')
    global operator
    operator = '+'

def subtraction():
    global num1 
    num1 = int(e.get())
    e.delete(0, tk.END)
    # e.insert(tk.END, '-')
    global operator 
    operator = '-'

def multiplication():
    global num1 
    num1 = int(e.get())
    e.delete(0, tk.END)
    # e.insert(tk.END, '*')
    global operator
    operator = '*'

def division():
    global num1 
    num1 = int(e.get())
    e.delete(0, tk.END)
    # e.insert(tk.END, '/')
    global operator
    operator = '/'

def calculation():
    global num1 
    global operator
    num2 = int(e.get())
    e.delete(0, tk.END)
    # e.insert(0, 0)
    if operator == '+':
        e.insert(0, num1 + num2)
    elif operator == '-':
        e.insert(0, num1 - num2)
    elif operator == '*':
        e.insert(0, num1 * num2)
    elif operator == '/':
        e.insert(0, num1 / num2)

# define the button
bt_7 = tk.Button(text='7', width=10, height=5, command=lambda: button_click(7))
bt_8 = tk.Button(text='8', width=10, height=5, command=lambda: button_click(8))
bt_9 = tk.Button(text='9', width=10, height=5, command=lambda: button_click(9))
bt_clear = tk.Button(text='Clear', width=10, height=5, command=lambda: e.delete(0, tk.END))

bt_4 = tk.Button(text='4', width=10, height=5, command=lambda: button_click(4))
bt_5 = tk.Button(text='5', width=10, height=5, command=lambda: button_click(5))
bt_6 = tk.Button(text='6', width=10, height=5, command=lambda: button_click(6))
bt_mul = tk.Button(text='*', width=10, height=5, command=multiplication)

bt_1 = tk.Button(text='1', width=10, height=5, command=lambda: button_click(1))
bt_2 = tk.Button(text='2', width=10, height=5, command=lambda: button_click(2))
bt_3 = tk.Button(text='3', width=10, height=5, command=lambda: button_click(3))
bt_div = tk.Button(text='/', width=10, height=5, command=division)

bt_0 = tk.Button(text='0', width=10, height=5, command=lambda: button_click(0))
bt_add = tk.Button(text='+', width=10, height=5, command=addition)
bt_sub = tk.Button(text='-', width=10, height=5, command=subtraction)
bt_equ = tk.Button(text='=', width=10, height=5, command=calculation)

# location the buttons
e.grid(row=0, column=0, columnspan=4, pady=10)
bt_7.grid(row=1, column=0)
bt_8.grid(row=1, column=1)
bt_9.grid(row=1, column=2)
bt_clear.grid(row=1, column=3)

bt_4.grid(row=2, column=0) 
bt_5.grid(row=2, column=1) 
bt_6.grid(row=2, column=2)
bt_mul.grid(row=2, column=3)

bt_1.grid(row=3, column=0)
bt_2.grid(row=3, column=1)
bt_3.grid(row=3, column=2)
bt_div.grid(row=3, column=3)

bt_0.grid(row=4, column=0)
bt_add.grid(row=4, column=1)
bt_sub.grid(row=4, column=2)
bt_equ.grid(row=4, column=3)

wd.mainloop()
