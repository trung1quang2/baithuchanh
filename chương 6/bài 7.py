print('Sinh viên: Lê Quang Trung')
print('Mã số SV: 235752021610012')
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius  

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

radius = float(input("Nhập bán kính hình tròn: "))
circle = Circle(radius)

print(f"Diện tích của hình tròn có bán kính {radius} là: {circle.area():.2f}")
print(f"Chu vi của hình tròn có bán kính {radius} là: {circle.circumference():.2f}")
