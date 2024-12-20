print('Sinh viên: Lê Quang Trung')
print('Mã số SV: 235752021610012')

def count_lines_in_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            num_lines = len(lines)
        
        print(f"Số dòng trong tệp '{filename}' là: {num_lines}")
    
    except FileNotFoundError:
        print(f"Tệp '{filename}' không tồn tại.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

filename = input("Nhập tên tệp văn bản cần đếm số dòng: ")
count_lines_in_file(filename)
