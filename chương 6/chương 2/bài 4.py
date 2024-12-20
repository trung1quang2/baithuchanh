print('sv : Lê quang Trung')
print('mssv : 235752021610012')
n = int(input("Nhập vào một số tự nhiên n (> 0): "))

if n > 0:
    
    for i in range(n, -1, -1):
        print(i)
else:
    print("Vui lòng nhập một số tự nhiên lớn hơn 0.")
