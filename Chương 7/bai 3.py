print('Sinh viên: Lê Quang Trung')
print('Mã số SV: 235752021610012')

def read_file(filename):
    try:
        with open(filename, 'r') as file:
          content = file.read()
        
        print(content)

    except FileNotFoundError:
        print(f"File '{filename}' không tồn tại.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

filename = input("Nhập tên tệp văn bản cần đọc: ")

