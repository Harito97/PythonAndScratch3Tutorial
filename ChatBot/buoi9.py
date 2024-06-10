import tkinter as tk 

# Hàm dựng, phương thức, thuộc tính
# AB, BC, CA
# A, B, C
# 66.66%

# Bách: C
# Nam: A
# Đáp án: B

# Đáp án: 1000 đối tượng trong code, 3000 đối tượng, 
# Bách chọn 200 đối tượng, Nam chọn 100 tỷ đối tượng
wd = tk.Tk()
wd.title('ChatBot')

text_area = tk.Text(width=40, height=20)
text_box = tk.Text(width=40, height=3)
button_clear = tk.Button(width=10, height=2, text='Clear all')
button_send = tk.Button(width=10, height=2, text='Send')

text_area.grid(row=0, column=0, padx=(15, 5), pady=5)
button_clear.grid(row=0, column=1, sticky='N', padx=5, pady=5)
text_box.grid(row=1, column=0, padx=(15,5), pady=5)
button_send.grid(row=1, column=1, padx=5, pady=5)

tk.mainloop()