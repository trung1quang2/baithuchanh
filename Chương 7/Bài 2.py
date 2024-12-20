print('Sinh viên: Lê Quang Trung')
print('Mã số SV: 235752021610012')
import os

def count_file_statistics(filename):
    try:
        if not os.path.exists(filename):
            print(f"File '{filename}' không tồn tại.")
            return
        
        with open(filename, 'r') as file:
            lines = file.readlines()

        num_lines = len(lines)
        
        num_words = 0
        num_chars = 0

        for line in lines:
            num_chars += len(line)  
            num_words += len(line.split()) 

        print(f"Số dòng trong file: {num_lines}")
        print(f"Số từ trong file: {num_words}")
        print(f"Số ký tự trong file: {num_chars}")

    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

filename = input("Nhập tên file cần tính số ký tự, số từ và số dòng: ")
count_file_statistics(filename)
