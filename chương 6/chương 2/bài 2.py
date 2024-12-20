print('sv : Lê quang Trung')
print('mssv : 235752021610012')
import math

x1 = int(input("Nhập x1 ---> "))
y1 = int(input("Nhập y1 ---> "))
x2 = int(input("Nhập x2 ---> "))
y2 = int(input("Nhập y2 ---> "))


d1 = (x2 - x1) ** 2
d2 = (y2 - y1) ** 2
res = math.sqrt(d1 + d2)

print("Khoảng cách giữa hai điểm:", res)
