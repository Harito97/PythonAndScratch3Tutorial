# Thêm phép trừ vào
import tkinter as tk

wd = tk.Tk()
wd.title("Casio Calculator")

# define e
e = tk.Entry(
    width=40,
    borderwidth=10,
    justify=tk.RIGHT,
    bg="green",
    font="Times 15 bold",
    fg="white",
)  # tạo đối tượng hộp nhập văn bản
e.insert(0, "0")


# num1 & operator
num1 = None
operator = None


## Define function ##
def bt_click(number: float):
    e.insert(tk.END, str(number))


# define operator
def add():
    if e.get() == '':
        print('Number 1 is None!')
        return
    global num1
    num1 = float(e.get())
    e.delete(0, tk.END)
    global operator
    operator = "+"


def sub():
    if e.get() == '':
        print('Number 1 is None!')
        return
    global num1
    num1 = float(e.get())
    e.delete(0, tk.END)
    global operator
    operator = "-"


def mul():
    if e.get() == '':
        print('Number 1 is None!')
        return
    global num1
    num1 = float(e.get())
    e.delete(0, tk.END)
    global operator
    operator = "*"


def div():
    if e.get() == '':
        print('Number 1 is None!')
        return
    global num1
    num1 = float(e.get())
    e.delete(0, tk.END)
    global operator
    operator = "/"


def double():
    if e.get() == '':
        print('Number 1 is None!')
        return
    global num1
    num1 = float(e.get())
    e.delete(0, tk.END)
    global operator
    operator = "** 2"


def sqrt():
    if e.get() == '':
        print('Number 1 is None!')
        return    
    global num1
    num1 = float(e.get())
    e.delete(0, tk.END)
    global operator
    operator = "** 0.5"


def abs_():
    if e.get() == '':
        print('Number 1 is None!')
        return
    global num1
    num1 = float(e.get())
    e.delete(0, tk.END)
    global operator
    operator = "abs"


# define calculation
def equal():
    global num1
    global operator

    if operator == None:
        print("Operator = None!")
        return
    elif not (operator == "** 2" or operator == "** 0.5" or operator == "abs"):
        temp = e.get()
        if temp == "":
            print("Case no input!")
            return
        else:
            num2 = float(e.get())

    e.delete(0, tk.END)
    if operator == "+":
        e.insert(0, num1 + num2)
    elif operator == "-":
        e.insert(0, num1 - num2)
    elif operator == "*":
        e.insert(0, num1 * num2)
    elif operator == "/":
        e.insert(0, num1 / num2)
    elif operator == "** 2":
        e.insert(0, num1**2)
    elif operator == "** 0.5":
        e.insert(0, num1**0.5)
    elif operator == "abs":
        e.insert(0, (num1 ** 2) ** 0.5)
    num1 = None
    operator = None


# define delete function
def delete():
    e.delete(0, tk.END)
    e.insert(0, "0")


## UI ##
# define buttons
bt_sq = tk.Button(
    text="sqrt",
    bg="green",
    font="Times 15 bold",
    fg="white",
    width=10,
    height=3,
    command=lambda: sqrt(),
)
bt_mu = tk.Button(
    text="** 2",
    bg="green",
    font="Times 15 bold",
    fg="white",
    width=10,
    height=3,
    command=lambda: double(),
)
bt_abs = tk.Button(
    text="abs",
    bg="green",
    font="Times 15 bold",
    fg="white",
    width=10,
    height=3,
    command=lambda: abs_(),
)
bt_clear = tk.Button(
    text="Clear",
    bg="green",
    font="Times 15 bold",
    fg="white",
    width=10,
    height=3,
    command=lambda: delete(),
)

bt_7 = tk.Button(
    text="7",
    bg="green",
    font="Times 15 bold",
    fg="white",
    width=10,
    height=3,
    command=lambda: bt_click(7),
)
bt_8 = tk.Button(
    text="8",
    bg="green",
    font="Times 15 bold",
    fg="white",
    width=10,
    height=3,
    command=lambda: bt_click(8),
)
bt_9 = tk.Button(
    text="9",
    bg="green",
    font="Times 15 bold",
    fg="white",
    width=10,
    height=3,
    command=lambda: bt_click(9),
)
bt_delete = tk.Button(
    text="Delete",
    bg="green",
    font="Times 15 bold",
    fg="white",
    width=10,
    height=3,
    command=lambda: e.delete(len(e.get()) - 1, tk.END),
)

bt_4 = tk.Button(
    text="4",
    bg="green",
    font="Times 15 bold",
    fg="white",
    width=10,
    height=3,
    command=lambda: bt_click(4),
)
bt_5 = tk.Button(
    text="5",
    bg="green",
    font="Times 15 bold",
    fg="white",
    width=10,
    height=3,
    command=lambda: bt_click(5),
)
bt_6 = tk.Button(
    text="6",
    bg="green",
    font="Times 15 bold",
    fg="white",
    width=10,
    height=3,
    command=lambda: bt_click(6),
)
bt_div = tk.Button(
    text="/",
    bg="green",
    font="Times 15 bold",
    fg="white",
    width=10,
    height=3,
    command=lambda: div(),
)

bt_1 = tk.Button(
    text="1",
    bg="green",
    font="Times 15 bold",
    fg="white",
    width=10,
    height=3,
    command=lambda: bt_click(1),
)
bt_2 = tk.Button(
    text="2",
    bg="green",
    font="Times 15 bold",
    fg="white",
    width=10,
    height=3,
    command=lambda: bt_click(2),
)
bt_3 = tk.Button(
    text="3",
    bg="green",
    font="Times 15 bold",
    fg="white",
    width=10,
    height=3,
    command=lambda: bt_click(3),
)
bt_mul = tk.Button(
    text="*",
    bg="green",
    font="Times 15 bold",
    fg="white",
    width=10,
    height=3,
    command=lambda: mul(),
)

bt_0 = tk.Button(
    text="0",
    bg="green",
    font="Times 15 bold",
    fg="white",
    width=10,
    height=3,
    command=lambda: bt_click(0),
)
bt_add = tk.Button(
    text="+",
    bg="green",
    font="Times 15 bold",
    fg="white",
    width=10,
    height=3,
    command=lambda: add(),
)
bt_sub = tk.Button(
    text="-",
    bg="green",
    font="Times 15 bold",
    fg="white",
    width=10,
    height=3,
    command=lambda: sub(),
)
bt_equal = tk.Button(
    text="=",
    bg="green",
    font="Times 15 bold",
    fg="white",
    width=10,
    height=3,
    command=lambda: equal(),
)

# to grid
# row 0
e.grid(row=0, column=0, columnspan=4, padx=5, pady=5)  # gắn đối tượng lên cửa sổ

# row 1
bt_sq.grid(row=1, column=0)
bt_mu.grid(row=1, column=1)
bt_abs.grid(row=1, column=2)
bt_clear.grid(row=1, column=3)

# row 2
bt_7.grid(row=2, column=0)
bt_8.grid(row=2, column=1)
bt_9.grid(row=2, column=2)
bt_delete.grid(row=2, column=3)

# row 3
bt_4.grid(row=3, column=0)
bt_5.grid(row=3, column=1)
bt_6.grid(row=3, column=2)
bt_div.grid(row=3, column=3)

# row 4
bt_1.grid(row=4, column=0)
bt_2.grid(row=4, column=1)
bt_3.grid(row=4, column=2)
bt_mul.grid(row=4, column=3)

# row 5
bt_0.grid(row=5, column=0)
bt_add.grid(row=5, column=1)
bt_sub.grid(row=5, column=2)
bt_equal.grid(row=5, column=3)

wd.mainloop()
