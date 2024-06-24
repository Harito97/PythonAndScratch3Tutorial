import tkinter as tk

wd = tk.Tk()
wd.title("Casio Calculator")

def bt_click(number: int): 
    e.insert(tk.END, str(number))


# define e
e = tk.Entry(
    width=40, borderwidth=10, justify=tk.RIGHT, bg='green', font='Times 15 bold', fg='white',
)  # tạo đối tượng hộp nhập văn bản

# define buttons
bt_sq = tk.Button(text='sqrt', bg='green', font='Times 15 bold', fg='white', width=10, height=3, command=lambda: ...)
bt_mu = tk.Button(text='Mu 2', bg='green', font='Times 15 bold', fg='white', width=10, height=3, command=lambda: ...)
bt_ttd = tk.Button(text='TrTDoi', bg='green', font='Times 15 bold', fg='white', width=10, height=3, command=lambda: ...)
bt_clear = tk.Button(text='Clear', bg='green', font='Times 15 bold', fg='white', width=10, height=3, command=lambda: e.delete(0, tk.END))

bt_7 = tk.Button(text='7', bg='green', font='Times 15 bold', fg='white', width=10, height=3, command=lambda: bt_click(7))
bt_8 = tk.Button(text='8', bg='green', font='Times 15 bold', fg='white', width=10, height=3, command=lambda: bt_click(8))
bt_9 = tk.Button(text='9', bg='green', font='Times 15 bold', fg='white', width=10, height=3, command=lambda: bt_click(9))
bt_delete = tk.Button(text='Delete', bg='green', font='Times 15 bold', fg='white', width=10, height=3, command=lambda: e.delete(len(e.get()) - 1, tk.END))

bt_4 = tk.Button(text='4', bg='green', font='Times 15 bold', fg='white', width=10, height=3, command=lambda: bt_click(4))
bt_5 = tk.Button(text='5', bg='green', font='Times 15 bold', fg='white', width=10, height=3, command=lambda: bt_click(5))
bt_6 = tk.Button(text='6', bg='green', font='Times 15 bold', fg='white', width=10, height=3, command=lambda: bt_click(6))
bt_div = tk.Button(text='/', bg='green', font='Times 15 bold', fg='white', width=10, height=3)

bt_1 = tk.Button(text='1', bg='green', font='Times 15 bold', fg='white', width=10, height=3, command=lambda: bt_click(1))
bt_2 = tk.Button(text='2', bg='green', font='Times 15 bold', fg='white', width=10, height=3, command=lambda: bt_click(2))
bt_3 = tk.Button(text='3', bg='green', font='Times 15 bold', fg='white', width=10, height=3, command=lambda: bt_click(3))
bt_mul = tk.Button(text='*', bg='green', font='Times 15 bold', fg='white', width=10, height=3)

bt_0 = tk.Button(text='0', bg='green', font='Times 15 bold', fg='white', width=10, height=3, command=lambda: bt_click(0))
bt_add = tk.Button(text='+', bg='green', font='Times 15 bold', fg='white', width=10, height=3)
bt_sub = tk.Button(text='-', bg='green', font='Times 15 bold', fg='white', width=10, height=3)
bt_equal = tk.Button(text='=', bg='green', font='Times 15 bold', fg='white', width=10, height=3)

# to grid
# row 0
e.grid(row=0, column=0, columnspan=4, padx = 5, pady=5)  # gắn đối tượng lên cửa sổ

# row 1
bt_sq.grid(row=1, column=0)
bt_mu.grid(row=1, column=1)
bt_ttd.grid(row=1, column=2)
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
