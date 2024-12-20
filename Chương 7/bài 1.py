print('Sinh viên: Lê Quang Trung')
print('Mã số SV: 235752021610012')

def reverse_file_content(filename):
    try:
        with open(filename, 'r') as file:
            content = file.readlines()

        reversed_content = [line.strip()[::-1] for line in content]

        print("\n".join(reversed_content))
        
    except FileNotFoundError:
        print(f"File '{filename}' không tồn tại.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

filename = input("Nhập tên file cần đọc và đảo ngược nội dung: ")
reverse_file_content(filename)
