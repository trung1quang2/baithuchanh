print('Sinh viên: Lê Quang Trung')
print('Mã số SV: 235752021610012')

def read_first_n_lines(filename, n):
    try:
        with open(filename, 'r') as file:
            lines = [file.readline().strip() for _ in range(n)]

        print("\n".join(lines))

    except FileNotFoundError:
        print(f"File '{filename}' không tồn tại.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

filename = input("Nhập tên tệp văn bản cần đọc: ")
n = int(input("Nhập số dòng bạn muốn đọc: "))
read_first_n_lines(filename, n)
