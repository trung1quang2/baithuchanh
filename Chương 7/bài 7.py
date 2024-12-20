print('Sinh viên: Lê Quang Trung')
print('Mã số SV: 235752021610012')

def write_list_to_file(filename, data_list):
    try:
        with open(filename, 'w') as file:
            for item in data_list:
                file.write(str(item) + "\n")
        
        print(f"Đã ghi nội dung vào tệp '{filename}'")
    
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

data = [1, 2, 3, 4, 5, 3.14, True]

filename = input("Nhập tên tệp cần ghi: ")

write_list_to_file(filename, data)
