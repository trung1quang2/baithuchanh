from tkinter import *
from tkinter import messagebox

print('Sinh viên: Lê Quang Trung')
print('Mã số SV: 235752021610012')

def NewFile(): 
    messagebox.showinfo("New File", "Đây là một file mới!")

def About(): 
    messagebox.showinfo("About", "Đây là một ví dụ đơn giản về menu trong Tkinter.")

root = Tk()
root.title("Ứng dụng Menu Tkinter")
root.geometry("500x400")  
root.configure(bg="#FAF9F6")  

menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu, tearoff=0)  
menu.add_cascade(label="File", menu=filemenu, font=("Helvetica", 12, "bold"), foreground="#4CAF50", activebackground="#8BC34A")

filemenu.add_command(label="New", command=NewFile, font=("Helvetica", 12), background="#FFEB3B", activebackground="#FFC107")
filemenu.add_separator() 
filemenu.add_command(label="Exit", command=root.quit, font=("Helvetica", 12), background="#FF5722", activebackground="#F44336")

helpmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Help", menu=helpmenu, font=("Helvetica", 12, "bold"), foreground="#2196F3", activebackground="#64B5F6")

helpmenu.add_command(label="About...", command=About, font=("Helvetica", 12), background="#9C27B0", activebackground="#D81B60")

label = Label(root, text="Chọn các lựa chọn từ menu!", font=("Arial", 16, "bold"), bg="#FAF9F6", fg="#333333")
label.pack(pady=50)
menu.config(bg="#3F51B5", fg="white", activebackground="#303F9F", activeforeground="white")

root.mainloop()
