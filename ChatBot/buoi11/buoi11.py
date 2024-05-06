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
    
text_area = tk.Text(width=40, height=20)
text_area.insert(tk.END, 'Computer: Nice to meet you again!') 
text_box = tk.Text(width=40, height=3)
button_clear = tk.Button(width=10, height=2, text='Clear all')
button_send = tk.Button(width=10, height=2, text='Send', command=send_text)

text_area.grid(row=0, column=0, padx=(15, 5), pady=5)
button_clear.grid(row=0, column=1, sticky='N', padx=5, pady=5)
text_box.grid(row=1, column=0, padx=(15,5), pady=5)
button_send.grid(row=1, column=1, padx=5, pady=5)

tk.mainloop()