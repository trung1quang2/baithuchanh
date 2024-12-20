print('sv : Lê quang Trung')
print('mssv : 235752021610012')
import math

a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

if a == 0:
    if b != 0:
        x = -c / b
        print(f"Phương trình bậc nhất có nghiệm: x = {x}")
    else:
        if c == 0:
            print("Phương trình có vô số nghiệm.")
        else:
            print("Phương trình vô nghiệm.")
else:
    delta = b * b - 4 * a * c

    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"Phương trình có hai nghiệm phân biệt: x1 = {x1} và x2 = {x2}")
    elif delta == 0:
        x1 = -b / (2 * a)
        print(f"Phương trình có một nghiệm kép: x = {x1}")
    else:
        print("Phương trình vô nghiệm (vì delta < 0).")


