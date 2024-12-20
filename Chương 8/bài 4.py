print('Sinh viên: Lê Quang Trung')
print('Mã số SV: 235752021610012')

from tkinter import *

window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('400x250') 
window.configure(bg="lightblue")  

lbl = Label(window, text="Hello, Chào mừng bạn đến với cửa sổ đồ họa!", 
            font=("Arial", 14, "bold"), fg="darkblue", bg="lightblue")
lbl.grid(column=0, row=0, padx=10, pady=20, columnspan=2) 

def clicked():
    lbl.configure(text="Button was clicked !!", fg="red")  

btn = Button(window, text="Click Me", command=clicked, font=("Arial", 12, "bold"), 
             bg="blue", fg="white", padx=20, pady=10, relief=SOLID)
btn.grid(column=0, row=1, columnspan=2, pady=20)  # Căn giữa button và thêm khoảng cách

window.mainloop()
