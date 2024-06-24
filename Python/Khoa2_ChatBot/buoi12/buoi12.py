import tkinter as tk 
import computer

wd = tk.Tk()
wd.title('ChatBot')

def send_text():
    user_text = text_box.get('1.0', tk.END)
    text_area.insert(tk.END, 'You: ' + user_text)
    text_box.delete('1.0', tk.END)
    computer_response(user_text)

def computer_response(text): 
    computer_text = computer.response(text) 
    text_area.insert(tk.END, 'Computer: ' + computer_text) 
    wd.update()
    computer.speak(computer_text)
    f = open('history.txt', 'w')
    f.write(text_area.get('3.0', tk.END))
    f.close()
    
text_area = tk.Text(width=40, height=20)
text_box = tk.Text(width=40, height=3)
button_clear = tk.Button(width=10, height=2, text='Clear all', command=lambda: text_area.delete('1.0', tk.END))
button_send = tk.Button(width=10, height=2, text='Send', command=send_text)

text_area.grid(row=0, column=0, padx=(15, 5), pady=5)
button_clear.grid(row=0, column=1, sticky='N', padx=5, pady=5)
text_box.grid(row=1, column=0, padx=(15,5), pady=5)
button_send.grid(row=1, column=1, padx=5, pady=5)

try:
    f = open('history.txt', 'r')
except:
    # khong doc duoc file vi file khong ton tai
    f = open('history.txt', 'x')
else:
    content = f.read()
    if content == '':
        content = 'Không có lịch sử trò chuyện trước đó!\n'
    else:
        content = 'Lịch sử trò chuyện trước đó là: \n' + content + '\n'
    text_area.insert('1.0', content)    # hang 1 cot 0
    # wd.update()
    # computer.speak(content)
finally:
    f.close()

text_area.insert(tk.END, '-------------Current-------------\nComputer: Nice to meet you again!\n') 
wd.update() 
computer.speak(text='Nice to meet you again!') 

tk.mainloop()