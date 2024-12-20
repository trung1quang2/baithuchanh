


from tkinter import *
from tkinter import messagebox

# Thông tin sinh viên
print("Sinh vien : Nguyen Hong Minh")
print("Ma so SV: 235752021610112")

# Hàm xử lý khi chọn "New File"
def NewFile(): 
    messagebox.showinfo("New File", "Đây là một file mới!")

# Hàm xử lý khi chọn "About"
def About(): 
    messagebox.showinfo("About", "Đây là một ví dụ đơn giản về menu trong Tkinter.")

# Tạo cửa sổ chính
root = Tk()
root.title("Ứng dụng Menu Tkinter")
root.geometry("500x400")  # Kích thước cửa sổ lớn hơn
root.configure(bg="#FAF9F6")  # Màu nền cửa sổ sáng, dễ chịu cho mắt

# Tạo menu bar
menu = Menu(root)
root.config(menu=menu)

# Tạo menu "File"
filemenu = Menu(menu, tearoff=0)  # tearoff=0 giúp không thể kéo menu ra ngoài cửa sổ
menu.add_cascade(label="File", menu=filemenu, font=("Helvetica", 12, "bold"), foreground="#4CAF50", activebackground="#8BC34A")

# Các mục trong menu "File"
filemenu.add_command(label="New", command=NewFile, font=("Helvetica", 12), background="#FFEB3B", activebackground="#FFC107")
filemenu.add_separator()  # Dòng phân cách
filemenu.add_command(label="Exit", command=root.quit, font=("Helvetica", 12), background="#FF5722", activebackground="#F44336")

# Tạo menu "Help"
helpmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Help", menu=helpmenu, font=("Helvetica", 12, "bold"), foreground="#2196F3", activebackground="#64B5F6")

# Các mục trong menu "Help"
helpmenu.add_command(label="About...", command=About, font=("Helvetica", 12), background="#9C27B0", activebackground="#D81B60")

# Cải thiện giao diện với label
label = Label(root, text="Chọn các lựa chọn từ menu!", font=("Arial", 16, "bold"), bg="#FAF9F6", fg="#333333")
label.pack(pady=50)

# Hiệu ứng cho cửa sổ khi di chuột vào các mục menu
menu.config(bg="#3F51B5", fg="white", activebackground="#303F9F", activeforeground="white")

# Chạy ứng dụng
root.mainloop()
