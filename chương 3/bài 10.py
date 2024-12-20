print('SV : Lê Quang Trung')
print('mssv : 235752021610012')
import math

def Tinh(R):
    if R <= 0:
        print("Bán kính phải là số dương!")
        return
    
    chu_vi = 2 * math.pi * R
    dien_tich = math.pi * R * R
    
    print(f"Chu vi hình tròn: {chu_vi:.2f}")
    print(f"Diện tích hình tròn: {dien_tich:.2f}")

try:
    R = float(input("Nhập bán kính hình tròn: "))
    Tinh(R)
except ValueError:
    print("Vui lòng nhập một giá trị hợp lệ cho bán kính!")
