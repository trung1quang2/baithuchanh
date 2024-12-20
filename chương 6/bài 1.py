print ('sinh viên: LÊ QUANG TRUNG')
print(' MSSV: 235752021610012')
class Circle:
    def __init__(self, radius):
        """Khởi tạo đối tượng Circle với bán kính"""
        self.radius = radius

    def area(self):
        """Tính diện tích của Circle"""
        return 3.14159 * self.radius * self.radius

circle = Circle(5)

print("Diện tích của hình tròn là:", circle.area())
