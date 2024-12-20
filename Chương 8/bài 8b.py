print('Sinh viên: Lê Quang Trung')
print('Mã sv: 235752021610012')
import tkinter as tk

def show_choice():
    label_result.config(text=f"Bạn đã chọn: {v.get()}")

root = tk.Tk()
root.title("Radio Button Example")
root.geometry("300x200")

v = tk.IntVar()

tk.Label(root, text="Chọn một số:", font=("Helvetica", 12)).pack(pady=10)
tk.Radiobutton(root, text="1", variable=v, value=1).pack(anchor="w", padx=20)
tk.Radiobutton(root, text="2", variable=v, value=2).pack(anchor="w", padx=20)
tk.Radiobutton(root, text="3", variable=v, value=3).pack(anchor="w", padx=20)

tk.Button(root, text="Click Me", command=show_choice).pack(pady=10)
label_result = tk.Label(root, text="Bạn đã chọn: ", font=("Helvetica", 12))
label_result.pack()

root.mainloop()
