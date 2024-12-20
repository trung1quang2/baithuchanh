print('Sinh viên: Lê Quang Trung')
print('Mã số SV: 235752021610012')

import shutil

def copy_file_using_shutil(source_file, destination_file):
    try:
        shutil.copy(source_file, destination_file)
        print(f"Đã sao chép tệp '{source_file}' sang tệp '{destination_file}'")
    
    except FileNotFoundError:
        print(f"Tệp nguồn '{source_file}' không tồn tại.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

source_file = input("Nhập tên tệp nguồn: ")
destination_file = input("Nhập tên tệp đích: ")

copy_file_using_shutil(source_file, destination_file)
