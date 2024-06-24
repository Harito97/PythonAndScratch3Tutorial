import tkinter as tk

wd = tk.Tk()
wd.title("Chat Bot app")


def send_text():
    user_text = text_box.get(
        "1.0", tk.END
    )  # lấy toàn bộ nội dung mà người dùng nhập vào
    text_area.configure(state='normal')
    text_area.insert(
        tk.END, "User: " + user_text.lower()
    )  # chèn nội dung người dùng nhập vào màn hình trò chuyện
    text_box.delete("1.0", tk.END)  # xóa nội dung người dùng gõ trước đó
    computer_response(user_text)
    text_area.configure(state='disabled')


def computer_response(text):
    computer_text = "Sorry, I don't understand."
    if "hello" in text:
        computer_text = "Hello."
    elif "name" in text:
        computer_text = "My name's Alex."
    elif "weather" in text:
        ...
    elif "bye" in text:
        computer_text = "Goodbye!"
    elif "good morning" in text:
        computer_text = "Good morning!"
    text_area.insert(tk.END, "Computer: " + computer_text + '\n')


text_area = tk.Text(width=40, height=20, bg='green')
text_area.configure(state='disabled')
text_box = tk.Text(width=40, height=3)
button_clear = tk.Button(width=10, height=2, text="Clear all")
button_send = tk.Button(width=10, height=2, text="Send", command=send_text)

text_area.grid(row=0, column=0, padx=(15, 5), pady=5)
text_box.grid(row=1, column=0, padx=(15, 5), pady=5)
button_clear.grid(row=0, column=1, sticky="S", padx=5, pady=5)
button_send.grid(row=1, column=1, padx=5, pady=5)

wd.mainloop()
