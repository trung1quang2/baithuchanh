print(' SV : Lê Quang Trung')
print('Mssv : 235752021610012')
a = int(input("Nhập giá trị a: "))
b = int(input("Nhập giá trị b: "))

if a >= b:
    print("Vui lòng đảm bảo rằng a nhỏ hơn b.")
else:
    print("Số nghịch đảo và kết quả dưới dạng thập phân trong khoảng (a, b):")
    
    for num in range(a + 1, b): 
        if num != 0:  
            inverse = 1 / num  
            print(f"Số: {num}, Số nghịch đảo: {inverse:.4f}")
        else:
            print("Số 0 không có nghịch đảo.")
