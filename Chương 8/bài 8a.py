print('Sinh viên: Lê Quang Trung')
print('Mã sv: 235752021610012')
      
import tkinter as tk

def create_personal_info_form():
    # Tạo cửa sổ chính
    root = tk.Tk()
    root.title("Thông Tin Cá Nhân")
    root.geometry("400x350")
    root.configure(bg="#f2f2f2")

    # Tiêu đề cửa sổ
    title_label = tk.Label(root, text="Thông tin cá nhân", font=("Helvetica", 16, "bold"), bg="#f2f2f2")
    title_label.grid(row=0, column=0, columnspan=2, pady=10)

    # Họ tên
    label_name = tk.Label(root, text="Họ tên:", font=("Helvetica", 12), bg="#f2f2f2")
    label_name.grid(row=1, column=0, padx=20, pady=10, sticky="e")
    entry_name = tk.Entry(root, width=30, font=("Helvetica", 12))
    entry_name.grid(row=1, column=1, padx=20, pady=10)

    # Ngày tháng năm sinh
    label_dob = tk.Label(root, text="Ngày tháng năm sinh:", font=("Helvetica", 12), bg="#f2f2f2")
    label_dob.grid(row=2, column=0, padx=20, pady=10, sticky="e")
    entry_dob = tk.Entry(root, width=30, font=("Helvetica", 12))
    entry_dob.grid(row=2, column=1, padx=20, pady=10)

    # MSSV
    label_mssv = tk.Label(root, text="MSSV:", font=("Helvetica", 12), bg="#f2f2f2")
    label_mssv.grid(row=3, column=0, padx=20, pady=10, sticky="e")
    entry_mssv = tk.Entry(root, width=30, font=("Helvetica", 12))
    entry_mssv.grid(row=3, column=1, padx=20, pady=10)

    # Ngành học
    label_major = tk.Label(root, text="Ngành học:", font=("Helvetica", 12), bg="#f2f2f2")
    label_major.grid(row=4, column=0, padx=20, pady=10, sticky="e")
    entry_major = tk.Entry(root, width=30, font=("Helvetica", 12))
    entry_major.grid(row=4, column=1, padx=20, pady=10)

    # Hàm in thông tin
    def print_info():
        name = entry_name.get()
        dob = entry_dob.get()
        mssv = entry_mssv.get()
        major = entry_major.get()
        print(f"Họ tên: {name}")
        print(f"Ngày tháng năm sinh: {dob}")
        print(f"MSSV: {mssv}")
        print(f"Ngành học: {major}")

    # Nút in thông tin
    button_print = tk.Button(root, text="In Thông Tin", command=print_info, bg="#4CAF50", fg="white", font=("Helvetica", 12))
    button_print.grid(row=5, column=0, columnspan=2, pady=20)

    # Nút đóng cửa sổ
    button_exit = tk.Button(root, text="Thoát", command=root.quit, bg="#f44336", fg="white", font=("Helvetica", 12))
    button_exit.grid(row=6, column=0, columnspan=2, pady=10)

    # Chạy ứng dụng
    root.mainloop()

create_personal_info_form()
