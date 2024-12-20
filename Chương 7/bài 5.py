print('Sinh viên: Lê Quang Trung')
print('Mã số SV: 235752021610012')

def combine_files(file1, file2, output_file):
    try:
        with open(file1, 'r') as f1:
            file1_content = f1.read()
        
        with open(file2, 'r') as f2:
            file2_content = f2.read()
        
        with open(output_file, 'w') as out_file:
            out_file.write(file1_content)
            out_file.write("\n")  
            out_file.write(file2_content)
        
        print(f"Đã kết nối {file1} và {file2} vào {output_file}")
    
    except FileNotFoundError as e:
        print(f"Lỗi: {e}")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

file1 = input("Nhập tên tệp 1: ")
file2 = input("Nhập tên tệp 2: ")
output_file = input("Nhập tên tệp kết quả (output): ")

combine_files(file1, file2, output_file)
